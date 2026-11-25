# GSE 工程基线迭代

- 内容标识：`2026-11-25-professional-engineering-baseline`
- 已合并版本：[PR #32](https://github.com/felixlark/generative-software-engineering/pull/32)，候选 head `5954014bc3e74db69a65c9bc0a92b2bfb807ea80`。
- 新能力：[professional-engineering-baseline](https://github.com/felixlark/generative-software-engineering/blob/5954014bc3e74db69a65c9bc0a92b2bfb807ea80/skills/professional-engineering-baseline/SKILL.md)要求实现类任务先核对集成基线、结果合同、验证层级和制品来源。GSE 入口继续负责选路，工程基线独立维护。
- 读者问题：AI 助手报告修复完成，但应用仍运行旧版本，或者只是测试通过、实际入口没有用。
- 真实案例：[Issue #31](https://github.com/felixlark/generative-software-engineering/issues/31)记录的近期审计发现，29 份 App 安装回执中有 5 份来自未合入主线的源码。该数字限于这次审计，不能外推为长期比例。
- 预期效果：把代码合并、制品安装和真实用户路径分开核对，减少把候选版当正式版的误判。没有同口径前后对照，不声称效率提升。

## 发布前审阅

按独立安装的 `copy-editing` 做简短审阅：

- 选题值得讲，因为它对应一个普通开发者能遇到的失败：被告知修好了，实际运行的仍是旧版本。
- 首稿避免沿用“冻结基线”“证据分层”“完成门禁”等内部词，改成测试、安装和真实使用三件可观察的事。
- 用“最近检查的 29 份安装记录”限定案例范围，不把一次审计写成普遍比例。
- 图文都围绕同一句读者价值，没有把完整工程清单塞进宣传稿。

结论：通过。可以制作双语文案和图卡，发布仍待逐次确认。
