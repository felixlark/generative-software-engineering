# Agent instructions

This repository develops the Generative Software Engineering method itself. Keep it product-agnostic and evidence-driven.

Before editing, inspect the current git status and preserve unrelated work. One writer owns the canonical checkout; concurrent work stays read-only and repository writes serialize. Do not create new worktrees or clean pre-existing residue without a separate exact user request. Generated development output follows the host's workspace instructions and stays outside `~/Documents`.

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

## 合并前评审

方案审查、代码审查和正式回报审查按各自适用范围办理，沿 [协作规范](docs/COLLABORATION.md#review-scope-and-evidence-reuse)复用有效证据。候选级独立代码审查按用户明确要求、适用项目合同或具体高风险缺口启用；本仓不另设一律等待 Codex 自动评审的门槛。现有用户指定及平台强制检查保留，适用的阻塞性意见须处理后再合并。

### Pre-merge review (English translation)

Apply proposal, code, and formal-report review within their respective scopes and reuse valid evidence under the [collaboration rules](docs/COLLABORATION.md#review-scope-and-evidence-reuse). Enable candidate-level independent code review when the user, an applicable project contract, or a specific high-risk gap requires it; this repository adds no blanket wait for Codex automatic review. Preserve existing user-required and platform-required checks and resolve applicable blocking findings before merging.
