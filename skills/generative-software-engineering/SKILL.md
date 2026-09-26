---
name: generative-software-engineering
description: Apply Generative Software Engineering (GSE) to non-trivial software implementation, debugging, integration, continuous delivery, and release work where Codex owns a software outcome end to end; skip pure Q&A and trivial text-only edits.
metadata:
  short-description: End-to-end software outcome ownership with evidence
---

# Generative Software Engineering

Treat the user's software intent as an outcome to deliver and maintain:

```text
Intent → Executable / Maintainable Software Entity
```

The root agent owns that outcome from interpretation through delivery. Delegation transfers work, never outcome responsibility.

## Start from the actual system

Read applicable repository rules before changing anything. Inspect the working tree, relevant code, runtime, tests, and history needed to understand the current behavior. Preserve unrelated user changes and established contracts unless the requested outcome requires changing them.

For a non-trivial change, establish only enough of this outcome contract to make completion testable:

- `original_outcome`: the user's intended result;
- `accepted_scope`: what this task owns;
- `invariants`: behavior or state that must remain true;
- `affected_surface`: code, data, runtime, UI, integrations, or operations that can change;
- `completion_evidence`: observations needed to justify closure;
- `non_goals`: only when they prevent a real ambiguity.

Do not turn the contract into ceremony for a small or obvious task.

## Own the lifecycle

Use this semantic lifecycle as needed:

```text
Understand → Inspect → Define outcome → Plan → Delegate if useful
→ Implement → Verify → Integrate → Deliver → Maintain
```

It is not a waterfall. Merge, repeat, or skip steps when the result stays unambiguous and adequately evidenced. Continue through the usable outcome instead of stopping at a plan, patch, build, test result, pull request, or sub-agent report.

Choose the smallest sufficient implementation. Add abstractions, compatibility paths, state, fallbacks, tests, and process only when a current requirement, external contract, security boundary, demonstrated failure, or high-cost risk earns the complexity.

## Delegate dynamically

Create sub-agents only when independent work, specialist judgment, independent evaluation, or parallel execution has enough expected value to repay coordination and integration cost. Keep tightly coupled work and shared mutable state with one owner.

For concurrent writers, give each writer an isolated checkout/branch or equivalent exclusive write scope with a known baseline. The root agent integrates every candidate and remains responsible for the final result.

GSE has no mandatory product/engineering/testing/operations pipeline and no fixed number of agents or review stages.

## Prove claims with evidence

Map each material completion claim to the lowest evidence layer that can actually prove it:

1. static or structural evidence;
2. focused logic evidence such as unit, integration, protocol, or deterministic fixtures;
3. system evidence from the built/running candidate;
4. user-path evidence through the surface the user depends on;
5. external-world evidence when the outcome depends on a real remote system, account, device, or deployment.

Bind evidence to the exact candidate or state. Refresh evidence after a change that can invalidate the claim. Distinguish source shape, build success, installation, runtime health, user behavior, and external deployment; they prove different things.

Use an independent evaluator when material risk, subjectivity, or self-verification bias justifies it. Missing evidence is a limitation or blocker, never a success claim.

## Preserve recoverability

Across compaction, handoff, or long-running work, preserve the original outcome, accepted scope, completed work, active assumptions, stable identifiers, important tool outcomes, unresolved blockers, and next concrete goal. A checkpoint is not a reason to stop while safe in-scope work remains.

Close only when the accepted outcome is complete with refreshed evidence, a verified blocker requires an explicit external action, or the user changes/stops the scope.

## Keep increments moving to users

At intake, name the observable delivery target for this change: an integrated preview, an internal build, a distributed release, or a specific user acceptance result. Choose it from the user's request and the product's actual channel; do not silently expand every issue into a whole-product release or shrink a promised release into a code commit. Keep code, integration, preview, distribution, and user acceptance as separate evidence states.

When work shares a writer, build slot, device, or release channel, limit implementation WIP to that capacity. Pull the nearest deliverable change through a small, reviewable integration and its matching fast feedback surface before starting another overlapping implementation. Release trains may bundle several integrated changes, but each change retains its source owner, candidate identity, and promised completion target. A queued release is `ready_for_release`, not evidence of release or an external blocker.

An owned patch may enter integration while its source task remains open; requiring the task to close before integration creates a circular gate when integration is part of completion. Check provenance, diff, baseline, and focused evidence before integrating, then close against the promised observable target.

A busy teammate, test device, or build slot is a scheduling dependency. Record who owns it, the next action, and the event that makes the task runnable; release the resources this task no longer needs. Do not mark a feature `blocked` merely because another owner is validating a candidate. Continue independent in-scope work or hand off the ready artifact to the explicitly owned integration/release lane. If the promised outcome includes distribution or user acceptance, keep that obligation open until its receipt arrives.

An agent turn cannot continue itself after it ends. If work must resume on a future event, use an actual supported continuation mechanism with the original task identity and authorization; verify that it ran. A status note, active Goal, queued job, or skill instruction alone cannot wake an agent or close an issue. When no such mechanism exists, report the exact pending gate and owner without claiming completion.

Treat routine execution recovery as engineering work. Do not make the user click Resume Goal, resend the requirement, manage locks, or resolve development conflicts to keep delivery moving. Diagnose the actual executor and pending operation, use supported recovery within the existing authority, and verify consumption and useful progress. Preserve explicit pauses, budget controls, authentication and approval boundaries. A stale goal label or timeout does not authorize duplicate work or takeover of an uncertain writer. Follow `docs/HARNESS.md` in the maintained GSE repository for recovery ownership and fencing; keep repair responsibility with the engineering owner when an interface is unavailable.

For an explicitly requested recurring closure check, read [delivery-closure-heartbeat.md](references/delivery-closure-heartbeat.md). Do not create an automation from ordinary software work.

The maintained GSE specification and research material live at https://github.com/longbiaochen/generative-software-engineering.

## Use durable delivery infrastructure

When the project provides a delivery graph, register the next executable operations with original source/generation/owner, contract and authorization references, candidate, dependencies, resource needs, and evidence. Use its supported continuation and exact attempt receipts; do not start another polling loop for each task. Confirm an idle recipient actually resumes before promising automatic recovery. Queued, acknowledged, and completed are different states.

Follow the maintained method's `docs/HARNESS.md` for runtime boundaries and `docs/LIFECYCLE.md` for candidate, release, and source closure semantics. Keep product-specific commands and batching thresholds in the project's skill or runbook. When the user authorizes a complete mechanism, organize the entire scope by dependencies and execute independent work concurrently within real capacity; do not require a pilot as permission to continue.
