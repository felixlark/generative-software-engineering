# 工程方法来源与适配边界

以下按需参考方法借鉴 Lauren Tan 的 [pstack](https://github.com/cursor/plugins/tree/e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a/pstack)，核验版本 0.15.9，提交 `e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a`。保留其 [MIT 许可与版权声明](../LICENSE.pstack)。这是选择性适配，不安装或执行 Cursor 插件，也不自动跟随上游更新。

| 本地方法 | 上游依据 |
| --- | --- |
| [修改影响与设计取舍](change-design.md) | [blast-radius](https://github.com/cursor/plugins/blob/e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a/pstack/skills/blast-radius/SKILL.md)、[architect](https://github.com/cursor/plugins/blob/e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a/pstack/skills/architect/SKILL.md) |
| [独立审查](independent-review.md) | [interrogate](https://github.com/cursor/plugins/blob/e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a/pstack/skills/interrogate/SKILL.md) |
| [项目验收地图](project-verification.md) | [create-verification-skill](https://github.com/cursor/plugins/blob/e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a/pstack/skills/create-verification-skill/SKILL.md) |
| [重复错误治理](repeated-errors.md) | [correct](https://github.com/cursor/plugins/blob/e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a/pstack/skills/correct/SKILL.md) |
| [性能结论核验](performance-evidence.md) | [benchmark-checklist](https://github.com/cursor/plugins/blob/e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a/pstack/skills/benchmark-checklist/SKILL.md)、[eval](https://github.com/cursor/plugins/blob/e43c7ee26e0038c6c1fa8380dd34ce86ff94cb2a/pstack/skills/poteto-mode/playbooks/eval.md) |

这些文件实例化 GSE 的现有责任、证据与复杂度原则；规范冲突以 [GSE 规范](https://github.com/felixlark/generative-software-engineering/blob/main/docs/SPECIFICATION.md) 的对应 owner 为准，用户目标、项目权限和真实工具合同保持优先。

适配保留风险驱动、单 owner、关键事实证明、独立证据判断和可复用验收；不移植 Cursor 的 Task／模型 slug／loop／alwaysApply 配置，也不引入强制委派、自动外发、worktree 或 PR 流水线。多模型共识不作为事实证明，注释和兼容层按实际合同保留；运行和发布走项目已授权控制面。

模型与推理强度沿用当前用户／任务设置，本套方法不维护第二份型号表。每次实际改动只加载所需参考，不要求读取上游全文或整套原则。
