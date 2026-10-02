[中文版](README.zh-CN.md)

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
