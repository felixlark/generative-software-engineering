# Agent instructions

This repository develops the Generative Software Engineering method itself. Keep it product-agnostic and evidence-driven.

Before editing, inspect the current git status and preserve unrelated work. One writer owns a checkout/branch; concurrent writers use isolated worktrees or equivalent write isolation.

Treat [`docs/SPECIFICATION.md`](docs/SPECIFICATION.md) as the normative method. Lifecycle, collaboration, evidence, minimal-engineering, and harness details each have one owning document linked from [`docs/README.md`](docs/README.md). Do not duplicate the same rule across files; link to its owner.

Prefer one root GSE that owns an intent end to end. Create temporary sub-agents only when independent work, specialist evaluation, or parallelism has clear value. Do not introduce a fixed director, department, or mandatory role pipeline.

For non-trivial changes, state the intended outcome, invariants, affected surface, and evidence before claiming completion. Use the lowest evidence layer that can prove each affected claim, and use real runtime/user-path evidence when lower layers cannot prove the behavior.

Keep changes minimally sufficient. Do not add speculative abstractions, compatibility layers, fallback state, tests, or governance for requirements that do not exist or risks that have not been demonstrated.

Research notes are hypotheses until promoted into the normative docs. Benchmarks must preserve task input, baseline, runtime/model configuration, tool access, evidence, and total participant cost well enough to compare alternatives fairly.

For GitHub README and public posts, follow the [communication language and publication receipt requirements](CONTRIBUTING.md#public-communication-languages).
