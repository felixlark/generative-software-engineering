# Evidence and verification

GSE treats verification as a mapping from **claims** to **evidence**, selected by impact and failure cost.

## Evidence hierarchy

Use the lowest layer that can actually prove the claim:

1. **Static/structural evidence** — types, schemas, lint, parsing, source structure.
2. **Focused logic evidence** — unit, integration, protocol, deterministic fixture, or targeted command.
3. **System evidence** — built candidate, process behavior, persistence, integration boundaries, resource behavior.
4. **User-path evidence** — interaction with the exact runnable candidate through the surface a user actually depends on.
5. **External-world evidence** — when the outcome depends on a real remote system, account, device, deployment, or other environment that lower layers cannot reproduce.

Higher layers are not automatically better. They are required when lower layers cannot establish the claim.

## Evidence rules

- Bind evidence to the exact candidate or state it proves.
- Refresh evidence after a change that can invalidate its claim.
- Distinguish source shape, build success, installation, runtime health, and user behavior; they prove different things.
- Prefer focused checks with strong defect-detection value over large suites that add little information.
- Use an independent evaluator when risk, subjectivity, or self-verification bias materially affects confidence.
- Record real limitations rather than converting missing evidence into a success claim.

## Completion gate

A completion record should make it possible to answer:

- What outcome was promised?
- What candidate/state was evaluated?
- What claims had to hold?
- What evidence supports each claim?
- What changed after the evidence was collected?
- What relevant limitation or blocker remains?

Use [`../templates/evidence-record.md`](../templates/evidence-record.md) when a durable evidence bundle is useful.
