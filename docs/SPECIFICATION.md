# GSE specification

## Definition

Generative Software Engineering (GSE) defines software work as:

```text
Intent → Executable / Maintainable Software Entity
```

The unit of responsibility is the **software outcome**, not a prompt, patch, test, role, or tool call. A root GSE owns that outcome from interpretation through delivery and subsequent maintenance.

## Core invariants

### One outcome, one end-to-end owner

One software intent has one root owner. The root GSE is responsible for understanding the request, inspecting the existing system, defining the outcome, choosing the implementation path, coordinating any delegated work, verifying the result, integrating changes, delivering the usable entity, and preserving a maintainable state.

Delegation transfers work, not outcome ownership.

### Organization follows risk and dependency

GSE has no mandatory organization chart. Temporary sub-agents may be useful for independent research, parallel implementation in isolated scopes, specialist security/performance work, or independent evaluation. The root GSE chooses them when expected quality or throughput gain exceeds coordination cost.

A fixed sequence of product, engineering, testing, operations, director, or reviewer roles is not part of GSE.

### Completion is a claim backed by evidence

A task is complete when the accepted intent is closed and every materially affected claim has adequate evidence. Compilation, a unit test, a pull request, a status marker, or a sub-agent report can support completion but cannot define it by themselves.

Evidence requirements are specified in [`EVIDENCE.md`](EVIDENCE.md).

### Work survives context loss

Chat context is working memory, not durable project memory. Recoverable work records stable outcome, scope, identifiers, completed work, tool outcomes, unresolved blockers, and the next concrete goal. The lifecycle and handoff contract are specified in [`LIFECYCLE.md`](LIFECYCLE.md).

### Concurrency preserves ownership

Concurrent work is governed by outcome, dependency, and write conflicts. Each writer has an isolated write scope and a reviewable integration result. No concurrent task may silently overwrite another task or a user's unrelated changes. See [`COLLABORATION.md`](COLLABORATION.md).

### Complexity must earn its place

An abstraction, state, fallback, compatibility path, test, or process step should exist because a current requirement, external contract, security boundary, demonstrated failure, or high-cost risk justifies it. See [`MINIMAL_SUFFICIENT_ENGINEERING.md`](MINIMAL_SUFFICIENT_ENGINEERING.md).

## What GSE is not

GSE is not a synonym for code generation, prompt engineering, harness engineering, multi-agent orchestration, or autonomous deployment. Those can be implementation capabilities inside a GSE system. The method remains valid as models, tools, context windows, and runtimes change.

## Method/runtime separation

The method defines responsibilities, lifecycle, collaboration semantics, evidence, and engineering discipline. A harness supplies context, tools, permissions, isolation, persistent identifiers, execution, and observation. Their boundary is specified in [`HARNESS.md`](HARNESS.md).
