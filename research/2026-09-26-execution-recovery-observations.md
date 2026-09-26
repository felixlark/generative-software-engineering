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

## Subsequent capacity recovery and delivery observations

A different idle original owner had no persisted goal and failed a fresh turn with an explicit model-capacity error. The coordinator used the supported desktop messaging interface with a task-local alternative model, retained the existing queued operation and activation fence, and observed its exact acknowledgement. The original owner then returned a hashed result receipt and resolved the read-only operation successfully. This establishes consumption and useful completion of that operation without a user resume action; it does not establish the simulator feature's acceptance or source closure. The blocked-goal owners described above still lack equivalent consumption evidence. This is one observed recovery, not a reliability estimate or proof that every stall shares this cause.

Two further delivery defects were corrected: a logical writer permit remained held after physical writer release while the same operation continued testing; and a prebuilt installer required its frozen candidate to equal the advancing mainline HEAD. The first now supports an owner-checked, receipt-bound stage release for acknowledged attempts. The second permits a frozen candidate that is an ancestor of mainline while rejecting downgrade or divergent ancestry relative to the installed candidate. Neither change removes physical locking, candidate integrity, or acceptance requirements.

A subsequent signed Mac build was installed, its provenance and new read-only source-inspection command were verified, and official native interaction navigated from the research board to the development board and selected the product project. The runtime resource check passed. This bounded installation smoke is not acceptance of every bundled feature. Separate iOS tests and actual simulator journeys retain their own candidates and obligations.

### Evaluation implications

Record the following separately, including failed and unresolved cases:

| Measure | Evidence needed |
| --- | --- |
| Engineering user interventions | Count actual user control-plane actions; keep product acceptance and identity verification separate |
| Recovery latency | Failure observation to exact consumption, and consumption to useful result |
| Outcome latency | Original intake to required source closure; unresolved cases remain censored |
| Coordination cost | All owner/coordinator/model tokens, tool calls, failed attempts and wall time |
| Effective throughput | Accepted requirements per elapsed time and resource budget, not messages or commits |
| Safety | Duplicate side effects, conflicting writers, stale candidate evidence and incorrect closure |

No aggregate cost or performance claim is justified by these observations. Reproducible evaluation should compare passive status reporting, timer-driven reconciliation, and event-driven reconciliation under the same task set and capacity, with controlled dropped events, capacity failures, stale blockers, late executors and candidate advancement. The current human/agent coordinator still performs diagnosis and task-local model selection; autonomous policy selection and safe arbitrary executor takeover remain unimplemented.

The official App Server documentation was fetched again on 2026-09-26. It states that thread resume alone does not update the thread timestamp, read does not load the thread, turns emit error/completion events, and model changes can be applied on resume. These distinctions support the observation model, but do not override deployment-specific tool permissions or prove desktop ownership from an independent App Server.


## Failed wake, executor continuation, and closure audit

Further observations distinguish delivery of an input from execution of its engineering operation. Two historical sessions failed during remote context compaction. A provider-specific official diagnostic identified an obsolete loopback endpoint and connection refusal, while the public service remained reachable. The supported configuration interface removed only that stale override with a version precondition; all other parsed configuration remained identical. Subsequent HTTP reachability and authenticated WebSocket handshake checks passed. A single fenced wake per affected session nevertheless failed again during compaction. The concrete endpoint used by those loaded sessions was not established; stale loaded configuration remains a hypothesis, not a verified cause. No identical wake was repeated after this failure.

The operation journal now permits an explicit repaired wake only with fresh official terminal-failure, queue/input, desktop, goal and repair evidence. It retains the original operation attempt and a per-failed-turn recovery history. Unknown effects, active execution, blocked or paused goals, budget/approval restrictions and unrelated acknowledgements do not qualify. An exact input found in a failed turn can acknowledge delivery without proving any engineering action. Inbound delegation messages must be distinguished from tools invoked by the target executor. Concurrent reservations and restart recovery were tested to prevent a second sender for the same failed wake.

Official readback then established that the two new failed turns contained only incoming coordinator messages, no engineering execution; their queues were empty and goals absent. The already existing coordinator completed the two independent read-only preparation operations, explicitly retaining the original outcome owner, identifying itself as executor, and recording the failed-turn and authorization evidence. Both original attempts obtained result receipts. This is useful continuation after a failed original session, not arbitrary write takeover, repair of the original compaction path, or closure of the underlying product requirements.

Other observed changes were implemented in the same delivery journal:

- Pre-dispatch diagnostics expose missing or expired resource observations, pending predecessors and unresolved owner attempts. Registration age is not mislabeled as last useful progress.
- A late queue response cannot overwrite a result already acknowledged or completed by the owner.
- Explicit null source generation is preserved for genuinely unversioned sources. A missing field remains unknown; operation review revisions do not become source generations.
- Recovery reads one full historical turn per page under the existing time and total-turn bounds. It still checks the persisted dispatch boundary and duplicate exact input identities. The observed large-response failure motivated this change; no comparative latency claim is made.
- A read-only source preflight verifies the reviewed gate list against source/owner/contract/candidate identity, recursive predecessor evidence, current inputs, receipt hashes and unresolved attempts. It excludes only its own acknowledged dependent closeout operation to avoid a self-dependency. The preflight explicitly does not establish complete contract coverage, source lifecycle closure, or user acceptance.

The graph suite passed 39 behavior tests at the recorded implementation revision. A live preflight over the current cross-platform acceptance operations correctly reported engineering readiness false, retaining failed mobile authentication journeys and incomplete Mac interaction coverage. This is a negative real-state check; no fully closed software requirement or end-to-end reliability rate is claimed. Two simulator installations and their version readbacks are separate from failed authenticated message journeys.

### Reproduction and evaluation boundaries

The corresponding product implementation commits are `081d8119` (pre-dispatch diagnostics), `6db8c3a3` (late response race), `e6666812`/`f4e3ce1d` (source generation), `3bea5d86`/`ab49138a` (fenced repaired wake) and `3bf0e212` (source preflight and bounded history pages). Private deployment, failure, configuration comparison and continuation receipts remain local; publishing raw identities or payloads is not part of this record.

An evaluation must count failed wake attempts and coordinator work, distinguish input delivery, engineering execution, operation completion and original requirement closure, and include unresolved outcomes in the denominator. No aggregate token, monetary cost, throughput or reliability improvement can be inferred from these cases. A future source-closeout adapter must also test missing gates despite a completed goal, incomplete goal-less results, wrong source or generation, stale evidence, duplicate effects and interrupted projection writes. The current preflight and manual supported lifecycle convergence do not constitute a fully autonomous release-and-close controller.


## Exact source generation and concurrent wake observation

Product commit `47b8338f` repairs a concrete preflight omission: direct required gates and the self-closeout exemption now compare the actual source generation, including explicit null, in addition to source, owner and contract. The new regression first reproduced incorrect readiness for a mismatched generation; all 40 graph tests passed after repair. Historical operation revisions remain immutable and cannot be silently accepted as source generations. Reuse requires an explicitly evidenced current-generation verification node depending on the historical evidence, without replaying the original build or external effect. The frozen worker was installed and its hash and a subsequent reconciliation tick were read back; the companion Skill matched the frozen commit. These are deployment and regression observations, not source closure.

A live resource-contention case then exposed a queued, unacknowledged notification acceptance operation holding a logical desktop permit while a signed Mac candidate waited for installation. Two coordinators independently inspected this gate. The first recorded its activation; the second reservation returned `may_send=false` and did not send again. Official readback subsequently showed an in-progress turn on the original owner. This demonstrates concurrent activation suppression in one real case. It does not yet prove operation consumption, permit release, Mac installation or final acceptance. Those later observations must be recorded separately.

The candidate build completed successfully and released its build permit. The original owner clarified that its contract requires local signed installation and affected simulator journeys, with no TestFlight distribution obligation. This prevents expanding one source into unnecessary publication while preserving all of its actual acceptance gates. No aggregate speedup or fully closed software case is claimed.


### Follow-up: consumed execution and resource handoff

The same notification operation subsequently completed an official installed-app read-only journey, produced a result receipt, released its desktop permit and reached a terminal original-owner turn. Independent hash checks matched the operation and release receipts; activation was recorded consumed. The desktop summary reader still returned an empty item list, while the official full persisted turn contained command and Computer Use execution. Empty summary items must therefore not be treated as evidence of no execution. Earlier in-flight persisted interruption status was likewise insufficient to infer termination while the desktop showed active.

After the release, the waiting Mac installation remained unrunnable because its resource observation had expired. The engineering coordinator refreshed the observation from the completed owner's explicit handoff and dispatched the already registered successor operation. This proves release-to-successor dispatch with coordinator participation; successor consumption and installation were still pending at the time of this note. It also identifies a remaining automation boundary: event delivery must refresh actual resource observations, not merely record release or rely on an old availability snapshot. No user action, duplicate business operation or forced lock removal was used. The original live-notification and actionable-handoff product gates remain unobserved, so the source is still open.

### Follow-up: successor installation and remaining controller boundaries

The successor subsequently consumed its exact attempt and installed signed Mac build 334 from frozen candidate `7da93accf9a5467761deafbb6074a93f15c5f7aa`. Its hashed receipt records official Computer Use interaction on an isolated completed-message fixture: summary title, lifecycle-specific ordering, nonempty result, expandable original content, reachable fixed actions, and return to the selected message. The ordinary installed application was restored and the resource check passed. This extends the earlier observation to actual successor execution and bounded installation acceptance. It does not close the original cross-platform requirement: authenticated mobile journeys remain unresolved, and fixture evidence has narrower coverage than live source evidence.

Inspection of the deployed implementation distinguishes automatically refreshed writer/build-lock observations from desktop/device observations that still require a supported tool and an engineering actor. A resource-release event clears a logical permit; it does not prove physical availability at the later dispatch instant. Simply extending the observation TTL or translating every release into “available” would hide this gap rather than repair it.

The next controller design should make an expired observation a prerequisite operation owned by engineering, with one deduplicated observer request per resource and observation epoch. A supported resource adapter should return current identity, occupancy and acquisition evidence; only then may a waiting executor claim the physical resource. If the adapter is unavailable, a bounded repair operation retains responsibility and its next check. This is a proposed extension, not an implemented autonomous observer. Unknown prior effects, user pauses and budget/approval controls remain fences under the normative [recovery contract](../docs/HARNESS.md#execution-recovery-ownership).

Closure needs an independent final transition: validate the original required gates, exact source generation, candidate and evidence; perform only the supported source lifecycle action; read back its terminal result. Operation success, a completed agent turn and source closure remain distinct. A missing source in a board query is not proof of archival or successful closure. The source-closeout adapter remains incomplete.

Official references checked on 2026-09-26:

- [Kubernetes Controllers](https://kubernetes.io/docs/concepts/architecture/controller/): observation, corrective action and current-state reporting form a control loop; independent controllers can manage separate concerns.
- [Temporal Activity Execution](https://docs.temporal.io/activity-execution): task loss is handled through timeout and retry semantics; external completion may arrive through asynchronous completion, signals or polling. Retry does not establish that an external effect is safe to repeat.
- [Temporal History Service](https://github.com/temporalio/temporal/blob/main/docs/architecture/history-service.md): persisted history tasks and a transactional outbox connect durable state changes with eventual dispatch. This motivates testing a crash between journal persistence and send, without claiming the current agent harness implements Temporal's guarantees.

For evaluation, distinguish event-triggered execution with coordinator assistance from fully autonomous observation and execution. Include idle-owner consumption, stale observations, lost completion responses, restart recovery and source-closeout interruption. Report unresolved outcomes and all coordinator cost; no aggregate reliability, throughput or novelty claim follows from this single successful resource handoff.
