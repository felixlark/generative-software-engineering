# Example: recovery across context loss

## Intent

A multi-day migration must continue across model-context compaction and handoff without silently losing requirements, completed work, or verification state.

## Outcome contract

The migrated system must preserve the accepted behavior and data contract. Work must remain recoverable after context loss. Completion requires migration evidence against the final candidate and a record of any external blocker that still prevents closure.

## Recoverable state

Before a context boundary, the root GSE preserves the original outcome, accepted scope, completed work, active assumptions, stable identifiers, important tool outcomes, unresolved blockers, and the next concrete goal. Large logs and transient reasoning are not treated as durable project state.

## Continuation

The next context resumes from the durable state, checks the current repository and runtime rather than replaying the old conversation, and refreshes evidence invalidated by subsequent changes. A passing checkpoint is treated as progress, not as a reason to stop while safe in-scope work remains.

## Evidence

The handoff can identify the exact candidate, completed migration steps, remaining work, and evidence already collected. Final validation is run against the integrated migrated system, including the user or external path when lower-level checks cannot prove the required behavior.

## Completion

The task closes when the accepted migration outcome is complete with refreshed evidence, or when a verified external blocker makes the next required action explicit. Context loss does not redefine the task.
