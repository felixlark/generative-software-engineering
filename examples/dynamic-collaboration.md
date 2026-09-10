# Example: dynamic collaboration

## Intent

A product has five requested fixes spanning UI, persistence, networking, and packaging. The requests arrived together, but they differ in dependency and risk.

## Outcome contract

All five user-visible outcomes must work in the same integrated candidate. Existing unrelated behavior must remain intact. Completion requires evidence appropriate to each affected surface plus an integrated user-path check for changes that interact.

## Organization decision

The root GSE first inspects the system and dependency graph. Two fixes touch the same persistence path and stay with one writer. A packaging fix is independent and goes to a temporary sub-agent in an isolated checkout. A networking investigation goes to a second sub-agent because it can produce an independent diagnosis without writing shared state. The remaining UI fix stays with the root because it depends on the persistence result.

There is no permanent product/developer/tester/director pipeline. The temporary organization is shaped by the actual work.

## Work and integration

Each delegated task receives a concrete outcome, baseline, write scope, evidence requirement, and handoff result. The root integrates the candidates, resolves interactions, and remains responsible for the final software entity.

## Evidence

Focused checks prove the local fixes. Packaging is validated on the produced artifact. Networking evidence reproduces the real failure mode and verifies the corrected path. The final candidate is exercised through the affected user journeys after integration.

## Completion

The task closes only when the five requested outcomes are present in one maintainable candidate and the evidence still applies after integration. Parallel activity by itself is not evidence of progress or completion.
