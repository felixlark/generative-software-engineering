---
name: generative-software-engineering
description: 软件开发、修复、重构、旧项目／屎山代码全面清理、集成与交付的统一入口。所有实现类任务默认先应用 professional-engineering-baseline，再按当前问题调用独立维护的工程技能，选择相称验证并完成真实交付；完全只读的解释、分析、调研和未落地草稿按请求交付。
metadata:
  revision: "2026-11-25"
  short-description: 统一工程入口，按需串联独立技能并完成真实交付
---

# GSE 工程入口

从用户要看到的结果出发，核对实际差异、范围、授权和验收入口，由原结果负责人持续完成最小完整变更与真实交付。小修直接实施和定向复验；重要取舍才形成方案。只读解释、设计或起草按用户所请求的产物交付。

GSE 维护结果责任、选路和交付衔接；专门方法由各自技能维护。新装工程或流程技能接入时，只记录触发条件、当前入口与交接结果，具体规则、案例、角色和工具协议留在原技能。调用时读取当前可用版本，更新各自来源即可生效，不把安装变成向 GSE 复制内容的步骤。

## 强制工程基线

所有会改变代码、配置、测试、构建、安装、部署、运行状态或工程规则的 GSE 任务，在实现前必须加载 [professional-engineering-baseline](../professional-engineering-baseline/SKILL.md)。它约束项目声明的集成基线、受控写入现场、增量集成、自动化验证、独立审查、正式制品来源、回滚和 worktree 生命周期。

完全只读的解释、分析、调研和未落地草稿不触发实现门禁。按风险裁剪检查，不能把基线变成额外审批；无法遵守时说明具体缺口，不得静默跳过或自述完成。

`professional-engineering-baseline` 是强制依赖。入口未安装、不可读或没有同步到当前主版本时，记录 `blocked(baseline-missing)`，停止受影响范围内的实现、构建、安装、发布、部署、运行状态变更和工程规则修改；只读分析可以继续。其他可选专项技能不可用时，才按原规则说明缺口并继续独立工作。

安装副本要与 GSE 源仓 `skills/professional-engineering-baseline/install-manifest.json` 的文件清单和 SHA-256 一致；用 GSE 源仓 `scripts/verify_engineering_skills.py` 对每个实际技能根读回。manifest 缺失、目标文件缺失或哈希不一致，同样记 `blocked(baseline-missing)`。

## 按当前问题选路

按[技能路由](references/skill-routing.md)定位当前安装入口，只加载本次实际需要的技能：

- 统筹项目持续交付、经理巡办或交付后运营时，使用 **software-project-manager**：对照完整需求与功能/性能目标，协调原负责人和待决定事项，并主动核现役用户旅程。
- 任何实现、修复、重构、集成、构建、安装、发布或工程治理任务，先应用 **professional-engineering-baseline**：核声明的集成基线与受控现场、定义结果和验证、按风险完成独立审查、控制制品来源与回滚，并按完成状态举证。
- 用户明确要求审查或精简多任务、多 Agent 并行开发治理，尤其是 lane、claim、worktree、合并顺序、分支回收与回滚规约时，使用 **parallel-delivery-review**：先识别真实共享写面和运行资源，优先复用现有 trunk、CI、merge queue、contract tests 与按层回滚。
- 决定实现范围、增加机制或验证工作量时，使用 **avoid-overkill** 的工程模式；它也适用于检查 GSE 自身的流程改动。
- 陈旧项目、屎山代码、全面精简或仓库瘦身，使用[旧项目全面清理](references/legacy-project-cleanup.md)，贯通需求、架构、代码、测试和部署；不是只格式化当前代码。
- 故障先用 **systematic-debugging**；需要理解调用链、历史理由或设计模块边界时，选对应 **pstack** 叶技能。
- 拟定或实质修改可执行方案时，调用 **egm:egm-auto-review** 做独立审查；用户明确选择完整 EGM 流程时走对应原技能。
- HTML、CSS 或浏览器端 JavaScript 工作，实施前调用 **modern-web-guidance:modern-web-guidance**；当前代码确需简化时调用 **code-simplifier**。
- macOS、iOS 或其他 Apple 平台的设计、实现、评审、构建、签名或分发工作，实施前调用 **apple-platform-guidance**：先核实际部署目标与 Xcode／SDK，再用 Apple 官方文档和 Xcode MCP 取事实；SwiftUI／AppKit、HIG、沙盒、公证和 App Store 规则不以模型记忆替代。
- 准备宣布完成时，按证据缺口调用 **verification-before-completion**；交付反复中断或提前返回时调用 **end-to-end-delivery**，已获准长周期接续沿 **long-running-delivery**。

这些是场景入口。加载一个技能不要求把整张表执行一遍；同一候选仍有效的检查与审查证据直接复用。依赖的定位、缺失处理及输出衔接统一见路由表，GSE 不保存替代执行副本。

## 执行与完成

编辑前核分支、已有改动与实际 writer，遵项目 checkout 政策。共享现场单 writer，未知副作用先对账。沿用已确认的需求、决定、授权和原任务；只问会改变目标、重要取舍或授权的问题。加载技能本身不扩展行动权限。

在授权内实现、验证、集成和交付。选择能覆盖实际失败及受影响行为的最低充分证据；服务、跨端、持久化和界面按真实在用版本与承诺入口验收。构建、安装、健康与业务接受各自举证。项目必需检查保留，相关变化才重验。

尽早集成可审阅、可回滚的完整增量。失败沿根因修复到原始需求满足；准确的外部阻塞记录在原案，继续独立获准工作。保留正常运行状态，汇报变化、验证及实质未完项。规范归[生命周期](https://github.com/felixlark/generative-software-engineering/blob/main/docs/LIFECYCLE.md)、[证据](https://github.com/felixlark/generative-software-engineering/blob/main/docs/EVIDENCE.md)与[最小充分工程](https://github.com/felixlark/generative-software-engineering/blob/main/docs/MINIMAL_SUFFICIENT_ENGINEERING.md)。

## GSE 自身的按需参考

- 候选级独立代码审查：用户、项目要求或具体高风险缺口时读[独立审查](references/independent-review.md)。
- 多入口验收与项目合同衔接：[项目验收地图](references/project-verification.md)；性能主张：[性能证据](references/performance-evidence.md)。
- 共享交接、增量集成与并行互等：[交付协调](references/delivery-coordination.md)及[解除协调停滞](https://github.com/felixlark/generative-software-engineering/blob/main/docs/COLLABORATION.md#resolve-coordination-stalls)。
- 方法归属、历史来源与维护边界：[方法来源](references/method-sources.md)。
