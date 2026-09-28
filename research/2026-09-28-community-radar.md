# Community radar — 2026-09-28

Non-normative research note. Window: 2026-09-21 00:00 through the scan on 2026-09-28, approximately 09:00 Asia/Shanghai. Sources retrieved on 2026-09-28. Publication dates below use the source's date or explicitly recorded UTC timestamp; retrieval dates are not publication dates.

## What this scan adds

The useful question this week is whether more agents improve an outcome under a deadline **and** at what total cost. A new preprint reports gains from decentralized cooperation, while a practitioner comparison illustrates how model, harness, rubric, and token accounting complicate comparisons. Neither establishes a generally superior organization or changes GSE's root ownership invariant.

The repository already has a [benchmark protocol](BENCHMARK_PROTOCOL.md) covering participant cost, controlled inputs, and evidence. This scan contributes dated external cases and a concrete follow-up experiment, rather than another copy of those rules. The two README versions now provide aligned paths from explanation to a task contract, comparison, and contribution.

## Sources and admission decisions

| Source and permanent reference | Author / organization | Publication date; type | Decision and relevance |
| --- | --- | --- | --- |
| [Agensh: Scaling Organizational Intelligence to 1,024 Agents, v1](https://arxiv.org/abs/2609.26781v1) | Zhihao Zhan, Ting Song, Li Dong, Shaohan Huang, Jianxun Lian, Yan Xia, Furu Wei; Microsoft Research | 2026-09-22; preprint | Include as an author-reported experiment testing decentralized cooperation at scale. Do not infer cost efficiency or reproduction readiness. |
| [A test of agentic workflows for software engineering](https://hankconn.github.io/a-test-of-agentic-workflows-for-software-engineering.html) | hankconn, site publisher | 2026-09-26; practitioner experiment / blog | Include as a methodology discussion, not a model ranking. The setup and limitations are more transferable than the scores. |
| [Hermes Agent v0.21.4 (v2026.9.21)](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.9.21) | NousResearch; release author teknium1 | 2026-09-21 18:10:55 UTC; GitHub release | Track only. The release is verifiable, but its curated notes are deferred to v0.22.0; no new GSE principle follows from release volume. |
| [DeepLearning.AI Course Code & Hands-On Materials](https://github.com/https-deeplearning-ai/deeplearning-ai/tree/ea8d55a0fad0490becc87e046acb1aa4d532d232) | https-deeplearning-ai GitHub organization | Publication date not established; repository architecture reference, snapshot retrieved 2026-09-28 | Use as background, not weekly news. Its directory separates course discovery from companion code and per-course setup. |

### Agensh: deadline gains are not a cost comparison

**Verified source content:** v1 describes workers gathering context, claiming tasks, taking action, verifying, and merging progress through shared workspace, messaging, and shared context. Its reported setup uses GPT-5.6-sol (high), the Copilot single-agent harness, a six-hour budget, and no Internet on five selected difficult ProgramBench tasks. We read the paper; we did not execute its experiments.

**Author-reported result:** increasing workers from 1 to 128 raises the mean final test-pass rate from 19.31% to 28.78%: **9.47 percentage points**, about **49% relative**. The 1,024-worker result is specifically on pandoc: 33.89% to 55.06%, not a five-task average. These rates measure partial test success, not completed, accepted software deliveries.

**Reproduction gap:** the paper advertises `https://github.com/microsoft/Agensh`, but Exa returned `CRAWL_NOT_FOUND` and an unauthenticated GitHub API repository lookup returned HTTP 404 during this scan. That does not establish whether the repository is private, moved, or absent. Code availability and an executable reproduction were not verified. Do not advertise this as a runnable tutorial yet.

**GSE hypothesis:** decentralized task discovery may help highly parallel work under tight deadlines, while a root owner remains accountable for scope and final acceptance. Accountability and central scheduling are different questions. The selected tasks, partial pass rates, and unmatched aggregate compute do not justify replacing the current method.

### Practitioner comparison: preserve the confounders

**Verified source content:** the article reports one trial per workflow, different product harnesses, medium reasoning, model judges, and costs calculated from token types in logs. It also gives bonus credit for anticipated future work. The table labels one configuration “2 runs,” so the one-trial statement needs clarification before pooling the numbers.

**Community interpretation:** the author's recommendations about particular models and reviewers are opinions based on that setup. They are not independently verified general results. A rubric rewarding speculative future readiness also differs from GSE's [minimal sufficient engineering](../docs/MINIMAL_SUFFICIENT_ENGINEERING.md).

**Admission:** retain the cost-accounting and rubric questions; reject a “best model” leaderboard. We did not audit the underlying logs, independently judge patches, or rerun the task. No quoted ranking becomes a repository recommendation.

### Learning hub: make the next action concrete

**Observed structure:** the DeepLearning.AI repository presents a course directory, links to separate companion repositories, and directs users to their setup instructions. It distinguishes a navigation hub from runnable course material.

**Local application:** the README learning-path table connects four reader goals to existing documents and tangible outputs. It explicitly labels current examples as explanatory, avoiding a false promise of runnable labs. The contribution route uses the existing contribution guide rather than introducing a new process. No course content was copied.

**Growth hypothesis:** clearer entry points, useful dated analysis, and explicit contribution opportunities may make the repository worth returning to or starring. No star conversion or causal growth improvement was measured. Additional diagrams and runnable tutorials are deferred until they explain a concrete gap or have verified executable material.

## Search coverage and exclusions

Exa discovery covered five areas: papers/evaluations; GitHub releases; X announcements; Reddit experience/failures; and learning-hub information architecture. Queries used the weekly dates and then narrowed to specific sources. This is a bounded scan, not exhaustive coverage of any platform.

| Area | Search angle / follow-up | Coverage and exclusions |
| --- | --- | --- |
| Papers and preprints | Coding-agent evaluations, human collaboration, and Agensh scaling | Deduplicated Agensh abstract, HTML, PDF, project page, and summaries into one paper. FLARE (`arXiv:2609.23808`) appeared with a 2026-09-20 search date, outside the window; not admitted as this week's finding. |
| GitHub and tool releases | Coding-agent releases in September 21–28; fetch source release | Hermes tag and timestamp confirmed through the GitHub API. Aggregator summaries were discovery aids only. Claude Code v2.1.277 was dated September 18 and excluded from weekly news. |
| X | Domain-targeted coding-agent evaluation search, then researcher announcements about Agensh | No qualifying original status URL obtained. Paper/project pages returned by broader searches are not X evidence. No X claim adopted. |
| Reddit | Domain-targeted coding-agent failure search, then cost/review discussions | No qualifying weekly original thread verified. Historical third-party Reddit snapshots from September 11–12 and secondary sentiment/ROI articles were not substituted for original discussions. |
| Learning repositories | Andrew Ng / DeepLearning.AI course and companion-code structure | Prefer the organization repository to learners' course copies. Use its structure as background; do not claim it launched this week or that stars demonstrate causation. |

Release tags, paper versions, and dated article URLs provide traceability. Mutable source pages may change; the learning-hub reference is pinned to the commit returned by GitHub during the scan. No new normative rule was admitted, and no external model/service was installed or benchmark run.

## Next experiment to pursue

Can delegated or decentralized execution reach the same **accepted outcome** sooner under a fixed **total cost**, not only a fixed deadline? Use the existing [benchmark protocol](BENCHMARK_PROTOCOL.md) to compare a single owner, dynamic delegation, and decentralized scheduling on both parallel and sequential tasks. Preserve the same acceptance rubric and baseline, count all participants and rework, and repeat trials before generalizing. This is a proposed experiment, not a completed result.

The first practical gate is to verify access to Agensh's advertised implementation and reproduction materials. Meanwhile, seek original X/Reddit posts with exact task inputs and traces; do not fill coverage gaps with unattributed sentiment.
