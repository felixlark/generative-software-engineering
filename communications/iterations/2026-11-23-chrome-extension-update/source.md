# Chrome 扩展加载来源核对

- 内容标识 `2026-11-23-chrome-extension-update`，对应已合并版本 `95f81608f49b8a785ce4f223e837dc9a8cb927d4`。[GSE #28](https://github.com/felixlark/generative-software-engineering/pull/28)
- 真实案例中，扩展迁入新仓后，日常 Chrome 在原加载目录把扩展从 1.2.7 重载到 1.2.9，并在实际页面核对了行为。GSE #28 还记录随后发生的加载目录迁移。双目录同版本是核对方法针对的情形。[案例回执](https://github.com/felixlark/x-use/issues/4#issuecomment-7091205794)
- 预期用途是尽早发现 Chrome 仍在加载旧路径，避免拿旧扩展的页面表现判断新版。该案例没有测量节省时间。
- 短稿制作时判断步骤可直接照做。用户复核后认为这个选题价值不足，于 2026-11-23 决定不发。
- [双语短稿、图片与替代文本](drafts.md)和[图卡源文件](render.swift)仅作历史留档。发布候选已撤回。
