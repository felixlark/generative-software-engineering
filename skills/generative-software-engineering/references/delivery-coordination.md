# Delivery coordination

Read this only when substantial development shares integration or release resources across tasks, or when an existing delivery workflow needs continuation or recovery. It is not an entry checklist for routine debugging.

## Shared integration and release resources

Treat each checkout and its Git state as one write scope. Follow the repository's permitted isolation policy. Check provenance, baseline compatibility, diff, focused evidence, and conflicts before integrating a candidate. Protect unrelated dirty work.

Assign one operator at a time to each shared build slot, installation target, desktop, device, or release channel. Do not mutate inputs used by an active build. Limit overlapping work by actual resource capacity; capacity and cadence are product decisions, not universal constants.

Keep changes small enough to review and observe on the product's fast feedback surface. A release lane may batch several changes while retaining their source owners, candidate identities, and promised delivery targets. It does not silently inherit or close their outcome contracts. An owned patch may enter integration while its source task remains open.

A busy lane is a scheduling dependency. Record the owner, next action, and event that makes the task runnable in the existing work record; release resources no longer needed. Continue independent in-scope work or hand off a ready artifact to the existing lane. If distribution or user acceptance is promised, keep that obligation open until its receipt arrives. A queued release is not evidence of release or an external blocker.

Evidence attached to an older candidate must be reassessed when a later change affects its claim. Freeze release candidate identity without freezing unrelated development. The maintained [collaboration rules](https://github.com/longbiaochen/generative-software-engineering/blob/main/docs/COLLABORATION.md) and [lifecycle](https://github.com/longbiaochen/generative-software-engineering/blob/main/docs/LIFECYCLE.md) define the method; local runbooks own commands and batching policy.

## Existing continuation and recovery mechanisms

An agent turn cannot continue itself after it ends. A status note, active Goal, queued job, or skill instruction alone cannot wake an agent or close an issue. Use an actual supported continuation mechanism when the authorized workflow requires one, and verify that it ran. If none exists, report the exact pending gate and owner without promising automatic recovery. Ordinary software work does not authorize a new recurring automation.

When a project already provides a delivery graph, register the next executable operations using its source identity, owner, authorization, candidate, dependencies, resources, and evidence. Use its supported events and attempt receipts rather than adding a polling loop per task. Queued, acknowledged, and completed are different states.

Treat routine executor recovery as engineering work within existing authority. Diagnose the pending operation and supported executor; verify useful progress after recovery. Preserve explicit pauses, budget controls, authentication and approval boundaries. A stale label or timeout does not authorize duplicate work or takeover of an uncertain writer. Read back uncertain side effects before retrying.

Follow the maintained [harness boundary](https://github.com/longbiaochen/generative-software-engineering/blob/main/docs/HARNESS.md) when changing the delivery infrastructure itself. Do not construct a new harness to repair a localized product defect.
