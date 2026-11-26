# Test execution strategy

This reference decides **which tests run when and which prior results may be reused**. The project
still owns what to test. [Evidence](../../../docs/EVIDENCE.md) defines claim-to-evidence mapping, and
[minimal sufficient engineering](../../../docs/MINIMAL_SUFFICIENT_ENGINEERING.md) defines test value and
the complexity budget.

“Required verification” does not mean “rerun the full suite after every edit.” It means the selected
evidence must cover the change and its real consumers at the right point in delivery.

## 1. Establish the impact closure

Before selecting checks, map the change to the objects that can actually be affected:

- changed source modules, build targets, configuration, migrations, and entry points;
- callers, protocol consumers, persistence readers, and runtime consumers;
- tests, fixtures, clocks, random seeds, external hosts, toolchains, and dependency locks;
- unchanged components whose external runtime or environment has changed.

Follow shared contracts to downstream consumers. Treat deleted, renamed, generated, or unmapped
objects as widening the affected set. An unknown dependency graph means “scope unknown,” never
“unaffected.”

## 2. Use three execution tiers

| Point | Purpose | Minimum scope |
| --- | --- | --- |
| Development iteration | expose direct errors quickly | static checks, the original regression, direct dependants |
| Pre-merge | prove the complete affected closure and shared boundaries | affected closure, contract tests, deterministic integration checks required by risk |
| Release or installation | prove the distributable artifact and committed user path | clean-source full suite required by the project, then artifact, installation, and user-path evidence |

The same test can supply evidence in more than one tier. Its prior success is reusable only while the
inputs it depends on remain equivalent. Project-required checks remain mandatory; this strategy only
prevents release-wide verification from becoming the default after every local edit.

## 3. Reuse only equivalent passing evidence

A cached or reused result must identify its complete applicability. Relevant inputs include:

- source tree or candidate commit;
- affected dependency closure and lockfiles;
- compiler, runtime, test framework, and test configuration;
- fixtures, test data, environment, random seed, and clock;
- operating system, device, external application, service, or host version when they affect behavior.

Do not reuse a result that was failed, cancelled, timed out, partial, unknown, or made green only by an
unexplained rerun. Do not reuse a passing result after any input that could invalidate it has changed.

Installed or deployed evidence may be reused when the exact artifact bytes, signatures, dependencies,
host, and environment remain unchanged. A source rebuild does not make an affected installation claim
current; neither does an unchanged source tree make an unrelated runtime test current after the host
changed.

## 4. Select tests by impact and risk

Use the project's build graph or test-impact map when available. Otherwise maintain the smallest
credible map from modules or directories to test entry points.

Widen the run when:

- a shared protocol, schema, database, permission, installer, signature, public API, or cross-module
  state changes;
- the source-to-test map is missing, stale, or cannot explain consumer coverage;
- an affected test fails or produces an unknown result;
- the compiler, dependency set, external host, platform, or test harness changes;
- the test infrastructure itself changes.

A small local implementation does not earn a test waiver merely because it is small. A large
repository does not force unrelated suites to run merely because they exist.

## 5. Keep test levels distinct

- Use deterministic unit tests for pure logic and state transitions.
- Use narrow integration and contract tests for protocols, persistence, processes, and shared boundaries.
- Isolate real applications, devices, networks, and host compatibility by version and run them once
  for the compatibility claim they support.
- Verify real user journeys on the installed or deployed candidate; lower-level tests cannot establish
  that layer.
- Run the project-required complete regression from clean inputs for release.

Coverage numbers are diagnostics, not proof that a test has value. A test that only matches source text,
repeats another assertion, or never can fail for a user-visible behavior does not become useful because
it raises coverage.

## 6. Repair costly suites before deleting tests

For a large or slow suite:

- split by business boundary and share construction through a small fixture;
- replace repeated real application or device loading with in-memory fakes where the claim is internal;
- keep one real-resource contract where that compatibility actually matters;
- replace fixed sleeps with events, injected clocks, or bounded polls;
- give each test and the suite an explicit failure timeout;
- terminate the test process group after a timeout so orphan workers cannot continue consuming resources;
- move capability-dependent tests into an auditable conditional group instead of permanently skipping them;
- remove tests for retired behavior together with the retired implementation.

Deleting tests is justified only by retired behavior or proven equivalent coverage. Start with repeated
resource loading, unbounded waits, duplicate fixtures, and obsolete contracts.

## 7. Run the complete suite when required

A clean complete suite remains mandatory when:

- producing a release, installation, deployment, or externally delivered artifact;
- changing shared contracts, persistence, migrations, security, permissions, signing, or installation;
- changing compilers, dependencies, real host versions, platforms, or runtime environments;
- the impact map is unreliable or cannot rule out untouched consumers;
- affected checks fail, return unknown, or recently missed a related defect;
- the project contract explicitly requires the complete suite for that batch.

A complete suite proves regression status for that exact candidate and environment. It does not replace
installation or user-path acceptance.

## 8. Record the execution decision

Record the impact closure, selected checks, reused evidence and cache key, invalidated checks, omitted
scope and reason, complete-suite timing, and separate test/install/user evidence. A local fix may use a
short command-and-result record. Cross-module, release, or high-risk work should link the project's
evidence record.

## Industry practice basis

GSE adapts the shared pattern without requiring a specific build system:

- [Bazel Test Encyclopedia](https://bazel.build/reference/test-encyclopedia): test targets, timeouts,
  and result states;
- [Bazel Remote Caching](https://bazel.build/remote/caching): complete-input identity for result reuse;
- [Gradle test caching](https://docs.gradle.org/current/userguide/java_testing.html#sec:test_caching):
  input/output validity and cache invalidation;
- [Nx affected](https://nx.dev/ci/features/affected): dependency-aware selection of affected tasks;
- [Google test sizes](https://testing.googleblog.com/2010/12/test-sizes.html): resource-based separation
  of test levels.
