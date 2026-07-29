/* Belajar Power BI — single shared script.
   Progress lives in localStorage only. No cookies, no network, no tracking.
   The whole site is readable with JS off; only progress tracking needs JS. */
(function () {
  "use strict";
  document.documentElement.classList.replace("no-js", "js");

  var CURRICULUM={total:23,modules:[{n:0,lessons:[{id:"m0-what-is-power-bi"},{id:"m0-install-power-bi-desktop"},{id:"m0-tour-of-the-window"}]},{n:1,lessons:[{id:"m1-understanding-data-sources"},{id:"m1-import-your-first-file"},{id:"m1-reading-the-load-screen"}]},{n:2,lessons:[{id:"m2-what-is-power-query"},{id:"m2-remove-columns-and-rows"},{id:"m2-fix-data-types"},{id:"m2-close-and-apply"}]},{n:3,lessons:[{id:"m3-what-is-a-data-model"},{id:"m3-create-a-relationship"},{id:"m3-reading-the-model-view"}]},{n:4,lessons:[{id:"m4-your-first-chart"},{id:"m4-cards-tables-slicers"},{id:"m4-formatting-and-layout"}]},{n:5,lessons:[{id:"m5-columns-vs-measures"},{id:"m5-your-first-measure"},{id:"m5-useful-measures"}]},{n:6,lessons:[{id:"m6-sign-in-and-publish"},{id:"m6-share-your-dashboard"}]},{n:7,lessons:[{id:"m7-build-the-dashboard"},{id:"m7-checklist-and-next-steps"}]}]};

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
