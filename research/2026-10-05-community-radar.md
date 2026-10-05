# Community radar — 2026-10-05

Non-normative research note. Window: 2026-09-28 00:00 through the scan on 2026-10-05, Asia/Shanghai. Sources were retrieved on 2026-10-05. Publication dates below come from the primary source, rather than retrieval time.

## What this scan adds

[E2E-SWE](https://arxiv.org/abs/2609.38335v1) is a new, traceable benchmark for an important boundary that issue-repair benchmarks do not directly cover: producing a complete, installable repository from a natural-language specification in an empty workspace. Its evaluation design is relevant to GSE because it makes a generated artifact independently installable and executable in a fresh container. It is **not** an evaluation of accepted software outcomes: hidden functional tests cannot establish that the specification captured user intent, that consequential actions were authorized, or that a deployed service works in its real environment.

The source supplies tasks, an adapter, and an execution/result layout, so it is more actionable than a benchmark claim without artifacts. It still does not justify a new GSE principle or a model ranking: the reported scores are author-run results, and this scan did not rerun the benchmark, audit its hidden tests, or compare total participant cost under GSE's protocol.

## Source and admission decision

| Source and permanent reference | Author / organization | Publication date; type | Decision and relevance |
| --- | --- | --- | --- |
| [E2E-SWE: Benchmarking LLMs on Building Working Codebases from Scratch, v1](https://arxiv.org/abs/2609.38335v1); [implementation and tasks](https://github.com/facebookresearch/E2E-SWE) | Hantian Ding, Chloe Bi, Jiacheng Zhu, John Yang, Matt Deitke, Pengcheng Yin, Zijian Wang, Rui Hou; Meta Superintelligence Labs / Facebook Research | 2026-09-29 18:02:25 UTC; arXiv preprint and public benchmark repository | Include as an author-reported, runnable whole-repository benchmark. It offers a useful evidence-layer contrast, not a replacement for GSE acceptance or a general performance claim. |

### What the authors provide

**Verified source content:** the paper describes 186 tasks across 11 programming languages. An agent receives a natural-language specification and an empty workspace, produces a repository plus `setup.sh`, and the result is installed in a fresh container and evaluated with hidden tests. A task counts as resolved only when every hidden test passes. The public repository provides the task set in Harbor format, a mini-swe-agent adapter, command examples, and per-run artifacts including verifier results, trajectories, append-only turn logs, timings, exceptions, and token usage.

**Author-reported result:** the paper evaluates 13 frontier models and reports pass@1 from 11.7% to 67.7%. The repository README says its leaderboard values are averaged over four independent runs. These are benchmark outcomes under the authors' harness and configuration; this scan did not reproduce them and does not treat them as a portable model ranking.

**Reproduction and scope limits:** the published run path calls for Python 3.12+, Harbor 0.22.0, mini-swe-agent 2.4.6, model credentials, and a documented one-line Harbor patch; without that patch, the authors say grading uploads no tests and all tasks score zero. The repository is CC BY-NC 4.0, permits evaluation and publication of results, and asks users not to train models on the data. Its offline hidden-test design is valuable functional evidence, but it does not prove requirements validity, operational safety, deployment health, or real-user acceptance.

### GSE interpretation

E2E-SWE supports a narrower, falsifiable research question: for work that starts with a sufficiently specified intent, does a GSE-guided configuration improve the rate of **clean-environment, fully functional repository completion** at matched total cost and time? It does not test the full GSE claim that an outcome has been accepted. A future comparison must retain the same task inputs and hidden-test criterion, report the exact model and harness configuration, count every participant and retry, preserve the generated repositories and traces, and separately document any acceptance evidence beyond the benchmark. Those requirements already belong to the [benchmark protocol](BENCHMARK_PROTOCOL.md); no normative document changes follow from this paper.

## Scan coverage and exclusions

Exa discovery reviewed 50 results across five distinct angles: papers/evaluations, first-party tool announcements, GitHub releases, original X posts, and original Reddit threads. The final source was then checked against the arXiv API and GitHub API/raw repository content. This is a bounded weekly scan, not an exhaustive platform census.

| Area | Admission or exclusion |
| --- | --- |
| Papers / preprints | Admit E2E-SWE because the v1 date is inside the window and the paper plus task repository are public. Exclude results dated 2026-09-27 or earlier from this week's findings. |
| GitHub / tool releases | No separate dated release met the combination of in-window date, primary release evidence, and material GSE relevance. E2E-SWE's public repository is cited as implementation evidence, not mislabelled as a release. |
| X | No in-window original status URL with a linked coding-agent experiment or trace was verified; no X claim is adopted. |
| Reddit | No in-window original thread with verifiable, task-level experiment evidence was found. Historical snapshots and recommendation threads were excluded. |
| Learning-hub architecture | No new high-quality, dated source changed the prior learning-path conclusion; avoid cosmetic README churn. |

## Next question

Before adopting E2E-SWE in a GSE comparison, verify that its license and Harbor patch fit the intended study, then execute a small, pre-registered matched comparison under [`BENCHMARK_PROTOCOL.md`](BENCHMARK_PROTOCOL.md). The key outcome is not a leaderboard position: preserve full-resolution rate, total participant cost, elapsed time, generated artifact, verifier output, and any acceptance evidence that the benchmark cannot supply.
