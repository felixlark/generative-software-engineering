# 代码简化

用于当前实现明显复杂或难读的部分，在写代码时直接应用；基本原则已进入GSE主入口，独立的`code-simplifier` Skill不是依赖项。

- 保持单一职责和明确接口，收敛重复状态、重复逻辑、不必要的抽象与分支；有助于理解合同的注释和抽象继续保留。
- 代码整理保持已承诺的输出、错误、外部副作用及公共接口。若目标是删除功能、限制、兼容层或专用测试，先按当前需求与实际消费者判断，不能为了保留旧测试而恢复已退役行为，也不能由整理代码推导删除授权。
- 只处理本次改动及直接相关代码；用户明确要求全仓精简时再扩大。可读性优先，不为了少写几行而合并不同职责或增加隐含行为。
- 已安装独立Skill且确需更多细节时，可按需参考其中适用内容；项目合同与GSE的当前范围优先，工具可用不要求新建Agent。
- 使用现有受影响检查。复用未失效的验证，只重验实际改变的结论；完成清楚、可维护的实现即可交付，不设置额外阶段、审批、审查角色、固定轮次或全量重跑。

规范归[最小充分工程](https://github.com/felixlark/generative-software-engineering/blob/main/docs/MINIMAL_SUFFICIENT_ENGINEERING.md#inline-simplification)，来源、改写边界与许可见[方法来源](method-sources.md#code-simplifier-in-the-implementation-loop)。
