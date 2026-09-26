# Harness boundary

GSE is a software-engineering method. A harness is the runtime infrastructure that makes the method executable.

A capable harness may provide:

- repository and environment context;
- tools for code, shell, browser, computer, devices, and external systems;
- permission and approval boundaries;
- persistent task and artifact identity;
- isolation for concurrent writers;
- model and reasoning configuration;
- sub-agent creation and coordination;
- logs, test results, screenshots, runtime observations, and other evidence;
- compaction and handoff support.

For delivery to continue across agent turns, the harness also needs an executable wake path: observe a meaningful event (for example a commit, test result, resource release, or deployment receipt), resume the original task or its owned release lane, and read back the resulting state. A skill or active status is instruction and metadata; neither schedules execution by itself. The runtime must preserve idempotency and permission boundaries when retrying uncertain publication actions.

GSE semantics must not depend on a particular model name, context-window size, UI, orchestration API, or vendor-specific role structure. Runtime capabilities can improve how the lifecycle is executed without changing who owns the outcome or what constitutes adequate evidence.

## Deterministic state and semantic judgment

Use model reasoning for ambiguous intent, planning, diagnosis, tradeoffs, and interpretation. Use deterministic mechanisms where identity, concurrency, schemas, permissions, candidate binding, or evidence integrity must be exact.

## Harness evaluation

A harness should be evaluated by whether it helps a root GSE complete real outcomes with lower failure, coordination, and recovery cost. Feature count alone is not a useful measure.

## Durable delivery operations

Represent independently executable operations with original source identity and generation, accountable owner, contract and authorization references, candidate and input identities, dependencies, resource demands, and next action. The source system remains authoritative for the requirement and closure; the execution journal records attempts and evidence references.

Persist dispatch intent before sending, correlate acknowledgements with exact request identity, and reconcile uncertain results before retrying. Resource observations have bounded validity, and scheduling reservations do not replace physical locks. Release resources while waiting for human decisions. Preserve fairness under contention and bound concurrent work by actual execution capacity. Evidence invalidation affects dependent claims and operations, without silently replaying uncertain external effects.

Resource events drive useful work; periodic reconciliation repairs missed events and interrupted processes. Verify both queue admission and actual consumption by an idle original owner. Report separately when a continuation is registered, dispatched, acknowledged, and completed. A successful test against an already running recipient does not prove that an idle task can be resumed.

Explicit full-scope implementation requests should be organized across the complete dependency graph. Independent work may proceed concurrently; correctness checks and component tests remain necessary, but a single-interface pilot is not an additional permission gate.

### Source discovery

An unchanged operation journal does not establish that no new requirement arrived. Before a project-wide reconciler exits on an unchanged queue or digest, it must also reconcile a supported source event cursor or a bounded source discovery pass. Compare stable source identities and meaningful revisions with existing references; inspect only new, changed, or unresolved sources. Preserve the original owner and accepted scope: discovering a discussion request does not authorize implementation. Record intake references in the existing coordination surface, not a second requirement database.

State the coverage boundary, pagination result and observation time. Failed discovery is unknown coverage, not an empty result; retain an engineering recovery action and backoff without replaying work. A canonical-directory listing cannot establish coverage of other hosts, historical directories or projectless sources. Known additional entry points need their own supported observation. Validate discovery with a requirement that arrives while the operation graph is unchanged, including a discussion-only source that must not be dispatched as implementation.

## Execution recovery ownership

Routine development recovery belongs to the engineering system. Do not make a user's click to resume a goal, resend a requirement, release a writer, or resolve a code conflict the sole continuation path. Users participate in product decisions and acceptance; identity verification, new authorization, explicit pauses, and budget limits retain their actual boundaries.

Separate persistent outcome responsibility from an execution session. A goal status, queued message, running-turn indicator, and delivered outcome are different observations. First repair or continue through the supported original execution interface. Independent read-only verification can advance while that interface is unavailable.

Changing executors requires evidence that the old executor has stopped or is effectively fenced at every relevant write boundary, plus preserved source/generation, candidate, authorization, unresolved attempts, and ownership. A journal lease alone does not fence a late process. Timeouts and unavailable sessions do not justify replaying uncertain writes or publications. New sessions must not bypass user pauses, approvals, budget controls, or tool restrictions.

Measure useful recovery by exact consumption, state-changing progress, and eventual outcome closure. State liveness assumptions explicitly: available runtime capacity, supported control interfaces, sufficient authority, and reachable dependencies. When these assumptions fail, the coordinator owns diagnosis and repair rather than silently delegating routine control-plane maintenance to the user.

Recovery decisions use fresh predicates: resource availability, exact queue consumption, executor errors, candidate validity, and unresolved effects. Retain a recovery owner, observation time, next action, wake condition or bounded backoff, and evidence references. A repeated observation is not progress and must not reset the progress clock. Exhausting a repair strategy escalates to an engineering owner for a different diagnosis; it does not automatically assign an operational chore to the user.

When a supported execution interface reports a specific model-capacity failure, an authorized alternative that meets the operation's capability requirements can continue the original work. Keep the scope local to the affected executor, preserve attempt identity and uncertainty fences, and verify consumption and useful output. Capacity failures, usage exhaustion, explicit pauses, and missing approval require distinct decisions. A successful recovery in one case is not evidence that an idle executor without the same error needs the same treatment.
