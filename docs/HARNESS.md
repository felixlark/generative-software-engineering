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
