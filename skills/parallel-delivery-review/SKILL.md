---
name: parallel-delivery-review
description: 仅在用户明确要求审查或设计多任务、多 Agent 并行开发治理，或怀疑 lane、claim、worktree、merge、分支回收和回滚规约过度设计时使用。把冲突分为 Git、合同、运行资源和外部效果，优先复用 trunk、CI/merge queue、contract tests、expand/contract 与现有发布机制；不处理普通实现或一般多 Agent 协作。
metadata:
  short-description: 审查并行交付治理，删除重复协调机制
---

# 并行交付治理审查

这是一个窄范围审查与设计模式，不拥有日常交付、项目优先级、实现分工或普通多 Agent 协调。结果责任、生命周期、证据和协作语义继续归属 GSE；具体项目优先级和 owner 归属 `software-project-manager`。

只在用户明确要求审查或设计并行开发治理时使用，例如 lane、claim、worktree、合并顺序、分支回收和回滚规约。一次普通的 worktree 任务、正常的多 Agent 实现或具体功能开发不触发本 skill。

## 先看真实冲突

先收集会改变当前决定的证据：反复冲突、长时间等待、合并后失效、重复验证、返工、过期 claim、错误基线或失败回退。没有实际冲突时，不预建 lane、队列、审批或状态机。

把冲突分开处理：

| 冲突 | 典型对象 |
| --- | --- |
| Git 写面 | checkout、index、branch、同一文件或生成物 |
| 合同语义 | producer/consumer、payload、顺序、持久化格式 |
| 运行资源 | build、install、service、database、port、device、window、desktop |
| 外部效果 | 同一消息、订单、回执、Run、业务对象或不可逆副作用 |

同一变更可占多个维度，按最高实际风险处理。

## 优先复用现有工程机制

| 问题 | 默认机制 |
| --- | --- |
| 并行写代码 | trunk、短分支、小 PR；并发 writer 使用项目允许的隔离 checkout |
| 合并交错 | CI、required checks、merge queue；平台不可用时才用单一集成 owner |
| 兼容合同 | 只对真实 consumer 做 contract tests；优先 additive change |
| 破坏合同或数据迁移 | expand → migrate → contract；每阶段可部署 |
| 发布解耦 | 现有 feature flag 或 progressive delivery；有实际需要才启用 |
| 安装或运行资源 | 项目已有的锁、owner、assignee 或资源键 |
| 外部副作用 | 单业务 owner、幂等、unknown 对账和补偿 |

项目已有平台和 GSE 规则优先。不要为了“统一”重造 CI、PR 状态、锁、队列或回滚系统。

## 判断机制是否值得保留

下面只评估**重复的并行协调机制**。项目、平台或法律要求的安全、合规、身份、数据完整性和不可逆动作控制始终保留，即使没有发生过冲突，也不得因本审查而删减。

一项 lane、claim、allowlist、门禁或台账只有同时满足以下条件才保留：

1. 能阻止已经发生或高概率发生的真实冲突。
2. 有明确 owner、释放条件和故障恢复。
3. 不能从 Issue、PR、CI、Git 或资源事实可靠派生。
4. 其协调成本低于它避免的返工和等待。

如果不能满足，删除或延后。重点检查：

- 固定 writer 数、需求排队数或模块 lane 数是否是未经测量的人为上限。
- claim 是否复制了 Issue/PR/CI 已经拥有的状态，并制造第二本账。
- allowlist 是否扩展到每个任务，而不是只覆盖发生过碰撞的共享面。
- 是否把模块名当作资源键，而真正的冲突在安装容器、服务或设备。
- 是否为可逆小修强制回滚演练、bundle 或额外审批。

## 资源租约与恢复

优先使用现有平台的 owner、assignee、branch、CI concurrency、deployment lock 或项目锁。确实需要自定义 claim 时，只记录 holder、资源键、取得证据、释放事件和未决效果；queued、waiting、ready 尽量从依赖和 PR 状态派生。

lease 过期只是调度信息，不授权接管。新 writer 必须先确认旧 writer 已停止或已隔离，并对 unknown 副作用完成对账。无法证明旧 writer 已停止时，由明确 owner 将受影响工作标为 blocked，不自行设计 TTL 抢占。

## 集成与回滚边界

- 依赖用 merge order 或平台队列表达，不建长期 integration branch。
- 合并前对齐当前 base，并验证同一 head；多个 PR 各自绿不代表交错合并后正确。
- 自动化 gate 优先于人工 main smoke。人工串行时，对**重复的交错防护**只保留一个能阻止交错的 gate，并绑定准确 head；项目或平台强制的安全、合规、审核和不可逆动作门禁不因此减少。
- 回滚分为代码 revert、恢复上一制品、数据或外部效果补偿。前两层可能由 Git 或安装系统完成；不可逆数据和外部副作用只能 forward-fix 或补偿。
- 高风险改动保留旧制品、兼容读或迁移回执；普通可逆代码改动不强制预演回滚。

## 分支与现场回收

- 已合并分支由 main 或 PR 保留提交身份；无 open PR、无活跃 lease 后可按规定宽限期删除，不为已合并分支额外 bundle。
- 未合并、暂停、dirty、owner 不明或含独有证据的分支才需要归档。
- worktree 先核 clean、进程和 owner；数量不是目标，回收是为了降低误选基线和混淆风险。

## 审查输出

给出五部分：

1. 已观察到的冲突、等待或失败，以及对应证据。
2. 必须保留的写面、资源键、合同和业务 owner。
3. 应删除或延后的 lane、claim 状态、队列、审批和重复台账。
4. 最小集成顺序、合并 gate、回滚边界和清理规则。
5. 仍未知或需用户决定的事项。

## 停止检查

- 没有实际资源冲突，不加全局串行。
- 平台已有隔离或门禁，不复制。
- 状态可由现有 Issue、PR、CI 或资源事实派生，不新增状态库。
- 回滚无法覆盖数据或外部副作用时，明确 forward-fix 或补偿条件。
- 并行收益小、交接成本更高时，留给一个 owner 完成。
