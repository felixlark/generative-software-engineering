# Delivery closure heartbeat

Use this reference when the user explicitly requests a recurring check that keeps software requirements moving through development, testing, release, and user acceptance. Apply repository rules and original authorization first. The heartbeat is a continuation mechanism, never evidence of delivery by itself.

## Scope and source of truth

- Reuse the original requirement, stable source ID, root owner, accepted outcome, and Goal or task. Do not create a duplicate requirement, incident, status database, or parallel ownership record for each stage. A project board is a projection; read its source when labels conflict.
- At each run, inspect only the accepted scope and directly blocking dependencies. Read current source task or Goal, Git candidate and dirty ownership, relevant checks, installed or deployed version, runtime health, user-path evidence, and external release receipts. Historical counts, old screenshots, and a previous heartbeat's summary are leads, not current proof.
- For remote releases, reconcile the local candidate receipt, archive or artifact identity, platform build identity, distribution availability, and real installed version separately. A remote build marked valid proves the platform has a build number; a local upload receipt proves what the local command attempted. Neither alone proves that the remote binary contains a particular commit or that users received it. Resolve a reused build number or uncertain upload by readback before any retry; never upload the same number merely because an earlier task called it missing.
- Keep project-specific paths, device identities, lifecycle commands, and release rules in that project's authority documents. A generic heartbeat must not infer permission to push, upload, publish, delete, send, or change production settings.

## Per-requirement closure contract

Track the next unmet gate in the original task, with an evidence link or explicit `not_applicable` reason for each gate:

| Gate | Readback needed |
| --- | --- |
| Admission | Original outcome, unique owner/source, affected surfaces, invariants, permissions, and acceptance path |
| Development | Exact owned change and commit; focused validation and unresolved failures |
| Integration | Target branch/candidate SHA, included requirements, cumulative diff, and checks against that candidate |
| Install or deployment | Actual running version and health; remote build, service, or distribution receipt when required |
| User acceptance | Real affected user path, data identity, visible result, and recovery behavior on the same valid candidate |
| Source closure | Original Goal/task and any applicable feedback or incident generation in a supported terminal state; temporary resource ownership released |

Do not mix evidence from different candidate SHAs, builds, configurations, accounts, devices, or user paths. A later change invalidates only the gates it affects; reassess that impact instead of blindly repeating every check. For multi-platform requirements, close only after every affected platform has its required evidence or the original outcome explicitly excludes it.

## Heartbeat decision loop

1. **Reconcile.** Compare source status with evidence. Flag false closure (`task_complete`, board `completed`, green CI, install, or upload without user acceptance), missing gates, stale candidate identity, and contradictory blocker labels.
2. **Deduplicate.** Match by stable source ID and outcome. If another task owns the next step or a device/build/release slot, preserve that owner, inspect its progress, and avoid concurrent writes, installs, or duplicate external actions. A pending job is not completion.
   When an old blocker becomes false, return the fresh evidence to the original owner and resume only the next safe gate. Do not infer that every later gate passed.
   Treat an `active` task or a held lease as ownership, not proof of forward progress. Check its latest meaningful event and, where applicable, the live process or device session before waiting again. If no progress is visible across the relevant cadence, inspect the specific dependency or ask the original owner for one focused status readback; do not spawn a replacement owner or repeat the same probe without new evidence.
3. **Choose one next action per actionable requirement.** Prefer the item closest to user delivery that can use available capacity. Run a focused check, repair a tool or environment failure, integrate an owned patch, validate a running candidate, or continue the original task. Use an independent evaluator only where risk merits it. Recheck unknown side effects before any retry.
4. **Handle blockers precisely.** Record the blocking condition, owner, evidence, smallest recovery action, and recheck trigger. Busy shared resources and ordinary tool errors call for coordination or repair; they are not automatically external blockers. Keep a Goal active while safe in-scope work remains. Pause or mark blocked only under the applicable Goal lifecycle rules and after confirming a true dependency on user action or external state.
5. **Close by readback.** Reconcile all required gates and the original terminal state after delivery; release task-owned resources. Stop or pause a task-specific heartbeat once its accepted outcome is closed, so later runs cannot reopen or duplicate it. Notify the user on meaningful progress, failure, completion, or a required decision. Stay quiet when the state is unchanged and no action is possible; do not send repetitive status messages or claim that scheduling itself fixed the problem.

Run the loop on meaningful events such as a commit, check result, installation, device release, deployment receipt, user acceptance result, or source status change. If the user requested a timer, choose a cadence proportionate to the system and use the supported automation tool. Prefer updating an existing matching automation. After creating or changing one, verify a subsequent scheduler-fired run and a fresh source or evidence readback; an `ACTIVE` setting alone is not execution proof. The scheduled prompt must preserve scope, source identities, authorization boundaries, and the instruction to act on the next safe gate rather than merely summarize it. A recurring run may inspect and advance work, but it must not silently take over another active writer or device owner.

Review the supported Scheduled recent-runs surface when available. Official documentation supports minute-based tasks in an existing chat but does not specify how a run is queued while that chat already has an active turn; absence of a visible new turn during an active turn does not, by itself, prove scheduler failure. If the run-history surface is unavailable or rate limited, record that verification is pending and back off rather than repeatedly refreshing it or reading private app state.

## Failure patterns this prevents

- **Too many open starts:** limit work in progress by the actual writer, build, desktop, device, and release capacity; finish a usable vertical slice before pulling another overlapping implementation.
- **Status conflation:** report code, tests, integration, install or deployment, runtime, user acceptance, and source closure separately. Board or agent turn completion is only its own event.
- **Candidate drift:** freeze the identity of a release candidate without freezing the whole repository; keep evidence bound to that candidate and update only affected gates after changes.
- **Lost ownership:** delegate bounded subwork, then return evidence to the original root owner; the heartbeat resumes that task instead of spawning a replacement.
- **Retry loops:** diagnose a changed hypothesis before retrying; if an operation may already have succeeded, read back its receipt before repeating it.
