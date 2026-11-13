# Collaboration

GSE treats multi-agent organization as a runtime decision shaped by dependency, risk, and integration cost.

## When delegation helps

Delegate when work can proceed independently, specialist judgment reduces a material risk, an independent evaluator reduces self-verification bias, or parallel execution has meaningful wall-clock value.

Keep work with the root GSE when tasks are tightly coupled, share mutable state, depend on the same interactive environment, or are too small to repay handoff and integration cost. Prefer direct work or concurrent tool calls for a small fix or deterministic collection; do not split work by fixed roles, stages, or headcount. Delegation retains the original task and root outcome owner.

## Sub-agent contract

A useful handoff contains:

- result to produce;
- common baseline;
- read scope and, if applicable, exclusive write scope;
- constraints and relevant authorization boundaries;
- evidence expected from the sub-agent;
- concise return format and unresolved blockers.

The reusable form is [`../templates/handoff.md`](../templates/handoff.md).

Sub-agents return evidence and a reviewable result. They do not close the root task merely because their local scope passed. A consumer may use a stable result as soon as its authorization and dependencies permit; it need not wait for the producer's entire turn or source task to close. The root owner checks the affected consumption result.

## Concurrent writers

Treat a checkout and its Git index/branch as one mutable write scope, even when agents intend to edit different files. Each concurrent writer needs an isolated checkout/branch or an equivalent exclusive write environment with a recorded baseline and relative write scope. Overlapping scopes must be serialized, split, or explicitly integrated against the same known baseline.

Apply the project's repository policy before choosing isolation. When it requires one canonical checkout on `main` and forbids new worktrees, serialize all source and Git writes there; parallel agents may inspect, research, or review without writing to that checkout. An isolated checkout is an option for projects that permit it, not a GSE requirement or an exception to local rules.

Protect unrelated dirty changes. A failed task cleans up only resources and changes it owns.

## Integration

The root GSE integrates candidates by checking baseline compatibility, scope, diff, evidence, and conflicts. Evidence attached to an older candidate is invalidated when a later change can affect the claim it was meant to prove.

Assign one accountable operator at a time to each shared build slot, installation target, desktop, device, or release channel. Do not start a competing operation or mutate a build's inputs while that operation depends on them. Coordinate actual shared capacity rather than adding a permanent concurrency limit. Independent development builds in separate caches that share no protected inputs or release resources do not require step-by-step release or desktop permission. The exact capacity and release cadence remain product decisions.

Carry tightly dependent steps and a shared interactive session continuously to a complete business-safe point: the intended operation and necessary save/readback are complete, its effects are known, and the next operator can proceed safely. A tool step or checkpoint alone does not require a handback. With no ready waiter for the resource, continue similar authorized work without releasing and requesting it again. When a waiter is ready, hand over at that safe point; release resources no longer needed while retaining outcome responsibility. Keep changes small enough to review and observe on the product's fast feedback surface.

Separate the **change owner** from the **release lane owner**. The latter can batch publication for several changes after checking candidate identity and each change's inclusion; it does not silently inherit or close their outcome contracts. A busy lane is a scheduling dependency with an owner and wake event, not automatically a blocked feature. See [continuous delivery states](LIFECYCLE.md#continuous-delivery-states).

## Messages and handover

Cross-task messages carry a consumable result, an actual resource handover, a new blocker, an unknown side effect, or a necessary correction. Supply the source task, changed artifact, necessary evidence, resource state, and next action. Reuse the original record rather than building parallel status ledgers or forwarding the same result through several layers.

An acknowledgement, final receipt, no-reply message, or unchanged status does not request another execution round. Preserve explicit pauses and budget controls. Reconcile uncertain effects and confirm the old writer has stopped or is effectively isolated before admitting a replacement. In-turn progress, cross-turn wakeup, and standing automation each require their own applicable authorization and supported mechanism; see [continuation](LIFECYCLE.md#continuation-and-compaction).

## Review scope and evidence reuse

Proposal review checks the intended approach and execution readiness. Code review checks a candidate implementation. Formal-report review checks the claims and evidence presented to its audience. Runtime validation proves affected behavior. Apply each only under its own user, project, or platform requirements; one does not automatically trigger the others. Candidate-level independent code review is required by an explicit user instruction, an applicable project contract, or a specific high-risk gap. Preserve existing user-required and platform-required checks.

Reuse evidence that covers the same candidate, environment, scope, and required independence. One independent review may satisfy multiple entrypoints for claims it actually checked; loading GSE, EGM, and a project template does not require separate panels. A change invalidates only affected conclusions. Keep uncovered claims explicit and recheck substantive changes rather than repeating valid review. Proposal-review mechanics remain in the [EGM reference](../skills/generative-software-engineering/references/egm-review.md).

## Measuring collaboration

Compare organizations on the same task inputs and environment. Record final quality, total model/tool cost across all participants, elapsed time, handoff count, rework, and failure modes. Do not infer efficiency from the root agent's token count alone.

The benchmark protocol is defined in [`../research/BENCHMARK_PROTOCOL.md`](../research/BENCHMARK_PROTOCOL.md).
