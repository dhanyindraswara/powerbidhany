#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Static-site generator for "Belajar Power BI".

This script is a DEVELOPMENT tool only. Its output is plain HTML/CSS/JS with
no runtime dependency on any build step — exactly what Cloudflare Pages serves.
Run it from the repo root:  python3 scripts/generate.py

Why a generator? The brief demands an identical template on every lesson page
and annotations declared as data. Rendering from one function guarantees that
consistency far better than hand-copying 23 lesson pages ever could.
"""

import os
import html
import zipfile
import random

from content import MODULES, SITE

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---------------------------------------------------------------------------
# small helpers
# ---------------------------------------------------------------------------

def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)


def lesson_id(mod_n, slug):
    return f"m{mod_n}-{slug}"


TOTAL_LESSONS = sum(len(m["lessons"]) for m in MODULES)


def module_url(n):
    return f"/module/{n}/"


def lesson_url(n, slug):
    return f"/module/{n}/{slug}/"


# ---------------------------------------------------------------------------
# shared chrome
# ---------------------------------------------------------------------------

def head(title, description, canonical=""):
    return f"""<!doctype html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<meta name="color-scheme" content="light">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/styles.css">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
"""


def header(active=None):
    def cls(name):
        return ' aria-current="page"' if active == name else ""
    return f"""<header class="site-header">
  <div class="container">
    <a class="brand" href="/">
      <span class="brand-mark" aria-hidden="true">bP</span>
      <span>Belajar Power BI</span>
    </a>
    <nav class="main-nav" aria-label="Main">
      <a href="/curriculum/"{cls('curriculum')}>Curriculum</a>
      <a href="/downloads/"{cls('downloads')}>Downloads</a>
      <a href="/about/"{cls('about')}>About</a>
    </nav>
  </div>
</header>
"""


def first_visit_banner():
    return """<div class="first-visit" id="firstVisit" hidden>
  <div class="container">
    <span>Your progress is saved to this browser only — no account, no tracking.</span>
    <button type="button" id="dismissFirstVisit">Got it</button>
  </div>
</div>
"""


def footer():
    module_links = "".join(
        f'<li><a href="{module_url(m["n"])}">Module {m["n"]} — {html.escape(m["title"])}</a></li>'
        for m in MODULES
    )
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <h3>Belajar Power BI</h3>
        <p>A free, beginner-first course that takes you from never opening
        Power BI to publishing your first dashboard. Built by {html.escape(SITE['author'])}.</p>
        <p class="js-only" id="footerProgress"></p>
      </div>
      <div>
        <h3>Course</h3>
        <ul class="footer-links">
          <li><a href="/curriculum/">Curriculum</a></li>
          <li><a href="/downloads/">Downloads</a></li>
          <li><a href="/about/">About</a></li>
        </ul>
      </div>
      <div>
        <h3>Settings</h3>
        <ul class="footer-links">
          <li><button type="button" class="reset-progress" id="resetProgress">Reset my progress</button></li>
        </ul>
        <p style="margin-top:16px;font-size:.85rem;">Progress is stored in this
        browser using localStorage. No cookies. No accounts. No tracking.</p>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© Belajar Power BI. Free to use and share.</span>
      <span>Power BI is a product of Microsoft. This site is an independent tutorial.</span>
    </div>
  </div>
</footer>
"""


def lightbox_and_scripts():
    return """<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Full-screen image">
  <button class="lightbox-close" id="lightboxClose" aria-label="Close full screen">×</button>
  <img id="lightboxImg" src="" alt="">
</div>
<script src="/assets/app.js" defer></script>
</body>
</html>
"""


def page(title, description, body, active=None, mobile_progress=False):
    mp = ""
    if mobile_progress:
        mp = """<div class="mobile-progress">
  <div class="container">
    <span class="label" id="mobileProgressLabel">Progress</span>
    <span class="bar"><span id="mobileProgressBar"></span></span>
  </div>
</div>"""
    return (
        head(title, description)
        + header(active)
        + first_visit_banner()
        + mp
        + f'<main id="main">\n{body}\n</main>\n'
        + footer()
        + lightbox_and_scripts()
    )


# ---------------------------------------------------------------------------
# annotation component (rendered as data → static HTML, works without JS)
# ---------------------------------------------------------------------------

def render_figure(figure, is_checkpoint=False):
    """Reusable annotated-screenshot component.

    `figure` is a dict: {src, alt, markers[], caption}. Each marker is
    {n, x, y, text_en, text_id, line}. Markers and legend are generated
    together from the same data so they never drift apart.
    """
    if not figure:
        return ""
    markers_html = []
    for mk in figure["markers"]:
        line = ""
        if mk.get("line"):
            ang = mk["line"].get("angle", 0)
            ln = mk["line"].get("len", 6)
            line = (
                f'<span class="callout-line" style="left:{mk["x"]}%;top:{mk["y"]}%;'
                f'width:{ln}%;transform:rotate({ang}deg);"></span>'
            )
        markers_html.append(line)
        markers_html.append(
            f'<span class="callout" style="left:{mk["x"]}%;top:{mk["y"]}%;" '
            f'aria-hidden="true">{mk["n"]}</span>'
        )
    legend_html = ""
    if figure["markers"]:
        items = "".join(
            f'<li><span>{mk["text_en"]}</span> '
            f'<span lang="id" class="lang-id">· {mk["text_id"]}</span></li>'
            for mk in figure["markers"]
        )
        legend_html = f'<ol class="figure-legend">{items}</ol>'
    caption = (
        f'<figcaption>{html.escape(figure["caption"])}</figcaption>'
        if figure.get("caption")
        else ""
    )
    return f"""<figure class="figure">
  <button type="button" class="figure-frame" data-full="{figure['src']}"
    aria-label="{html.escape(figure['alt'])} (tap to open full screen)">
    <img src="{figure['src']}" alt="{html.escape(figure['alt'])}" loading="lazy" decoding="async">
    {''.join(markers_html)}
  </button>
  {legend_html}
  {caption}
</figure>"""


def bil(en, idt):
    """Render a bilingual paragraph pair (English then Bahasa Indonesia)."""
    return (
        f'<p>{en}</p>\n'
        f'<p lang="id" class="lang-id" style="color:var(--text-muted)">{idt}</p>'
    )


# ---------------------------------------------------------------------------
# module rail (persistent on every lesson page)
# ---------------------------------------------------------------------------

def render_rail(current_mod, current_slug):
    blocks = []
    for mod in MODULES:
        lessons_html = []
        for les in mod["lessons"]:
            lid = lesson_id(mod["n"], les["slug"])
            is_current = mod["n"] == current_mod and les["slug"] == current_slug
            aria = ' aria-current="page"' if is_current else ""
            lessons_html.append(
                f'<li><a href="{lesson_url(mod["n"], les["slug"])}" '
                f'data-lesson-id="{lid}"{aria}>'
                f'<span class="rail-state" aria-hidden="true"></span>'
                f'<span>{html.escape(les["title"])}</span></a></li>'
            )
        blocks.append(
            f'<div class="rail-module">'
            f'<div class="rail-module-title">Module {mod["n"]}</div>'
            f'<ul class="rail-lessons">{"".join(lessons_html)}</ul></div>'
        )
    return f"""<nav class="module-rail" aria-label="Course progress">
  <h2>Your progress</h2>
  {''.join(blocks)}
</nav>"""


# ---------------------------------------------------------------------------
# lesson page — the identical template
# ---------------------------------------------------------------------------

def render_lesson(mod, les, prev_link, next_link):
    lid = lesson_id(mod["n"], les["slug"])

    # 4. dataset button
    if les["dataset"]:
        ds = les["dataset"]
        dataset_html = f"""<div class="dataset-cta">
  <div class="ds-text">
    <strong>Practice dataset: {html.escape(ds['name'])}</strong>
    <span>{ds['desc_en']} <span lang="id">/ {ds['desc_id']}</span></span>
  </div>
  <a class="btn btn-download" href="/datasets/{ds['file']}" download>⬇ Download dataset</a>
</div>"""
    else:
        dataset_html = """<div class="notice">
  <strong>No download needed.</strong> This is a reading lesson —
  just follow along. <span lang="id">Nggak perlu download apa-apa, cukup dibaca.</span>
</div>"""

    # 5. numbered steps
    steps_html = []
    for st in les["steps"]:
        menu = ""
        if st.get("menu_path"):
            menu = f'<p class="menu-path">Menu path: <span class="path">{st["menu_path"]}</span></p>'
        img = render_figure(st.get("image")) if st.get("image") else ""
        steps_html.append(
            f"""<li class="step">
  {bil(st['instruction_en'], st['instruction_id'])}
  {menu}
  {img}
</li>"""
        )

    # 6. checkpoint (highlight colour used here and only here)
    checkpoint_html = f"""<div class="checkpoint">
  <h3><span aria-hidden="true">✓</span> Checkpoint — you should now see this</h3>
  {bil(les['checkpoint_en'], les['checkpoint_id'])}
  {render_figure(les.get('checkpoint_image'), is_checkpoint=True)}
</div>"""

    # 8. common mistakes
    mistakes_items = "".join(
        f"<li><strong>{html.escape(mk['title_en'])}</strong> "
        f'<span lang="id">/ {html.escape(mk["title_id"])}</span><br>'
        f'{mk["text_en"]} '
        f'<span lang="id" class="lang-id" style="color:var(--text-muted)">{mk["text_id"]}</span></li>'
        for mk in les["mistakes"]
    )

    difficulty = les["difficulty"]

    body = f"""<div class="container">
  <div class="lesson-layout">
    {render_rail(mod['n'], les['slug'])}
    <article class="lesson-content" data-lesson-id="{lid}">

      <nav class="breadcrumb" aria-label="Breadcrumb">
        <ol>
          <li><a href="{module_url(mod['n'])}">Module {mod['n']}</a></li>
          <li aria-current="page">{html.escape(les['title'])}</li>
        </ol>
      </nav>

      <h1>{html.escape(les['title'])}</h1>

      <p class="outcome">In about {les['minutes']} minutes you will be able to
      {les['outcome_en']}<br>
      <span lang="id" style="font-weight:400;color:var(--text-muted)">Dalam sekitar
      {les['minutes']} menit kamu bakal bisa {les['outcome_id']}</span></p>

      <div class="meta-row">
        <span class="meta-item">⏱ <strong>{les['minutes']} min</strong></span>
        <span class="meta-item">📊 Difficulty: <strong>{difficulty}</strong></span>
        <span class="meta-item">✅ You need first: <strong>{html.escape(les['need_first_en'])}</strong></span>
      </div>

      {dataset_html}

      {bil(les['intro_en'], les['intro_id'])}

      <ol class="steps">
        {''.join(steps_html)}
      </ol>

      {checkpoint_html}

      <div class="callout-block">
        <h3>Why this matters <span lang="id" style="font-weight:400;color:var(--text-muted)">/ Kenapa ini penting</span></h3>
        {bil(les['why_en'], les['why_id'])}
      </div>

      <div class="callout-block">
        <h3>Common mistakes <span lang="id" style="font-weight:400;color:var(--text-muted)">/ Kesalahan yang sering terjadi</span></h3>
        <ul class="mistakes">
          {mistakes_items}
        </ul>
      </div>

      <div class="lesson-actions">
        <div class="complete-row">
          <button type="button" class="btn btn-secondary mark-complete" id="markComplete"
            data-lesson-id="{lid}">Mark this lesson complete</button>
          <span class="complete-state js-only" id="completeState"></span>
        </div>
        <a class="btn btn-primary next-step" href="{next_link['url']}">{html.escape(next_link['label'])} →</a>
      </div>

    </article>
  </div>
</div>"""

    title = f"{les['title']} — Module {mod['n']} — Belajar Power BI"
    desc = f"Lesson: {les['title']}. In about {les['minutes']} minutes you will be able to {les['outcome_en']}"
    return page(title, desc, body, mobile_progress=True)


# ---------------------------------------------------------------------------
# module overview page
# ---------------------------------------------------------------------------

def render_module(mod):
    first = mod["lessons"][0]
    lessons_html = []
    for i, les in enumerate(mod["lessons"], 1):
        lid = lesson_id(mod["n"], les["slug"])
        lessons_html.append(
            f"""<a class="lesson-index-item" href="{lesson_url(mod['n'], les['slug'])}"
      data-lesson-id="{lid}">
  <span class="lesson-index-num" aria-hidden="true">{i}</span>
  <span class="lesson-index-body">
    <strong>{html.escape(les['title'])}</strong>
    <span>{les['minutes']} min · {les['difficulty']}</span>
  </span>
  <span aria-hidden="true">→</span>
</a>"""
        )
    body = f"""<div class="container reading">
  <section class="module-hero" style="padding-bottom:0">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <ol>
        <li><a href="/curriculum/">Curriculum</a></li>
        <li aria-current="page">Module {mod['n']}</li>
      </ol>
    </nav>
    <p class="eyebrow">Module {mod['n']}</p>
    <h1>{html.escape(mod['title'])}</h1>
    {bil(mod['summary_en'], mod['summary_id'])}
  </section>

  <section style="padding-top:32px">
    <h2>Lessons in this module</h2>
    <div class="lesson-index">
      {''.join(lessons_html)}
    </div>
    <p style="margin-top:32px">
      <a class="btn btn-primary" href="{lesson_url(mod['n'], first['slug'])}">Start this module →</a>
    </p>
  </section>
</div>"""
    title = f"Module {mod['n']} — {mod['title']} — Belajar Power BI"
    desc = mod["summary_en"]
    return page(title, desc, body)


# ---------------------------------------------------------------------------
# homepage
# ---------------------------------------------------------------------------

def render_home():
    path_nodes = "".join(
        f"""<a class="path-node" href="{module_url(m['n'])}">
  <span class="node-num" aria-hidden="true">{m['n']}</span>
  <span class="node-title">{html.escape(m['title'])}</span>
  <span class="node-meta">{len(m['lessons'])} lesson{'s' if len(m['lessons'])!=1 else ''}</span>
</a>"""
        for m in MODULES
    )

    builds = [
        ("A cleaned dataset", "Data yang sudah kamu rapikan sendiri di Power Query"),
        ("A linked data model", "Dua tabel yang terhubung lewat sebuah relationship"),
        ("Working measures", "Total, count, dan average yang kamu tulis dengan DAX"),
        ("An interactive dashboard", "Card, chart, dan slicer yang saling terhubung"),
        ("A published report", "Dashboard yang tayang online dan bisa kamu bagikan"),
        ("Real confidence", "Kemampuan mengulang semuanya dari layar kosong"),
    ]
    builds_html = "".join(
        f'<li><strong>{en}</strong><br><span lang="id" style="color:var(--text-muted)">{idt}</span></li>'
        for en, idt in builds
    )

    body = f"""<section class="hero">
  <div class="container reading">
    <p class="eyebrow">Free · Beginner-first · Bahasa Indonesia &amp; English</p>
    <h1>Go from never opening Power BI to publishing your first dashboard.</h1>
    <p class="lede">A calm, step-by-step course of 8 finite modules — no jargon,
    no rushing, and a screenshot for every single click.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="{lesson_url(0, MODULES[0]['lessons'][0]['slug'])}">Start Module 0 →</a>
      <span class="hero-note">Takes about 4 hours total. Go at your own pace.</span>
    </div>
  </div>
</section>

<section>
  <div class="container reading">
    <p class="section-label">Who this is for</p>
    <h2>Made for people who have zero data background.</h2>
    <div class="audience-grid" style="margin-top:24px">
      <div class="audience-card is-for">
        <h3>This is for you if…</h3>
        <ul>
          <li>You need Power BI for work and have never opened it</li>
          <li>You've failed a YouTube tutorial before and felt lost</li>
          <li>You want plain language, not jargon</li>
          <li>You're more comfortable reading in Bahasa Indonesia</li>
        </ul>
      </div>
      <div class="audience-card not-for">
        <h3>This is <em>not</em> for you if…</h3>
        <ul>
          <li>You already build reports and want advanced DAX</li>
          <li>You want Python, SQL, or data-science theory</li>
          <li>You're looking for a quick cheatsheet, not a course</li>
        </ul>
      </div>
    </div>
    <div class="notice" style="margin-top:24px">
      <strong>You'll read on any device, but you practise on a Windows laptop.</strong>
      Power BI Desktop only runs on Windows. Browse the lessons on your phone; do the
      exercises on a computer. <span lang="id">Baca di HP boleh, tapi latihannya di laptop Windows, ya.</span>
    </div>
  </div>
</section>

<section class="section-dark">
  <div class="container">
    <div class="reading" style="margin-bottom:32px">
      <p class="section-label" style="color:var(--accent)">The whole path</p>
      <h2>Eight modules. That's the entire journey.</h2>
      <p>This course is finite and completable. Here is every module, start to
      finish — nothing hidden, nothing endless.</p>
    </div>
    <div class="path-map">
      {path_nodes}
    </div>
  </div>
</section>

<section>
  <div class="container reading">
    <p class="section-label">What you'll have built</p>
    <h2>By the last lesson, you'll own a real, finished dashboard.</h2>
    <ul class="build-list" style="margin-top:24px">
      {builds_html}
    </ul>
  </div>
</section>

<section>
  <div class="container reading" style="text-align:center">
    <h2>Ready? Start at the very beginning.</h2>
    <p class="lede" style="margin-inline:auto">Module 0 is just reading — no
    software needed yet. Ten minutes from now you'll understand what Power BI
    actually is.</p>
    <a class="btn btn-primary" href="{lesson_url(0, MODULES[0]['lessons'][0]['slug'])}">Start Module 0 →</a>
  </div>
</section>"""
    return page(
        "Belajar Power BI — from zero to your first dashboard",
        "A free, beginner-first Power BI course in Bahasa Indonesia and English. "
        "From never opening Power BI to publishing your first dashboard, in 8 modules.",
        body,
    )


# ---------------------------------------------------------------------------
# curriculum page
# ---------------------------------------------------------------------------

def render_curriculum():
    rows = []
    for mod in MODULES:
        lids = [lesson_id(mod["n"], l["slug"]) for l in mod["lessons"]]
        rows.append(
            f"""<a class="module-row" href="{module_url(mod['n'])}"
      data-module="{mod['n']}" data-lesson-ids="{','.join(lids)}">
  <div class="module-row-head">
    <span class="module-badge" aria-hidden="true">{mod['n']}</span>
    <div>
      <p class="module-title">{html.escape(mod['title'])}</p>
      <span class="module-lesson-count" data-count="{len(mod['lessons'])}">
        {len(mod['lessons'])} lessons · <span class="mod-done-count">0</span>/{len(mod['lessons'])} complete
      </span>
    </div>
  </div>
  <div class="module-progress-bar" aria-hidden="true"><span></span></div>
</a>"""
        )
    body = f"""<div class="container reading">
  <section style="padding-bottom:0">
    <h1>Curriculum</h1>
    <p class="lead">Eight modules, {TOTAL_LESSONS} lessons, one finished dashboard.
    Work top to bottom — each module builds on the one before it.</p>

    <div class="progress-summary">
      <div class="progress-ring js-only" id="progressRing" aria-hidden="true">
        <span class="ring-label" id="ringLabel">0%</span>
      </div>
      <div>
        <strong id="progressHeadline">Ready when you are.</strong>
        <p style="margin:4px 0 0;color:var(--text-muted)" id="progressSub">
          Your progress appears here once you mark a lesson complete. Saved to this
          browser only.</p>
      </div>
    </div>
  </section>

  <section style="padding-top:24px">
    <div class="module-list">
      {''.join(rows)}
    </div>
  </section>
</div>"""
    return page(
        "Curriculum — Belajar Power BI",
        "All 8 modules and every lesson, with your progress across the course.",
        body,
        active="curriculum",
    )


# ---------------------------------------------------------------------------
# downloads page
# ---------------------------------------------------------------------------

def render_downloads():
    seen = {}
    for mod in MODULES:
        for les in mod["lessons"]:
            ds = les.get("dataset")
            if ds and ds["file"] not in seen:
                seen[ds["file"]] = (ds, mod, les)
    rows = "".join(
        f"""<tr>
  <td><strong>{html.escape(ds['name'])}</strong><br>
      <span style="color:var(--text-muted)">{ds['desc_en']}</span></td>
  <td><a href="{module_url(mod['n'])}">Module {mod['n']}</a></td>
  <td><a class="btn btn-download" href="/datasets/{ds['file']}" download>⬇ {ds['file']}</a></td>
</tr>"""
        for ds, mod, les in seen.values()
    )
    body = f"""<div class="container reading">
  <section style="padding-bottom:0">
    <h1>Downloads</h1>
    <p class="lead">Every practice dataset in one place. Small, safe CSV files —
    nothing to install. <span lang="id">Semua dataset latihan di satu tempat.</span></p>
    <div class="notice">
      <strong>How to use these:</strong> download the file for the lesson you're on,
      then load it with <span class="path">Home ▸ Get data ▸ Text/CSV</span> inside
      Power BI Desktop.
    </div>
  </section>
  <section style="padding-top:24px">
    <table class="download-table">
      <thead>
        <tr><th>Dataset</th><th>Used in</th><th>File</th></tr>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table>
  </section>
</div>"""
    return page(
        "Downloads — Belajar Power BI",
        "All practice datasets for the course in one place.",
        body,
        active="downloads",
    )


# ---------------------------------------------------------------------------
# about page
# ---------------------------------------------------------------------------

def render_about():
    body = f"""<div class="container reading">
  <section>
    <h1>About this course</h1>
    <p class="lead">Made for the version of me who once opened Power BI, felt
    completely lost, and closed it again.</p>

    <h2>Why it exists</h2>
    {bil(
      "Most Power BI tutorials assume you already know what a database is, move too "
      "fast, and are written in dense English. This course assumes none of that. "
      "It is written for working professionals in Indonesia who need Power BI for "
      "their job and are starting from absolute zero.",
      "Kebanyakan tutorial Power BI mengira kamu sudah tahu apa itu database, "
      "jalannya kecepatan, dan ditulis dalam bahasa Inggris yang padat. Kursus ini "
      "nggak begitu. Ditulis buat pekerja di Indonesia yang butuh Power BI untuk "
      "kerja dan mulai dari benar-benar nol."
    )}

    <h2>How it's built</h2>
    <ul>
      <li>Every lesson uses the exact same template, so you always know what to expect.</li>
      <li>Every click has a screenshot with numbered callouts.</li>
      <li>Explanations are in casual Bahasa Indonesia and English, side by side.</li>
      <li>Power BI's own menu names are kept in English, so you can find them.</li>
    </ul>

    <h2>Your privacy</h2>
    {bil(
      "This site has no accounts, no login, no database, no analytics, and no "
      "cookies. Your progress is saved in your own browser using localStorage and "
      "never leaves your device. You can clear it any time from the footer.",
      "Situs ini nggak punya akun, login, database, analitik, atau cookie. "
      "Progresmu disimpan di browser-mu sendiri pakai localStorage dan nggak pernah "
      "keluar dari perangkatmu. Kamu bisa menghapusnya kapan saja dari footer."
    )}

    <h2>A note on the screenshots</h2>
    {bil(
      "The screenshots on this site are clean placeholders that show the annotation "
      "system. When you follow along in real Power BI Desktop, your screen will "
      "match the described menus and buttons even if the placeholder art is simplified.",
      "Screenshot di situs ini adalah placeholder bersih yang menunjukkan sistem "
      "anotasi. Saat kamu mengikuti di Power BI Desktop asli, layarmu akan cocok "
      "dengan menu dan tombol yang dijelaskan meski gambar placeholder-nya disederhanakan."
    )}

    <p style="margin-top:32px">
      <a class="btn btn-primary" href="/curriculum/">See the curriculum →</a>
    </p>
  </section>
</div>"""
    return page(
        "About — Belajar Power BI",
        "Who made this free beginner Power BI course, and why.",
        body,
        active="about",
    )


# ---------------------------------------------------------------------------
# app.js  (single shared file, includes the progress manifest)
# ---------------------------------------------------------------------------

def render_app_js():
    # manifest kept in sync with the curriculum
    manifest_modules = []
    for m in MODULES:
        lessons = ",".join(
            '{id:"%s"}' % lesson_id(m["n"], l["slug"]) for l in m["lessons"]
        )
        manifest_modules.append('{n:%d,lessons:[%s]}' % (m["n"], lessons))
    manifest = (
        "var CURRICULUM={total:%d,modules:[%s]};"
        % (TOTAL_LESSONS, ",".join(manifest_modules))
    )

    return (
        """/* Belajar Power BI — single shared script.
   Progress lives in localStorage only. No cookies, no network, no tracking.
   The whole site is readable with JS off; only progress tracking needs JS. */
(function () {
  "use strict";
  document.documentElement.classList.replace("no-js", "js");

  """
        + manifest
        + """

  var KEY = "pbi-progress-v1";
  var SEEN = "pbi-seen-explainer-v1";

  function getDone() {
    try { return JSON.parse(localStorage.getItem(KEY)) || []; }
    catch (e) { return []; }
  }
  function setDone(list) {
    try { localStorage.setItem(KEY, JSON.stringify(list)); } catch (e) {}
  }
  function isDone(id) { return getDone().indexOf(id) !== -1; }
  function toggle(id) {
    var list = getDone(), i = list.indexOf(id);
    if (i === -1) list.push(id); else list.splice(i, 1);
    setDone(list);
    return list.indexOf(id) !== -1;
  }
  function doneCount() {
    var done = getDone(), n = 0;
    CURRICULUM.modules.forEach(function (m) {
      m.lessons.forEach(function (l) { if (done.indexOf(l.id) !== -1) n++; });
    });
    return n;
  }
  function pct() {
    return CURRICULUM.total ? Math.round((doneCount() / CURRICULUM.total) * 100) : 0;
  }

  /* ---- first-visit explainer (inline banner, never a modal) ---- */
  function initFirstVisit() {
    var el = document.getElementById("firstVisit");
    if (!el) return;
    var seen = false;
    try { seen = localStorage.getItem(SEEN) === "1"; } catch (e) {}
    if (!seen) el.hidden = false;
    var btn = document.getElementById("dismissFirstVisit");
    if (btn) btn.addEventListener("click", function () {
      el.hidden = true;
      try { localStorage.setItem(SEEN, "1"); } catch (e) {}
    });
  }

  /* ---- module rail state (lesson pages) ---- */
  function paintRail() {
    var links = document.querySelectorAll(".rail-lessons a[data-lesson-id]");
    links.forEach(function (a) {
      var li = a.parentNode;
      if (isDone(a.getAttribute("data-lesson-id"))) {
        li.classList.add("is-done");
        a.querySelector(".rail-state").textContent = "✓";
      } else {
        li.classList.remove("is-done");
        a.querySelector(".rail-state").textContent = "";
      }
    });
  }

  /* ---- mobile top progress bar ---- */
  function paintMobileProgress() {
    var bar = document.getElementById("mobileProgressBar");
    var label = document.getElementById("mobileProgressLabel");
    if (!bar) return;
    bar.style.width = pct() + "%";
    if (label) label.textContent = pct() + "% complete · " + doneCount() + "/" + CURRICULUM.total;
  }

  /* ---- lesson: mark complete ---- */
  function initMarkComplete() {
    var btn = document.getElementById("markComplete");
    if (!btn) return;
    var id = btn.getAttribute("data-lesson-id");
    var state = document.getElementById("completeState");
    function render() {
      var done = isDone(id);
      btn.classList.toggle("is-done", done);
      btn.textContent = done ? "✓ Completed — click to undo" : "Mark this lesson complete";
      if (state) state.textContent = done ? "Nice. This lesson is saved as done." : "";
      paintRail();
      paintMobileProgress();
    }
    btn.addEventListener("click", function () { toggle(id); render(); });
    render();
  }

  /* ---- curriculum page ---- */
  function initCurriculum() {
    var ring = document.getElementById("progressRing");
    if (!ring) return;
    var p = pct();
    ring.style.setProperty("--pct", p);
    var lbl = document.getElementById("ringLabel");
    if (lbl) lbl.textContent = p + "%";
    var head = document.getElementById("progressHeadline");
    var sub = document.getElementById("progressSub");
    if (head) head.textContent = doneCount() === 0
      ? "Ready when you are." : doneCount() + " of " + CURRICULUM.total + " lessons done.";
    if (sub && doneCount() > 0) sub.textContent = "Keep going — you're " + p + "% of the way there.";

    var done = getDone();
    document.querySelectorAll(".module-row").forEach(function (row) {
      var ids = (row.getAttribute("data-lesson-ids") || "").split(",").filter(Boolean);
      var d = ids.filter(function (id) { return done.indexOf(id) !== -1; }).length;
      var fill = row.querySelector(".module-progress-bar > span");
      if (fill) fill.style.width = ids.length ? (d / ids.length * 100) + "%" : "0";
      var count = row.querySelector(".mod-done-count");
      if (count) count.textContent = d;
      if (d === ids.length && ids.length) row.classList.add("is-complete");
    });
  }

  /* ---- module overview page ---- */
  function initModuleIndex() {
    document.querySelectorAll(".lesson-index-item[data-lesson-id]").forEach(function (a) {
      if (isDone(a.getAttribute("data-lesson-id"))) {
        a.classList.add("is-done");
        a.querySelector(".lesson-index-num").textContent = "✓";
      }
    });
  }

  /* ---- footer progress line ---- */
  function initFooter() {
    var el = document.getElementById("footerProgress");
    if (el && doneCount() > 0) el.textContent = "You've completed " + doneCount()
      + " of " + CURRICULUM.total + " lessons (" + pct() + "%).";
  }

  /* ---- reset progress ---- */
  function initReset() {
    var btn = document.getElementById("resetProgress");
    if (!btn) return;
    btn.addEventListener("click", function () {
      if (!window.confirm("Reset all progress? This clears the lessons you've marked complete on this browser.")) return;
      try { localStorage.removeItem(KEY); } catch (e) {}
      location.reload();
    });
  }

  /* ---- lightbox: tap a screenshot to open full-screen (pinch-zoom) ---- */
  function initLightbox() {
    var box = document.getElementById("lightbox");
    var img = document.getElementById("lightboxImg");
    var close = document.getElementById("lightboxClose");
    if (!box || !img) return;
    var lastFocus = null;
    function open(src, alt) {
      lastFocus = document.activeElement;
      img.src = src; img.alt = alt || "";
      box.classList.add("is-open");
      close.focus();
    }
    function shut() {
      box.classList.remove("is-open");
      img.src = "";
      if (lastFocus && lastFocus.focus) lastFocus.focus();
    }
    document.querySelectorAll(".figure-frame[data-full]").forEach(function (f) {
      f.addEventListener("click", function () {
        var im = f.querySelector("img");
        open(f.getAttribute("data-full"), im ? im.alt : "");
      });
    });
    close.addEventListener("click", shut);
    box.addEventListener("click", function (e) { if (e.target === box) shut(); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && box.classList.contains("is-open")) shut();
    });
  }

  initFirstVisit();
  paintRail();
  paintMobileProgress();
  initMarkComplete();
  initCurriculum();
  initModuleIndex();
  initFooter();
  initReset();
  initLightbox();
})();
"""
    )


# ---------------------------------------------------------------------------
# placeholder screenshots (light Power BI-style SVG mockups)
# ---------------------------------------------------------------------------

def svg_mock(title, markers):
    """A clean, light mock of the Power BI Desktop window.
    Real screenshots from the user drop straight into the same <img>/data slots."""
    # colours
    ink = "#1F1F1F"; muted = "#646569"; border = "#E5E9ED"; surface = "#F7F9FB"
    accent = "#02A0C1"
    W, H = 1000, 600
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'role="img" aria-hidden="true" font-family="Plus Jakarta Sans, sans-serif">',
        f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>',
        # title bar
        f'<rect width="{W}" height="34" fill="{surface}"/>',
        f'<circle cx="18" cy="17" r="5" fill="{accent}"/>',
        f'<text x="34" y="22" font-size="13" fill="{muted}">Power BI Desktop — {html.escape(title)}</text>',
        # ribbon
        f'<rect y="34" width="{W}" height="70" fill="#FFFFFF" stroke="{border}"/>',
    ]
    for i, tab in enumerate(["Home", "Insert", "Modeling", "View", "Help"]):
        parts.append(
            f'<text x="{24 + i*70}" y="54" font-size="12" fill="{muted}">{tab}</text>'
        )
    for i in range(6):
        x = 24 + i * 90
        parts.append(f'<rect x="{x}" y="64" width="72" height="30" rx="6" fill="{surface}"/>')
        parts.append(f'<text x="{x+36}" y="83" font-size="10" fill="{muted}" text-anchor="middle">command</text>')
    # left view rail
    parts.append(f'<rect y="104" width="46" height="{H-104}" fill="{surface}" stroke="{border}"/>')
    for i in range(3):
        y = 130 + i * 44
        parts.append(f'<rect x="12" y="{y}" width="22" height="22" rx="5" fill="#FFFFFF" stroke="{border}"/>')
    # canvas
    parts.append(f'<rect x="46" y="104" width="640" height="{H-104}" fill="#FFFFFF"/>')
    parts.append(f'<rect x="80" y="150" width="560" height="380" rx="10" fill="{surface}" stroke="{border}"/>')
    parts.append(f'<text x="360" y="345" font-size="16" fill="{muted}" text-anchor="middle">{html.escape(title)}</text>')
    # right panes
    parts.append(f'<rect x="686" y="104" width="150" height="{H-104}" fill="#FFFFFF" stroke="{border}"/>')
    parts.append(f'<text x="700" y="128" font-size="11" fill="{ink}" font-weight="600">Visualizations</text>')
    for r in range(2):
        for c in range(4):
            parts.append(f'<rect x="{700 + c*33}" y="{140 + r*33}" width="26" height="26" rx="5" fill="{surface}" stroke="{border}"/>')
    parts.append(f'<rect x="836" y="104" width="164" height="{H-104}" fill="#FFFFFF" stroke="{border}"/>')
    parts.append(f'<text x="850" y="128" font-size="11" fill="{ink}" font-weight="600">Fields</text>')
    for i in range(5):
        parts.append(f'<text x="856" y="{150 + i*24}" font-size="11" fill="{muted}">▸ field {i+1}</text>')
    parts.append("</svg>")
    return "\n".join(parts)


def collect_images():
    imgs = {}
    for mod in MODULES:
        for les in mod["lessons"]:
            for st in les["steps"]:
                if st.get("image"):
                    imgs[st["image"]["src"]] = st["image"]["alt"]
            if les.get("checkpoint_image"):
                ci = les["checkpoint_image"]
                imgs[ci["src"]] = ci["alt"]
    return imgs


def render_favicon():
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
        '<rect width="32" height="32" rx="7" fill="#02A0C1"/>'
        '<rect x="8" y="16" width="4" height="9" rx="1" fill="#fff"/>'
        '<rect x="14" y="11" width="4" height="14" rx="1" fill="#fff"/>'
        '<rect x="20" y="7" width="4" height="18" rx="1" fill="#fff"/>'
        "</svg>"
    )


# ---------------------------------------------------------------------------
# datasets
# ---------------------------------------------------------------------------

def build_datasets():
    rnd = random.Random(42)
    products = [
        ("P01", "Espresso", 18000),
        ("P02", "Latte", 28000),
        ("P03", "Cappuccino", 27000),
        ("P04", "Americano", 22000),
        ("P05", "Croissant", 20000),
        ("P06", "Cold Brew", 30000),
    ]

    # coffee-sales.csv (clean)
    lines = ["Date,Product,Quantity,Price"]
    for i in range(90):
        p = rnd.choice(products)
        day = rnd.randint(1, 28)
        qty = rnd.randint(1, 5)
        lines.append(f"2026-03-{day:02d},{p[1]},{qty},{p[2]}")
    write("datasets/coffee-sales.csv", "\n".join(lines) + "\n")

    # messy-orders.csv (deliberately messy)
    ml = ["Order ID,Order Date,Product,City,Price,Notes"]
    cities = ["Jakarta", "Bandung", "Surabaya", "Jakata", "Medan"]
    for i in range(60):
        p = rnd.choice(products)
        city = rnd.choice(cities)
        date = f"2026-04-{rnd.randint(1,28):02d}"
        price = str(p[2])
        oid = f"O{1000+i}"
        ml.append(f"{oid},{date},Coffee - {p[1]},{city},{price},")
        if i % 12 == 0:
            ml.append(",,,,,")  # blank row
    write("datasets/messy-orders.csv", "\n".join(ml) + "\n")

    # sales.csv + products.csv → zip
    def sales_csv(prefix="", n=120):
        s = ["Order ID,Product ID,Amount,Order Date"]
        for i in range(n):
            p = rnd.choice(products)
            qty = rnd.randint(1, 5)
            amount = qty * p[2]
            date = f"2026-05-{rnd.randint(1,28):02d}"
            s.append(f"{prefix}{2000+i},{p[0]},{amount},{date}")
        return "\n".join(s) + "\n"

    def products_csv():
        s = ["Product ID,Product Name,Price"]
        for pid, name, price in products:
            s.append(f"{pid},{name},{price}")
        return "\n".join(s) + "\n"

    def make_zip(path, files):
        full = os.path.join(ROOT, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with zipfile.ZipFile(full, "w", zipfile.ZIP_DEFLATED) as z:
            for name, data in files.items():
                z.writestr(name, data)

    make_zip("datasets/sales-and-products.zip", {
        "sales.csv": sales_csv("S"),
        "products.csv": products_csv(),
    })
    make_zip("datasets/capstone-superstore.zip", {
        "capstone-sales.csv": sales_csv("C", 200),
        "capstone-products.csv": products_csv(),
    })


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    # top-level pages
    write("index.html", render_home())
    write("curriculum/index.html", render_curriculum())
    write("downloads/index.html", render_downloads())
    write("about/index.html", render_about())

    # module + lesson pages, with prev/next wiring
    flat = []
    for mod in MODULES:
        for les in mod["lessons"]:
            flat.append((mod, les))

    for mod in MODULES:
        write(f"module/{mod['n']}/index.html", render_module(mod))

    for idx, (mod, les) in enumerate(flat):
        prev_link = None
        if idx > 0:
            pm, pl = flat[idx - 1]
            prev_link = {"url": lesson_url(pm["n"], pl["slug"]), "label": pl["title"]}
        if idx < len(flat) - 1:
            nm, nl = flat[idx + 1]
            next_link = {"url": lesson_url(nm["n"], nl["slug"]), "label": "Next: " + nl["title"]}
        else:
            next_link = {"url": "/curriculum/", "label": "Back to curriculum — you finished!"}
        write(
            f"module/{mod['n']}/{les['slug']}/index.html",
            render_lesson(mod, les, prev_link, next_link),
        )

    # shared JS
    write("assets/app.js", render_app_js())

    # images
    write("assets/img/favicon.svg", render_favicon())
    for src, alt in collect_images().items():
        rel = src.lstrip("/")
        # title = last path segment prettified
        name = os.path.splitext(os.path.basename(src))[0].replace("-", " ")
        write(rel, svg_mock(name, []))

    # datasets
    build_datasets()

    print(f"Generated site: {TOTAL_LESSONS} lessons across {len(MODULES)} modules.")


if __name__ == "__main__":
    main()
