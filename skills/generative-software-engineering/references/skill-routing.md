# 工程技能路由与维护归属

GSE 是统一入口，负责选路、连接产物与完成原始结果。下表按当前决定选择专门技能；方法正文和配套资源由原技能持续维护。

## 定位与调用

1. 先按当前宿主技能目录中的名称和位置取得实际 `SKILL.md`。插件有命名空间时使用完整名称；表中的叶技能也可由已安装的 pstack 根目录定位。只读对应入口，不展开整个技能树。
2. 读取当前入口，沿其合同获取本次必要的参考、角色或工具；保留用户决定、项目控制面、授权及现有有效证据。路径、命名空间、版本和工具参数由实际安装来源解析，GSE 不固定机器路径或插件缓存版本。
3. 某项未安装、不可见或工具不可用时，先沿宿主正式安装／修复入口处理。`professional-engineering-baseline` 是实现类任务的强制依赖；它不可用时记录 `blocked(baseline-missing)`，停止受影响范围内的实现、构建、安装、发布、部署、运行状态变更和工程规则修改，只读分析可继续。其他可选专项技能不可用时，说明具体技能、受影响能力与缺口，继续独立获准工作；不把 GSE 的历史适配冒充该技能执行、独立评审或专项验收。

## 范围与投入

| 何时调用 | 当前技能名 | 交接回 GSE 的结果 |
| --- | --- | --- |
| 所有会改变代码、配置、测试、构建、安装、发布、运行状态或工程规则的开发任务，在实现前 | `professional-engineering-baseline` | 声明的集成基线与受控现场、结果合同、自动化验证、按风险的独立审查、制品来源、回滚、worktree 生命周期和分层完成状态 |
| 项目负责人巡办、完整需求持续交付、跨模块协调或交付后运营 | `software-project-manager` | 需求与功能/性能验收差距、原owner的近期成果和依赖处置、必要用户决定及真实运行/交付证据 |
| 用户明确要求审查或设计多任务／多 Agent 并行开发治理，或精简 lane、claim、worktree、分支回收与回滚规约 | `parallel-delivery-review` | 实际冲突面、保留或删除的协调机制、最小隔离、集成与按层回滚方案及相称证据 |
| 确定实现范围、增加抽象／回退／测试或检查流程成本时 | `avoid-overkill`，工程模式 | 与当前结果和证据相称的变更、验证范围及停止条件 |
| 修改代码后确有复杂、难读的局部实现 | `code-simplifier` | 本次范围内的行为保持型简化与受影响验证 |

明确要求陈旧项目／屎山代码全面清理时，沿 GSE 自有的[清理工作流](legacy-project-cleanup.md)串联这些技能及下方影响分析、审查与交付入口。它拥有跨产物清理合同和证据账，不复制各技能的方法正文，也不要求执行全部工程技能。

avoid-overkill 的案例和写作模式继续由它维护；纯论文写作走原写作技能入口，GSE 不接管该工作流。

## 理解、调试与设计

pstack 是 Lauren Tan 的工程技能工具集。按实际安装目录读取需要的叶技能；无需先启动其总控、面板或整套模式。

| 何时调用 | 当前技能名 | 交接回 GSE 的结果 |
| --- | --- | --- |
| 行为／调用链不清楚 | `how`（pstack） | 带当前源码或运行依据的解释 |
| 历史理由或归属会影响当前选择 | `why`（pstack） | 已核来源的设计理由与未知项 |
| 故障原因不明或原问题复现 | `systematic-debugging` | 根因依据、修复及原失败路径验证 |
| 存在重要模块／接口／类型取舍 | `architect`（pstack） | 调用者用法、边界与选定设计 |
| 接口、协议、持久化或共享状态变化，安全前提未证实 | `blast-radius`（pstack） | 关键事实、真实消费者及影响证据 |
| 多个真实用户入口，验收方法需要形成可复用地图 | `create-verification-skill` / `maintain-verification-skill`（pstack） | 项目自身维护的验收入口及实际覆盖 |
| 同类错误复发，确需固化经验 | `correct` / `principle-encode-lessons-in-structure`（pstack） | 落在项目归属处的修复或可执行反馈 |
| 根据性能数字选型或声称改进 | `benchmark-checklist`（pstack） | 可比条件、正确性与测量结论 |

## 方案审查

EGM 是 Google 的 Elephant & Goldfish Model，使用保有上下文的负责人和新上下文读者审查方案。GSE 将稳定候选、原要求、当前决定及必要来源交给 EGM，继续负责核实发现与原始交付。

| 何时调用 | 当前技能名 | 交接回 GSE 的结果 |
| --- | --- | --- |
| 新拟或实质修改可执行方案，且非明确小修／格式调整 | `egm:egm-auto-review` | 实际完成的独立审查、裁决、修订与未解决项 |
| 用户明确要互动构思、分节起草或完整评审／迭代流程 | `egm:egm-brainstorm` / `egm:egm-draft` / `egm:egm-review` / `egm:egm-review-loop`，按请求选择 | 原技能定义的产物与实际完成状态 |

审查人数、标准、角色文件、复审和收敛条件从所选 EGM 当前技能读取；本入口不维护另一份协议。方案审查与候选代码审查按[各自范围](https://github.com/felixlark/generative-software-engineering/blob/main/docs/COLLABORATION.md#review-scope-and-evidence-reuse)取证。

## 平台、验证与持续交付

| 何时调用 | 当前技能名 | 交接回 GSE 的结果 |
| --- | --- | --- |
| HTML、CSS、浏览器端 JavaScript 或 Web 界面，在实施前 | `modern-web-guidance:modern-web-guidance` | 当前官方指南及受影响实现的采用情况 |
| 本机 Chrome 已解压扩展更新、重载、换加载目录或回滚 | [`chrome-extension-update`](https://github.com/felixlark/generative-software-engineering/blob/main/skills/chrome-extension-update/SKILL.md) | OCU 实际加载路径、版本、ID、启用状态及受影响页面读回 |
| 生成或实质修改 Codex 技能 | `skill-creator` | 作用域清楚的技能及适用的检查结果 |
| 准备声称完成，但候选与真实结果的证据尚需核对 | `verification-before-completion` | 与候选和声明绑定的完成证据及真实缺口 |
| 反复工具故障、临时恢复后复发、验收缺口或提前返回 | `end-to-end-delivery` | 执行链恢复和原始结果的完成证据 |
| 已获准长周期开发或接续 | `long-running-delivery` | 沿原任务保持的进度、交接与交付结果 |

## GSE 宣发审阅

| 何时调用 | 当前技能名 | 交接回 GSE 的结果 |
| --- | --- | --- |
| GSE 选题与短稿已写出，尚未翻译或做图时 | `copy-editing`（[Corey Haines / marketingskills](https://github.com/coreyhaines31/marketingskills/tree/main/skills/copy-editing)） | 是否值得讲、目标读者是否能看懂，以及必要修改；衔接归[迭代宣发](https://github.com/felixlark/generative-software-engineering/blob/main/communications/growth.md) |

## 今后接入新技能

先查原技能是否已覆盖当前问题。接入只增加必要触发、名称／发现方式及返回产物；改进专门方法时改其自身归属。技能各自更新，调用方读取当前版本。这里不设更新定时器，也不承诺替来源自动升级。

历史归因与保留许可见[方法来源](method-sources.md)。GSE 自有规范继续维护结果责任、交付与证据语义。

新技能接入交付时，将新增能力、用途、典型案例、预期效果和实际证据交给[迭代宣发入口](https://github.com/felixlark/generative-software-engineering/blob/main/communications/growth.md)先审选题和短稿，通过后再生成对应内容包；具体生产与运营方法继续使用各自技能。
