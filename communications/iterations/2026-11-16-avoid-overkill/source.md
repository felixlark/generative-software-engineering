# GSE 迭代笔记 01：avoid-overkill

- 内容标识：`2026-11-16-avoid-overkill`；对应交付：`88e46270b54d8dee4f02672f85b1101df0b918a5`，接入与路由清理已合并。
- GSE：Generative Software Engineering，生成式软件工程，从用户意图推进到可用软件的统一工程入口。
- 新能力：按当前需求和证据选择工程投入；决定是否需要抽象、回退或更多验证时，调用独立的 avoid-overkill 工程模式。
- 一手来源：[6Kmfi6HP/avoid-overkill](https://github.com/6Kmfi6HP/avoid-overkill)，本轮核读仓库说明及当前实际安装技能。公开署源写“来源／Source: 6Kmfi6HP/avoid-overkill”，不推定未核实的个人作者身份。
- 已验证：GSE 入口、当前技能定位、安装文件与场景选路；各技能的方法继续由自身维护。
- 示意案例：修复保存失败，先定位根因、完成修复，再验证用户能保存。用于解释方法，不声称本次修复了真实保存功能。
- 预期效果：减少无依据机制和重复工作，使交付路径更清楚。尚无同口径实战对照，不写节省比例。
- 公开身份：仅 @felixlark。正文、图、替代文本及预览均不包含现实身份；当前稿不附可能关联现实身份的 GSE 仓库链接。
- 状态：本轮首发已获明确授权并完成发布、官方读回和实际页面验收；后续逐次确认。双语正文见 drafts.md，图像提示词保留原文，最终图以 poster-zh.png 与 poster-en.png 为准。

## 交付文件

- [中文海报](poster-zh.png)与[英文海报](poster-en.png)
- [双语文案与替代文本](drafts.md)
- [中文生成提示词](prompt-zh.txt)与[英文生成提示词](prompt-en.txt)

图像使用内置 image_gen 生成，并定向补充来源署名；主 Agent 已逐项核对文字、概念示意、来源和公开身份。

## 公开结果

- [中文帖子](https://x.com/felixlark/status/2122168914285351344) · [发布页面实录](evidence/published-zh.png)
- [English post](https://x.com/felixlark/status/2122168925849030958) · [Published page](evidence/published-en.png)
- [发布回执与观测时点](publication.json)
