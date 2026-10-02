# book-infographic

> Turn a book into a human-made-looking infographic — not an AI template.

`book-infographic` is a skill (a reusable playbook) for AI assistants. Give it a book — a title, pasted text, or a link to an article/review — and it produces a polished, editorial-style infographic PNG. Content analysis comes first, layout second, rendering last, with a reader-advocate QA gate before anything ships.

## How it works

1. **Intake** — book title (+ author), excerpt, or article link. Title only? Key facts are researched first; quotes, dates, and numbers are never invented.
2. **Classify** — the book gets one primary type (plus up to two secondary types) from a 10-type library; unknown types fall back to a bespoke protocol instead of being force-fit.
3. **Content Brief** — every headline and sentence is finalized in plain spoken language *before* any layout discussion.
4. **Layout Brief** — the layout is chosen from the *information relationship* (7 patterns), with one amplified takeaway, a visual motif, and a restrained palette.
5. **Render** — a single 1080px-wide HTML file rendered to a 2× PNG via `bin/render.py` (Playwright + Chromium).
6. **QA** — a Reader Advocate checks the PNG the way a phone reader would see it; any failure sends the work back for rework.

Operating rules: copy before layout · one book, one visual character (never reuse a skeleton across a batch) · graphics must carry information · max three colors plus paper tone · spoken-language headers, never boilerplate.

## Book types

| # | Type | Analysis dimensions (examples) |
|---|------|-------------------------------|
| 1 | History | timeline beats, periodization, turning points, one-line historical pattern |
| 2 | Biography | life stages, decisive choices, character drivers, legacy & controversy |
| 3 | Ideas / Philosophy | core theses, concept relationships, argument chain, what's debatable |
| 4 | Social-science theory | base assumptions, core model, predictions, explanatory limits |
| 5 | Natural science | core mechanism, key evidence, old belief overturned, open questions |
| 6 | Thinking methods | toolbox (name + how to use + example), counter-intuitive points |
| 7 | Business / Management | key numbers, action framework, org rollout, failure modes |
| 8 | Psychology / Growth | core model, misconceptions, practical steps, strength of evidence |
| 9 | Technical practice | core principle, mental model, option comparison, common gotchas |
| 10 | Literary fiction | story arc, character map, transformation, themes (experimental) |

## Layout patterns

Timeline · Toolbox · Concept map · Dashboard · Character arc · Comparison matrix · Causal mechanism — chosen from the information relationship, never defaulted.

## Examples

Five infographics generated from a Chinese-language holiday reading list (each book got a different layout):

**1. 尼克《人工智能简史（第三版）》** — *A Brief History of Artificial Intelligence* — timeline layout
![Brief History of AI](examples/brief-history-of-ai.png)

**2. 马兆远《世界的逻辑》** — *The Logic of the World* — toolbox layout
![The Logic of the World](examples/the-logic-of-the-world.png)

**3. 张笑宇《AI文明史·前史》** — *A History of AI Civilization: Prehistory* — concept-map layout
![Prehistory of AI Civilization](examples/prehistory-of-ai-civilization.png)

**4. 邵怡蕾《硅基经济学》** — *Silicon-Based Economics* — comparison-matrix layout
![Silicon-Based Economics](examples/silicon-based-economics.png)

**5. 李开复《AI未来已来》** — *AI Future Is Here* — dashboard layout
![AI Future Is Here](examples/ai-future-is-here.png)

## Use as a skill

Copy this folder into your assistant's skills directory and point the assistant at `SKILL.md`. The full workflow, the type–dimension library, layout patterns, and the QA checklist live in `SKILL.md` and `references/`.

## Requirements

- Python 3
- Playwright + Chromium: `pip install playwright && python -m playwright install chromium`
- Noto Sans CJK SC / Noto Serif CJK SC (with system fallbacks) for CJK text rendering

---

## 中文说明

> 把一本书变成一张"像人做的"信息图，而不是 AI 模板。

`book-infographic` 是一个可复用的 skill（工作手册），供 AI 助手使用。输入一本书——书名、原文摘录，或一篇相关文章链接——它会产出一张精致的、编辑风格的信息图 PNG。流程是：先做内容分析，再定版式，最后渲染，发布前还有一道"读者代言人"质检关。

### 工作流程

1. **输入**——书名（+作者）、摘录或文章链接。只有书名时，先查证关键事实；不编造引文、日期和数字。
2. **分类**——从 10 种书籍类型中指定一个主类型（最多加两个次类型）；对不上的类型走定制兜底流程，不硬套。
3. **内容简报**——先用口语化的语言定稿所有标题和文案，再谈版式。
4. **版式简报**——根据信息之间的关系从 7 种版式中选择，定一个放大呈现的核心结论、一个视觉母题和克制的配色。
5. **渲染**——单个 1080px 宽的 HTML，经 `bin/render.py`（Playwright + Chromium）渲染为 2 倍 PNG。
6. **质检**——以手机读者的视角检查 PNG；不通过就打回重做。

铁律：先定文案再做视觉 · 一书一貌（同一批不许复用骨架）· 图形必须承载信息 · 最多三种主色 + 纸色 · 栏目标题用人话，不用"核心概念/作者简介"式八股。

### 书籍类型与版式

类型（10 种）：历史、传记、思想/哲学、社科理论、自然科学、思维方法、商业/管理、心理/成长、技术实务、文学虚构。
版式（7 种）：时间线、工具箱、概念地图、仪表盘、人物弧光、对比矩阵、因果机制——按信息关系选用，绝不默认套用。

### 示例

上面五张信息图来自一份中文假期书单，每本书用了不同的版式，见英文部分的示例。

### 作为 skill 使用

把整个文件夹复制到你的 AI 助手的 skills 目录，让助手阅读 `SKILL.md` 即可。完整流程、类型—维度库、版式模式和质检清单分别在 `SKILL.md` 和 `references/` 中。

### 环境要求

- Python 3
- Playwright + Chromium：`pip install playwright && python -m playwright install chromium`
- Noto Sans CJK SC / Noto Serif CJK SC（带系统回退），用于中文渲染
