# 现代 Web 平台指导

Modern Web Guidance 是由 Google Chrome、Microsoft Edge、Mozilla Firefox 和 MDN 团队及社区共同维护的 Web 开发技能，按需提供平台用法、无障碍与浏览器兼容建议。GSE 在现有实施与验证循环中调用它。

## 何时使用

实现或修改 HTML、CSS、浏览器端 JavaScript、Web 界面、无障碍、安全或性能行为时，先查当前任务对应的指南，再选择实现和依赖。框架中的标准 Web 平台行为同样适用；纯后端、构建配置、文案修改和原生 App 不触发此路径。复用仍适用的已取指南。

## 按需查询与实施

已安装官方 `modern-web-guidance` 技能时，读取并沿其当前合同执行。无该技能的宿主可用官方 CLI（命令行工具，Node.js 22 或更新版）完成同一查询：

```sh
npx -y modern-web-guidance@latest search "light dismiss dialog" --skill-version 2026_11_09-5bcc021b
```

将示例查询替换为当前能力的二至五个英文词，描述一个具体的界面或平台动作；省略项目名和框架名，多项能力分别查询。按返回的描述选择真实 ID，再取得指南：

```sh
npx -y modern-web-guidance@latest retrieve "<search 返回的 ID>"
```

有 `pnpm` 时可用 `pnpm dlx modern-web-guidance@latest` 替换 `npx -y modern-web-guidance@latest`。查询无匹配时，用具体组件名或同义词改写一次，必要时查 `list`；仍未覆盖则说明缺口，不套用无关指南。大输出若保存到临时文件，完整读取该文件。工具故障沿宿主正式入口修复；未取得指南时明确受影响范围。

实施前确认项目支持的浏览器或内嵌运行时。Baseline 是 Web 功能跨主流浏览器的可用性标记；官方指南默认允许 Widely available（广泛可用）功能直接使用，其他功能按指南采取兼容方案。项目明确的支持范围优先，不能把“Chrome 可用”当成跨浏览器成立。按实际需求选原生能力、特性检测和必要降级，保留仍承担兼容义务的库与行为；适配框架时保留指南涉及的语义、焦点、生命周期及无障碍约束。

完成时对照实际取到的指南核查受影响实现，并沿 GSE 原有验收覆盖真实用户路径和承诺的浏览器。指南符合、编译通过和运行验收分别留证；在结果中简述真正采用的指南与关键取舍。遵守已安装官方技能的使用披露合同。

## 已有代码现代化

仅在用户要求目录或项目范围的旧模式审计／现代化时使用扫描；单一组件修复或功能开发继续定向查询。

```sh
npx -y modern-web-guidance@latest legacy-scan <目标路径> --json
```

依次扫描、按每项 `keepWhen`／`dropWhen`（保留／排除条件）核查上下文、报告有效发现；获得修改授权时再取对应指南、实施并验证。扫描仅覆盖可确定性检测的部分指南；零发现不能证明全面现代化。必要兼容代码、特性检测、第三方代码或相似但用途不同的实现可能被命中，不为清零删除它们。修改后重扫受影响文件，并运行能覆盖变化的既有检查与真实入口验收。

本适配不新增全仓扫描、CI 机器人、自动升级、固定浏览器门槛或评审阶段。上游评测及案例数字属于其任务与环境，不能直接作为 GSE 效率结论。

## 来源与维护

选择性适配 [GoogleChrome/modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance)，核读提交 `4dd968349e54ca45a05dd5c818fb035c9054b022` 的 [Skill](https://github.com/GoogleChrome/modern-web-guidance/blob/4dd968349e54ca45a05dd5c818fb035c9054b022/skills/modern-web-guidance/SKILL.md) 和包版本 1.0.0；查询协议标识为 `2026_11_09-5bcc021b`，不是 npm 包版本。命令使用上游 `latest`；更新时重新核对协议、支持范围和许可，不假定所有版本行为相同。

参考[官方文档](https://developer.chrome.com/docs/modern-web-guidance)、[现代化流程](https://developer.chrome.com/docs/modern-web-guidance/modernization-workflow)及 [ChromiumDev 原帖](https://x.com/ChromiumDev/status/2121339675667309047)。保留上游 [Apache-2.0 许可](../LICENSE.modern-web-guidance)，本参考由 GSE 改写维护，指南内容继续从官方工具按需获取。
