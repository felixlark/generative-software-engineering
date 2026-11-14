# Minimal sufficient engineering

Minimal sufficient engineering asks for the smallest system that fully closes the current outcome and protects demonstrated risks.

## Scope discipline

A request for capability A authorizes A and the changes directly required to make A work safely and maintainably. Adjacent capability B belongs in scope only when it blocks A, shares the same demonstrated root cause, or is already a stable contract that A must preserve.

## Complexity budget

Add a new abstraction, state, adapter, fallback, feature flag, migration, compatibility path, retry policy, or permanent process rule only when at least one concrete need justifies it:

- a current requirement cannot be expressed cleanly through the existing path;
- an external protocol or compatibility obligation exists now;
- a security, identity, privacy, data-integrity, or irreversible-action boundary requires it;
- an observed failure demonstrates the missing behavior;
- an uncontrolled environment requires bounded and observable recovery.

Prefer changes that reduce duplicate state, responsibility, rules, and future change points.

## Inline simplification

Simplify while implementing the current change: give modules one clear responsibility and explicit interfaces, reduce duplicate state, unnecessary abstractions and branches, and prefer readable code over fewer lines. Keep this work within the requested scope.

Behavior-preserving cleanup retains the promised outputs, errors, side effects and public contracts. Removing a capability, limit, compatibility path or dedicated test instead follows the current requirement and actual consumer evidence; it is not justified by a simplifier's stylistic preference.

Use the [code-simplification guidance](../skills/generative-software-engineering/references/code-simplification.md) when an affected implementation is visibly complex or hard to read. The core guidance works without another installed skill. This is part of implementation, not a new stage, reviewer role, approval, fixed number of passes or full-test requirement. Reuse valid evidence and refresh only the affected checks. Judge the change by clearer responsibilities and lower maintenance burden, not deleted line or test counts.

## Test value

Tests exist to catch meaningful regressions at a useful cost. Prove each business assertion at the cheapest reliable layer, and keep higher-level tests for wiring, environment, or user behavior that lower layers cannot prove.

Do not preserve a test merely because it once encoded an implementation detail. When a requirement changes, update or remove obsolete tests instead of adding compatibility behavior solely to satisfy them.

## Retirement

When a capability or workaround is retired, remove its entry points, implementation, configuration, documentation, and dedicated tests in the same change unless a current compatibility obligation requires a bounded reader or migration path.
