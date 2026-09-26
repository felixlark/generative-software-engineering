# Evidence-Aware Scheduling for Continuous Agentic Software Delivery

Working manuscript, 26 September 2026. Not submitted; no comparative experimental results. Prepared by the integration owner while the dedicated writing task awaits an unresolved runtime approval. This file is the integration owner's draft; the writing task retains responsibility for literature verification and submission preparation in its assigned directory.

## Abstract

Software agents can finish coding turns while the underlying requests remain undelivered. Concurrent agents share source trees, build capacity, interactive environments, and distribution channels, yet these resources often have independent ownership and recovery mechanisms. A successful dispatch therefore need not imply execution, and a passed test need not remain valid for the released artifact. We formulate continuous agentic delivery as scheduling over requirement ownership, operation dependencies, resource constraints, and artifact–evidence relations. The proposed mechanism combines durable operation attempts, separately acknowledged executor activation, candidate-bound evidence invalidation, and bounded release batching. Its objective is to improve accepted delivery per unit total development cost while constraining unsafe closure, duplicate effects, and starvation. An initial implementation provides transactional reservations, request correlation, resource observations, and release planning. Operational observations expose a gap between queue admission, apparent activation, and actual execution; they do not establish end-to-end liveness or performance gains. We present an evaluation protocol against durable FIFO and established scheduling baselines, with fault injection, cost accounting, and component ablations. Comparative effectiveness remains to be measured.

## 1. Introduction

The unit of software responsibility is an accepted outcome, rather than an agent turn. A request can require modifications on several platforms, an integrated candidate, interactive validation, distribution, and read-back confirmation. These stages have different evidence requirements and resource capacities. Increasing coding concurrency can grow the downstream queue without increasing delivered functionality.

Three failure modes motivate this work. First, mutual exclusion prevents conflicting writes but does not ensure that a waiting owner is resumed. Second, evidence obtained on an earlier candidate may be incorrectly reused after integration changes its inputs. Third, a scheduler can observe successful submission while the recipient never produces execution evidence. A periodic report of these conditions is not recovery.

We investigate whether a joint model of operations, resources, and evidence can reduce these losses at acceptable orchestration cost. The proposed contributions are a delivery contract, an executable recovery protocol, and an evaluation of evidence-sensitive scheduling. The first two have partial implementation support; the third remains a research hypothesis. DAG scheduling, durable execution, locks, and batching individually are established techniques and are not claimed as novel.

## 2. Related work and positioning

Durable workflow systems such as Temporal persist execution and message history [1]. Kubernetes controllers repeatedly reconcile observed and desired state [2]. Incremental build systems such as Skyframe track dependencies and invalidate affected computations [3]. Merge queues validate integrated candidates [4]. Resource-constrained project scheduling supplies the optimization foundation [5]. These systems provide strong implementation and evaluation baselines, rather than straw-man comparators.

Agent frameworks and long-horizon software benchmarks are discussed in the source research note linked below. Their relationship to shared interactive resources, release receipts, and evidence invalidation needs additional full-text review before a literature novelty claim. This manuscript is not a systematic review. The proposed research question concerns the coupling of candidate evidence, executor availability, and delivery scheduling across changing requirements.

## 3. Delivery model

Let Q be requirements with immutable source identity and revision, owner, accepted contract, and authorization references. Let O be executable operations in a directed acyclic dependency graph for the current revision. Requirements may share operations, such as publication of one release batch. Let R be resources with capacities c_r(t), observation validity intervals, and independently enforced physical locks. Let A be immutable candidate artifacts and E evidence records.

An evidence record e identifies its candidate artifact, claim, validator, relevant environment and input digests, outcome, and receipt. Define valid(e,t) only when its receipt is available, its declared dependencies still match, and any applicable time or environmental constraints hold. An unknown dependency is not treated as unchanged. Claims of selective reuse require an explicit dependency contract; unmodeled dependencies remain a threat to soundness.

An operation o is eligible only if its authorization is applicable, inputs are current, required predecessors have valid success evidence, and no unresolved attempt for o exists. A feasible selected set S satisfies sum_{o in S} d(o,r) <= available_r(t) for each resource r, after accounting for outstanding reservations. A scheduling reservation is not a substitute for acquiring the actual source, device, or publication lock.

The semantic lifecycle covers intake, inspection, outcome definition, planning and optional delegation, implementation, verification, integration, delivery, and maintenance. These are responsibilities rather than mandatory serial departments. Feature, defect, and feedback sources use the same model; the accepted result determines necessary gates.

## 4. Recovery and scheduling mechanism

### 4.1 Persistent attempts and activation

Before external dispatch, a transaction records the attempt identity and outbox intent. A response is correlated with the exact client message identity, not a matching text fragment. A missing response enters an unknown state and requires read-back reconciliation. Timeout alone never authorizes replay of a possibly executed external effect.

Queue admission and executor activation are distinct actions. When an official runtime reports that an owner needs activation, the coordinator persists activation intent before calling the supported activation interface. It then records submission and, separately, exact consumption. A new in-progress turn is weaker evidence than an acknowledged operation and tool/output progress. Uncertain activation is also reconciled before retrying.

### 4.2 Reconciliation

```text
on event or bounded reconciliation interval:
    collect source revisions, receipts, executor observations, resource state
    transaction:
        invalidate affected evidence and dependent claims
        retain unresolved external attempts as fenced
        form eligible frontier and select capacity-compatible operations
        persist reservations and dispatch intents
    dispatch through the supported runtime; record exact receipts
    activate idle owners only through a separately fenced activation path
    on execution, reacquire physical locks and recheck candidate/authority
    accept completion only with required current evidence
    release resources and enable dependent operations
```

The initial scheduler uses FIFO and aging. The research variant estimates the incremental cost of required validation after each candidate change, and schedules within a fairness-constrained frontier to reduce redundant validation and accepted completion delay. Estimates are learned or calibrated only from training traces. Hard eligibility and authorization constraints precede optimization. No optimality claim is made.

### 4.3 Version and release identity

A commit identifies source; a platform build identifies a new installable candidate; a user-facing semantic version identifies a release batch. Platforms share the batch identity and requirement inclusion while retaining independent artifact digests and receipts. Simulator binaries and signed device archives are distinct artifacts. An artifact already produced cannot be made safe by deleting a failed requirement from its inclusion list.

Batch admission has count and age bounds plus an urgent path. A project-specific starting policy is five ready requirements or a 24-hour oldest-ready wait. These are engineering parameters, not research conclusions. Required verification and publication authority remain gates. Incoming work cannot indefinitely delay a frozen batch.

## 5. Properties and limitations

**Local uniqueness.** A transaction and a unique unresolved-attempt constraint can prevent two local reservations for the same operation. This is not a distributed exactly-once guarantee.

**Evidence safety.** Closure requires current evidence for each required claim and read-back of the source lifecycle. The argument assumes correct dependency declarations and trustworthy validators; the scheduler cannot infer semantic truth from a receipt's hash.

**Conditional progress.** Eventual delivery requires finite executable work, eventual resource availability, functioning runtime activation, effective agents, and eventual external decisions. A permanently unavailable executor violates these assumptions. The observed stalled activation demonstrates why unconditional liveness would be false. Aging alone also cannot resolve impossible resource demands or external unknown outcomes.

**Failure containment.** A failed operation blocks its genuine dependents. Unrelated eligible work remains executable. Human waits should release resources that are not required to preserve an unresolved external action.

## 6. Evaluation protocol

Research questions: RQ1, does the mechanism reduce lost continuation and unsafe closure? RQ2, does evidence-aware scheduling improve accepted throughput and tail latency compared with durable FIFO/aging? RQ3, what total coordination cost does it add? RQ4, under what workload/resource regimes does it help or hurt?

Compare (B0) the observed existing coordination workflow, (B1) durable executor with FIFO/aging, (B2) the same executor with critical-path priority, and (P) evidence-aware scheduling on the same executor. Use identical model, reasoning configuration, permissions, source revisions, resource capacity, acceptance contract, and publication policy. Differences between B1/B2/P must be scheduling policy only. Separately compare activation fencing and evidence invalidation by ablation; retain other durability protections.

Use a disclosed mixture of single-platform defects, cross-platform changes, shared-release batches, and changing-input tasks. Freeze arrivals and fault traces, randomize policy order across paired runs, and reset environments to equivalent baselines. Reserve tasks for calibration; do not tune on evaluation traces. Determine repetitions after a variance pilot, report all exclusions and incomplete runs, and preregister the final analysis before confirmatory evaluation.

Measure accepted requirements per wall-clock hour, median and p95 arrival-to-acceptance time, resource utilization, queue age by class, recoverable-fault recovery time, invalid evidence reuse, unsafe closure, and duplicate external effects. Unfinished tasks are censored outcomes, not discarded successes. Report completion curves and horizon completion rates so p95 over only completed tasks cannot hide starvation.

Total development cost includes all parent/child model usage, retries, compilation, test and device time, coordinator invocations, human intervention, and repair time. Report raw units and a disclosed price schedule, with sensitivity analysis; do not collapse unlike quantities without stating weights. Product CPU, memory, responsiveness, and regression behavior are separate outcome-quality constraints. Lower agent cost is not evidence of a faster product.

Inject process loss before/after dispatch, lost responses, duplicate notifications, stale resource observations, changed candidate inputs, missing receipts, executor non-consumption, and delayed human decisions. Simulated publication adapters test failure handling; real channel validation is separately reported and cannot be replaced by mocks. Estimate paired effect sizes with confidence intervals, cluster by task/repository, and report adverse cases as well as averages.

## 7. Current implementation observations

The prototype includes transactional operation registration, unique unresolved attempts, bounded resource observations, queue correlation, an activation journal, and release-plan validation. A local run reported 17 graph behavior tests and 15 release-plan tests passing. These counts are engineering evidence, not independent experimental observations.

One active-recipient queue flow and one resource-release-to-queue flow produced correlated receipts. Subsequent business operations remained queued after the desktop reported activation. No exact consumption evidence was available. The system therefore has not demonstrated end-to-end automatic recovery for idle owners or complete product delivery. Comparative performance, cost savings, and quality improvements are unmeasured. Public artifacts must omit private thread identities and user content.

## 8. Discussion and threats to validity

The expected benefit of selective evidence reuse can disappear when dependency inference is conservative, validation is cheap, or requirements invalidate each other frequently. Scheduling optimization can cost more than it saves. Candidate batching trades feedback latency for amortized build and release cost. A single shared desktop may remain the dominant capacity constraint regardless of available model parallelism.

Other threats include model nondeterminism, differing vendor runtime semantics, flaky UI environments, errors in requirement completion labels, incomplete cost telemetry, publication authorization delays, and one-product selection bias. A controlled trace evaluation must be complemented by prospective project use. Responsibility and failure explanations remain human-reviewable even when scheduling is automated.

## 9. Conclusion and publication route

The proposed framework treats delivery as persistent responsibility across operation, resource, and evidence graphs. Its initial implementation supports several safety mechanisms but has exposed an unresolved executor-activation boundary. The next empirical step is to validate consumption and complete the controlled comparisons; neither a working scheduler nor the observed failure alone establishes research novelty.

Potential venues include ICSE/FSE/ASE for evaluated software-engineering contributions and EMSE/TSE for a fuller empirical study. Specific tracks, deadlines, artifact and AI-disclosure rules remain to be checked when selecting a venue. No submission or preprint is authorized by this draft. Coordinate any disclosure with patent review first; author list, affiliations, CRediT, funding, data availability, and AI assistance statements remain factual fields to resolve.

## References and provenance

The following are identifiable sources carried forward from the [research ledger](2026-09-25-continuous-delivery-graph.md#11-来源与阅读记录); this drafting pass did not newly reread their full texts.

1. Temporal, [Workflow Execution](https://docs.temporal.io/workflow-execution) and [Handling Messages](https://docs.temporal.io/handling-messages).
2. Kubernetes, [Controllers](https://kubernetes.io/docs/concepts/architecture/controller/).
3. Bazel, [Skyframe](https://bazel.build/reference/skyframe).
4. GitHub, [Managing a merge queue](https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue).
5. Hartmann and Briskorn, *An updated survey of variants and extensions of the resource-constrained project scheduling problem*, European Journal of Operational Research 297(1), 1–14, 2022. [DOI](https://doi.org/10.1016/j.ejor.2021.05.004).
6. Kleppmann, [How to do distributed locking](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html), 2016.

This is an AI-assisted working draft requiring author review, completed literature verification, and actual experiments before submission.
