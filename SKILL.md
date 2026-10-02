---
name: "book_infographic"
description: "Turns a book (title, source text, or article link) into a human-made-looking infographic: classify the book, pick analysis dimensions, write the copy brief, choose a layout, render the PNG, and QA it like a picky reader."
---

# Book Infographic

## Purpose
Produce one infographic per book that reads like a real editor and designer made it — not an AI template. This skill owns the full chain: content analysis first, layout second, render last, with a reader-advocate QA gate before anything ships.

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

### 3. Layout Brief (role: Information Designer)
- Read `references/layout-patterns.md`.
- Choose the layout from the *information relationship* (timeline, toolbox, concept map, dashboard, character arc, comparison matrix, causal mechanism) — never default to one skeleton, and never reuse the same skeleton across books in one batch.
- Define: primary structure (+ optional secondary), the one amplified takeaway line (~2x size), a visual motif carried through the whole piece, palette (max 3 colors + paper tone), typographic scale, and where key numbers become visual anchors.

### 4. Build & render
- Build a single 1080px-wide HTML file (`Noto Sans CJK SC` / `Noto Serif CJK SC` with system fallbacks, paper background).
- Render with `bin/render.py` → 2x PNG, full page.

### 5. QA (role: Reader Advocate — has veto power)
- Run `references/quality-checklist.md` against the PNG as a phone reader would see it.
- Any failure sends the work back to step 2 (content) or step 3 (layout). Re-render and re-check.

### 6. Final check
- Open the PNG and verify: no clipped text, no overflow, no mojibake.
- The 3-second test: theme, structure, and the one amplified conclusion must be recognizable at a glance on a phone screen.

Present the Classification, Dimension Selection, Content Brief, and Layout Brief to the user before rendering; proceed on their go-ahead (skip only if they said "just render it"). Deliver the PNG plus the QA Report.

## Output Contract
- One PNG per book (1080px wide, 2x scale), saved under a per-project folder.
- The four briefs (Classification, Dimension Selection, Content Brief, Layout Brief) and the QA Report — as short sections in chat or as files, whichever the user prefers.
- Every factual claim (author bio, dates, numbers, quotes) traceable to the source material or prior research; no invented facts.

## Operating Rules
1. Copy before layout. No visual work until the Content Brief is locked.
2. One book, one character: a distinct visual motif and structure per book; batch work must not share a skeleton.
3. Graphics must carry information (timeline, comparison, matrix, flow, map). At most one purely decorative illustration; delete it if it doesn't aid understanding.
4. Max three main colors plus paper tone. No all-centered, all-card, full-rounded-corner, gradient-everywhere styling.
5. Column headers in natural spoken language (e.g. "这本书在回答什么", "他凭什么写"), never "核心概念" / "作者简介" boilerplate.
6. Mixed types: pick dimensions from each type and fuse them into one brief; never concatenate two templates.
7. Unknown types: use the fallback protocol; record the new type so the library grows.
8. The Reader Advocate can veto at step 5. A veto is a rework order, not a suggestion.
