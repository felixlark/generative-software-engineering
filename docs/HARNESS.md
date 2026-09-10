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

GSE semantics must not depend on a particular model name, context-window size, UI, orchestration API, or vendor-specific role structure. Runtime capabilities can improve how the lifecycle is executed without changing who owns the outcome or what constitutes adequate evidence.

## Deterministic state and semantic judgment

Use model reasoning for ambiguous intent, planning, diagnosis, tradeoffs, and interpretation. Use deterministic mechanisms where identity, concurrency, schemas, permissions, candidate binding, or evidence integrity must be exact.

## Harness evaluation

A harness should be evaluated by whether it helps a root GSE complete real outcomes with lower failure, coordination, and recovery cost. Feature count alone is not a useful measure.
