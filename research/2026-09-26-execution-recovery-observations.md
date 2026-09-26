# Execution recovery and stale blockers: observations

This engineering record extends the continuous-delivery working paper. It is not a comparative experiment or a novelty claim. Product-private task identifiers and message content are intentionally omitted.

## Observed sequence

Two original requirement sessions retained blocked goals while the desktop reported active turns. Their exact continuation messages remained queued. An independent App Server reported the threads as not loaded, which does not establish the state of the desktop executor. No causal claim that the goal status alone caused non-consumption is supported.

The original blocker descriptions included unavailable device capacity, mainline integration concerns, and an absent distribution build. Subsequent read-only reconciliation found both patches in mainline, an uploaded candidate containing both commits, and a matching build number in the distribution service with VALID state. The candidate receipt and source ancestry are distinct from current interaction acceptance and source-lifecycle closure, which remain unverified. Thus an unavailable owner session need not prevent independent verification from retiring stale assumptions.

A request for the user to manually resume goals was withdrawn: routine engineering recovery belongs to the system. A periodic continuation was configured, but configuration alone is not an execution or delivery receipt. The durable operation journal continues to preserve unresolved attempts; no competing writer or duplicate upload was started.

## Mechanism and experiment implications

The normative rule is [execution recovery ownership](../docs/HARNESS.md#execution-recovery-ownership). Evaluate session recovery and evidence reconciliation separately: they can unblock different portions of a delivery graph. Include a baseline that refreshes blocker predicates against authoritative services, rather than comparing only with a passive task list.

Inject stale blocked labels after successful publication, queued-but-unconsumed inputs, conflicting desktop/persistent status, lost upload responses, late old executors, explicit user pauses, and budget exhaustion. Measure human control-plane interventions, time to invalidate stale blockers, duplicate effects, evidence integrity, and time to source closure. Do not score creation of a replacement session or an active heartbeat as recovery success.

Executor takeover remains a design requiring actual write-boundary fencing and supported control-plane verification. This observation provides no evidence that arbitrary existing sessions can be safely taken over, and does not authorize bypassing runtime restrictions.

## Source read in this revision

[OpenAI Codex App Server](https://developers.openai.com/codex/app-server), retrieved 2026-09-26: distinguishes thread resume, turn start/steer, completion notifications, and goal read operations; recommends the SDK for automated jobs. Interface documentation does not prove deployment-specific takeover safety.

Private raw receipts are retained in the product's local delivery evidence directory. Any research artifact release requires a separate sanitized package and authorization. No paper submission, patent filing, or public disclosure occurred in this revision.
