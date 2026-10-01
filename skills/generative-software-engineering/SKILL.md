---
name: generative-software-engineering
description: Guide substantial software development that needs cross-component design, coordinated integration, or delivery architecture. Use for features, structural refactoring, and systemic defects; skip localized debugging, routine bug fixes, environment recovery, small configuration edits, and read-only reviews.
metadata:
  short-description: Engineering guidance for substantial software changes
---

# Generative Software Engineering

GSE is a software development method for turning a user intent into usable, maintainable software. Apply it when engineering decisions span components, integration boundaries, or delivery mechanisms.

## Choose the right scope

Routine work follows the project's existing rules and relevant domain skills. Reproducing a bug, inspecting a log, repairing a tool, changing a setting, or making a localized fix does not by itself need GSE. A difficult investigation or a long task is not sufficient reason to load a full development method.

Escalate to GSE when findings require coordinated changes, structural design, or a new integration or delivery approach. State the concrete reason briefly. Explicit user invocation also applies, with detail proportional to the requested work.

Loading GSE does not create a planning gate, role pipeline, Goal, automation, delivery graph, or release project. Use existing project mechanisms when needed. Do not load the full methodology or conditional references by default.

## Develop toward a usable result

For consequential decisions, establish the intended outcome, scope, affected behavior, important invariants, and completion evidence in the existing task record. Obvious details do not need a formal contract or separate document.

Inspect the relevant system, implement a small coherent change, verify it, integrate it, and reach the delivery target implied by the request and existing authorization. These are adaptable engineering activities, not mandatory sequential stages. Do not expand a localized change into a whole-product release or stop a promised user delivery at a code commit.

Prefer established software engineering practices: small batches, short integration cycles, focused regression checks, reproducible candidates, and fast user feedback. Add architecture or process only when a current requirement or demonstrated risk justifies it.

## Coordinate only where needed

Each requested outcome has an accountable task owner. This does not require a permanent project-wide coordinating Agent. Delegate independent implementation, research, or review when its value exceeds handoff and integration cost.

Follow repository policy for source and Git writes. Parallel writers require permitted isolation and known baselines; shared mutable resources require exclusive ownership. GSE does not override local rules or prescribe a fixed agent count.

For multi-task integration, batched releases, resource queues, or stalled delivery continuations, read [delivery-coordination.md](references/delivery-coordination.md). Ordinary fixes do not need this reference.

## Verify the affected behavior

Choose evidence that can prove the actual claim. Focused tests may prove logic; changed user paths need verification on the appropriate running surface. Bind evidence to the relevant candidate or state and refresh only conclusions affected by subsequent changes.

Distinguish implementation, checks, deployment or installation, runtime behavior, and acceptance when those states matter to the request. Use independent evaluation where material risk or subjectivity warrants it; do not add a review stage automatically.

Preserve consequential user decisions and unresolved work across handoffs or context loss. Check original messages before treating a summary or an unanswered recommendation as a confirmed requirement. Close against the accepted outcome and its evidence; identify the exact remaining dependency when it is unfinished.

## Conditional references

- For an explicitly requested recurring closure check, read [delivery-closure-heartbeat.md](references/delivery-closure-heartbeat.md). A scheduled check is continuation, not delivery evidence.
- For methodology design or deeper engineering questions, consult the maintained [specification](https://github.com/longbiaochen/generative-software-engineering/blob/main/docs/SPECIFICATION.md) and its linked owning documents. Product commands and operational details belong in the project's rules and runbooks.
