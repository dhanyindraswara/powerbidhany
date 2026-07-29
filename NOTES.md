# Notes — assumptions & things I had to decide

A short, honest list of everything I was unsure about or had to assume, as the
brief asked for.

## 1. The curriculum content was a placeholder — I wrote it

Section 12 of the brief listed only the eight **module titles** and left a
`[PASTE YOUR FULL CURRICULUM HERE]` marker. Since the final instruction was
"Build the complete site. Do not stop partway and ask", I authored the full
curriculum myself: 23 lessons, each with real steps, menu paths, checkpoints,
"why this matters", and specific common-mistakes notes for a true beginner.

**Please review the lesson text for accuracy against your teaching intentions.**
It is written to be correct and beginner-safe, but it is my content, not yours.
All of it lives in one file (`scripts/content.py`) so it is easy to edit.

Lesson counts per module: 0→3, 1→3, 2→4, 3→3, 4→3, 5→3, 6→2, 7→2 (23 total).
Adjust freely in `content.py`.

## 2. Screenshots are drawn, not captured

The brief says *you* will supply raw Power BI Desktop screenshots. Rather than
leave grey boxes, I drew all 55 of them in `scripts/art.py` as light-mode SVG
mockups of the real UI — the ribbon with its actual command names, the
Visualizations and Fields panes, the Power Query Editor with Applied Steps,
Model view with the 1-to-many symbols, the CSV import dialog, the Microsoft
Store, and the Power BI Service in a browser.

They are deliberately *simplified but accurate*: every menu name, button and
pane is where it really is and spelled as it really is, so a learner following
along recognises their own screen. They are not pixel-perfect reproductions.
When you have real captures, drop them in per the README — the annotation
system takes them unchanged. Alt text is already written for the real
screenshot each figure represents.

## 3. Accent colour vs WCAG AA — a real conflict I had to resolve

Two constraints collided:

- Token spec: accent `#02A0C1` for "interactive elements, links".
- Non-negotiable #6: WCAG AA contrast throughout, no exceptions.

`#02A0C1` as **text** on white is only **3.09:1** — it fails AA (needs 4.5:1),
and white text on it (buttons) is the same 3.09:1. There is no way to honour
both literally.

Resolution: I kept `#02A0C1` as the brand accent for everything that is **not
text** — fills, borders, focus rings, hover tints, and the annotation markers
(non-text elements only need 3:1, which it passes). For **text** — links,
button labels, uppercase eyebrows, menu-path chips — I introduced a darker
sibling in the same hue, `--accent-strong: #0A7C8F` (4.89:1), with an even
darker hover. On the dark section dividers the bright accent has enough
contrast (5.8:1) and is used as-is. I believe this honours the *intent* of both
constraints; if you would rather relax AA and keep the literal accent on
buttons, change `--accent-strong` back to `--accent` in `assets/styles.css`.

The annotation markers themselves keep the spec-mandated style exactly (accent
fill, white numeral, 2px white ring). Their numerals are decorative and
`aria-hidden`; the accessible information lives in the numbered legend text
beneath each image, which is dark-on-white and easily passes AA.

## 4. Bilingual handling — now a toggle

Interface chrome stays in English. Tutorial content is written in both English
and casual Bahasa Indonesia ("aku"/"kamu", never "gue"), and an **ID / EN**
switch in the header picks which to read.

Both languages stay in the HTML; the toggle only sets `data-lang` on `<html>`
and CSS hides the other. That keeps the "must work with JavaScript disabled for
reading" requirement intact — with JS off you simply see both, which is what the
site did before the toggle existed.

The default follows the browser language and falls back to Bahasa Indonesia,
since that is the target audience. Assumption worth checking: I decided ID
should win the fallback rather than EN. One line in `app.js` if you disagree.

Power BI menu names are left in English inside both languages, as required, so
learners can still find them in the app.

## 5. "Datasets as .zip"

Two lessons reference multi-table datasets (`sales-and-products.zip`,
`capstone-superstore.zip`). I generated real zip files each containing two CSVs
(a sales table and a products table) so the Module 3 relationship lesson has
two things to relate. The single-table lessons use plain `.csv`.

## 6. Static routing / clean URLs

Routes like `/module/1/import-your-first-file` are implemented as
`module/1/import-your-first-file/index.html`. Cloudflare Pages serves these as
clean URLs automatically, so no `_redirects` file is needed. All internal links
are root-absolute (`/module/1/…`) so they work at any depth.

## 7. The generator is a dev tool, not a build step

The brief forbids a build step. The delivered site is plain static files with
zero build. `scripts/generate.py` is a **development** convenience that produces
those files and guarantees the identical-template requirement; Cloudflare never
runs it. If you would prefer the repo to contain *only* hand-equivalent static
files, you can delete `scripts/` after generating — the site is unaffected.

## 8. First-visit explainer

Implemented as a slim inline bar under the header (not a modal), shown once and
dismissible, remembered via `localStorage`. Because it only concerns progress
(which needs JS), it is hidden by default in the HTML and revealed by JS, so
no-JS readers never see a dead control.

## 9. Things I deliberately did NOT add

Per the brief: no testimonials, no feature grid, no pricing, no newsletter
popup, no dark-mode toggle, no analytics, no cookies. No decorative use of the
accent. No neon/glow/glass/gradient-text/parallax/particles.
