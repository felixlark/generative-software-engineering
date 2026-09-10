# Generative Software Engineering

Generative Software Engineering (GSE) treats the unit of software work as an owned transformation from intent into a usable, maintainable software entity:

```text
Intent → Executable / Maintainable Software Entity
```

A GSE agent owns the outcome end to end: understand the intent, inspect reality, define the result contract, implement, verify, integrate, deliver, and maintain. It may delegate independent work to temporary sub-agents when parallelism, expertise, or independent evaluation has clear value, while retaining responsibility for the final outcome.

> 中文摘要：GSE 把“软件生成”从 `Prompt → Code` 提升为 `Intent → Executable / Maintainable Software Entity`。一个根 Agent 对结果端到端负责；组织结构按任务风险动态生成；完成必须由与风险相称的真实证据证明；工程复杂度只保留当前需求和真实风险所需要的最小充分部分。

## Why GSE

Agentic software development fails when code generation is mistaken for delivery. A patch can compile while the user journey is broken, a test can pass while the installed system is unhealthy, and a large multi-agent organization can add more coordination cost than engineering value.

GSE therefore centers five ideas:

1. **Outcome ownership** — one root GSE owns one software intent end to end.
2. **Recoverable lifecycle** — work progresses through explicit outcome, evidence, and handoff state rather than chat history alone.
3. **Risk-shaped collaboration** — sub-agents are created dynamically for independent work; no fixed role pipeline is required.
4. **Evidence-driven completion** — completion is claimed only when evidence covers the behavior and system qualities affected by the change.
5. **Minimal sufficient engineering** — add only the states, abstractions, tests, compatibility paths, and process needed for current requirements and demonstrated risks.

## Repository map

- [`docs/SPECIFICATION.md`](docs/SPECIFICATION.md) — normative GSE model and invariants.
- [`docs/LIFECYCLE.md`](docs/LIFECYCLE.md) — task lifecycle, outcome contract, continuation, and closure.
- [`docs/COLLABORATION.md`](docs/COLLABORATION.md) — dynamic sub-agent and concurrent-writer model.
- [`docs/EVIDENCE.md`](docs/EVIDENCE.md) — evidence hierarchy and completion gates.
- [`docs/MINIMAL_SUFFICIENT_ENGINEERING.md`](docs/MINIMAL_SUFFICIENT_ENGINEERING.md) — complexity and test-value discipline.
- [`docs/HARNESS.md`](docs/HARNESS.md) — boundary between GSE semantics and the agent harness/runtime.
- [`templates/`](templates/) — lightweight outcome, handoff, and evidence templates.
- [`examples/`](examples/) — worked examples.
- [`research/`](research/) — hypotheses, benchmark protocol, and open research questions.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`AGENTS.md`](AGENTS.md) — contribution and agent-working rules for this repository.

The repository name `generative-software-engineering` is an intentional three-segment kebab-name exception for this project. It does not define a general repository naming policy.

## Status

This repository is a living research and methods project. The normative surface is deliberately small. Research notes may propose changes, but only material promoted into the specification changes the current GSE contract.
