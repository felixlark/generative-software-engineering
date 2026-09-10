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

A context boundary, sub-goal completion, or passing test is a checkpoint. It is not a reason to stop while safe in-scope work remains.

## Closure

Close the task only when one of these conditions holds:

1. the accepted outcome is complete and relevant evidence has been refreshed after the final candidate change;
2. a verified blocker prevents further safe in-scope progress and the next required external action is explicit; or
3. the owner of the intent changes or stops the scope.

Maintenance feeds observed failures, user feedback, and research findings back into the smallest change that improves the software entity or the method.
