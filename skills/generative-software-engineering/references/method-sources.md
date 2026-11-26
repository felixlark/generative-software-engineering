# 方法来源与维护归属

## 当前执行来源

当前触发条件、技能名称、发现方式及交接产物统一归[技能路由](skill-routing.md)。GSE 维护入口与交付衔接；专门方法读取各自实际安装的当前 `SKILL.md` 及必要资源。未来接入同样只加路由，方法修订回原技能。

| 独立来源 | 用途与归属 |
| --- | --- |
| [avoid-overkill](https://github.com/6Kmfi6HP/avoid-overkill) | 工程投入与写作比例；本次核读当前安装入口及 README，工程模式接入 GSE，案例继续由该技能维护 |
| Lauren Tan 的 [pstack](https://github.com/cursor/plugins/tree/main/pstack) | 工程专项叶技能；调用当前安装入口，GSE 不再维护其执行步骤副本 |
| Google 的 [Elephant & Goldfish Model](https://github.com/google/elephant-goldfish-model) | 方案构思、起草与独立审查；角色、标准、迭代合同归 EGM |
| Anthropic 的 [code-simplifier](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-simplifier) | 当前代码的行为保持型简化；使用实际安装技能 |
| [Modern Web Guidance](https://github.com/GoogleChrome/modern-web-guidance) | Chrome、Edge、Firefox、MDN 团队与社区维护的 Web 指导；协议、工具参数与平台指南归官方技能 |

其他工程技能依当前宿主目录定位，依赖可用性和实际调用分别取证。本入口不固定版本，不代表自动安装／升级原技能；复用仍有效的来源证据。

[测试执行策略](test-execution-strategy.md)是 GSE 自有的执行参考。当前安装目录没有通用的测试
调度 Skill：`modernize-tests` 只负责 Swift Testing／XCTest 写法，`ios-development-delivery`
只覆盖 Apple 平台交付，`avoid-overkill` 只提供投入比例原则。GSE 只吸收这些入口之外的通用
测试选择、证据复用和发布门边界，不复制平台测试方法。

## 历史适配与归因

下列版本只记录旧适配出处，不再充当专门技能的执行合同。现存参考文件保留薄入口，旧备份仅供追溯；保留第三方许可与版权声明。

- pstack：历史核验 0.15.9、提交 `e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a`；2026-11-11 另核读 `63912a91d52c43946f974f2aaf661334a6116a82` 的第一性原理专题。保留 [MIT 许可](../LICENSE.pstack)。
- EGM：历史适配依据本机 0.1.2，旧版曾内置角色、裁决与收敛规则；现改为调用原技能。保留 Copyright 2026 Google LLC 与 [Apache-2.0 许可](../LICENSE.egm)。
- code-simplifier：历史核读提交 `b5b01ac4f889fec0c4c6bb89f27ca7c8574473f6`，保留对应 [Apache-2.0 许可](../LICENSE.code-simplifier)。实际安装技能的许可依其来源，历史声明不推定覆盖新版本。
- Modern Web Guidance：历史核读提交 `4dd968349e54ca45a05dd5c818fb035c9054b022`、npm 包 1.0.0；旧查询协议快照退出 GSE 执行参考。保留 [Apache-2.0 许可](../LICENSE.modern-web-guidance)。
- Lauren（`@poteto`）游戏开发经验的独立归纳留在原研究记录，作者自述与 GSE 实验结果分别取证；研究未晋升时保持研究状态。

GSE 自有责任、生命周期和证据语义见[规范](https://github.com/felixlark/generative-software-engineering/blob/main/docs/SPECIFICATION.md)。宿主模型、工具与权限继续沿用户及项目约定。
