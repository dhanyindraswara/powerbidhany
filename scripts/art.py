# -*- coding: utf-8 -*-
"""
Screenshot artwork for Belajar Power BI.

Draws recognisable, light-mode mockups of the real Power BI Desktop UI as SVG:
the ribbon with its actual command names, the view rail, the Visualizations and
Fields panes, the Power Query Editor with Applied Steps, Model view, dialogs,
and the browser-based Power BI Service.

Each scene is keyed by the image file name used in content.py. ANCHORS holds the
marker geometry for a scene (percentages of the image box), because where a
callout must land is a property of the artwork, not of the lesson text. The
legend wording stays in content.py. If you later swap in a real screenshot,
delete its ANCHORS entry and the x/y from content.py is used instead.
"""

import html as _html

# --- palette: Fluent / Power BI Desktop ------------------------------------
CH = "#F3F2F1"      # chrome, ribbon
BD = "#E1DFDD"      # light border
BD2 = "#D2D0CE"     # stronger border
TX = "#323130"      # text
MU = "#605E5C"      # muted text
WH = "#FFFFFF"
YEL = "#F2C811"     # Power BI yellow
BLU = "#0078D4"     # Fluent selection blue
BLL = "#DEECF9"     # selection fill
GRN = "#107C41"     # Power Query green
GRL = "#E6F4EA"
GRID = "#EDEBE9"
BAR = "#118DFF"     # default Power BI chart blue
SEL = "#C7E0F4"

W, H = 1000, 620    # standard window canvas


# ---------------------------------------------------------------------------
# primitives
# ---------------------------------------------------------------------------

def e(s):
    return _html.escape(str(s))


def rect(x, y, w, h, fill, stroke=None, rx=0, sw=1):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{s}/>'


def txt(x, y, s, size=11, fill=TX, weight=400, anchor="start", style=""):
    st = f' font-style="{style}"' if style else ""
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'font-weight="{weight}" text-anchor="{anchor}"{st}>{e(s)}</text>')


def line(x1, y1, x2, y2, stroke=BD, sw=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="{sw}"{d}/>')


def svg(body, w=W, h=H):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'role="img" aria-hidden="true" '
            f'font-family="Segoe UI, Plus Jakarta Sans, sans-serif">'
            f'{rect(0,0,w,h,WH)}{body}</svg>')


def pbi_logo(x, y, s=14):
    """The Power BI yellow bar mark."""
    u = s / 14.0
    return (rect(x, y, s, s, YEL, rx=2)
            + rect(x + 3 * u, y + 8 * u, 2 * u, 4 * u, "#7A5C00")
            + rect(x + 6 * u, y + 5 * u, 2 * u, 7 * u, "#7A5C00")
            + rect(x + 9 * u, y + 2.5 * u, 2 * u, 9.5 * u, "#7A5C00"))


# ---------------------------------------------------------------------------
# Power BI Desktop shell
# ---------------------------------------------------------------------------

RIBBON_HOME = ["Paste", "Get data", "Excel", "OneLake", "SQL Server",
               "Enter data", "Transform data", "Refresh", "New visual",
               "Text box", "New measure", "Publish"]

TABS = ["File", "Home", "Insert", "Modeling", "View", "Optimize", "Help"]


def titlebar(title="Untitled - Power BI Desktop", signin=False, w=W):
    p = [rect(0, 0, w, 30, CH), line(0, 30, w, 30, BD2)]
    p.append(pbi_logo(10, 8))
    p.append(txt(32, 20, title, 11, MU))
    if signin:
        p.append(txt(w - 120, 20, "Sign in", 11, BLU, 600))
    p.append(txt(w - 58, 20, "—   ▢   ✕", 11, MU))
    return "".join(p)


def ribbon(active=1, hi=None, w=W, y0=30):
    """Ribbon: tab strip + Home command buttons. `hi` highlights a command."""
    p = [rect(0, y0, w, 66, CH), line(0, y0 + 66, w, y0 + 66, BD2)]
    x = 12
    for i, t in enumerate(TABS):
        tw = len(t) * 6.5 + 18
        if i == active:
            p.append(rect(x, y0 + 2, tw, 20, WH, rx=3))
            p.append(line(x + 6, y0 + 22, x + tw - 6, y0 + 22, BLU, 2))
        p.append(txt(x + tw / 2, y0 + 16, t, 10.5, TX if i == active else MU,
                     600 if i == active else 400, "middle"))
        x += tw + 4
    # command buttons
    x = 12
    for name in RIBBON_HOME:
        bw = max(46, len(name) * 5.4 + 16)
        on = (hi == name)
        p.append(rect(x, y0 + 28, bw, 34, BLL if on else WH,
                      BLU if on else BD, rx=3, sw=2 if on else 1))
        p.append(rect(x + bw / 2 - 6, y0 + 32, 12, 11, BLU if on else "#8A8886", rx=2))
        p.append(txt(x + bw / 2, y0 + 57, name, 8.5, TX if on else MU,
                     700 if on else 400, "middle"))
        x += bw + 5
    return "".join(p)


def view_rail(active=0, y0=96, h=None, w=44):
    """The three view icons down the left edge: Report, Table, Model."""
    h = h or (H - y0 - 26)
    p = [rect(0, y0, w, h, CH), line(w, y0, w, y0 + h, BD)]
    for i in range(3):
        y = y0 + 14 + i * 40
        on = (i == active)
        p.append(rect(8, y, 28, 28, WH if on else "none", BLU if on else None,
                      rx=4, sw=2))
        if i == 0:      # report: bar chart
            p.append(rect(14, y + 16, 3, 7, BLU if on else MU))
            p.append(rect(19, y + 11, 3, 12, BLU if on else MU))
            p.append(rect(24, y + 7, 3, 16, BLU if on else MU))
        elif i == 1:    # table: grid
            for r in range(3):
                p.append(rect(14, y + 8 + r * 5, 16, 3, BLU if on else MU))
        else:           # model: linked boxes
            p.append(rect(13, y + 8, 8, 7, "none", BLU if on else MU))
            p.append(rect(23, y + 16, 8, 7, "none", BLU if on else MU))
            p.append(line(21, y + 12, 23, y + 19, BLU if on else MU, 1.5))
    return "".join(p)


VIS_ICONS = 22


def vis_pane(x=700, w=150, y0=96, selected=None, fmt=False, h=None):
    """Visualizations pane: chart-type icon grid, or the Format tab."""
    h = h or (H - y0 - 26)
    p = [rect(x, y0, w, h, WH), line(x, y0, x, y0 + h, BD)]
    p.append(txt(x + 10, y0 + 18, "Visualizations", 10.5, TX, 700))
    # the three tab icons: Build / Format / Analytics
    for i, lbl in enumerate(["▤", "🖌", "🔍"]):
        bx = x + 10 + i * 26
        on = (fmt and i == 1) or (not fmt and i == 0)
        p.append(rect(bx, y0 + 26, 22, 20, BLL if on else WH, BLU if on else BD, rx=3))
        p.append(txt(bx + 11, y0 + 40, lbl, 10, TX, 400, "middle"))
    if fmt:
        p.append(line(x + 8, y0 + 54, x + w - 8, y0 + 54, BD))
        rows = ["Visual", "General", "  Title", "  Effects", "  Header icons"]
        for i, r in enumerate(rows):
            yy = y0 + 72 + i * 26
            on = (r == "  Title")
            if on:
                p.append(rect(x + 6, yy - 12, w - 12, 22, BLL, rx=3))
            p.append(txt(x + 12, yy + 3, r, 10, TX if on else MU, 700 if on else 400))
            p.append(rect(x + w - 30, yy - 7, 18, 10, BLU if on else "#C8C6C4", rx=5))
            p.append(f'<circle cx="{x + w - (16 if on else 25)}" cy="{yy - 2}" r="4" fill="{WH}"/>')
    else:
        # chart type icon grid (4 across)
        for i in range(16):
            r, c = divmod(i, 4)
            bx, by = x + 10 + c * 34, y0 + 56 + r * 30
            on = (selected == i)
            p.append(rect(bx, by, 28, 24, BLL if on else CH, BLU if on else BD,
                          rx=3, sw=2 if on else 1))
            col = BLU if on else "#8A8886"
            if i == 0:      # clustered bar (horizontal)
                for k in range(3):
                    p.append(rect(bx + 5, by + 5 + k * 6, 8 + k * 5, 4, col))
            elif i == 1:    # clustered column
                for k in range(3):
                    p.append(rect(bx + 6 + k * 6, by + 18 - k * 5, 4, 3 + k * 5, col))
            elif i == 6:    # card
                p.append(txt(bx + 14, by + 17, "123", 9, col, 700, "middle"))
            elif i == 9:    # slicer
                for k in range(3):
                    p.append(rect(bx + 6, by + 5 + k * 6, 4, 4, "none", col))
                    p.append(rect(bx + 13, by + 6 + k * 6, 9, 2, col))
            else:
                p.append(rect(bx + 7, by + 7, 14, 10, col, rx=1))
        # field wells
        p.append(line(x + 8, y0 + 190, x + w - 8, y0 + 190, BD))
        for i, wname in enumerate(["Y-axis", "X-axis", "Legend"]):
            yy = y0 + 208 + i * 40
            p.append(txt(x + 12, yy, wname, 9.5, MU, 600))
            p.append(rect(x + 10, yy + 6, w - 20, 20, CH, BD, rx=3))
    return "".join(p)


def fields_pane(x=850, w=150, y0=96, tables=None, hi=None, h=None, measures=None):
    """Fields pane listing tables and their columns."""
    h = h or (H - y0 - 26)
    tables = tables or []
    measures = measures or []
    p = [rect(x, y0, w, h, WH), line(x, y0, x, y0 + h, BD)]
    p.append(txt(x + 10, y0 + 18, "Fields", 10.5, TX, 700))
    p.append(rect(x + 8, y0 + 26, w - 16, 20, CH, BD, rx=3))
    p.append(txt(x + 14, y0 + 40, "Search", 9, "#A19F9D"))
    y = y0 + 62
    for tname, cols in tables:
        p.append(txt(x + 12, y, "▾", 9, MU))
        p.append(txt(x + 24, y, tname, 10, TX, 700))
        y += 20
        for c in cols:
            on = (hi == c)
            if on:
                p.append(rect(x + 16, y - 11, w - 26, 18, BLL, rx=3))
            p.append(rect(x + 24, y - 8, 9, 9, WH, BLU if on else "#A19F9D", rx=2))
            if on:
                p.append(txt(x + 26.5, y - 0.5, "✓", 8, BLU, 700))
            p.append(txt(x + 39, y, c, 9.5, TX if on else MU, 600 if on else 400))
            y += 19
        y += 6
    for ms in measures:
        p.append(f'<text x="{x + 24}" y="{y}" font-size="9" fill="{BLU}">▮</text>')
        p.append(txt(x + 38, y, ms, 9.5, TX, 600))
        y += 19
    return "".join(p)


def page_tabs(w=W, h=H, label="Page 1"):
    y = h - 26
    return "".join([
        rect(0, y, w, 26, CH), line(0, y, w, y, BD2),
        rect(10, y + 4, 62, 18, WH, BD, rx=3),
        txt(41, y + 16, label, 9.5, TX, 600, "middle"),
        txt(84, y + 16, "+", 12, MU),
    ])


def shell(canvas="", *, title="Untitled - Power BI Desktop", tab=1, hi=None,
          view=0, right=True, vis_sel=None, fmt=False, tables=None,
          fields_hi=None, measures=None, signin=False, page="Page 1"):
    """Compose a full Power BI Desktop window."""
    cw = 700 if right else W
    p = [titlebar(title, signin), ribbon(tab, hi), view_rail(view)]
    p.append(rect(44, 96, cw - 44, H - 96 - 26, "#F8F8F8"))
    p.append(canvas)
    if right:
        p.append(vis_pane(700, 150, selected=vis_sel, fmt=fmt))
        p.append(fields_pane(850, 150, tables=tables, hi=fields_hi,
                             measures=measures))
    p.append(page_tabs(label=page))
    return svg("".join(p))


# ---------------------------------------------------------------------------
# canvas contents (visuals)
# ---------------------------------------------------------------------------

PRODUCTS = [("Latte", 1.0), ("Cold Brew", .82), ("Cappuccino", .70),
            ("Americano", .55), ("Espresso", .41), ("Croissant", .28)]


def visual_box(x, y, w, h, title=None, selected=False):
    p = [rect(x, y, w, h, WH, BLU if selected else BD, rx=2, sw=2 if selected else 1)]
    if title:
        p.append(txt(x + 12, y + 20, title, 11, TX, 700))
    return "".join(p)


def bar_chart(x, y, w, h, title="Amount by Product Name", selected=False,
              only=None):
    p = [visual_box(x, y, w, h, title, selected)]
    ax = x + 92
    aw = w - 110
    data = PRODUCTS if only is None else [d for d in PRODUCTS if d[0] == only]
    for i, (name, v) in enumerate(data):
        by = y + 38 + i * ((h - 56) / max(len(PRODUCTS), 1))
        p.append(txt(ax - 8, by + 11, name, 9, MU, 400, "end"))
        p.append(rect(ax, by, max(6, aw * v), 13, BAR, rx=1))
    p.append(line(ax, y + 32, ax, y + h - 14, BD))
    return "".join(p)


def card_visual(x, y, w, h, value="Rp 48.7M", label="Total Sales",
                selected=False):
    return "".join([
        visual_box(x, y, w, h, None, selected),
        txt(x + w / 2, y + h / 2 + 4, value, 24, TX, 700, "middle"),
        txt(x + w / 2, y + h / 2 + 24, label, 10, MU, 400, "middle"),
    ])


def slicer_visual(x, y, w, h, checked=None, selected=False):
    p = [visual_box(x, y, w, h, "Product Name", selected)]
    for i, (name, _) in enumerate(PRODUCTS):
        yy = y + 34 + i * 24
        on = (checked == name)
        p.append(rect(x + 12, yy, 12, 12, WH, BLU if on else "#A19F9D", rx=2))
        if on:
            p.append(txt(x + 15, yy + 9.5, "✓", 9, BLU, 700))
        p.append(txt(x + 32, yy + 10, name, 9.5, TX if on else MU,
                     600 if on else 400))
    return "".join(p)


def heading_text(x, y, s="Coffee sales dashboard", size=17):
    return txt(x, y, s, size, TX, 700)


# ---------------------------------------------------------------------------
# data grid (Power Query + preview dialogs)
# ---------------------------------------------------------------------------

TYPE_ICON = {"abc": "ABC", "123": "123", "date": "📅", "dec": "1.2"}


def data_grid(x, y, w, h, cols, rows, types=None, sel_col=None, blanks=(),
              hi_cell=None):
    """cols: list of names. rows: list of lists. types: list of type keys."""
    n = len(cols)
    cw = w / n
    p = [rect(x, y, w, h, WH, BD)]
    # header
    p.append(rect(x, y, w, 26, CH))
    for i, c in enumerate(cols):
        cx = x + i * cw
        if sel_col == i:
            p.append(rect(cx, y, cw, h, SEL, rx=0))
            p.append(rect(cx, y, cw, 26, "#9BC7E4"))
        if types:
            p.append(txt(cx + 8, y + 17, TYPE_ICON.get(types[i], "ABC"), 8, MU, 700))
            p.append(txt(cx + 30, y + 17, c, 9.5, TX, 600))
        else:
            p.append(txt(cx + 8, y + 17, c, 9.5, TX, 600))
        p.append(line(cx, y, cx, y + h, BD))
    # Real grids use a fixed row height and leave blank space below the data,
    # rather than stretching a handful of rows over the whole pane.
    rh = 30
    total = int((h - 26) // rh)
    for r in range(total):
        ry = y + 26 + r * rh
        p.append(line(x, ry, x + w, ry, GRID))
        if r >= len(rows) or r in blanks:
            continue
        for i, v in enumerate(rows[r]):
            cx = x + i * cw
            al = "end" if (types and types[i] in ("123", "dec")) else "start"
            tx_ = cx + cw - 10 if al == "end" else cx + 8
            p.append(txt(tx_, ry + rh / 2 + 4, v, 9.5, TX, 400, al))
    return "".join(p)


PQ_COLS = ["Order ID", "Order Date", "Product", "City", "Price", "Notes"]
PQ_ROWS = [
    ["O1000", "2026-04-03", "Coffee - Latte", "Jakarta", "28000", ""],
    ["O1001", "2026-04-05", "Coffee - Espresso", "Bandung", "18000", ""],
    ["", "", "", "", "", ""],
    ["O1003", "2026-04-09", "Coffee - Cold Brew", "Jakata", "30000", ""],
    ["O1004", "2026-04-11", "Coffee - Latte", "Surabaya", "28000", ""],
    ["O1005", "2026-04-12", "Coffee - Americano", "Medan", "22000", ""],
]


def pq_shell(*, steps=None, cols=None, rows=None, types=None, sel_col=None,
             hi_ribbon=None, menu=None, dialog=None, blanks=(), title="messy-orders"):
    """The Power Query Editor window."""
    cols = cols or PQ_COLS
    rows = rows or PQ_ROWS
    steps = steps or ["Source", "Promoted Headers", "Changed Type"]
    p = [rect(0, 0, W, 30, CH), line(0, 30, W, 30, BD2)]
    p.append(rect(10, 8, 14, 14, GRN, rx=2))
    p.append(txt(32, 20, f"{title} - Power Query Editor", 11, MU))
    p.append(txt(W - 58, 20, "—   ▢   ✕", 11, MU))
    # ribbon
    p.append(rect(0, 30, W, 66, CH))
    p.append(line(0, 96, W, 96, BD2))
    x = 12
    for i, t in enumerate(["File", "Home", "Transform", "Add Column", "View", "Tools"]):
        tw = len(t) * 6.5 + 18
        if i == 1:
            p.append(rect(x, 32, tw, 20, WH, rx=3))
            p.append(line(x + 6, 52, x + tw - 6, 52, GRN, 2))
        p.append(txt(x + tw / 2, 46, t, 10.5, TX if i == 1 else MU,
                     600 if i == 1 else 400, "middle"))
        x += tw + 4
    x = 12
    for name in ["Close & Apply", "New Source", "Refresh Preview", "Choose Columns",
                 "Remove Columns", "Keep Rows", "Remove Rows", "Split Column",
                 "Group By", "Replace Values"]:
        bw = max(52, len(name) * 5.2 + 16)
        on = (hi_ribbon == name)
        p.append(rect(x, 58, bw, 34, GRL if on else WH, GRN if on else BD,
                      rx=3, sw=2 if on else 1))
        p.append(rect(x + bw / 2 - 6, 62, 12, 11, GRN if on else "#8A8886", rx=2))
        p.append(txt(x + bw / 2, 87, name, 8.2, TX if on else MU,
                     700 if on else 400, "middle"))
        x += bw + 5
    # queries pane
    p.append(rect(0, 96, 150, H - 96, WH))
    p.append(line(150, 96, 150, H, BD))
    p.append(txt(12, 116, "Queries [1]", 10, TX, 700))
    p.append(rect(8, 126, 134, 22, BLL, rx=3))
    p.append(txt(18, 141, "▦ " + title, 9.5, TX, 600))
    # grid
    p.append(data_grid(150, 96, 610, H - 96, cols, rows, types, sel_col, blanks))
    # query settings
    p.append(rect(760, 96, 240, H - 96, WH))
    p.append(line(760, 96, 760, H, BD))
    p.append(txt(772, 116, "Query Settings", 10.5, TX, 700))
    p.append(txt(772, 140, "▾ PROPERTIES", 9, MU, 600))
    p.append(rect(770, 148, 220, 22, WH, BD, rx=3))
    p.append(txt(778, 163, title, 9, TX))
    p.append(txt(772, 192, "▾ APPLIED STEPS", 9, MU, 600))
    for i, s in enumerate(steps):
        yy = 204 + i * 26
        last = (i == len(steps) - 1)
        if last:
            p.append(rect(768, yy, 224, 22, BLL, rx=3))
        p.append(txt(778, yy + 15, "⚙", 9, MU))
        p.append(txt(794, yy + 15, s, 9.5, TX, 700 if last else 400))
        p.append(txt(982, yy + 15, "✕", 8, MU, 400, "end"))
    if menu:
        p.append(menu)
    if dialog:
        p.append(dialog)
    return svg("".join(p))


def context_menu(x, y, items, hi=None, w=170):
    h = len(items) * 24 + 10
    p = [rect(x + 2, y + 2, w, h, "#00000012", rx=4),
         rect(x, y, w, h, WH, BD2, rx=4)]
    for i, it in enumerate(items):
        yy = y + 6 + i * 24
        on = (it == hi)
        if on:
            p.append(rect(x + 3, yy, w - 6, 22, BLL, rx=3))
        p.append(txt(x + 14, yy + 15, it, 10, TX, 700 if on else 400))
    return "".join(p)


def dialog_box(x, y, w, h, title, body="", buttons=("OK", "Cancel"), hi_btn=None):
    p = [rect(x + 3, y + 3, w, h, "#00000018", rx=6),
         rect(x, y, w, h, WH, BD2, rx=6),
         rect(x, y, w, 40, CH, rx=6),
         rect(x, y + 30, w, 10, CH),
         txt(x + 16, y + 25, title, 12, TX, 700),
         txt(x + w - 16, y + 25, "✕", 11, MU, 400, "end"),
         body]
    bx = x + w - 16
    for b in reversed(buttons):
        bw = 76
        bx -= bw
        on = (hi_btn == b)
        p.append(rect(bx, y + h - 46, bw, 30, BLU if on else WH,
                      BLU if on else BD2, rx=3, sw=2 if on else 1))
        p.append(txt(bx + bw / 2, y + h - 26, b, 10.5, WH if on else TX,
                     700 if on else 400, "middle"))
        bx -= 10
    return "".join(p)


# ---------------------------------------------------------------------------
# scenes
# ---------------------------------------------------------------------------

COFFEE = [("coffee-sales", ["Date", "Product", "Quantity", "Price"])]
SALESP = [("Sales", ["Order ID", "Product ID", "Amount", "Order Date"]),
          ("Products", ["Product ID", "Product Name", "Price"])]


def sc_window_tour():
    return shell(bar_chart(80, 130, 580, 380, None) if False else "",
                 tables=COFFEE)


def sc_empty_desktop():
    p = txt(372, 300, "Add data to your report", 13, "#A19F9D", 400, "middle")
    return shell(p, right=True, tables=[])


def sc_getdata():
    return shell("", hi="Get data", tables=[])


def sc_getdata_menu():
    menu = context_menu(120, 150, ["Excel workbook", "Text/CSV", "Web",
                                   "SQL Server database", "More…"], hi="Text/CSV")
    return shell(menu, hi="Get data", tables=[])


def sc_fields_loaded():
    return shell(txt(372, 300, "Add data to your report", 13, "#A19F9D", 400, "middle"),
                 tables=COFFEE)


def sc_store(get=False):
    p = [rect(0, 0, W, 56, CH), line(0, 56, W, 56, BD2)]
    p.append(txt(24, 34, "Microsoft Store", 15, TX, 700))
    p.append(rect(300, 14, 420, 30, WH, BD2, rx=15))
    p.append(txt(320, 34, "🔍  Power BI Desktop", 11, TX))
    if not get:
        for i in range(3):
            y = 90 + i * 96
            on = (i == 0)
            p.append(rect(40, y, W - 80, 82, WH, BLU if on else BD, rx=6, sw=2 if on else 1))
            p.append(rect(56, y + 14, 54, 54, "#F5F5F5", BD, rx=8))
            p.append(pbi_logo(70, 28 + i * 96, 26))
            p.append(txt(128, y + 34, "Power BI Desktop" if on else "Power BI Report Builder",
                         13, TX, 700))
            p.append(txt(128, y + 54, "Microsoft Corporation  ·  Free", 10, MU))
            p.append(rect(W - 160, y + 26, 90, 30, BLU, rx=4))
            p.append(txt(W - 115, y + 46, "Get", 11, WH, 700, "middle"))
    else:
        p.append(rect(60, 100, 120, 120, "#F5F5F5", BD, rx=12))
        p.append(pbi_logo(96, 136, 48))
        p.append(txt(210, 140, "Power BI Desktop", 22, TX, 700))
        p.append(txt(210, 168, "Microsoft Corporation", 12, MU))
        p.append(txt(210, 190, "Free  ·  In-app purchases", 11, MU))
        p.append(rect(210, 210, 130, 40, BLU, rx=4))
        p.append(txt(275, 236, "Get", 14, WH, 700, "middle"))
        p.append(line(60, 300, W - 60, 300, BD))
        p.append(txt(60, 330, "Turn your data into real insights.", 12, MU))
    return svg("".join(p), W, 420 if get else H)


def sc_file_browser():
    p = [rect(0, 0, W, H, "#F8F8F8")]
    p.append(dialog_box(60, 40, 880, 520, "Open", "", ("Open", "Cancel"), "Open"))
    p.append(rect(76, 96, 200, 400, "#FAFAFA", BD, rx=4))
    for i, f in enumerate(["Quick access", "Desktop", "Downloads", "Documents",
                           "Pictures", "This PC"]):
        on = (f == "Downloads")
        if on:
            p.append(rect(80, 110 + i * 30, 192, 26, BLL, rx=3))
        p.append(txt(94, 128 + i * 30, "📁  " + f, 10, TX, 700 if on else 400))
    p.append(rect(292, 96, 632, 400, WH, BD, rx=4))
    p.append(rect(292, 96, 632, 28, CH))
    p.append(txt(306, 115, "Name", 9.5, MU, 600))
    p.append(txt(700, 115, "Date modified", 9.5, MU, 600))
    p.append(txt(860, 115, "Size", 9.5, MU, 600))
    files = ["capstone-superstore.zip", "coffee-sales.csv", "messy-orders.csv",
             "notes.txt", "report-draft.pbix"]
    for i, f in enumerate(files):
        yy = 130 + i * 30
        on = (f == "coffee-sales.csv")
        if on:
            p.append(rect(294, yy, 628, 26, BLL, rx=2))
        p.append(txt(310, yy + 17, "📄  " + f, 10, TX, 700 if on else 400))
        p.append(txt(700, yy + 17, "29/07/2026", 9.5, MU))
        p.append(txt(860, yy + 17, "4 KB", 9.5, MU))
    p.append(txt(76, 520, "File name:", 10, MU))
    p.append(rect(150, 506, 480, 26, WH, BD2, rx=3))
    p.append(txt(160, 524, "coffee-sales.csv", 10, TX))
    return svg("".join(p))


def sc_csv_preview(delim_hi=False, buttons_only=False):
    if buttons_only:
        p = [rect(0, 0, 700, 200, "#F8F8F8")]
        p.append(rect(40, 40, 620, 120, WH, BD2, rx=8))
        p.append(rect(90, 78, 200, 44, WH, BD2, rx=4))
        p.append(txt(190, 105, "Transform data", 13, TX, 600, "middle"))
        p.append(txt(190, 140, "opens the cleaning editor", 10, MU, 400, "middle"))
        p.append(rect(410, 78, 200, 44, BLU, rx=4))
        p.append(txt(510, 105, "Load", 13, WH, 700, "middle"))
        p.append(txt(510, 140, "brings data straight in", 10, MU, 400, "middle"))
        return svg("".join(p), 700, 200)
    p = [rect(0, 0, W, H, "#F8F8F8")]
    p.append(dialog_box(50, 30, 900, 540, "coffee-sales.csv", "",
                        ("Load", "Transform data", "Cancel"), "Load"))
    # settings row
    for i, (lbl, val) in enumerate([("File origin", "65001: Unicode (UTF-8)"),
                                    ("Delimiter", "Comma"),
                                    ("Data type detection", "Based on first 200 rows")]):
        x = 70 + i * 290
        p.append(txt(x, 78, lbl, 9.5, MU, 600))
        on = (delim_hi and lbl == "Delimiter")
        p.append(rect(x, 86, 260, 28, WH, BLU if on else BD2, rx=3, sw=2 if on else 1))
        p.append(txt(x + 10, 105, val, 10, TX, 700 if on else 400))
        p.append(txt(x + 246, 105, "▾", 9, MU))
    p.append(data_grid(70, 130, 860, 370,
                       ["Date", "Product", "Quantity", "Price"],
                       [["2026-03-04", "Latte", "2", "28000"],
                        ["2026-03-05", "Espresso", "1", "18000"],
                        ["2026-03-05", "Cold Brew", "3", "30000"],
                        ["2026-03-06", "Cappuccino", "2", "27000"],
                        ["2026-03-07", "Croissant", "1", "20000"],
                        ["2026-03-08", "Americano", "4", "22000"],
                        ["2026-03-09", "Latte", "1", "28000"]],
                       ["date", "abc", "123", "123"]))
    return svg("".join(p))


def sc_pq_editor():
    return pq_shell(blanks=(2,))


def sc_pq_select_column():
    return pq_shell(sel_col=5, blanks=(2,))


def sc_pq_remove_rows():
    menu = context_menu(300, 96, ["Remove Top Rows", "Remove Bottom Rows",
                                  "Remove Alternate Rows", "Remove Duplicates",
                                  "Remove Blank Rows", "Remove Errors"],
                        hi="Remove Blank Rows", w=200)
    return pq_shell(hi_ribbon="Remove Rows", menu=menu, blanks=(2,))


def sc_pq_types():
    return pq_shell(cols=["Order ID", "Order Date", "Product", "City", "Price"],
                    rows=[r[:5] for r in PQ_ROWS if any(r)],
                    types=["abc", "abc", "abc", "abc", "abc"],
                    steps=["Source", "Promoted Headers", "Removed Columns",
                           "Removed Blank Rows"])


def sc_pq_fixed_types():
    return pq_shell(cols=["Order ID", "Order Date", "Product", "City", "Price"],
                    rows=[r[:5] for r in PQ_ROWS if any(r)],
                    types=["abc", "date", "abc", "abc", "dec"],
                    steps=["Source", "Promoted Headers", "Removed Columns",
                           "Removed Blank Rows", "Changed Type"])


def sc_pq_cleaned():
    return pq_shell(cols=["Order ID", "Order Date", "Product", "City", "Price"],
                    rows=[r[:5] for r in PQ_ROWS if any(r)],
                    steps=["Source", "Promoted Headers", "Removed Columns",
                           "Removed Blank Rows"])


def sc_pq_replace():
    body = "".join([
        txt(370, 150, "Replace one value with another in the selected columns.",
            10, MU),
        txt(370, 186, "Value To Find", 10, TX, 600),
        rect(370, 194, 300, 28, WH, BD2, rx=3),
        txt(380, 213, "Jakata", 10.5, TX),
        txt(370, 250, "Replace With", 10, TX, 600),
        rect(370, 258, 300, 28, WH, BD2, rx=3),
        txt(380, 277, "Jakarta", 10.5, TX),
    ])
    dlg = dialog_box(350, 110, 340, 260, "Replace Values", body,
                     ("OK", "Cancel"), "OK")
    return pq_shell(sel_col=3, dialog=dlg, blanks=(2,))


def sc_pq_close_apply():
    return pq_shell(hi_ribbon="Close & Apply",
                    cols=["Order ID", "Order Date", "Product", "City", "Price"],
                    rows=[r[:5] for r in PQ_ROWS if any(r)],
                    types=["abc", "date", "abc", "abc", "dec"],
                    steps=["Source", "Promoted Headers", "Removed Columns",
                           "Removed Blank Rows", "Changed Type",
                           "Replaced Value", "Split Column by Delimiter"])


def sc_applied():
    return shell(txt(372, 300, "Add data to your report", 13, "#A19F9D", 400, "middle"),
                 tables=[("messy-orders", ["Order ID", "Order Date", "Product",
                                           "City", "Price"])])


# --- model view ------------------------------------------------------------

def model_table(x, y, w, cols, title, hi=None):
    h = 34 + len(cols) * 22 + 8
    p = [rect(x + 2, y + 2, w, h, "#00000010", rx=6),
         rect(x, y, w, h, WH, BD2, rx=6),
         rect(x, y, w, 30, CH, rx=6), rect(x, y + 20, w, 10, CH),
         txt(x + 14, y + 20, title, 11.5, TX, 700)]
    for i, c in enumerate(cols):
        yy = y + 34 + i * 22
        on = (hi == c)
        if on:
            p.append(rect(x + 4, yy, w - 8, 20, BLL, rx=3))
        p.append(txt(x + 16, yy + 14, c, 10, TX, 700 if on else 400))
    return "".join(p), h


def sc_model(drag=False, cardinality=False, linked=True):
    p = [titlebar("Coffee Dashboard - Power BI Desktop"), ribbon(3),
         view_rail(2), rect(44, 96, W - 44, H - 96 - 26, "#FAFAFA")]
    s, sh = model_table(120, 170, 210, ["Order ID", "Product ID", "Amount",
                                        "Order Date"], "Sales",
                        "Product ID" if drag else None)
    pr, ph = model_table(640, 170, 210, ["Product ID", "Product Name", "Price"],
                         "Products", "Product ID" if drag else None)
    p += [s, pr]
    if linked:
        y1 = 170 + 34 + 1 * 22 + 10       # Sales.Product ID row
        y2 = 170 + 34 + 0 * 22 + 10       # Products.Product ID row
        p.append(line(330, y1, 640, y2, BLU if drag else "#7A7A7A", 2,
                      "6 4" if drag else None))
        mx, my = (330 + 640) / 2, (y1 + y2) / 2
        if cardinality:
            p.append(txt(352, y1 - 6, "*", 18, "#7A7A7A", 700))
            p.append(txt(620, y2 - 6, "1", 13, "#7A7A7A", 700))
            p.append(f'<polygon points="{mx-8},{my-6} {mx+4},{my} {mx-8},{my+6}" fill="#7A7A7A"/>')
    if drag:
        p.append(f'<circle cx="640" cy="{170+44}" r="14" fill="none" stroke="{BLU}" stroke-width="2"/>')
    p.append(page_tabs())
    return svg("".join(p))


def sc_model_view_icon():
    p = [rect(0, 0, 260, 300, "#FAFAFA"), view_rail(2, y0=20, h=260, w=64)]
    p.append(txt(84, 52, "Report view", 12, MU))
    p.append(txt(84, 92, "Table view", 12, MU))
    p.append(txt(84, 132, "Model view", 12, TX, 700))
    return svg("".join(p), 260, 300)


# --- report visuals --------------------------------------------------------

def sc_vis_pick(sel=0):
    canvas = visual_box(90, 140, 560, 340, None, True) + txt(
        370, 315, "Select fields to build the visual", 11, "#A19F9D", 400, "middle")
    return shell(canvas, vis_sel=sel, tables=SALESP)


def sc_bar_built():
    return shell(bar_chart(90, 140, 560, 340, "Amount by Product Name", True),
                 vis_sel=0, tables=SALESP, fields_hi="Amount")


def sc_card_pick():
    return shell(visual_box(90, 140, 240, 130, None, True), vis_sel=6,
                 tables=SALESP)


def sc_dashboard(sel_slicer=None, tidy=False, heading=False, cards=1,
                 title="Amount by Product Name"):
    p = []
    if heading:
        p.append(heading_text(90, 128))
    top = 145 if heading else 130
    if cards == 1:
        p.append(card_visual(430, top, 220, 90))
    else:
        for i, (v, l) in enumerate([("Rp 48.7M", "Total Sales"),
                                    ("1,204", "Order Count"),
                                    ("Rp 40.4K", "Average Sale")]):
            p.append(card_visual(250 + i * 140, top, 130, 84, v, l))
    p.append(slicer_visual(90, top, 145, 330, sel_slicer))
    p.append(bar_chart(250, top + 100, 400, 230, title if not tidy else "Sales by product",
                       only=sel_slicer))
    return shell("".join(p), tables=SALESP,
                 measures=["Total Sales", "Order Count", "Average Sale"] if cards > 1 else None)


def sc_format_pane():
    canvas = bar_chart(90, 140, 560, 340, "Sales by product", True)
    return shell(canvas, fmt=True, tables=SALESP)


def sc_new_measure_menu():
    menu = context_menu(660, 170, ["New measure", "New column", "New quick measure",
                                   "Refresh data", "Edit query", "Rename"],
                        hi="New measure", w=180)
    return shell(menu, tables=SALESP)


def sc_measure_formula():
    p = [rect(44, 96, 656, 40, CH), line(44, 136, 700, 136, BD)]
    p.append(txt(56, 121, "✓  ✕", 11, MU))
    p.append(rect(96, 102, 590, 28, WH, BLU, rx=3, sw=2))
    p.append(txt(106, 121, "1", 9, "#A19F9D"))
    p.append(f'<text x="122" y="121" font-size="11.5" font-family="Consolas, monospace">'
             f'<tspan fill="{TX}">Total Sales = </tspan>'
             f'<tspan fill="#0000C0" font-weight="700">SUM</tspan>'
             f'<tspan fill="{TX}">(</tspan>'
             f'<tspan fill="#008000">Sales[Amount]</tspan>'
             f'<tspan fill="{TX}">)</tspan></text>')
    p.append(rect(300, 136, 220, 74, WH, BD2, rx=4))
    for i, s in enumerate(["Amount", "Order Date", "Order ID"]):
        on = (i == 0)
        if on:
            p.append(rect(303, 140 + i * 22, 214, 20, BLL, rx=2))
        p.append(txt(314, 154 + i * 22, "▦  " + s, 9.5, TX, 700 if on else 400))
    p.append(txt(372, 380, "Total Sales", 12, "#A19F9D", 400, "middle"))
    return shell("".join(p), tables=SALESP)


def sc_measure_card():
    return shell(card_visual(230, 200, 260, 130, "Rp 48.7M", "Total Sales", True),
                 vis_sel=6, tables=SALESP,
                 measures=["Total Sales"])


def sc_three_cards():
    p = []
    for i, (v, l) in enumerate([("Rp 48.7M", "Total Sales"),
                                ("1,204", "Order Count"),
                                ("Rp 40.4K", "Average Sale")]):
        p.append(card_visual(90 + i * 190, 140, 175, 110, v, l))
    p.append(bar_chart(90, 275, 555, 210, "Sales by product"))
    return shell("".join(p), tables=SALESP,
                 measures=["Total Sales", "Order Count", "Average Sale"])


def sc_signin():
    p = [titlebar("Coffee Dashboard - Power BI Desktop", signin=True), ribbon(1)]
    p.append(rect(0, 96, W, 120, "#FAFAFA"))
    p.append(rect(W - 200, 6, 120, 22, "none", BLU, rx=4, sw=2))
    return svg("".join(p), W, 220)


def sc_publish_button():
    p = [titlebar("Coffee Dashboard - Power BI Desktop"), ribbon(1, hi="Publish")]
    p.append(rect(0, 96, W, 90, "#FAFAFA"))
    return svg("".join(p), W, 186)


def browser(title, body, url="app.powerbi.com", h=H):
    p = [rect(0, 0, W, 74, CH), line(0, 74, W, 74, BD2)]
    for i, c in enumerate(["#FF5F57", "#FEBC2E", "#28C840"]):
        p.append(f'<circle cx="{22 + i*18}" cy="18" r="6" fill="{c}"/>')
    p.append(rect(90, 8, 240, 22, WH, BD, rx=6))
    p.append(txt(102, 23, title, 9.5, TX, 600))
    p.append(rect(20, 40, W - 40, 26, WH, BD2, rx=13))
    p.append(txt(40, 58, "🔒  " + url, 10, MU))
    p.append(body)
    return svg("".join(p), W, h)


def sc_published():
    p = [rect(0, 74, W, H - 74, "#F5F5F5")]
    p.append(rect(0, 74, 200, H - 74, WH))
    p.append(txt(16, 104, "Power BI", 13, TX, 700))
    for i, s in enumerate(["Home", "Browse", "OneLake", "My workspace"]):
        on = (s == "My workspace")
        if on:
            p.append(rect(8, 122 + i * 30, 184, 24, BLL, rx=4))
        p.append(txt(20, 139 + i * 30, s, 10, TX, 700 if on else 400))
    p.append(txt(222, 108, "Coffee Dashboard", 15, TX, 700))
    p.append(rect(W - 260, 92, 90, 26, WH, BD2, rx=4))
    p.append(txt(W - 215, 109, "Share", 10, TX, 600, "middle"))
    p.append(rect(220, 128, W - 250, H - 158, WH, BD, rx=6))
    p.append(heading_text(240, 158))
    for i, (v, l) in enumerate([("Rp 48.7M", "Total Sales"), ("1,204", "Order Count"),
                                ("Rp 40.4K", "Average Sale")]):
        p.append(card_visual(400 + i * 120, 172, 112, 74, v, l))
    p.append(slicer_visual(240, 172, 140, 300, None))
    p.append(bar_chart(400, 258, 340, 214, "Sales by product"))
    return browser("Coffee Dashboard - Power BI", "".join(p))


def sc_share_button():
    p = [rect(0, 74, W, 200, "#F5F5F5")]
    p.append(rect(20, 90, W - 40, 44, WH, BD, rx=6))
    p.append(txt(40, 118, "Coffee Dashboard", 13, TX, 700))
    for i, s in enumerate(["File", "Export", "Chat in Teams", "Get insights"]):
        p.append(txt(230 + i * 92, 118, s, 10, MU))
    p.append(rect(W - 150, 98, 100, 28, WH, BLU, rx=4, sw=2))
    p.append(txt(W - 100, 117, "Share", 10.5, BLU, 700, "middle"))
    return browser("Coffee Dashboard - Power BI", "".join(p), h=274)


def sc_shared():
    body = "".join([
        txt(370, 150, "Grant access to", 10, TX, 600),
        rect(370, 158, 300, 30, WH, BD2, rx=3),
        txt(380, 178, "rina@perusahaan.co.id", 10.5, TX),
        rect(370, 200, 300, 26, CH, BD, rx=3),
        txt(380, 218, "Can view  ▾", 10, TX, 600),
        txt(370, 252, "☑  Notify recipients by email", 10, MU),
        txt(370, 274, "☐  Allow recipients to share", 10, MU),
    ])
    p = [rect(0, 74, W, H - 74, "#F5F5F5")]
    p.append(dialog_box(340, 110, 360, 300, "Send link", body, ("Send", "Copy link"), "Send"))
    return browser("Coffee Dashboard - Power BI", "".join(p))


# --- concept diagrams ------------------------------------------------------

def diagram(body, w=1000, h=380):
    return svg(body, w, h)


def sc_three_parts():
    p = []
    items = [("Power BI Desktop", "you build here", pbi_logo(0, 0, 0)),
             ("Report file (.pbix)", "what you make", ""),
             ("Power BI Service", "you publish here", "")]
    for i, (t, s, _) in enumerate(items):
        x = 60 + i * 320
        p.append(rect(x, 90, 260, 180, WH, BD2, rx=12))
        p.append(rect(x, 90, 260, 6, BLU, rx=3))
        if i == 0:
            p.append(pbi_logo(x + 110, 130, 40))
        elif i == 1:
            p.append(rect(x + 108, 130, 44, 52, CH, BD2, rx=4))
            p.append(txt(x + 130, 163, ".pbix", 10, MU, 700, "middle"))
        else:
            p.append(f'<circle cx="{x+130}" cy="150" r="22" fill="none" stroke="{BLU}" stroke-width="2"/>')
            p.append(txt(x + 130, 156, "www", 10, BLU, 700, "middle"))
        p.append(txt(x + 130, 216, t, 13, TX, 700, "middle"))
        p.append(txt(x + 130, 240, s, 11, MU, 400, "middle"))
        if i < 2:
            ax = x + 275
            p.append(line(ax, 180, ax + 30, 180, BLU, 2))
            p.append(f'<polygon points="{ax+30},{174} {ax+42},{180} {ax+30},{186}" fill="{BLU}"/>')
    return diagram("".join(p))


def sc_flow(steps, title=None, h=300):
    p = []
    if title:
        p.append(txt(500, 50, title, 15, TX, 700, "middle"))
    n = len(steps)
    bw = 190
    gap = (1000 - 80 - n * bw) / max(n - 1, 1)
    for i, s in enumerate(steps):
        x = 40 + i * (bw + gap)
        p.append(rect(x, 110, bw, 90, CH, BD2, rx=10))
        p.append(f'<circle cx="{x+bw/2}" cy="140" r="16" fill="{BLU}"/>')
        p.append(txt(x + bw / 2, 146, str(i + 1), 12, WH, 700, "middle"))
        p.append(txt(x + bw / 2, 180, s, 12, TX, 600, "middle"))
        if i < n - 1:
            ax = x + bw + 6
            p.append(line(ax, 155, ax + gap - 12, 155, "#B3B0AD", 2))
            p.append(f'<polygon points="{ax+gap-12},{149} {ax+gap},{155} {ax+gap-12},{161}" fill="#B3B0AD"/>')
    return diagram("".join(p), 1000, h)


def sc_sources():
    p = []
    items = [("Excel workbook", ".xlsx", "#217346"),
             ("CSV file", ".csv", BLU),
             ("Database", "server", "#8661C5")]
    for i, (t, s, col) in enumerate(items):
        x = 90 + i * 290
        on = (i == 1)
        p.append(rect(x, 90, 230, 180, WH, col if on else BD2, rx=12, sw=3 if on else 1))
        p.append(rect(x + 85, 120, 60, 70, CH, BD2, rx=6))
        p.append(rect(x + 85, 120, 60, 18, col, rx=6))
        p.append(rect(x + 85, 132, 60, 6, col))
        p.append(txt(x + 115, 168, s, 11, TX, 700, "middle"))
        p.append(txt(x + 115, 218, t, 13, TX, 700, "middle"))
        if on:
            p.append(rect(x + 60, 232, 110, 22, col, rx=11))
            p.append(txt(x + 115, 247, "used here", 10, WH, 700, "middle"))
    return diagram("".join(p))


def sc_two_tables(idea=False):
    p = []
    left = ["Product ID", "Amount", "Order Date"]
    right = ["Product ID", "Product Name", "Price"]
    s, sh = model_table(90, 110, 250, left, "Sales  (many rows)")
    r, rh = model_table(660, 110, 250, right, "Products  (one per product)")
    p += [s, r]
    y1 = 110 + 34 + 10
    y2 = 110 + 34 + 10
    p.append(line(340, y1, 660, y2, BLU, 2))
    p.append(txt(500, y1 - 12, "linked on Product ID", 11, BLU, 700, "middle"))
    if idea:
        p.append(txt(215, 300, "facts", 12, MU, 600, "middle"))
        p.append(txt(785, 300, "descriptions", 12, MU, 600, "middle"))
    return diagram("".join(p), 1000, 330)


def sc_col_vs_measure():
    p = [line(500, 60, 500, 320, BD, 1, "6 6")]
    p.append(txt(250, 90, "Column", 15, TX, 700, "middle"))
    p.append(txt(250, 114, "stored on every row", 11, MU, 400, "middle"))
    p.append(data_grid(80, 134, 340, 150, ["Product", "Price"],
                       [["Latte", "28000"], ["Espresso", "18000"],
                        ["Cold Brew", "30000"], ["Latte", "28000"]],
                       ["abc", "dec"]))
    p.append(txt(750, 90, "Measure", 15, TX, 700, "middle"))
    p.append(txt(750, 114, "calculated on demand", 11, MU, 400, "middle"))
    p.append(rect(620, 134, 260, 100, WH, BD2, rx=8))
    p.append(txt(750, 180, "Rp 48.7M", 24, TX, 700, "middle"))
    p.append(txt(750, 204, "Total Sales", 10, MU, 400, "middle"))
    p.append(f'<text x="750" y="262" font-size="11" fill="{MU}" text-anchor="middle" '
             f'font-family="Consolas, monospace">SUM(Sales[Amount])</text>')
    p.append(txt(750, 292, "changes when you filter", 11, BLU, 600, "middle"))
    return diagram("".join(p), 1000, 330)


def sc_checklist(done=False):
    p = []
    items = [("Data is clean", "no blanks, right types"),
             ("Model is linked", "joined on Product ID"),
             ("Visuals are tidy", "titles, aligned, slicer works")]
    for i, (t, s) in enumerate(items):
        y = 70 + i * 90
        p.append(rect(120, y, 760, 70, WH, BD2, rx=10))
        p.append(f'<circle cx="168" cy="{y+35}" r="18" fill="#DFF6E8" stroke="#107C41" stroke-width="2"/>')
        p.append(txt(168, y + 41, "✓", 17, "#107C41", 700, "middle"))
        p.append(txt(206, y + 30, t, 13, TX, 700))
        p.append(txt(206, y + 52, s, 11, MU))
    return diagram("".join(p), 1000, 350)


def sc_finished():
    p = [f'<circle cx="500" cy="130" r="60" fill="#DFF6E8" stroke="#107C41" stroke-width="3"/>',
         txt(500, 148, "✓", 52, "#107C41", 700, "middle"),
         txt(500, 232, "All 8 modules complete", 20, TX, 700, "middle"),
         txt(500, 260, "You built and published a real dashboard.", 12, MU, 400, "middle")]
    for i in range(8):
        x = 340 + i * 40
        p.append(rect(x, 285, 30, 8, "#107C41", rx=4))
    return diagram("".join(p), 1000, 340)


def sc_capstone_layout():
    p = [rect(60, 40, 880, 400, WH, BD2, rx=10)]
    p.append(rect(60, 40, 880, 46, CH, rx=10))
    p.append(rect(60, 76, 880, 10, CH))
    p.append(txt(84, 70, "Coffee sales dashboard", 15, TX, 700))
    for i in range(3):
        p.append(rect(250 + i * 230, 104, 210, 80, CH, BD, rx=8))
        p.append(txt(355 + i * 230, 150, "measure card", 11, MU, 600, "middle"))
    p.append(rect(84, 104, 150, 316, CH, BD, rx=8))
    p.append(txt(159, 268, "slicer", 11, MU, 600, "middle"))
    p.append(rect(250, 200, 670, 220, CH, BD, rx=8))
    p.append(txt(585, 316, "bar chart", 11, MU, 600, "middle"))
    return diagram("".join(p), 1000, 480)


# ---------------------------------------------------------------------------
# registry: image file name -> scene
# ---------------------------------------------------------------------------

SCENES = {
    # module 0
    "three-parts": sc_three_parts,
    "cp-mental-model": lambda: sc_flow(["Get data", "Clean", "Connect", "Show"]),
    "store-search": lambda: sc_store(False),
    "store-get": lambda: sc_store(True),
    "cp-empty-desktop": sc_empty_desktop,
    "window-tour": sc_window_tour,
    "cp-named-window": sc_window_tour,
    # module 1
    "cp-sources": sc_sources,
    "getdata-button": sc_getdata,
    "file-browser": sc_file_browser,
    "csv-preview": lambda: sc_csv_preview(),
    "cp-fields-loaded": sc_fields_loaded,
    "delimiter": lambda: sc_csv_preview(delim_hi=True),
    "cp-two-buttons": lambda: sc_csv_preview(buttons_only=True),
    # module 2
    "pq-editor": sc_pq_editor,
    "cp-pq-open": sc_pq_editor,
    "pq-select-column": sc_pq_select_column,
    "pq-remove-rows": sc_pq_remove_rows,
    "cp-cleaned-grid": sc_pq_cleaned,
    "pq-type-icons": sc_pq_types,
    "cp-fixed-types": sc_pq_fixed_types,
    "pq-replace": sc_pq_replace,
    "pq-close-apply": sc_pq_close_apply,
    "cp-applied": sc_applied,
    # module 3
    "model-two-tables": lambda: sc_two_tables(),
    "cp-model-idea": lambda: sc_two_tables(idea=True),
    "model-view-icon": sc_model_view_icon,
    "model-drag": lambda: sc_model(drag=True),
    "cp-relationship": lambda: sc_model(),
    "model-cardinality": lambda: sc_model(cardinality=True),
    "cp-cardinality": lambda: sc_model(cardinality=True),
    # module 4
    "vis-pick-bar": lambda: sc_vis_pick(0),
    "vis-bar-built": sc_bar_built,
    "cp-first-chart": sc_bar_built,
    "vis-card": sc_card_pick,
    "vis-slicer": lambda: sc_dashboard(),
    "cp-interactive": lambda: sc_dashboard(sel_slicer="Latte"),
    "format-pane": sc_format_pane,
    "cp-tidy-page": lambda: sc_dashboard(tidy=True, heading=True),
    # module 5
    "measure-vs-column": sc_col_vs_measure,
    "cp-col-vs-measure": sc_col_vs_measure,
    "new-measure": sc_new_measure_menu,
    "measure-formula": sc_measure_formula,
    "cp-measure-card": sc_measure_card,
    "three-cards": sc_three_cards,
    "cp-headline-row": sc_three_cards,
    # module 6
    "signin": sc_signin,
    "publish-button": sc_publish_button,
    "cp-published": sc_published,
    "share-button": sc_share_button,
    "cp-shared": sc_shared,
    # module 7
    "capstone-layout": sc_capstone_layout,
    "cp-capstone-done": sc_published,
    "checklist": sc_checklist,
    "cp-finished": sc_finished,
}


# ---------------------------------------------------------------------------
# marker anchors (percentages of the image box), per image
# ---------------------------------------------------------------------------

SIZES = {
    "store-get": (1000, 420),
    "signin": (1000, 220),
    "publish-button": (1000, 186),
    "share-button": (1000, 274),
    "model-view-icon": (260, 300),
    "cp-two-buttons": (700, 200),
    "cp-mental-model": (1000, 300),
    "three-parts": (1000, 380),
    "cp-sources": (1000, 380),
    "model-two-tables": (1000, 330),
    "cp-model-idea": (1000, 330),
    "measure-vs-column": (1000, 330),
    "cp-col-vs-measure": (1000, 330),
    "checklist": (1000, 350),
    "cp-finished": (1000, 340),
    "capstone-layout": (1000, 480),
}

# Each entry is (x, y) for the marker, or (x, y, tx, ty) to place the marker
# clear of a small control and draw a connector to the point it refers to —
# so a numbered circle never hides the button it is pointing at.
ANCHORS = {
    "three-parts": [(19, 62), (50, 62), (81, 62)],
    "store-search": [(60, 3.8), (12, 20)],
    "store-get": [(20, 34, 25, 55)],
    "window-tour": [(30, 4.5), (37, 55), (7.5, 26, 2.2, 26), (75, 15), (90, 15)],
    "getdata-button": [(9.2, 27, 9.2, 15.8)],
    "file-browser": [(63, 27.9), (80, 79, 80, 83)],
    "csv-preview": [(50, 45), (72.4, 82, 72.4, 85.5)],
    "delimiter": [(34.5, 16.1), (63.5, 16.1)],
    "cp-two-buttons": [(27, 30, 27, 45), (73, 30, 73, 45)],
    "pq-editor": [(7.5, 32), (45, 45), (88, 33)],
    "pq-select-column": [(70.9, 30, 70.9, 19)],
    "pq-remove-rows": [(56.4, 27, 56.4, 15), (40, 33.7)],
    "pq-type-icons": [(17, 25, 17, 17.6), (34, 25, 34, 17.6), (55, 25, 55, 17.6)],
    "pq-replace": [(43, 34.4), (43, 44.7)],
    "pq-close-apply": [(5.4, 30, 5.4, 15.5)],
    "model-two-tables": [(21, 15), (79, 15), (50, 27)],
    "model-view-icon": [(8.5, 70, 8.5, 49)],
    "model-drag": [(22, 40.5), (74, 30)],
    "model-cardinality": [(62, 27.5, 62, 32.5), (35, 45, 35, 40)],
    "vis-pick-bar": [(76, 20.5, 72.4, 26.5), (37, 50)],
    "vis-bar-built": [(37, 50), (76, 20.5, 72.4, 26.5), (76, 50, 77.5, 52)],
    "vis-card": [(76, 26, 72.4, 32)],
    "vis-slicer": [(16, 45), (54, 28), (45, 62)],
    "format-pane": [(76, 18, 74.7, 22), (76, 32, 74.5, 35)],
    "measure-vs-column": [(25, 20), (75, 20)],
    "new-measure": [(80, 22, 87, 26), (72, 33)],
    "measure-formula": [(39, 27, 39, 18.5), (32, 27)],
    "three-cards": [(17.7, 26), (36.7, 26), (55.7, 26)],
    "signin": [(88, 45, 88, 13)],
    "publish-button": [(78.9, 75, 78.9, 50)],
    "share-button": [(90, 72, 90, 47)],
    "capstone-layout": [(21, 14.5), (35, 30), (58, 65), (16, 55)],
    "checklist": [(16.8, 30), (16.8, 56), (16.8, 82)],
}


def size(name):
    return SIZES.get(name, (W, H))


def render(name):
    """Return the SVG for an image file base name, or None if not in the set."""
    fn = SCENES.get(name)
    return fn() if fn else None


def anchors(name):
    return ANCHORS.get(name)
