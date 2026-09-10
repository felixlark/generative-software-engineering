# Documentation ownership

GSE uses a single-owner documentation rule: one rule has one home. Other documents link to that rule instead of restating it with slightly different wording.

| Document | Owns |
| --- | --- |
| [`SPECIFICATION.md`](SPECIFICATION.md) | definition, core invariants, root ownership, completion semantics |
| [`LIFECYCLE.md`](LIFECYCLE.md) | recoverable task lifecycle, outcome contract, continuation and closure |
| [`COLLABORATION.md`](COLLABORATION.md) | delegation, concurrency, isolation, integration responsibilities |
| [`EVIDENCE.md`](EVIDENCE.md) | evidence hierarchy, claim-to-evidence mapping, invalidation |
| [`MINIMAL_SUFFICIENT_ENGINEERING.md`](MINIMAL_SUFFICIENT_ENGINEERING.md) | scope, complexity budget, test value, retirement |
| [`HARNESS.md`](HARNESS.md) | runtime capabilities and the boundary between method and infrastructure |

Templates instantiate these rules without extending them. Examples illustrate them. Research notes can challenge them but are non-normative until promoted here.
