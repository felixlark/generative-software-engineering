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
| [`professional-engineering-baseline`](../skills/professional-engineering-baseline/SKILL.md) | mandatory operating gates for implementation tasks: controlled work base, automated checks, risk-based independent review, artifact provenance, rollback, and workspace lifecycle |
| [test execution strategy](../skills/generative-software-engineering/references/test-execution-strategy.md) | affected-test selection, safe result reuse, execution tiers, and release-wide verification boundary |

Templates instantiate these rules without extending them. Examples illustrate them. Research notes can challenge them but are non-normative until promoted here.

The [GSE Skill](../skills/generative-software-engineering/SKILL.md) owns engineering routing and delivery integration. It must load the [professional engineering baseline](../skills/professional-engineering-baseline/SKILL.md) before implementation; that Skill owns Agent-specific operating gates while the documents above own normative method semantics. Its install manifest and [`scripts/verify_engineering_skills.py`](../scripts/verify_engineering_skills.py) bind every installed copy to the expected file hashes and relative links. The [routing table](../skills/generative-software-engineering/references/skill-routing.md) then calls independently maintained specialist skills; their execution details stay at the source. Research proposals remain in [research](../research/README.md) until promoted.
