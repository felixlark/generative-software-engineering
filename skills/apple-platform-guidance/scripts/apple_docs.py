#!/usr/bin/env python3
"""Fetch Apple's official Markdown documentation representation."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit, urlunsplit
from urllib.request import Request, urlopen


ALLOWED_HOST = "developer.apple.com"
USER_AGENT = "Codex-Apple-Platform-Guidance/1.0"


def markdown_url(url: str) -> str:
    parsed = urlsplit(url)
    if parsed.scheme != "https" or parsed.hostname != ALLOWED_HOST:
        raise ValueError("only https://developer.apple.com URLs are accepted")
    if not parsed.path or parsed.path == "/":
        raise ValueError("the URL must identify a documentation or design page")
    path = parsed.path.rstrip("/")
    if not path.endswith(".md"):
        path += ".md"
    return urlunsplit(("https", parsed.netloc, path, parsed.query, ""))


def fetch(url: str, timeout: float) -> tuple[str, str]:
    source = markdown_url(url)
    request = Request(
        source,
        headers={
            "Accept": "text/markdown,text/plain;q=0.9,*/*;q=0.1",
            "User-Agent": USER_AGENT,
        },
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8", errors="replace")
    except HTTPError as error:
        if error.code == 404:
            raise RuntimeError(
                f"no official Markdown response at {source}; open the original "
                "Apple page and use its HTML representation"
            ) from error
        raise RuntimeError(f"Apple returned HTTP {error.code} for {source}") from error
    except URLError as error:
        raise RuntimeError(f"could not reach {source}: {error.reason}") from error
    if not body.lstrip().startswith(("<!--", "#")):
        raise RuntimeError(
            f"{source} did not return Markdown; use the original Apple page"
        )
    return source, body


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    fetch_parser = subparsers.add_parser(
        "fetch", help="fetch the official Markdown representation of an Apple page"
    )
    fetch_parser.add_argument("url")
    fetch_parser.add_argument("--timeout", type=float, default=30.0)
    fetch_parser.add_argument(
        "--json", action="store_true", help="emit source metadata and content as JSON"
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        source, body = fetch(args.url, args.timeout)
    except (RuntimeError, ValueError) as error:
        print(f"apple-docs: {error}", file=sys.stderr)
        return 2
    if args.json:
        json.dump(
            {
                "source": args.url,
                "markdown_url": source,
                "fetched_at": datetime.now(timezone.utc).isoformat(),
                "content": body,
            },
            sys.stdout,
            ensure_ascii=False,
            indent=2,
        )
        sys.stdout.write("\n")
    else:
        sys.stdout.write(body)
        if body and not body.endswith("\n"):
            sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
