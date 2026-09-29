# Lifecycle

A GSE task uses a recoverable lifecycle:

```text
Understand → Inspect → Define outcome → Plan → Delegate if useful
→ Implement → Verify → Integrate → Deliver → Maintain
```

The sequence is a semantic lifecycle, not a mandatory waterfall. Steps may overlap, repeat, merge, or be skipped when the result remains unambiguous and adequately evidenced.

## Outcome contract

Before a non-trivial change becomes implementation work, record enough of the following to make completion testable:

- `original_outcome`: the user's intended result.
- `accepted_scope`: what this task owns.
- `non_goals`: only when needed to prevent a real ambiguity.
- `invariants`: behavior or state that must remain true.
- `affected_surface`: code, data, runtime, UI, integration, or operational surfaces touched.
- `completion_evidence`: observations required to justify closure.

For delivery work, also state the **observable target channel** at intake: integrated preview, internal build, distributed release, or a particular user acceptance result. Choose the smallest target that fulfills the actual request. Every source uses the same responsibility model. Derive required gates from the affected surfaces and the accepted outcome; feature, bug, feedback, and release labels do not add or remove gates. Changing this target later requires an explicit user decision or a newly observed requirement, not a convenient reinterpretation of a blocked task.

Use [`../templates/outcome-contract.md`](../templates/outcome-contract.md) when a persistent record helps.

## Inspect before changing

Inspect the repository, runtime, active work, and relevant history before editing. Preserve user changes and established system behavior unless the outcome requires changing them. Treat the current system as evidence, while distinguishing implemented behavior from stale plans or documentation.

## Continuation and compaction

A long-running task must remain recoverable without replaying the full conversation. Preserve at least:

- `original_outcome`
- `accepted_scope`
- `non_goals`
- `completed_work`
- `active_assumptions`
- `stable_ids`
- `important_tool_outcomes`
- `unresolved_blockers`
- `next_concrete_goal`

When finalizing a design after lossy compaction, use summaries as retrieval aids and verify consequential choices against original user messages and actual question responses. A submitted question, preselected recommendation, or delivery acknowledgement is not an answer. Preserve source identifiers, apply explicit corrections and later replacements in order, and distinguish confirmed requirements, engineering defaults, unresolved capability checks, and implementation evidence. If the original source cannot be recovered, disclose the unverified decision instead of inventing confirmation. Update each rule in its owning document and synchronize affected design, tests, operations, and skill entrypoints; keep superseded requirements out of active specifications.

A context boundary, sub-goal completion, or passing test is a checkpoint. It is not a reason to stop while safe in-scope work remains.

## Continuous delivery states

Keep implementation and distribution distinct without losing ownership:

| State | Evidence and next action |
| --- | --- |
| `patch_ready` | Owned diff and focused checks are reviewable; integrate against the current target. |
| `integrated_preview` | Exact commit is on the integration line and observable in the promised fast feedback surface; record any remaining release obligation. |
| `ready_for_release` | Candidate, included changes, and required checks are known; a release lane owns the next publication action. This is queue state, not an external blocker or a shipped result. |
| `released` | The requested channel has a read-back distribution or deployment receipt bound to the candidate. |
| `accepted` | The affected user path has been exercised on that channel, when the outcome requires it. |

These are evidence states, not a mandatory sequence for every change. A product may combine stages or omit a channel that the outcome does not require. One release may carry several changes; each retains its original owner and promised target. The release lane owns the shared publication operation, while the root owner remains responsible for resolving any unmet promise on its source task. Never close an issue merely because it entered a release queue.

Integration is part of reaching the promised outcome. Do not require the source task to be in a successful terminal state before its owned, verified patch can be integrated; that makes integration and closure depend on each other. Admit a patch using its provenance, exact diff, baseline, and relevant focused checks, then verify the integrated candidate on the target feedback surface before closing the task at its agreed delivery target.

If a shared writer, environment, or tester is busy, record the current owner, the exact next gate, and the event that will make the work runnable. Use a supported event or scheduler continuation to resume the original task when needed. An active status, a completed agent turn, or a document saying “continue” cannot execute a future action. If no continuation mechanism exists, expose that operating gap explicitly instead of marking the work complete or falsely blocked.

## Closure

Close the task only when one of these conditions holds:

1. the accepted outcome is complete and relevant evidence has been refreshed after the final candidate change;
2. a verified blocker prevents further safe in-scope progress and the next required external action is explicit; or
3. the owner of the intent changes or stops the scope.

Maintenance feeds observed failures, user feedback, and research findings back into the smallest change that improves the software entity or the method.

## Candidate and release identity

A source commit identifies code. Each new installable candidate has a platform build identity and immutable artifact digests. A user-facing product version identifies a release batch; individual edits need not change that version. Use patch increments for compatible fixes, minor increments for compatible feature additions, and major increments for product-defined incompatible changes. Projects own their initial version and concrete batching thresholds.

Mac, mobile, and other platforms share the lifecycle and release inclusion contract while using their actual verification and distribution channels. A simulator artifact and a signed device archive require distinct identities and applicable evidence even when built from the same source. Batch on a bounded age or count threshold, allow urgent work to advance, and freeze inclusion so incoming changes cannot postpone ready work indefinitely. Triggering a batch schedules publication work; only a real channel receipt proves delivery.
