# Belajar Power BI

A free, production-ready learning website that takes an absolute beginner from
never having opened Power BI to publishing their first dashboard. Bilingual
(English + casual Bahasa Indonesia), light-first, WCAG-AA, and completely static.

- **8 modules · 23 lessons · one finished dashboard**
- No framework, no build step at serve time, no npm dependencies at runtime
- Progress saved to `localStorage` only — no accounts, no cookies, no tracking
- Deploys to Cloudflare Pages exactly as delivered

---

## File tree

```
/
├── index.html                      Homepage
├── curriculum/index.html           All 8 modules + progress
├── downloads/index.html            Every practice dataset in one place
├── about/index.html                Who made this and why
├── module/
│   ├── 0/index.html                Module overview
│   ├── 0/what-is-power-bi/index.html
│   ├── 0/install-power-bi-desktop/index.html
│   ├── 0/tour-of-the-window/index.html
│   ├── 1/ … 7/                     (same shape for every module)
│   └── 7/checklist-and-next-steps/index.html
├── assets/
│   ├── styles.css                  One shared stylesheet (design tokens as CSS vars)
│   ├── app.js                      One shared script (progress, rail, lightbox)
│   └── img/                        Screenshots (SVG placeholders) + favicon
├── datasets/
│   ├── coffee-sales.csv
│   ├── messy-orders.csv
│   ├── sales-and-products.zip
│   └── capstone-superstore.zip
├── scripts/                        DEV ONLY — not served, not required to deploy
│   ├── content.py                  All curriculum content, as structured data
│   ├── art.py                      Draws the Power BI UI screenshots as SVG
│   └── generate.py                 Renders the static site from that content
├── README.md
└── NOTES.md                        Assumptions and open questions
```

Every page under `/`, `/curriculum/`, `/downloads/`, `/about/`, `/module/*` is a
plain, fully-written `index.html`. There are **no** placeholders or
"repeat for other modules" — all 23 lessons are written out.

---

## Deploy to Cloudflare Pages

The site is already static HTML/CSS/JS. There is nothing to build.

### Option A — Connect your Git repository (recommended)

1. Push this repository to GitHub (or GitLab).
2. In the Cloudflare dashboard go to **Workers & Pages → Create → Pages →
   Connect to Git**.
3. Select this repository.
4. On the **Build settings** screen:
   - **Framework preset:** `None`
   - **Build command:** *(leave empty)*
   - **Build output directory:** `/`  *(the repository root)*
5. Click **Save and Deploy**. Cloudflare publishes the root of the repo as-is.

Because pages live in folders as `index.html`, Cloudflare serves clean URLs
automatically (`/module/1/` → `module/1/index.html`).

### Option B — Direct upload (no Git)

1. In **Workers & Pages → Create → Pages → Upload assets**, create a project.
2. Drag the entire repository folder (or a zip of it) into the uploader.
3. Deploy. Done.

### Option C — Wrangler CLI

```bash
npm install -g wrangler        # one-time
wrangler pages deploy . --project-name belajar-power-bi
```

### Custom domain

After the first deploy, open the project → **Custom domains → Set up a domain**
and follow the DNS prompt.

---

## Regenerating the site (for maintainers)

The HTML is generated from one content file so every lesson stays on the
**identical template**. You only edit content; you never hand-edit 23 pages.

```bash
python3 scripts/generate.py     # rewrites all HTML, app.js, images, datasets
```

- `scripts/content.py` — the single source of truth. Curriculum text, steps,
  menu paths, checkpoints, common mistakes, and **screenshot annotations** all
  live here as data.
- `scripts/generate.py` — the renderer. Requires only the Python standard
  library (no pip installs).

The `scripts/` folder is a development convenience. It is **not** needed to
serve or deploy the site — Cloudflare only ever sees the generated static files.

---

## The annotation component

Raw Power BI screenshots are annotated with numbered callout markers and a
matching legend. Annotations are declared **as data next to the image**, never
hardcoded into page markup, so the same component renders every figure on the
site.

### Declaring a figure (in `scripts/content.py`)

```python
fig(
    "/assets/img/getdata-button.svg",              # image src
    "The Home ribbon with the Get data button …",  # alt text (screen readers)
    [
        m(1, 14, 22, "The Get data button on the Home tab",   # English legend
                     "Tombol Get data di tab Home"),           # Bahasa legend
        # m(number, x%, y%, english, indonesian, line=optional)
    ],
    caption="",                                     # optional caption
)
```

- `x` / `y` are **percentages** of the image box, so markers stay correct at
  any width and on any screen size.
- `m(...)` optionally takes `line={"angle": deg, "len": pct}` to draw a
  connector so a marker can sit **offset** from a tight UI element instead of
  covering it.

### What it renders

For each figure the component (`render_figure` in `generate.py`) outputs:

1. A `<figure>` with the image inside a real `<button class="figure-frame">`
   (keyboard-focusable; tap/click/Enter opens the full-screen lightbox with
   native pinch-zoom).
2. Circular **callout markers** positioned by percentage:
   accent-colour fill, white numeral, 2px white outer ring + a faint dark ring
   so they stay legible against any screenshot background. Markers are
   `aria-hidden`.
3. A numbered **legend** (`<ol class="figure-legend">`) directly beneath the
   image, generated from the *same* marker data — so markers and legend can
   never drift out of sync. The legend text is the accessible source of truth
   and carries both languages.
4. The `alt` text you supplied, on the `<img>`, for screen-reader users.

### Where the marker geometry comes from

Marker positions live in `scripts/art.py` (`ANCHORS`), because *where* a callout
must land is a property of the artwork, while the legend wording is content. An
anchor is either:

```python
(x, y)               # marker sits on the element
(x, y, tx, ty)       # marker sits clear at (x, y), connector drawn to (tx, ty)
```

The four-value form is used for small controls — a ribbon button, the Sign in
link — so the numbered circle never covers the thing it points at. The connector
angle is computed in pixel space from the image's real aspect ratio, so it stays
correct at every screen width.

If an image has no `ANCHORS` entry, the `x`/`y` you gave in `content.py` is used
instead.

---

## Screenshot artwork

`scripts/art.py` draws every screenshot as a clean, light-mode SVG mock of the
real Power BI UI: the ribbon with its actual command names, the view rail, the
Visualizations and Fields panes, the Power Query Editor with Applied Steps,
Model view with relationship cardinality, the CSV import dialog, the Microsoft
Store, and the browser-based Power BI Service.

Scenes are keyed by image file name in the `SCENES` registry, so adding or
changing a picture is a one-line change. SVG keeps every page tiny and every
label crisp at any zoom.

### Swapping in real captures

Replace the SVGs in `assets/img/` with real (unannotated) Power BI Desktop
screenshots, keeping the same file names — or point the `fig(...)` `src` at new
files. Then delete that image's `ANCHORS` entry in `art.py` and set each
marker's `x`/`y` in `content.py` to land on the right UI element. No page markup
changes.

---

## Language toggle

Interface chrome stays in English. Tutorial content is written in both English
and casual Bahasa Indonesia, and an **ID / EN** switch in the header chooses
which one to read.

- Both languages are always present in the HTML. The toggle only sets
  `data-lang` on `<html>`, and CSS hides the other one — so with JavaScript
  disabled the reader still gets *everything*, nothing is lost.
- The choice is remembered in `localStorage` (`pbi-lang-v1`) and applies across
  every page.
- The default follows the browser's language, falling back to Bahasa Indonesia,
  because that is who this course is written for.
- Power BI's own menu names stay in English in both languages, so learners can
  always find them in the app.

---

## Accessibility & performance notes

- **WCAG AA contrast** throughout. The bright brand accent `#02A0C1` is used
  only for non-text elements (fills, borders, focus rings, markers). Text links
  and control labels use a darker sibling `--accent-strong: #0A7C8F` (≥ 4.5:1).
  See `NOTES.md` for the reasoning.
- **Works with JavaScript disabled** for reading; only progress tracking needs
  JS. All content, images, and legends are in the static HTML.
- **Keyboard navigable** end to end with visible focus states; a skip link is
  the first focusable element on every page.
- **Every page is well under 200 KB** excluding images (largest ≈ 18 KB).
- Screenshots are `loading="lazy"` and `decoding="async"`.
- The only external resource is the Google Font (Plus Jakarta Sans). If it is
  blocked, the site falls back to `system-ui` and stays fully usable.

---

## Privacy

No accounts, no login, no backend, no database, no analytics, no cookies, no
tracking of any kind. Progress lives in `localStorage` under the single key
`pbi-progress-v1` and never leaves the browser. A **Reset my progress** control
is in the footer of every page.
