# Collaboration

GSE treats multi-agent organization as a runtime decision shaped by dependency, risk, and integration cost.

## When delegation helps

Delegate when work can proceed independently, specialist judgment reduces a material risk, an independent evaluator reduces self-verification bias, or parallel execution has meaningful wall-clock value.

Keep work with the root GSE when tasks are tightly coupled, share mutable state, depend on the same interactive environment, or are too small to repay handoff and integration cost.

## Sub-agent contract

A useful handoff contains:

- result to produce;
- common baseline;
- read scope and, if applicable, exclusive write scope;
- constraints and relevant authorization boundaries;
- evidence expected from the sub-agent;
- concise return format and unresolved blockers.

The reusable form is [`../templates/handoff.md`](../templates/handoff.md).

Sub-agents return evidence and a reviewable result. They do not close the root task merely because their local scope passed.

## Concurrent writers

Treat a checkout and its Git index/branch as one mutable write scope, even when agents intend to edit different files. Each concurrent writer needs an isolated checkout/branch or an equivalent exclusive write environment with a recorded baseline and relative write scope. Overlapping scopes must be serialized, split, or explicitly integrated against the same known baseline.

Apply the project's repository policy before choosing isolation. When it requires one canonical checkout on `main` and forbids new worktrees, serialize all source and Git writes there; parallel agents may inspect, research, or review without writing to that checkout. An isolated checkout is an option for projects that permit it, not a GSE requirement or an exception to local rules.

Protect unrelated dirty changes. A failed task cleans up only resources and changes it owns.

## Integration

The root GSE integrates candidates by checking baseline compatibility, scope, diff, evidence, and conflicts. Evidence attached to an older candidate is invalidated when a later change can affect the claim it was meant to prove.

Assign one accountable operator at a time to each shared build slot, installation target, desktop, device, or release channel. Do not start a competing operation or mutate a build's inputs while that operation depends on them. Limit concurrent implementation by the capacity of its narrowest shared resource. When that limit is full, help move an integrated change through verification or release before starting another overlapping change. Keep changes small enough to review and observe on the product's fast feedback surface. The exact capacity and release cadence are product decisions, not universal GSE constants.

Separate the **change owner** from the **release lane owner**. The latter can batch publication for several changes after checking candidate identity and each change's inclusion; it does not silently inherit or close their outcome contracts. A busy lane is a scheduling dependency with an owner and wake event, not automatically a blocked feature. See [continuous delivery states](LIFECYCLE.md#continuous-delivery-states).

## Measuring collaboration

Compare organizations on the same task inputs and environment. Record final quality, total model/tool cost across all participants, elapsed time, handoff count, rework, and failure modes. Do not infer efficiency from the root agent's token count alone.

The benchmark protocol is defined in [`../research/BENCHMARK_PROTOCOL.md`](../research/BENCHMARK_PROTOCOL.md).
