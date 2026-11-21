---
name: generative-software-engineering
description: 软件开发、修复、重构、旧项目／屎山代码全面清理、集成与交付的统一入口。按当前问题调用独立维护的工程技能，选择相称验证并完成真实交付。
metadata:
  revision: "2026-11-16"
  short-description: 统一工程入口，按需串联独立技能并完成真实交付
---

# GSE 工程入口

从用户要看到的结果出发，核对实际差异、范围、授权和验收入口，由原结果负责人持续完成最小完整变更与真实交付。小修直接实施和定向复验；重要取舍才形成方案。只读解释、设计或起草按用户所请求的产物交付。

GSE 维护结果责任、选路和交付衔接；专门方法由各自技能维护。新装工程或流程技能接入时，只记录触发条件、当前入口与交接结果，具体规则、案例、角色和工具协议留在原技能。调用时读取当前可用版本，更新各自来源即可生效，不把安装变成向 GSE 复制内容的步骤。

## 按当前问题选路

按[技能路由](references/skill-routing.md)定位当前安装入口，只加载本次实际需要的技能：

- 统筹项目持续交付、经理巡办或交付后运营时，使用 **software-project-manager**：对照完整需求与功能/性能目标，协调原负责人和待决定事项，并主动核现役用户旅程。
- 决定实现范围、增加机制或验证工作量时，使用 **avoid-overkill** 的工程模式；它也适用于检查 GSE 自身的流程改动。
- 陈旧项目、屎山代码、全面精简或仓库瘦身，使用[旧项目全面清理](references/legacy-project-cleanup.md)，贯通需求、架构、代码、测试和部署；不是只格式化当前代码。
- 故障先用 **systematic-debugging**；需要理解调用链、历史理由或设计模块边界时，选对应 **pstack** 叶技能。
- 拟定或实质修改可执行方案时，沿 **GSE 方案审查**核对目标、假设、风险、方案、验证与交付；需要独立判断时使用当前实际可用的独立评审能力，并复用真实评审证据。
- HTML、CSS 或浏览器端 JavaScript 工作，实施前调用 **modern-web-guidance:modern-web-guidance**；当前代码确需简化时调用 **code-simplifier**。
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
