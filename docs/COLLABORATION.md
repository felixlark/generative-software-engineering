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

Each concurrent writer owns one checkout/branch or an equivalent isolated write environment. Record the baseline and relative write scope. Overlapping write scopes must be serialized, split, or explicitly integrated against the same known baseline.

Protect unrelated dirty changes. A failed task cleans up only resources and changes it owns.

## Integration

The root GSE integrates candidates by checking baseline compatibility, scope, diff, evidence, and conflicts. Evidence attached to an older candidate is invalidated when a later change can affect the claim it was meant to prove.

## Measuring collaboration

Compare organizations on the same task inputs and environment. Record final quality, total model/tool cost across all participants, elapsed time, handoff count, rework, and failure modes. Do not infer efficiency from the root agent's token count alone.

The benchmark protocol is defined in [`../research/BENCHMARK_PROTOCOL.md`](../research/BENCHMARK_PROTOCOL.md).
