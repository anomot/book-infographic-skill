---
name: "book_infographic"
description: "Turns a book (title, source text, or article link) into human-made-looking infographics: single image by default, or an overview plus module pages for information-dense books. Classify the book, pick analysis dimensions, write the copy brief, choose a layout, render the PNG(s), and QA like a picky reader."
---

# Book Infographic

## Purpose
Produce infographics per book that read like a real editor and designer made them — not AI templates. Single image is the default; for information-dense books, an optional multi-image mode produces one overview page plus 2–5 module pages under a single visual language. This skill owns the full chain: content analysis first, layout second, render last, with a reader-advocate QA gate before anything ships.

## Workflow

### 0. Intake
- Accept: book title (+ author), pasted text/excerpt, or a link to an article/review about the book.
- If only a title is given, research the book's key facts (author background, core arguments, structure) from reliable sources before writing anything. Never invent quotes, data, or publication facts.

### 1. Classify (role: Book Analyst)
- Read `references/type-dimension-library.md`.
- Assign one primary type and at most two secondary types. Books are often mixed — combine dimensions, never staple two templates together.
- If no type fits, run the unknown-type fallback: answer the five universal questions, infer 2–4 bespoke dimensions from the table of contents / narrative structure / mode of argument, and record why. Do not force-fit.

### 2. Content Brief (role: Book Analyst)
- Answer the five universal questions, then add the type-specific dimensions chosen in step 1.
- Write the **Content Brief** first: every headline and every sentence finalized, in plain spoken language, before any layout discussion. Template in `references/quality-checklist.md`.
- Cut anything that is true but adds no information. If a sentence doesn't help a phone reader in 3 seconds, it doesn't ship.

### 3. Mode decision (role: Book Analyst)
- Default: **single image**.
- Recommend **multi-image** when any of these hold: the Content Brief yields 4+ strong dimensions that each deserve a page and compression would damage them; the book has a natural modular structure (parts, methods, case clusters); or the user explicitly asks for it.
- Record the decision and one-line reason alongside the briefs. The user confirms the mode together with the briefs before any rendering.

### 4. Layout Brief (role: Information Designer)
- Read `references/layout-patterns.md`.
- **Single mode:** choose the layout from the *information relationship* (timeline, toolbox, concept map, dashboard, character arc, comparison matrix, causal mechanism) — never default to one skeleton, and never reuse the same skeleton across books in one batch.
- **Multi-image mode:** first define one master visual language for the whole set (palette, motif, type scale, number anchors); then choose a layout pattern *per page* from that page's information relationship — pages may use different skeletons, unity comes from the shared visual language. The overview page carries the book's core thesis plus a module map (each module's number, title, and the question it answers). Each module page gets its own **Module Brief** (template in `references/quality-checklist.md`).
- Define: primary structure (+ optional secondary), the one amplified takeaway line (~2x size), a visual motif carried through the whole piece, palette (max 3 colors + paper tone), typographic scale, and where key numbers become visual anchors.

### 5. Build & render
- Build 1080px-wide HTML files (`Noto Sans CJK SC` / `Noto Serif CJK SC` with system fallbacks, paper background) — one per page.
- Render each with `bin/render.py` → 2x PNG, full page.
- File naming: single mode `book-slug.png`; multi-image mode `overview.png`, `module-01.png`, `module-02.png`, … under one per-book folder.

### 6. QA (role: Reader Advocate — has veto power)
- Run `references/quality-checklist.md` against each PNG as a phone reader would see it. In multi-image mode, also run the multi-image consistency section.
- Any failure sends the work back to step 2 (content) or step 4 (layout). Re-render and re-check.

### 7. Final check
- Open each PNG and verify: no clipped text, no overflow, no mojibake.
- The 3-second test: theme, structure, and the one amplified conclusion must be recognizable at a glance on a phone screen. In multi-image mode, the set must read as one book, not N posters.

Present the Classification, Dimension Selection, Content Brief, Layout Brief (plus the mode decision, and Module Briefs in multi-image mode) to the user before rendering; proceed on their go-ahead (skip only if they said "just render it"). Deliver the PNG(s) plus the QA Report.

## Output Contract
- Single mode: one PNG per book (1080px wide, 2x scale). Multi-image mode: `overview.png` + `module-NN.png` (max 6 images total including the overview), all under a per-book folder.
- The four master briefs (Classification, Dimension Selection, Content Brief, Layout Brief), plus one Module Brief per module page in multi-image mode, and the QA Report — as short sections in chat or as files, whichever the user prefers.
- Every factual claim (author bio, dates, numbers, quotes) traceable to the source material or prior research; no invented facts.

## Operating Rules
1. Copy before layout. No visual work until the Content Brief is locked.
2. One book, one visual language: a distinct motif, palette, and type scale per book; batch work must not share a skeleton. In multi-image mode, pages may use different layout patterns — unity comes from the shared visual language, not identical skeletons.
3. Graphics must carry information (timeline, comparison, matrix, flow, map). At most one purely decorative illustration; delete it if it doesn't aid understanding.
4. Max three main colors plus paper tone. No all-centered, all-card, full-rounded-corner, gradient-everywhere styling.
5. Column headers in natural spoken language (e.g. "这本书在回答什么", "他凭什么写"), never "核心概念" / "作者简介" boilerplate.
6. Mixed types: pick dimensions from each type and fuse them into one brief; never concatenate two templates.
7. Unknown types: use the fallback protocol; record the new type so the library grows.
8. The Reader Advocate can veto at step 6. A veto is a rework order, not a suggestion.
9. Multi-image guardrails: the overview answers only "the thesis + the map" — never a shrunken full version of the book. Every module page must pass the "why does this page exist" test: if it can't name its own question, it doesn't ship. Cap 2–5 module pages. Module numbers appear both on the overview map and on the module page header.
