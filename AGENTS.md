# Agent instructions

This repository develops the Generative Software Engineering method itself. Keep it product-agnostic and evidence-driven.

Before editing, inspect the current git status and preserve unrelated work. One writer owns a checkout/branch; concurrent writers use isolated worktrees or equivalent write isolation.

Treat [`docs/SPECIFICATION.md`](docs/SPECIFICATION.md) as the normative method. Lifecycle, collaboration, evidence, minimal-engineering, and harness details each have one owning document linked from [`docs/README.md`](docs/README.md). Do not duplicate the same rule across files; link to its owner.

Prefer one root GSE that owns an intent end to end. Create temporary sub-agents only when independent work, specialist evaluation, or parallelism has clear value. Do not introduce a fixed director, department, or mandatory role pipeline.

For non-trivial changes, state the intended outcome, invariants, affected surface, and evidence before claiming completion. Use the lowest evidence layer that can prove each affected claim, and use real runtime/user-path evidence when lower layers cannot prove the behavior.

Keep changes minimally sufficient. Do not add speculative abstractions, compatibility layers, fallback state, tests, or governance for requirements that do not exist or risks that have not been demonstrated.

Research notes are hypotheses until promoted into the normative docs. Benchmarks must preserve task input, baseline, runtime/model configuration, tool access, evidence, and total participant cost well enough to compare alternatives fairly.

For GitHub README and public posts, follow the [communication language and publication receipt requirements](CONTRIBUTING.md#public-communication-languages).

## 限制类改动规则

1. 新增或调小任何上限、槽位、名额、闸门、门槛、退避（包括并发数、负载准入、超时退避等）时，PR 正文须单列「新增限制」一节，写明位置、默认值和依据，经仓库负责人定稿后才可合并。此类改动不得绕过 PR 直接进入 main。
2. 资源类参数默认不限、只观测；确需限制时须通过显式配置开启，不得在代码中写死最大值。外部硬限制（如外部接口限流、部署锁）须在注释中写明来源。

### Limit-change rules (English translation)

1. When adding or lowering any limit, slot count, quota, gate, threshold, or backoff (including concurrency, load admission, and timeout backoff), the PR body must include a separate “新增限制” (New limits) section stating the location, default value, and rationale. The repository owner must finalize the change before it can be merged. Such changes must not bypass a PR to enter main directly.
2. Resource parameters default to unlimited operation with observation only. Any necessary limit must be enabled through explicit configuration; do not hard-code maximum values. Comments must cite the source of external hard limits, such as external API rate limits or deployment locks.
