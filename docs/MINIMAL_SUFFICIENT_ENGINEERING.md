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

## Test value

Tests exist to catch meaningful regressions at a useful cost. Prove each business assertion at the cheapest reliable layer, and keep higher-level tests for wiring, environment, or user behavior that lower layers cannot prove.

Do not preserve a test merely because it once encoded an implementation detail. When a requirement changes, update or remove obsolete tests instead of adding compatibility behavior solely to satisfy them.

## Retirement

When a capability or workaround is retired, remove its entry points, implementation, configuration, documentation, and dedicated tests in the same change unless a current compatibility obligation requires a bounded reader or migration path.
