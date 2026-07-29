# -*- coding: utf-8 -*-
"""
All curriculum content for Belajar Power BI, as structured data.

Kept separate from the renderer so the whole site stays consistent:
every lesson is built from the identical template in generate.py.

Bilingual fields:
  *_en  -> English (also used for interface chrome parity)
  *_id  -> Bahasa Indonesia, casual register, "aku"/"kamu" (never "gue")
"""

SITE = {
    "name": "Belajar Power BI",
    "tagline_en": "From never opening Power BI to publishing your first dashboard.",
    "author": "Dhany Indraswara",
}


def fig(src, alt, markers, caption=""):
    """Helper to declare an annotated figure as data."""
    return {"src": src, "alt": alt, "markers": markers, "caption": caption}


def m(n, x, y, en, idt, line=None):
    """One numbered callout marker. x/y are percentages of the image box."""
    return {"n": n, "x": x, "y": y, "text_en": en, "text_id": idt, "line": line}


# ---------------------------------------------------------------------------
# MODULES
# ---------------------------------------------------------------------------

MODULES = [
    # =====================================================================
    # MODULE 0
    # =====================================================================
    {
        "n": 0,
        "title": "What Power BI actually is",
        "summary_en": "Before touching a single button, understand what this tool "
        "is for, install it, and learn your way around the window.",
        "summary_id": "Sebelum menyentuh satu tombol pun, kita pahami dulu tool ini "
        "buat apa, kita install, lalu kenalan sama tampilannya.",
        "lessons": [
            {
                "slug": "what-is-power-bi",
                "title": "What Power BI actually is",
                "minutes": 8,
                "difficulty": "Very easy",
                "need_first_en": "Nothing. Just read.",
                "need_first_id": "Nggak butuh apa-apa. Baca aja.",
                "outcome_en": "explain, in one sentence, what Power BI does and the "
                "three things it is made of.",
                "outcome_id": "menjelaskan dalam satu kalimat apa itu Power BI dan "
                "tiga bagian utamanya.",
                "dataset": None,
                "intro_en": "Power BI is a free tool from Microsoft that turns a "
                "boring table of numbers into charts and dashboards you can actually "
                "read at a glance. That is the whole idea. You bring in data, you "
                "shape it, and you show it.",
                "intro_id": "Power BI itu tool gratis dari Microsoft yang mengubah "
                "tabel angka yang membosankan jadi grafik dan dashboard yang enak "
                "dibaca sekilas. Itu aja inti-nya. Kamu masukin data, kamu rapikan, "
                "lalu kamu tampilkan.",
                "steps": [
                    {
                        "instruction_en": "Meet the three parts. Power BI Desktop, "
                        "the app you install on Windows, is where you build. The "
                        "<span class='term' title='A single file, ending in .pbix, "
                        "that holds your data, your model, and your charts all "
                        "together'>report</span> is the file you make. The "
                        "<span class='term' title='Microsoft&#39;s website where a "
                        "finished report lives so other people can open it'>Power BI "
                        "Service</span> is the website where you publish it so others "
                        "can see it.",
                        "instruction_id": "Kenalan sama tiga bagiannya. Power BI "
                        "Desktop, aplikasi yang kamu install di Windows, tempat kamu "
                        "membangun. Report adalah file yang kamu buat. Power BI "
                        "Service adalah website tempat kamu mempublikasikan supaya "
                        "orang lain bisa lihat.",
                        "menu_path": None,
                        "image": fig(
                            "/assets/img/three-parts.svg",
                            "A diagram with three labelled boxes left to right: Power "
                            "BI Desktop where you build, the .pbix report file you "
                            "create, and the Power BI Service website where you "
                            "publish.",
                            [
                                m(1, 18, 50, "Power BI Desktop — where you build",
                                  "Power BI Desktop — tempat membangun"),
                                m(2, 50, 50, "The report file (.pbix)",
                                  "File report (.pbix)"),
                                m(3, 82, 50, "Power BI Service — where you publish",
                                  "Power BI Service — tempat publikasi"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "Know what it is NOT. Power BI is not a "
                        "place to type in data by hand like Excel. It reads data that "
                        "already exists somewhere — a spreadsheet, a file, a database "
                        "— and helps you present it.",
                        "instruction_id": "Tahu apa yang BUKAN Power BI. Power BI "
                        "bukan tempat mengetik data satu-satu kayak Excel. Dia membaca "
                        "data yang sudah ada di suatu tempat — spreadsheet, file, atau "
                        "database — lalu bantu kamu menampilkannya.",
                        "menu_path": None,
                        "image": None,
                    },
                    {
                        "instruction_en": "See the shape of the journey. Every Power "
                        "BI project follows the same four moves: get data, clean data, "
                        "connect data, show data. This whole course is those four "
                        "moves, slowly.",
                        "instruction_id": "Lihat gambaran besarnya. Setiap proyek "
                        "Power BI ikut empat langkah yang sama: ambil data, rapikan "
                        "data, hubungkan data, tampilkan data. Seluruh kursus ini ya "
                        "empat langkah itu, pelan-pelan.",
                        "menu_path": None,
                        "image": None,
                    },
                ],
                "checkpoint_en": "You can now say a sentence like: \"Power BI is a "
                "free Microsoft tool that takes data I already have and turns it into "
                "charts I can share.\" If you can say that, you are ready.",
                "checkpoint_id": "Kamu sekarang bisa bilang kalimat kayak gini: "
                "\"Power BI itu tool gratis dari Microsoft yang mengambil data yang "
                "sudah aku punya dan mengubahnya jadi grafik yang bisa aku bagikan.\" "
                "Kalau kamu bisa bilang itu, kamu siap lanjut.",
                "checkpoint_image": fig(
                    "/assets/img/cp-mental-model.svg",
                    "A simple four-step arrow diagram reading get data, clean, "
                    "connect, show.",
                    [],
                ),
                "why_en": "People quit Power BI in week one because they expect a "
                "fancier Excel and get confused. Knowing it is a present-the-data tool, "
                "not an enter-the-data tool, saves you that confusion.",
                "why_id": "Banyak orang berhenti belajar Power BI di minggu pertama "
                "karena mengira ini Excel versi mewah, lalu bingung. Tahu bahwa ini "
                "tool untuk menampilkan data, bukan mengetik data, menyelamatkan kamu "
                "dari kebingungan itu.",
                "mistakes": [
                    {
                        "title_en": "Trying to type data into Power BI",
                        "title_id": "Mencoba mengetik data langsung di Power BI",
                        "text_en": "Beginners open Power BI and look for an empty grid "
                        "to type into. There isn't one, on purpose. Your data lives in "
                        "a file first.",
                        "text_id": "Pemula membuka Power BI dan mencari kotak kosong "
                        "buat diketik. Nggak ada, dan itu memang disengaja. Datamu "
                        "harus ada di file dulu.",
                    },
                    {
                        "title_en": "Confusing Power BI Desktop with the website",
                        "title_id": "Mencampur Power BI Desktop dengan website-nya",
                        "text_en": "You build on Desktop, you publish to the Service. "
                        "They look similar but do different jobs.",
                        "text_id": "Kamu membangun di Desktop, kamu publikasi ke "
                        "Service. Keduanya mirip tapi tugasnya beda.",
                    },
                ],
            },
            {
                "slug": "install-power-bi-desktop",
                "title": "Installing Power BI Desktop",
                "minutes": 12,
                "difficulty": "Easy",
                "need_first_en": "A Windows PC or laptop.",
                "need_first_id": "PC atau laptop Windows.",
                "outcome_en": "have Power BI Desktop installed and opening on your "
                "own computer.",
                "outcome_id": "sudah menginstal Power BI Desktop dan bisa membukanya "
                "di komputermu sendiri.",
                "dataset": None,
                "intro_en": "Power BI Desktop only runs on Windows. If you use a Mac, "
                "see the note at the bottom before you start. Installing is free and "
                "takes about ten minutes.",
                "intro_id": "Power BI Desktop cuma jalan di Windows. Kalau kamu pakai "
                "Mac, baca catatan di bawah dulu sebelum mulai. Instalnya gratis dan "
                "makan waktu sekitar sepuluh menit.",
                "steps": [
                    {
                        "instruction_en": "Open the Microsoft Store on your Windows "
                        "computer. Click the Start button and type <code>Microsoft "
                        "Store</code>, then open it.",
                        "instruction_id": "Buka Microsoft Store di komputer Windows "
                        "kamu. Klik tombol Start lalu ketik <code>Microsoft Store</code>, "
                        "terus buka.",
                        "menu_path": "Start ▸ Microsoft Store",
                        "image": fig(
                            "/assets/img/store-search.svg",
                            "The Microsoft Store window with a search box at the top "
                            "and the word Power BI typed into it.",
                            [
                                m(1, 50, 12, "The search box at the top",
                                  "Kotak pencarian di atas"),
                                m(2, 30, 45, "The Power BI Desktop result",
                                  "Hasil Power BI Desktop"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "Search for <code>Power BI Desktop</code> "
                        "and click the result published by Microsoft Corporation. "
                        "Publisher matters — pick the official one.",
                        "instruction_id": "Cari <code>Power BI Desktop</code> lalu "
                        "klik hasil yang diterbitkan oleh Microsoft Corporation. "
                        "Penerbit itu penting — pilih yang resmi.",
                        "menu_path": None,
                        "image": None,
                    },
                    {
                        "instruction_en": "Click the blue <strong>Get</strong> "
                        "button and wait for it to download and install. This can "
                        "take a few minutes on a slower connection.",
                        "instruction_id": "Klik tombol biru <strong>Get</strong> "
                        "lalu tunggu proses download dan instalnya. Bisa beberapa "
                        "menit kalau koneksimu lambat.",
                        "menu_path": None,
                        "image": fig(
                            "/assets/img/store-get.svg",
                            "The Power BI Desktop store page showing a blue Get "
                            "button.",
                            [
                                m(1, 72, 30, "The blue Get button",
                                  "Tombol biru Get"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "When it finishes, open Power BI Desktop "
                        "from the Start menu. The first time, a yellow welcome screen "
                        "appears. Close it with the × in its corner.",
                        "instruction_id": "Setelah selesai, buka Power BI Desktop "
                        "dari Start menu. Pertama kali dibuka, muncul layar sambutan "
                        "kuning. Tutup dengan tombol × di pojoknya.",
                        "menu_path": "Start ▸ Power BI Desktop",
                        "image": None,
                    },
                ],
                "checkpoint_en": "You should now see the main Power BI Desktop window: "
                "a ribbon of tabs along the top, a big empty white area in the middle, "
                "and panes down the right side.",
                "checkpoint_id": "Sekarang kamu harusnya melihat jendela utama Power "
                "BI Desktop: deretan tab (ribbon) di atas, area putih kosong besar di "
                "tengah, dan panel-panel di sisi kanan.",
                "checkpoint_image": fig(
                    "/assets/img/cp-empty-desktop.svg",
                    "The empty Power BI Desktop window after first opening it, with "
                    "the ribbon, blank canvas, and right-side panes.",
                    [],
                ),
                "why_en": "Getting the real tool open on your own machine is the step "
                "most people skip by only watching videos. You learn Power BI by "
                "clicking, not by watching.",
                "why_id": "Membuka tool aslinya di komputer sendiri adalah langkah "
                "yang paling sering dilewati orang yang cuma nonton video. Power BI "
                "dipelajari dengan mengklik, bukan dengan menonton.",
                "mistakes": [
                    {
                        "title_en": "Installing on a Mac",
                        "title_id": "Menginstal di Mac",
                        "text_en": "Power BI Desktop is Windows-only. On a Mac you "
                        "need Windows through Parallels, Boot Camp, or a cloud PC. "
                        "There is no Mac version, and there won't be one.",
                        "text_id": "Power BI Desktop cuma untuk Windows. Di Mac kamu "
                        "butuh Windows lewat Parallels, Boot Camp, atau cloud PC. "
                        "Nggak ada versi Mac, dan memang nggak akan ada.",
                    },
                    {
                        "title_en": "Downloading a random installer from a website",
                        "title_id": "Download installer sembarangan dari website",
                        "text_en": "Use the Microsoft Store or Microsoft's official "
                        "download page only. Other sites may bundle unwanted software.",
                        "text_id": "Pakai Microsoft Store atau halaman download resmi "
                        "Microsoft saja. Situs lain bisa menyelipkan software yang "
                        "nggak kamu mau.",
                    },
                ],
            },
            {
                "slug": "tour-of-the-window",
                "title": "A tour of the Power BI Desktop window",
                "minutes": 10,
                "difficulty": "Easy",
                "need_first_en": "Power BI Desktop installed and open.",
                "need_first_id": "Power BI Desktop sudah terinstal dan terbuka.",
                "outcome_en": "name the ribbon, the canvas, the three view icons, and "
                "the two right-side panes without hesitating.",
                "outcome_id": "menyebut ribbon, canvas, tiga ikon view, dan dua panel "
                "kanan tanpa ragu.",
                "dataset": None,
                "intro_en": "The window looks busy at first. It isn't. There are only "
                "five areas that matter, and once you can name them, nothing here "
                "surprises you again.",
                "intro_id": "Jendelanya kelihatan ramai di awal. Sebenarnya nggak "
                "kok. Cuma ada lima area yang penting, dan begitu kamu bisa menyebut "
                "namanya, nggak ada lagi yang bikin kaget.",
                "steps": [
                    {
                        "instruction_en": "Find the <span class='term' title='The "
                        "strip of buttons and tabs across the very top of the "
                        "window'>ribbon</span> across the top. It holds every command, "
                        "grouped into tabs like Home, Insert, and View.",
                        "instruction_id": "Temukan ribbon di bagian paling atas. Di "
                        "sini semua perintah, dikelompokkan jadi tab seperti Home, "
                        "Insert, dan View.",
                        "menu_path": None,
                        "image": fig(
                            "/assets/img/window-tour.svg",
                            "The Power BI Desktop window with five areas marked: the "
                            "ribbon across the top, the canvas in the middle, the "
                            "three view icons on the left edge, the Visualizations "
                            "pane, and the Fields pane on the right.",
                            [
                                m(1, 40, 8, "The ribbon (commands live here)",
                                  "Ribbon (semua perintah di sini)"),
                                m(2, 42, 55, "The canvas (your charts go here)",
                                  "Canvas (grafikmu diletakkan di sini)"),
                                m(3, 5, 40, "The three view icons",
                                  "Tiga ikon view", {"angle": 0, "len": 8}),
                                m(4, 74, 30, "Visualizations pane",
                                  "Panel Visualizations"),
                                m(5, 92, 30, "Fields pane",
                                  "Panel Fields"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "Look at the big white middle. This is the "
                        "<span class='term' title='The blank page where your charts "
                        "and tables are placed'>canvas</span>. Right now it is empty "
                        "because you have no data yet.",
                        "instruction_id": "Lihat area putih besar di tengah. Ini "
                        "canvas. Sekarang kosong karena kamu belum punya data.",
                        "menu_path": None,
                        "image": None,
                    },
                    {
                        "instruction_en": "On the far left edge, find three small "
                        "icons stacked vertically. These switch between Report view, "
                        "Table view, and Model view. You will meet each one later.",
                        "instruction_id": "Di tepi paling kiri, temukan tiga ikon "
                        "kecil bertumpuk vertikal. Ini untuk berpindah antara Report "
                        "view, Table view, dan Model view. Nanti kamu kenalan sama "
                        "masing-masing.",
                        "menu_path": None,
                        "image": None,
                    },
                    {
                        "instruction_en": "On the right, find two panes: "
                        "<strong>Visualizations</strong> (the chart types you can "
                        "add) and <strong>Fields</strong> (the columns from your "
                        "data). They are empty now — that is normal.",
                        "instruction_id": "Di kanan, temukan dua panel: "
                        "<strong>Visualizations</strong> (jenis grafik yang bisa "
                        "ditambah) dan <strong>Fields</strong> (kolom dari datamu). "
                        "Sekarang kosong — itu wajar.",
                        "menu_path": None,
                        "image": None,
                    },
                ],
                "checkpoint_en": "Point at your screen and name all five areas out "
                "loud: ribbon, canvas, view icons, Visualizations, Fields. If you can "
                "do that, this module is done.",
                "checkpoint_id": "Tunjuk layarmu dan sebutkan kelima area itu keras-"
                "keras: ribbon, canvas, ikon view, Visualizations, Fields. Kalau kamu "
                "bisa, modul ini selesai.",
                "checkpoint_image": fig(
                    "/assets/img/cp-named-window.svg",
                    "The Power BI Desktop window with all five areas clearly "
                    "labelled.",
                    [],
                ),
                "why_en": "Every tutorial you ever read will say things like \"in the "
                "Fields pane, drag…\". If those words already mean something to you, "
                "you follow instructions three times faster.",
                "why_id": "Setiap tutorial yang kamu baca nanti bakal bilang hal kayak "
                "\"di panel Fields, seret…\". Kalau kata-kata itu sudah punya makna "
                "buat kamu, kamu mengikuti instruksi tiga kali lebih cepat.",
                "mistakes": [
                    {
                        "title_en": "Panicking that the panes are empty",
                        "title_id": "Panik karena panelnya kosong",
                        "text_en": "Empty Visualizations and Fields panes are correct "
                        "before you load data. They fill up in Module 1.",
                        "text_id": "Panel Visualizations dan Fields yang kosong itu "
                        "benar sebelum kamu memuat data. Nanti terisi di Modul 1.",
                    },
                    {
                        "title_en": "Clicking every ribbon button to see what happens",
                        "title_id": "Mengklik semua tombol ribbon buat lihat efeknya",
                        "text_en": "Tempting, but you will get lost. Follow the "
                        "lessons and each button gets introduced when you need it.",
                        "text_id": "Menggoda, tapi kamu bakal tersesat. Ikuti pelajaran "
                        "dan setiap tombol diperkenalkan saat kamu memang butuh.",
                    },
                ],
            },
        ],
    },
    # =====================================================================
    # MODULE 1
    # =====================================================================
    {
        "n": 1,
        "title": "Getting data in",
        "summary_en": "Bring your first real data into Power BI from a file, and "
        "understand what the load screen is asking you.",
        "summary_id": "Masukkan data asli pertamamu ke Power BI dari sebuah file, "
        "dan pahami apa yang ditanyakan layar pemuatan.",
        "lessons": [
            {
                "slug": "understanding-data-sources",
                "title": "Where data comes from",
                "minutes": 8,
                "difficulty": "Easy",
                "need_first_en": "Module 0 finished.",
                "need_first_id": "Modul 0 sudah selesai.",
                "outcome_en": "recognise the three data sources a beginner will "
                "actually use and know which one this course uses.",
                "outcome_id": "mengenali tiga sumber data yang benar-benar dipakai "
                "pemula dan tahu mana yang dipakai kursus ini.",
                "dataset": None,
                "intro_en": "Power BI can read data from over a hundred places. You "
                "need exactly three of them right now, and this course uses the "
                "simplest one.",
                "intro_id": "Power BI bisa membaca data dari lebih dari seratus "
                "tempat. Kamu cuma butuh tiga sekarang, dan kursus ini pakai yang "
                "paling sederhana.",
                "steps": [
                    {
                        "instruction_en": "Source one: an Excel file. A workbook "
                        "ending in <code>.xlsx</code>. The most common starting point "
                        "for office work.",
                        "instruction_id": "Sumber satu: file Excel. Workbook yang "
                        "berakhiran <code>.xlsx</code>. Titik awal paling umum buat "
                        "kerjaan kantor.",
                        "menu_path": None,
                        "image": None,
                    },
                    {
                        "instruction_en": "Source two: a "
                        "<span class='term' title='A plain text file where each value "
                        "is separated by a comma; opens in Excel but is lighter'>CSV "
                        "file</span>, ending in <code>.csv</code>. A plain, simple "
                        "table. This is what we download in every lesson.",
                        "instruction_id": "Sumber dua: file CSV, berakhiran "
                        "<code>.csv</code>. Tabel yang polos dan sederhana. Ini yang "
                        "kita download di tiap pelajaran.",
                        "menu_path": None,
                        "image": None,
                    },
                    {
                        "instruction_en": "Source three: a database. A big shared "
                        "store of data at your company. You will meet these at work, "
                        "but you do not need one to learn.",
                        "instruction_id": "Sumber tiga: database. Tempat penyimpanan "
                        "data besar yang dipakai bersama di kantormu. Kamu bakal "
                        "ketemu ini di kerjaan, tapi buat belajar kamu nggak butuh.",
                        "menu_path": None,
                        "image": None,
                    },
                ],
                "checkpoint_en": "You know that this course uses CSV files, that they "
                "are just simple tables, and that every lesson gives you one to "
                "download.",
                "checkpoint_id": "Kamu tahu kursus ini pakai file CSV, bahwa itu cuma "
                "tabel sederhana, dan tiap pelajaran kasih satu buat kamu download.",
                "checkpoint_image": fig(
                    "/assets/img/cp-sources.svg",
                    "Three labelled file icons representing an Excel workbook, a CSV "
                    "file, and a database.",
                    [],
                ),
                "why_en": "Choosing the wrong source type is the number one reason a "
                "beginner's first import fails. Knowing you want \"Text/CSV\" removes "
                "that whole class of mistake.",
                "why_id": "Salah memilih jenis sumber adalah alasan nomor satu kenapa "
                "impor pertama pemula gagal. Tahu bahwa kamu mau \"Text/CSV\" "
                "menghilangkan seluruh jenis kesalahan itu.",
                "mistakes": [
                    {
                        "title_en": "Opening a CSV in Excel first and re-saving it",
                        "title_id": "Membuka CSV di Excel dulu lalu menyimpan ulang",
                        "text_en": "You don't need to. Power BI reads the .csv "
                        "directly. Re-saving can quietly change your data.",
                        "text_id": "Kamu nggak perlu. Power BI membaca .csv secara "
                        "langsung. Menyimpan ulang bisa diam-diam mengubah datamu.",
                    },
                    {
                        "title_en": "Thinking you need a database to start",
                        "title_id": "Mengira kamu butuh database buat mulai",
                        "text_en": "You don't. A single small file is enough to learn "
                        "every skill in this course.",
                        "text_id": "Nggak butuh. Satu file kecil sudah cukup buat "
                        "belajar semua skill di kursus ini.",
                    },
                ],
            },
            {
                "slug": "import-your-first-file",
                "title": "Import your first file",
                "minutes": 12,
                "difficulty": "Easy",
                "need_first_en": "Power BI Desktop open. Download the dataset below.",
                "need_first_id": "Power BI Desktop terbuka. Download dataset di bawah.",
                "outcome_en": "load a CSV file into Power BI and see its rows appear.",
                "outcome_id": "memuat file CSV ke Power BI dan melihat baris-barisnya "
                "muncul.",
                "dataset": {
                    "name": "Coffee shop sales",
                    "file": "coffee-sales.csv",
                    "desc_en": "90 rows of pretend sales from a small coffee shop.",
                    "desc_id": "90 baris penjualan pura-pura dari kedai kopi kecil.",
                },
                "intro_en": "Time to bring real data in. Download the coffee shop "
                "file above, remember where it saves (usually your Downloads folder), "
                "and follow along.",
                "intro_id": "Saatnya masukin data asli. Download file kedai kopi di "
                "atas, ingat di mana dia tersimpan (biasanya folder Downloads), lalu "
                "ikuti langkahnya.",
                "steps": [
                    {
                        "instruction_en": "On the Home tab of the ribbon, click "
                        "<strong>Get data</strong>. A menu drops down.",
                        "instruction_id": "Di tab Home pada ribbon, klik <strong>Get "
                        "data</strong>. Menu akan turun.",
                        "menu_path": "Home ▸ Get data",
                        "image": fig(
                            "/assets/img/getdata-button.svg",
                            "The Home ribbon of Power BI Desktop with the Get data "
                            "button highlighted near the left.",
                            [
                                m(1, 14, 22, "The Get data button on the Home tab",
                                  "Tombol Get data di tab Home"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "Choose <strong>Text/CSV</strong> from the "
                        "list. If you don't see it, click <em>More…</em> and search "
                        "for it.",
                        "instruction_id": "Pilih <strong>Text/CSV</strong> dari "
                        "daftar. Kalau nggak kelihatan, klik <em>More…</em> lalu cari.",
                        "menu_path": "Home ▸ Get data ▸ Text/CSV",
                        "image": None,
                    },
                    {
                        "instruction_en": "A file browser opens. Find "
                        "<code>coffee-sales.csv</code> in your Downloads folder, click "
                        "it once, then click <strong>Open</strong>.",
                        "instruction_id": "Jendela pencari file terbuka. Temukan "
                        "<code>coffee-sales.csv</code> di folder Downloads, klik "
                        "sekali, lalu klik <strong>Open</strong>.",
                        "menu_path": None,
                        "image": fig(
                            "/assets/img/file-browser.svg",
                            "A file open dialog showing the coffee-sales.csv file "
                            "selected in the Downloads folder.",
                            [
                                m(1, 40, 45, "The coffee-sales.csv file",
                                  "File coffee-sales.csv"),
                                m(2, 82, 88, "The Open button",
                                  "Tombol Open"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "A preview window appears showing your "
                        "table. Look it over — this is your data. Don't touch the "
                        "settings at the top yet.",
                        "instruction_id": "Muncul jendela pratinjau yang menampilkan "
                        "tabelmu. Perhatikan dulu — ini datamu. Jangan sentuh "
                        "pengaturan di atas dulu.",
                        "menu_path": None,
                        "image": fig(
                            "/assets/img/csv-preview.svg",
                            "The CSV import preview window showing columns for Date, "
                            "Product, Quantity, and Price with a Load button at the "
                            "bottom right.",
                            [
                                m(1, 45, 40, "A preview of your rows and columns",
                                  "Pratinjau baris dan kolommu"),
                                m(2, 80, 90, "The Load button",
                                  "Tombol Load"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "Click the blue <strong>Load</strong> "
                        "button at the bottom right. Power BI pulls the data in.",
                        "instruction_id": "Klik tombol biru <strong>Load</strong> di "
                        "kanan bawah. Power BI menarik datanya masuk.",
                        "menu_path": None,
                        "image": None,
                    },
                ],
                "checkpoint_en": "In the Fields pane on the right you should now see "
                "<strong>coffee-sales</strong> with a small triangle you can expand to "
                "reveal the column names.",
                "checkpoint_id": "Di panel Fields sebelah kanan sekarang harusnya "
                "muncul <strong>coffee-sales</strong> dengan segitiga kecil yang bisa "
                "kamu buka untuk memperlihatkan nama-nama kolom.",
                "checkpoint_image": fig(
                    "/assets/img/cp-fields-loaded.svg",
                    "The Fields pane now showing the coffee-sales table expanded to "
                    "reveal Date, Product, Quantity, and Price columns.",
                    [],
                ),
                "why_en": "This is the single most-used action in all of Power BI. "
                "You will click Get data at the start of every project for the rest of "
                "your career. Get comfortable with it now.",
                "why_id": "Ini aksi yang paling sering dipakai di seluruh Power BI. "
                "Kamu bakal klik Get data di awal tiap proyek sepanjang kariermu. "
                "Nyamanin diri sama ini sekarang.",
                "mistakes": [
                    {
                        "title_en": "Clicking Transform data instead of Load",
                        "title_id": "Mengklik Transform data padahal maunya Load",
                        "text_en": "Both buttons are on the preview screen. For now "
                        "click Load. Transform opens a whole editor you meet in "
                        "Module 2.",
                        "text_id": "Kedua tombol ada di layar pratinjau. Untuk "
                        "sekarang klik Load. Transform membuka editor lengkap yang "
                        "kamu temui di Modul 2.",
                    },
                    {
                        "title_en": "Losing track of where the file downloaded",
                        "title_id": "Lupa di mana file ter-download",
                        "text_en": "If you can't find the file, check your browser's "
                        "downloads list — it shows the exact folder.",
                        "text_id": "Kalau nggak nemu file-nya, cek daftar unduhan di "
                        "browser — di situ ada folder persisnya.",
                    },
                ],
            },
            {
                "slug": "reading-the-load-screen",
                "title": "Reading the load screen",
                "minutes": 9,
                "difficulty": "Easy",
                "need_first_en": "Lesson 1.2 finished, coffee-sales loaded.",
                "need_first_id": "Pelajaran 1.2 selesai, coffee-sales sudah dimuat.",
                "outcome_en": "understand the two choices Power BI offers you on the "
                "import preview and pick correctly.",
                "outcome_id": "memahami dua pilihan yang ditawarkan Power BI di "
                "pratinjau impor dan memilih dengan benar.",
                "dataset": {
                    "name": "Coffee shop sales",
                    "file": "coffee-sales.csv",
                    "desc_en": "The same file from the last lesson.",
                    "desc_id": "File yang sama dari pelajaran sebelumnya.",
                },
                "intro_en": "That preview window had a couple of settings you skipped. "
                "Now let's look at them so they never confuse you.",
                "intro_id": "Jendela pratinjau tadi punya beberapa pengaturan yang "
                "kamu lewati. Sekarang kita lihat supaya nggak pernah bikin bingung.",
                "steps": [
                    {
                        "instruction_en": "Re-open the import: Home ▸ Get data ▸ "
                        "Text/CSV, pick the coffee file again to reach the preview.",
                        "instruction_id": "Buka lagi impornya: Home ▸ Get data ▸ "
                        "Text/CSV, pilih file kopi lagi untuk sampai ke pratinjau.",
                        "menu_path": "Home ▸ Get data ▸ Text/CSV",
                        "image": None,
                    },
                    {
                        "instruction_en": "Look at <strong>Delimiter</strong> at the "
                        "top. A delimiter is the character that separates columns. For "
                        "a CSV it should say Comma. Leave it.",
                        "instruction_id": "Lihat <strong>Delimiter</strong> di atas. "
                        "Delimiter adalah karakter yang memisahkan kolom. Untuk CSV "
                        "harusnya tertulis Comma. Biarkan.",
                        "menu_path": None,
                        "image": fig(
                            "/assets/img/delimiter.svg",
                            "The CSV preview window with the Delimiter dropdown at the "
                            "top set to Comma and a data type detection dropdown "
                            "beside it.",
                            [
                                m(1, 22, 12, "Delimiter — should say Comma",
                                  "Delimiter — harusnya Comma"),
                                m(2, 55, 12, "Data type detection",
                                  "Deteksi tipe data"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "See the two buttons at the bottom: "
                        "<strong>Load</strong> takes the data straight in. "
                        "<strong>Transform data</strong> opens the cleaning editor "
                        "first. Choose Load for clean files, Transform when data needs "
                        "fixing.",
                        "instruction_id": "Lihat dua tombol di bawah: "
                        "<strong>Load</strong> langsung memasukkan data. "
                        "<strong>Transform data</strong> membuka editor pembersih "
                        "dulu. Pilih Load untuk file yang rapi, Transform kalau data "
                        "perlu diperbaiki.",
                        "menu_path": None,
                        "image": None,
                    },
                    {
                        "instruction_en": "For this clean file, click "
                        "<strong>Load</strong>. In the next module you will click "
                        "Transform on purpose.",
                        "instruction_id": "Untuk file yang rapi ini, klik "
                        "<strong>Load</strong>. Di modul berikutnya kamu bakal klik "
                        "Transform dengan sengaja.",
                        "menu_path": None,
                        "image": None,
                    },
                ],
                "checkpoint_en": "You can explain, in your own words, the difference "
                "between the Load button and the Transform data button.",
                "checkpoint_id": "Kamu bisa menjelaskan, dengan kata-katamu sendiri, "
                "beda tombol Load dan tombol Transform data.",
                "checkpoint_image": fig(
                    "/assets/img/cp-two-buttons.svg",
                    "A close-up of the Load and Transform data buttons with short "
                    "labels explaining each.",
                    [],
                ),
                "why_en": "Every import ends on this screen. Knowing which button does "
                "what means you never accidentally skip cleaning, or accidentally get "
                "stuck in an editor you didn't want.",
                "why_id": "Setiap impor berakhir di layar ini. Tahu tombol mana "
                "melakukan apa berarti kamu nggak pernah nggak sengaja melewati "
                "pembersihan, atau nggak sengaja terjebak di editor yang nggak kamu "
                "mau.",
                "mistakes": [
                    {
                        "title_en": "Changing the delimiter when it was already right",
                        "title_id": "Mengubah delimiter padahal sudah benar",
                        "text_en": "If your columns look correct in the preview, don't "
                        "touch the delimiter. Changing it can scramble the table.",
                        "text_id": "Kalau kolommu sudah kelihatan benar di pratinjau, "
                        "jangan sentuh delimiter. Mengubahnya bisa mengacak tabel.",
                    },
                    {
                        "title_en": "Loading the same file twice",
                        "title_id": "Memuat file yang sama dua kali",
                        "text_en": "If you already loaded coffee-sales, loading again "
                        "makes coffee-sales (2). Delete duplicates from the Fields "
                        "pane by right-clicking.",
                        "text_id": "Kalau coffee-sales sudah dimuat, memuat lagi "
                        "membuat coffee-sales (2). Hapus duplikatnya dari panel Fields "
                        "dengan klik kanan.",
                    },
                ],
            },
        ],
    },
    # =====================================================================
    # MODULE 2
    # =====================================================================
    {
        "n": 2,
        "title": "Cleaning with Power Query",
        "summary_en": "Real data is messy. Meet the editor that fixes it, and learn "
        "the four cleaning moves you'll use forever.",
        "summary_id": "Data asli itu berantakan. Kenalan sama editor yang "
        "membersihkannya, dan pelajari empat gerakan pembersihan yang kamu pakai "
        "selamanya.",
        "lessons": [
            {
                "slug": "what-is-power-query",
                "title": "What Power Query is",
                "minutes": 9,
                "difficulty": "Easy",
                "need_first_en": "Module 1 finished.",
                "need_first_id": "Modul 1 sudah selesai.",
                "outcome_en": "open the Power Query Editor and understand that it "
                "records your steps.",
                "outcome_id": "membuka Power Query Editor dan paham bahwa dia merekam "
                "langkah-langkahmu.",
                "dataset": {
                    "name": "Messy orders",
                    "file": "messy-orders.csv",
                    "desc_en": "60 rows with blank cells, wrong types, and extra "
                    "columns — deliberately messy.",
                    "desc_id": "60 baris dengan sel kosong, tipe salah, dan kolom "
                    "berlebih — sengaja dibikin berantakan.",
                },
                "intro_en": "<span class='term' title='The built-in editor inside "
                "Power BI where you clean and reshape data before it loads'>Power "
                "Query</span> is a room inside Power BI where you tidy data before it "
                "reaches your charts. Its superpower: it remembers every change as a "
                "step, so you can redo it on new data instantly.",
                "intro_id": "Power Query adalah ruangan di dalam Power BI tempat kamu "
                "merapikan data sebelum sampai ke grafikmu. Kekuatannya: dia mengingat "
                "setiap perubahan sebagai langkah, jadi kamu bisa mengulanginya di "
                "data baru seketika.",
                "steps": [
                    {
                        "instruction_en": "Download <code>messy-orders.csv</code> "
                        "above. Then Home ▸ Get data ▸ Text/CSV and pick it. This time, "
                        "click <strong>Transform data</strong>, not Load.",
                        "instruction_id": "Download <code>messy-orders.csv</code> di "
                        "atas. Lalu Home ▸ Get data ▸ Text/CSV dan pilih file itu. "
                        "Kali ini, klik <strong>Transform data</strong>, bukan Load.",
                        "menu_path": "Home ▸ Get data ▸ Text/CSV ▸ Transform data",
                        "image": None,
                    },
                    {
                        "instruction_en": "The Power Query Editor opens in a new "
                        "window. It looks like Power BI but greener. Your data fills "
                        "the middle.",
                        "instruction_id": "Power Query Editor terbuka di jendela baru. "
                        "Tampilannya mirip Power BI tapi lebih hijau. Datamu mengisi "
                        "bagian tengah.",
                        "menu_path": None,
                        "image": fig(
                            "/assets/img/pq-editor.svg",
                            "The Power Query Editor window showing the data grid in "
                            "the centre, the Queries list on the left, and the Applied "
                            "Steps panel on the right.",
                            [
                                m(1, 10, 40, "Queries — your tables",
                                  "Queries — tabel-tabelmu", {"angle": 0, "len": 7}),
                                m(2, 48, 45, "The data grid",
                                  "Grid data"),
                                m(3, 88, 40, "Applied Steps — every change recorded",
                                  "Applied Steps — tiap perubahan direkam"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "Look at the <strong>Applied Steps</strong> "
                        "panel on the right. Power BI already added a few steps for "
                        "you. Every future change adds another line here.",
                        "instruction_id": "Lihat panel <strong>Applied Steps</strong> "
                        "di kanan. Power BI sudah menambah beberapa langkah untukmu. "
                        "Setiap perubahan berikutnya menambah satu baris di sini.",
                        "menu_path": None,
                        "image": None,
                    },
                ],
                "checkpoint_en": "You are inside the Power Query Editor, you can see "
                "the messy data, and you can find the Applied Steps list on the right.",
                "checkpoint_id": "Kamu sudah di dalam Power Query Editor, bisa melihat "
                "data berantakannya, dan bisa menemukan daftar Applied Steps di kanan.",
                "checkpoint_image": fig(
                    "/assets/img/cp-pq-open.svg",
                    "The Power Query Editor open with the Applied Steps panel "
                    "highlighted.",
                    [],
                ),
                "why_en": "In real jobs, the same messy report lands on your desk every "
                "month. Because Power Query records steps, you clean it once and "
                "replay the recipe forever. That is why it exists.",
                "why_id": "Di dunia kerja, laporan berantakan yang sama mendarat di "
                "mejamu tiap bulan. Karena Power Query merekam langkah, kamu "
                "membersihkannya sekali lalu memutar ulang resepnya selamanya. Itu "
                "alasan dia ada.",
                "mistakes": [
                    {
                        "title_en": "Closing the editor with the X and losing steps",
                        "title_id": "Menutup editor dengan X dan kehilangan langkah",
                        "text_en": "Use Home ▸ Close & Apply to save your work. The "
                        "window X can discard it.",
                        "text_id": "Pakai Home ▸ Close & Apply untuk menyimpan "
                        "kerjaanmu. Tombol X pada jendela bisa membuangnya.",
                    },
                    {
                        "title_en": "Thinking Power Query changes the original file",
                        "title_id": "Mengira Power Query mengubah file aslinya",
                        "text_en": "It never touches your CSV. All cleaning happens "
                        "inside Power BI only.",
                        "text_id": "Dia nggak pernah menyentuh file CSV-mu. Semua "
                        "pembersihan terjadi di dalam Power BI saja.",
                    },
                ],
            },
            {
                "slug": "remove-columns-and-rows",
                "title": "Remove columns and rows you don't need",
                "minutes": 11,
                "difficulty": "Easy",
                "need_first_en": "Power Query open with messy-orders.",
                "need_first_id": "Power Query terbuka dengan messy-orders.",
                "outcome_en": "delete an unwanted column and remove blank rows.",
                "outcome_id": "menghapus kolom yang nggak dibutuhkan dan membuang "
                "baris kosong.",
                "dataset": {
                    "name": "Messy orders",
                    "file": "messy-orders.csv",
                    "desc_en": "Same messy file from the last lesson.",
                    "desc_id": "File berantakan yang sama dari pelajaran sebelumnya.",
                },
                "intro_en": "The messy file has a useless Notes column and some "
                "totally blank rows. Let's throw them out. This is the most common "
                "cleaning you'll ever do.",
                "intro_id": "File berantakan ini punya kolom Notes yang nggak berguna "
                "dan beberapa baris kosong. Ayo buang. Ini pembersihan paling umum "
                "yang bakal kamu lakukan.",
                "steps": [
                    {
                        "instruction_en": "Click once on the header of the "
                        "<strong>Notes</strong> column to select the whole column. It "
                        "turns a light colour.",
                        "instruction_id": "Klik sekali pada header kolom "
                        "<strong>Notes</strong> untuk memilih seluruh kolom. Warnanya "
                        "berubah jadi lebih terang.",
                        "menu_path": None,
                        "image": fig(
                            "/assets/img/pq-select-column.svg",
                            "The Power Query data grid with the Notes column header "
                            "selected and highlighted.",
                            [
                                m(1, 70, 18, "Click the Notes column header",
                                  "Klik header kolom Notes"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "Right-click the header and choose "
                        "<strong>Remove</strong>. The column disappears and a "
                        "\"Removed Columns\" step appears on the right.",
                        "instruction_id": "Klik kanan headernya dan pilih "
                        "<strong>Remove</strong>. Kolomnya hilang dan langkah "
                        "\"Removed Columns\" muncul di kanan.",
                        "menu_path": "Right-click column ▸ Remove",
                        "image": None,
                    },
                    {
                        "instruction_en": "Now the blank rows. On the Home tab click "
                        "<strong>Remove Rows</strong>, then <strong>Remove Blank "
                        "Rows</strong>.",
                        "instruction_id": "Sekarang baris kosongnya. Di tab Home klik "
                        "<strong>Remove Rows</strong>, lalu <strong>Remove Blank "
                        "Rows</strong>.",
                        "menu_path": "Home ▸ Remove Rows ▸ Remove Blank Rows",
                        "image": fig(
                            "/assets/img/pq-remove-rows.svg",
                            "The Home ribbon of Power Query with the Remove Rows menu "
                            "open showing the Remove Blank Rows option.",
                            [
                                m(1, 30, 20, "Remove Rows menu",
                                  "Menu Remove Rows"),
                                m(2, 40, 55, "Remove Blank Rows",
                                  "Remove Blank Rows"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "Check the Applied Steps panel. You should "
                        "now see both your steps listed in order. You can click any "
                        "step to travel back in time.",
                        "instruction_id": "Cek panel Applied Steps. Sekarang harusnya "
                        "kedua langkahmu tercatat berurutan. Kamu bisa klik langkah "
                        "mana pun untuk kembali ke masa lalu.",
                        "menu_path": None,
                        "image": None,
                    },
                ],
                "checkpoint_en": "The Notes column is gone, there are no empty rows, "
                "and Applied Steps shows Removed Columns followed by Removed Blank "
                "Rows.",
                "checkpoint_id": "Kolom Notes hilang, nggak ada baris kosong, dan "
                "Applied Steps menampilkan Removed Columns lalu Removed Blank Rows.",
                "checkpoint_image": fig(
                    "/assets/img/cp-cleaned-grid.svg",
                    "The cleaned data grid without the Notes column, and the Applied "
                    "Steps panel showing two new steps.",
                    [],
                ),
                "why_en": "Extra columns and blank rows make every later chart harder "
                "and slower. Cleaning them at the door means everything downstream "
                "just works.",
                "why_id": "Kolom berlebih dan baris kosong bikin setiap grafik nanti "
                "lebih susah dan lambat. Membersihkannya di pintu masuk bikin semua "
                "hal setelahnya langsung beres.",
                "mistakes": [
                    {
                        "title_en": "Deleting a column you actually needed",
                        "title_id": "Menghapus kolom yang sebenarnya dibutuhkan",
                        "text_en": "No panic — just delete the Removed Columns step "
                        "from Applied Steps and the column comes right back.",
                        "text_id": "Nggak usah panik — cukup hapus langkah Removed "
                        "Columns dari Applied Steps dan kolomnya kembali lagi.",
                    },
                    {
                        "title_en": "Removing rows by hand one at a time",
                        "title_id": "Menghapus baris satu per satu manual",
                        "text_en": "Use the Remove Rows menu. Manual deleting doesn't "
                        "record as a repeatable step.",
                        "text_id": "Pakai menu Remove Rows. Menghapus manual nggak "
                        "terekam sebagai langkah yang bisa diulang.",
                    },
                ],
            },
            {
                "slug": "fix-data-types",
                "title": "Fix data types",
                "minutes": 11,
                "difficulty": "Medium",
                "need_first_en": "Columns and rows cleaned from the last lesson.",
                "need_first_id": "Kolom dan baris sudah dibersihkan dari pelajaran "
                "sebelumnya.",
                "outcome_en": "set a column to the correct type so numbers add up and "
                "dates sort properly.",
                "outcome_id": "mengatur kolom ke tipe yang benar supaya angka bisa "
                "dijumlah dan tanggal bisa diurutkan dengan benar.",
                "dataset": {
                    "name": "Messy orders",
                    "file": "messy-orders.csv",
                    "desc_en": "Continue with your cleaned file.",
                    "desc_id": "Lanjut dengan file yang sudah kamu bersihkan.",
                },
                "intro_en": "Every column has a <span class='term' title='What kind "
                "of value a column holds: text, whole number, decimal, date, and so "
                "on'>data type</span>. If a number column is set to text, Power BI "
                "won't add it up. Fixing types is quiet but essential.",
                "intro_id": "Setiap kolom punya data type. Kalau kolom angka disetel "
                "sebagai teks, Power BI nggak akan menjumlahkannya. Memperbaiki tipe "
                "itu senyap tapi wajib.",
                "steps": [
                    {
                        "instruction_en": "Look at the tiny icon on the left of each "
                        "column header. <code>ABC</code> means text, "
                        "<code>123</code> means whole number, a calendar means date.",
                        "instruction_id": "Lihat ikon kecil di kiri tiap header "
                        "kolom. <code>ABC</code> berarti teks, <code>123</code> "
                        "berarti bilangan bulat, kalender berarti tanggal.",
                        "menu_path": None,
                        "image": fig(
                            "/assets/img/pq-type-icons.svg",
                            "Column headers in Power Query each showing a small data "
                            "type icon to the left of the column name.",
                            [
                                m(1, 12, 18, "ABC icon = text",
                                  "Ikon ABC = teks"),
                                m(2, 45, 18, "123 icon = whole number",
                                  "Ikon 123 = bilangan bulat"),
                                m(3, 78, 18, "Calendar icon = date",
                                  "Ikon kalender = tanggal"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "The <strong>Price</strong> column shows "
                        "ABC (text) but holds numbers. Click its type icon.",
                        "instruction_id": "Kolom <strong>Price</strong> menampilkan "
                        "ABC (teks) padahal isinya angka. Klik ikon tipenya.",
                        "menu_path": None,
                        "image": None,
                    },
                    {
                        "instruction_en": "Choose <strong>Decimal Number</strong> "
                        "from the list. The icon changes and the values line up to the "
                        "right, which means they are now real numbers.",
                        "instruction_id": "Pilih <strong>Decimal Number</strong> dari "
                        "daftar. Ikonnya berubah dan nilainya rata kanan, tandanya "
                        "sekarang benar-benar angka.",
                        "menu_path": "Click type icon ▸ Decimal Number",
                        "image": None,
                    },
                    {
                        "instruction_en": "Do the same for <strong>Order Date</strong>: "
                        "click its type icon and choose <strong>Date</strong>.",
                        "instruction_id": "Lakukan hal sama untuk <strong>Order "
                        "Date</strong>: klik ikon tipenya dan pilih "
                        "<strong>Date</strong>.",
                        "menu_path": "Click type icon ▸ Date",
                        "image": None,
                    },
                    {
                        "instruction_en": "If a box asks to \"Replace current\" or "
                        "\"Add new step\", choose <strong>Replace current</strong>.",
                        "instruction_id": "Kalau ada kotak menanyakan \"Replace "
                        "current\" atau \"Add new step\", pilih <strong>Replace "
                        "current</strong>.",
                        "menu_path": None,
                        "image": None,
                    },
                ],
                "checkpoint_en": "Price shows a decimal-number icon and Order Date "
                "shows a calendar icon. Numbers sit on the right, dates read as real "
                "dates.",
                "checkpoint_id": "Price menampilkan ikon angka desimal dan Order Date "
                "menampilkan ikon kalender. Angka berada di kanan, tanggal terbaca "
                "sebagai tanggal betulan.",
                "checkpoint_image": fig(
                    "/assets/img/cp-fixed-types.svg",
                    "The data grid with corrected type icons on the Price and Order "
                    "Date columns.",
                    [],
                ),
                "why_en": "The most common \"my total is wrong\" bug in Power BI is a "
                "number column stuck as text. Fix types early and you dodge hours of "
                "confusion later.",
                "why_id": "Bug \"kok totalku salah\" paling umum di Power BI adalah "
                "kolom angka yang nyangkut jadi teks. Perbaiki tipe sejak awal dan "
                "kamu terhindar dari berjam-jam kebingungan nanti.",
                "mistakes": [
                    {
                        "title_en": "Ignoring the little type icons entirely",
                        "title_id": "Mengabaikan ikon tipe kecil itu sama sekali",
                        "text_en": "They are easy to miss but they control "
                        "everything. Always glance at them after loading data.",
                        "text_id": "Gampang terlewat tapi mengontrol segalanya. "
                        "Selalu lirik ikonnya setelah memuat data.",
                    },
                    {
                        "title_en": "Setting a date to a number by accident",
                        "title_id": "Menyetel tanggal jadi angka nggak sengaja",
                        "text_en": "Dates turn into big numbers like 45000. If that "
                        "happens, undo the step and pick Date instead.",
                        "text_id": "Tanggal berubah jadi angka besar seperti 45000. "
                        "Kalau itu terjadi, batalkan langkahnya dan pilih Date.",
                    },
                ],
            },
            {
                "slug": "close-and-apply",
                "title": "Split, replace, and close & apply",
                "minutes": 12,
                "difficulty": "Medium",
                "need_first_en": "Types fixed from the last lesson.",
                "need_first_id": "Tipe sudah diperbaiki dari pelajaran sebelumnya.",
                "outcome_en": "replace a bad value, split a column, and load your "
                "cleaned data back into Power BI.",
                "outcome_id": "mengganti nilai yang salah, memecah kolom, dan memuat "
                "data bersihmu kembali ke Power BI.",
                "dataset": {
                    "name": "Messy orders",
                    "file": "messy-orders.csv",
                    "desc_en": "Finish cleaning the same file.",
                    "desc_id": "Selesaikan pembersihan file yang sama.",
                },
                "intro_en": "Two more everyday moves — replacing typos and splitting a "
                "crammed column — then we lock in all your work with Close & Apply.",
                "intro_id": "Dua gerakan sehari-hari lagi — mengganti typo dan memecah "
                "kolom yang terlalu padat — lalu kita kunci semua kerjaanmu dengan "
                "Close & Apply.",
                "steps": [
                    {
                        "instruction_en": "The <strong>City</strong> column has "
                        "\"Jakata\" misspelled. Right-click that column and choose "
                        "<strong>Replace Values</strong>.",
                        "instruction_id": "Kolom <strong>City</strong> punya "
                        "\"Jakata\" yang salah ketik. Klik kanan kolom itu dan pilih "
                        "<strong>Replace Values</strong>.",
                        "menu_path": "Right-click column ▸ Replace Values",
                        "image": fig(
                            "/assets/img/pq-replace.svg",
                            "The Replace Values dialog in Power Query with a Value To "
                            "Find box and a Replace With box.",
                            [
                                m(1, 35, 40, "Value To Find: Jakata",
                                  "Value To Find: Jakata"),
                                m(2, 35, 62, "Replace With: Jakarta",
                                  "Replace With: Jakarta"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "Type <code>Jakata</code> in \"Value To "
                        "Find\" and <code>Jakarta</code> in \"Replace With\", then "
                        "click OK.",
                        "instruction_id": "Ketik <code>Jakata</code> di \"Value To "
                        "Find\" dan <code>Jakarta</code> di \"Replace With\", lalu "
                        "klik OK.",
                        "menu_path": None,
                        "image": None,
                    },
                    {
                        "instruction_en": "The <strong>Product</strong> column holds "
                        "\"Coffee - Latte\" style values. Select it, then Home ▸ Split "
                        "Column ▸ By Delimiter, choose the dash, and click OK.",
                        "instruction_id": "Kolom <strong>Product</strong> berisi nilai "
                        "gaya \"Coffee - Latte\". Pilih kolomnya, lalu Home ▸ Split "
                        "Column ▸ By Delimiter, pilih tanda strip, dan klik OK.",
                        "menu_path": "Home ▸ Split Column ▸ By Delimiter",
                        "image": None,
                    },
                    {
                        "instruction_en": "Happy with the data? On the Home tab click "
                        "<strong>Close &amp; Apply</strong>. The editor closes and "
                        "your clean data loads into Power BI.",
                        "instruction_id": "Sudah puas dengan datanya? Di tab Home klik "
                        "<strong>Close &amp; Apply</strong>. Editor menutup dan data "
                        "bersihmu masuk ke Power BI.",
                        "menu_path": "Home ▸ Close & Apply",
                        "image": fig(
                            "/assets/img/pq-close-apply.svg",
                            "The top-left of the Power Query Home ribbon with the "
                            "Close & Apply button highlighted.",
                            [
                                m(1, 12, 30, "Close & Apply",
                                  "Close & Apply"),
                            ],
                        ),
                    },
                ],
                "checkpoint_en": "You are back in the main Power BI window, the messy "
                "table now sits clean in the Fields pane, and a short \"applying "
                "changes\" bar flashed by.",
                "checkpoint_id": "Kamu kembali ke jendela utama Power BI, tabel "
                "berantakan tadi sekarang bersih di panel Fields, dan bar \"applying "
                "changes\" singkat sempat lewat.",
                "checkpoint_image": fig(
                    "/assets/img/cp-applied.svg",
                    "The main Power BI window after Close & Apply, with the cleaned "
                    "orders table in the Fields pane.",
                    [],
                ),
                "why_en": "Replace and Split handle the two messiest things in real "
                "data: typos and squashed-together values. Close & Apply is the "
                "handshake that carries your recipe into the rest of Power BI.",
                "why_id": "Replace dan Split menangani dua hal paling berantakan di "
                "data asli: typo dan nilai yang menempel jadi satu. Close & Apply "
                "adalah jabat tangan yang membawa resepmu ke seluruh Power BI.",
                "mistakes": [
                    {
                        "title_en": "Forgetting to click Close & Apply",
                        "title_id": "Lupa mengklik Close & Apply",
                        "text_en": "Your cleaning stays trapped in the editor until "
                        "you apply it. No apply, no clean data in your charts.",
                        "text_id": "Pembersihanmu terjebak di editor sampai kamu "
                        "menerapkannya. Nggak apply, nggak ada data bersih di grafik.",
                    },
                    {
                        "title_en": "Splitting on the wrong character",
                        "title_id": "Memecah pakai karakter yang salah",
                        "text_en": "Match the delimiter to what's actually between "
                        "your values — a dash, a space, or a comma. Preview before OK.",
                        "text_id": "Cocokkan delimiter dengan yang benar-benar ada di "
                        "antara nilaimu — strip, spasi, atau koma. Lihat pratinjau "
                        "sebelum OK.",
                    },
                ],
            },
        ],
    },
    # =====================================================================
    # MODULE 3
    # =====================================================================
    {
        "n": 3,
        "title": "The data model",
        "summary_en": "Two tables are stronger than one. Learn what a relationship is "
        "and connect tables so they can talk to each other.",
        "summary_id": "Dua tabel lebih kuat dari satu. Pelajari apa itu relationship "
        "dan hubungkan tabel supaya bisa saling bicara.",
        "lessons": [
            {
                "slug": "what-is-a-data-model",
                "title": "What a data model is",
                "minutes": 9,
                "difficulty": "Medium",
                "need_first_en": "Module 2 finished.",
                "need_first_id": "Modul 2 sudah selesai.",
                "outcome_en": "explain why you keep facts and descriptions in separate "
                "tables.",
                "outcome_id": "menjelaskan kenapa kamu memisahkan fakta dan deskripsi "
                "ke tabel yang berbeda.",
                "dataset": {
                    "name": "Sales and products",
                    "file": "sales-and-products.zip",
                    "desc_en": "Two CSV files: sales rows, and a product list.",
                    "desc_id": "Dua file CSV: baris penjualan, dan daftar produk.",
                },
                "intro_en": "A <span class='term' title='The set of tables in your "
                "report plus the connections between them'>data model</span> is just "
                "your tables plus the links between them. The big idea: keep the "
                "things that repeat (product names, prices) in their own small table.",
                "intro_id": "Data model itu cuma tabel-tabelmu plus hubungan di "
                "antaranya. Ide besarnya: simpan hal yang berulang (nama produk, "
                "harga) di tabel kecilnya sendiri.",
                "steps": [
                    {
                        "instruction_en": "Picture a sales table with 10,000 rows. "
                        "Writing the full product name on every row wastes space and "
                        "invites typos.",
                        "instruction_id": "Bayangkan tabel penjualan dengan 10.000 "
                        "baris. Menulis nama produk lengkap di tiap baris memboroskan "
                        "ruang dan mengundang typo.",
                        "menu_path": None,
                        "image": None,
                    },
                    {
                        "instruction_en": "Instead, the sales table stores a short "
                        "<strong>Product ID</strong>, and a separate small "
                        "<strong>Products</strong> table stores the ID plus its full "
                        "name and price. One name, stored once.",
                        "instruction_id": "Sebagai gantinya, tabel penjualan menyimpan "
                        "<strong>Product ID</strong> pendek, dan tabel kecil terpisah "
                        "<strong>Products</strong> menyimpan ID plus nama lengkap dan "
                        "harganya. Satu nama, disimpan sekali.",
                        "menu_path": None,
                        "image": fig(
                            "/assets/img/model-two-tables.svg",
                            "Two tables side by side: a large Sales table with a "
                            "Product ID column, and a small Products table with "
                            "Product ID, Name, and Price, joined by a line between the "
                            "matching ID columns.",
                            [
                                m(1, 22, 45, "Sales table — many rows, uses Product ID",
                                  "Tabel Sales — banyak baris, pakai Product ID"),
                                m(2, 78, 45, "Products table — one row per product",
                                  "Tabel Products — satu baris per produk"),
                                m(3, 50, 45, "The link joins them on Product ID",
                                  "Hubungan menyatukan lewat Product ID"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "The line joining them on Product ID is a "
                        "<span class='term' title='A link that tells Power BI how two "
                        "tables match up, usually on a shared ID column'>relationship</"
                        "span>. It lets a chart from one table use names from the "
                        "other.",
                        "instruction_id": "Garis yang menyatukan keduanya lewat "
                        "Product ID adalah relationship. Ini memungkinkan grafik dari "
                        "satu tabel memakai nama dari tabel lain.",
                        "menu_path": None,
                        "image": None,
                    },
                ],
                "checkpoint_en": "You can explain: facts go in one table, the "
                "descriptions they point to go in another, and a relationship links "
                "them by a shared ID.",
                "checkpoint_id": "Kamu bisa menjelaskan: fakta masuk ke satu tabel, "
                "deskripsi yang dirujuknya masuk ke tabel lain, dan relationship "
                "menyatukan lewat ID bersama.",
                "checkpoint_image": fig(
                    "/assets/img/cp-model-idea.svg",
                    "A simple diagram of a facts table linked to a descriptions table "
                    "by a shared ID.",
                    [],
                ),
                "why_en": "Almost every real Power BI report has several tables linked "
                "this way. Understanding the idea now means the Model view won't feel "
                "like a tangle of spaghetti later.",
                "why_id": "Hampir semua report Power BI asli punya beberapa tabel yang "
                "terhubung begini. Paham idenya sekarang berarti Model view nggak "
                "bakal terasa kayak seporsi spageti kusut nanti.",
                "mistakes": [
                    {
                        "title_en": "Cramming everything into one giant table",
                        "title_id": "Menjejalkan semua ke satu tabel raksasa",
                        "text_en": "It works for tiny data but breaks down fast. "
                        "Separate tables keep things clean and fast.",
                        "text_id": "Itu jalan buat data kecil tapi cepat ambruk. Tabel "
                        "terpisah menjaga semuanya bersih dan cepat.",
                    },
                    {
                        "title_en": "Expecting the link to appear by magic",
                        "title_id": "Berharap hubungan muncul dengan ajaib",
                        "text_en": "Sometimes Power BI guesses relationships, "
                        "sometimes you make them yourself. You'll do that next lesson.",
                        "text_id": "Kadang Power BI menebak relationship, kadang kamu "
                        "yang membuatnya sendiri. Kamu melakukannya di pelajaran "
                        "berikutnya.",
                    },
                ],
            },
            {
                "slug": "create-a-relationship",
                "title": "Create a relationship",
                "minutes": 12,
                "difficulty": "Medium",
                "need_first_en": "Both tables loaded (sales and products).",
                "need_first_id": "Kedua tabel sudah dimuat (sales dan products).",
                "outcome_en": "join two tables in Model view by dragging one ID onto "
                "another.",
                "outcome_id": "menyatukan dua tabel di Model view dengan menyeret satu "
                "ID ke ID lainnya.",
                "dataset": {
                    "name": "Sales and products",
                    "file": "sales-and-products.zip",
                    "desc_en": "Load both CSV files before you start.",
                    "desc_id": "Muat kedua file CSV sebelum mulai.",
                },
                "intro_en": "Now we connect the two tables for real. It's a single "
                "drag, done in the Model view.",
                "intro_id": "Sekarang kita hubungkan kedua tabel beneran. Cuma satu "
                "tarikan, dilakukan di Model view.",
                "steps": [
                    {
                        "instruction_en": "Click the <strong>Model view</strong> "
                        "icon, the third icon on the far left edge (it looks like "
                        "connected boxes).",
                        "instruction_id": "Klik ikon <strong>Model view</strong>, "
                        "ikon ketiga di tepi paling kiri (bentuknya seperti kotak yang "
                        "terhubung).",
                        "menu_path": "Left edge ▸ Model view",
                        "image": fig(
                            "/assets/img/model-view-icon.svg",
                            "The three view icons on the left edge of Power BI with "
                            "the third Model view icon highlighted.",
                            [
                                m(1, 30, 55, "The Model view icon (third one)",
                                  "Ikon Model view (yang ketiga)"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "You see both tables as boxes with their "
                        "column names. If a line already joins them, Power BI guessed "
                        "the relationship — you're done, skip to the checkpoint.",
                        "instruction_id": "Kamu lihat kedua tabel sebagai kotak berisi "
                        "nama kolom. Kalau sudah ada garis yang menyatukan, Power BI "
                        "sudah menebak relationship — selesai, lompat ke checkpoint.",
                        "menu_path": None,
                        "image": None,
                    },
                    {
                        "instruction_en": "If there's no line, drag "
                        "<strong>Product ID</strong> from the Sales box and drop it "
                        "onto <strong>Product ID</strong> in the Products box.",
                        "instruction_id": "Kalau nggak ada garis, seret "
                        "<strong>Product ID</strong> dari kotak Sales dan jatuhkan ke "
                        "<strong>Product ID</strong> di kotak Products.",
                        "menu_path": None,
                        "image": fig(
                            "/assets/img/model-drag.svg",
                            "Two table boxes in Model view with an arrow showing "
                            "Product ID being dragged from the Sales table onto "
                            "Product ID in the Products table.",
                            [
                                m(1, 25, 60, "Drag Product ID from Sales",
                                  "Seret Product ID dari Sales"),
                                m(2, 75, 40, "Drop it on Product ID in Products",
                                  "Jatuhkan di Product ID di Products"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "A line now connects the two boxes. That "
                        "line is your relationship. Hover it and it highlights the two "
                        "linked columns.",
                        "instruction_id": "Sekarang garis menghubungkan kedua kotak. "
                        "Garis itu relationship-mu. Arahkan kursor ke garis dan dia "
                        "menyorot dua kolom yang terhubung.",
                        "menu_path": None,
                        "image": None,
                    },
                ],
                "checkpoint_en": "A single line runs between the Sales and Products "
                "boxes, connecting their Product ID columns.",
                "checkpoint_id": "Satu garis membentang antara kotak Sales dan "
                "Products, menghubungkan kolom Product ID mereka.",
                "checkpoint_image": fig(
                    "/assets/img/cp-relationship.svg",
                    "Two tables in Model view joined by a single relationship line "
                    "between their Product ID columns.",
                    [],
                ),
                "why_en": "This one line is what lets you build a chart of sales "
                "totals broken down by product name — even though sales and names live "
                "in different tables. It's the quiet engine under every good report.",
                "why_id": "Satu garis ini yang memungkinkan kamu membuat grafik total "
                "penjualan dipecah per nama produk — padahal penjualan dan nama ada di "
                "tabel berbeda. Ini mesin senyap di balik setiap report yang bagus.",
                "mistakes": [
                    {
                        "title_en": "Dragging the wrong columns together",
                        "title_id": "Menyeret kolom yang salah",
                        "text_en": "Always join ID to matching ID. Joining Name to "
                        "Price makes a broken, meaningless link.",
                        "text_id": "Selalu satukan ID ke ID yang cocok. Menyatukan "
                        "Name ke Price membuat hubungan rusak yang nggak bermakna.",
                    },
                    {
                        "title_en": "Making two relationships between the same tables",
                        "title_id": "Membuat dua relationship antara tabel yang sama",
                        "text_en": "You usually want just one active line. If you see "
                        "a dotted extra line, delete it by clicking and pressing "
                        "Delete.",
                        "text_id": "Biasanya kamu cuma mau satu garis aktif. Kalau ada "
                        "garis putus-putus tambahan, hapus dengan klik lalu tekan "
                        "Delete.",
                    },
                ],
            },
            {
                "slug": "reading-the-model-view",
                "title": "Reading the Model view",
                "minutes": 8,
                "difficulty": "Easy",
                "need_first_en": "A relationship created from the last lesson.",
                "need_first_id": "Relationship sudah dibuat dari pelajaran sebelumnya.",
                "outcome_en": "read the little symbols on a relationship line and know "
                "your tables are connected the normal way.",
                "outcome_id": "membaca simbol kecil di garis relationship dan tahu "
                "tabelmu terhubung dengan cara yang normal.",
                "dataset": None,
                "intro_en": "That line has tiny symbols at each end. You don't need to "
                "master them, but recognising the normal, healthy pattern gives you "
                "confidence.",
                "intro_id": "Garis itu punya simbol kecil di tiap ujung. Kamu nggak "
                "perlu menguasainya, tapi mengenali pola normal yang sehat bikin kamu "
                "pede.",
                "steps": [
                    {
                        "instruction_en": "Hover the relationship line. One end shows "
                        "a <strong>1</strong>, the other shows an asterisk "
                        "<strong>*</strong>. This is the normal one-to-many pattern.",
                        "instruction_id": "Arahkan kursor ke garis relationship. Satu "
                        "ujung menunjukkan <strong>1</strong>, ujung lain menunjukkan "
                        "tanda bintang <strong>*</strong>. Ini pola one-to-many yang "
                        "normal.",
                        "menu_path": None,
                        "image": fig(
                            "/assets/img/model-cardinality.svg",
                            "A relationship line between two tables showing a 1 on the "
                            "Products end and an asterisk on the Sales end.",
                            [
                                m(1, 72, 42, "The 1 sits on the Products side",
                                  "Angka 1 di sisi Products"),
                                m(2, 28, 55, "The * sits on the Sales side",
                                  "Tanda * di sisi Sales"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "Read it as: <em>one</em> product can appear "
                        "in <em>many</em> sales rows. That's exactly right for our "
                        "data.",
                        "instruction_id": "Baca sebagai: <em>satu</em> produk bisa "
                        "muncul di <em>banyak</em> baris penjualan. Itu persis benar "
                        "untuk data kita.",
                        "menu_path": None,
                        "image": None,
                    },
                    {
                        "instruction_en": "An arrow on the line shows which way "
                        "filtering flows. For beginners, the default single arrow is "
                        "what you want. Don't change it.",
                        "instruction_id": "Panah pada garis menunjukkan arah aliran "
                        "filter. Untuk pemula, panah tunggal bawaan itu yang kamu mau. "
                        "Jangan diubah.",
                        "menu_path": None,
                        "image": None,
                    },
                ],
                "checkpoint_en": "You can point at the 1 and the * on your "
                "relationship line and say which table is the \"one\" side.",
                "checkpoint_id": "Kamu bisa menunjuk angka 1 dan tanda * di garis "
                "relationship-mu dan menyebut tabel mana yang sisi \"one\".",
                "checkpoint_image": fig(
                    "/assets/img/cp-cardinality.svg",
                    "The relationship line labelled with the 1 and many ends clearly "
                    "marked.",
                    [],
                ),
                "why_en": "When a report shows weird totals, nine times out of ten the "
                "relationship symbols are wrong. Reading them is your first debugging "
                "check, forever.",
                "why_id": "Kalau report menampilkan total aneh, sembilan dari sepuluh "
                "kali simbol relationship-nya salah. Membacanya adalah pengecekan "
                "debug pertamamu, selamanya.",
                "mistakes": [
                    {
                        "title_en": "Turning on both-direction arrows to \"fix\" things",
                        "title_id": "Menyalakan panah dua arah buat \"memperbaiki\"",
                        "text_en": "This causes more problems than it solves for "
                        "beginners. Leave the arrow single.",
                        "text_id": "Ini menimbulkan lebih banyak masalah daripada "
                        "solusi buat pemula. Biarkan panahnya tunggal.",
                    },
                    {
                        "title_en": "Worrying about the symbols too much",
                        "title_id": "Terlalu mengkhawatirkan simbolnya",
                        "text_en": "For one-to-many joins on IDs, the defaults are "
                        "almost always correct. Recognise, don't obsess.",
                        "text_id": "Untuk join one-to-many pada ID, bawaannya hampir "
                        "selalu benar. Kenali saja, nggak usah berlebihan.",
                    },
                ],
            },
        ],
    },
    # =====================================================================
    # MODULE 4
    # =====================================================================
    {
        "n": 4,
        "title": "First visuals",
        "summary_en": "Finally, charts. Build a bar chart, add a card and a slicer, "
        "and make the whole thing readable.",
        "summary_id": "Akhirnya, grafik. Bikin bar chart, tambah card dan slicer, "
        "dan bikin semuanya enak dibaca.",
        "lessons": [
            {
                "slug": "your-first-chart",
                "title": "Your first chart",
                "minutes": 12,
                "difficulty": "Easy",
                "need_first_en": "Module 3 finished, tables loaded and linked.",
                "need_first_id": "Modul 3 selesai, tabel dimuat dan terhubung.",
                "outcome_en": "build a bar chart showing sales by product.",
                "outcome_id": "membuat bar chart yang menampilkan penjualan per "
                "produk.",
                "dataset": {
                    "name": "Sales and products",
                    "file": "sales-and-products.zip",
                    "desc_en": "The linked tables from Module 3.",
                    "desc_id": "Tabel terhubung dari Modul 3.",
                },
                "intro_en": "This is the moment it clicks. In three drags you'll turn "
                "your numbers into a bar chart. Switch to Report view (the top icon on "
                "the left edge) first.",
                "intro_id": "Ini momen semuanya ngeklik. Dalam tiga tarikan kamu "
                "mengubah angkamu jadi bar chart. Pindah ke Report view dulu (ikon "
                "paling atas di tepi kiri).",
                "steps": [
                    {
                        "instruction_en": "In the Visualizations pane, click the "
                        "<strong>Clustered bar chart</strong> icon. An empty chart "
                        "box appears on the canvas.",
                        "instruction_id": "Di panel Visualizations, klik ikon "
                        "<strong>Clustered bar chart</strong>. Kotak grafik kosong "
                        "muncul di canvas.",
                        "menu_path": "Visualizations pane ▸ Clustered bar chart",
                        "image": fig(
                            "/assets/img/vis-pick-bar.svg",
                            "The Visualizations pane with the clustered bar chart icon "
                            "highlighted among the chart type icons.",
                            [
                                m(1, 50, 20, "The clustered bar chart icon",
                                  "Ikon clustered bar chart"),
                                m(2, 30, 60, "The empty chart appears here",
                                  "Grafik kosong muncul di sini"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "In the Fields pane, tick "
                        "<strong>Product Name</strong> from the Products table. It "
                        "drops into the chart's Y-axis.",
                        "instruction_id": "Di panel Fields, centang <strong>Product "
                        "Name</strong> dari tabel Products. Dia masuk ke Y-axis "
                        "grafik.",
                        "menu_path": None,
                        "image": None,
                    },
                    {
                        "instruction_en": "Now tick <strong>Amount</strong> from the "
                        "Sales table. Bars appear instantly, one per product.",
                        "instruction_id": "Sekarang centang <strong>Amount</strong> "
                        "dari tabel Sales. Batang langsung muncul, satu per produk.",
                        "menu_path": None,
                        "image": fig(
                            "/assets/img/vis-bar-built.svg",
                            "A finished clustered bar chart on the canvas showing one "
                            "bar per product, with Product Name on the axis and Amount "
                            "as the value.",
                            [
                                m(1, 45, 45, "One bar per product",
                                  "Satu batang per produk"),
                                m(2, 80, 30, "Product Name is on the axis",
                                  "Product Name di sumbu"),
                                m(3, 80, 55, "Amount is the value",
                                  "Amount jadi nilainya"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "Notice this worked across two tables: names "
                        "from Products, amounts from Sales. That's your relationship "
                        "doing its job.",
                        "instruction_id": "Perhatikan ini bekerja lintas dua tabel: "
                        "nama dari Products, jumlah dari Sales. Itu relationship-mu "
                        "sedang bekerja.",
                        "menu_path": None,
                        "image": None,
                    },
                ],
                "checkpoint_en": "A horizontal bar chart sits on your canvas with a "
                "labelled bar for each product, longest bar for the best seller.",
                "checkpoint_id": "Bar chart horizontal ada di canvas-mu dengan batang "
                "berlabel untuk tiap produk, batang terpanjang untuk yang paling "
                "laku.",
                "checkpoint_image": fig(
                    "/assets/img/cp-first-chart.svg",
                    "A completed bar chart of Amount by Product Name on the report "
                    "canvas.",
                    [],
                ),
                "why_en": "The tick-a-field, get-a-chart loop is how you'll build "
                "every visual from now on. Once this feels natural, the whole tool "
                "opens up.",
                "why_id": "Loop centang-field, dapat-grafik adalah cara kamu membangun "
                "setiap visual mulai sekarang. Begitu ini terasa alami, seluruh "
                "tool-nya terbuka.",
                "mistakes": [
                    {
                        "title_en": "Ticking a field with no chart selected",
                        "title_id": "Mencentang field tanpa grafik terpilih",
                        "text_en": "Power BI makes a brand-new visual instead of "
                        "filling yours. Click your chart first, then tick fields.",
                        "text_id": "Power BI membuat visual baru alih-alih mengisi "
                        "punyamu. Klik grafikmu dulu, baru centang field.",
                    },
                    {
                        "title_en": "Putting a text field where a number belongs",
                        "title_id": "Menaruh field teks di tempat angka",
                        "text_en": "Amount must be a number (Module 2). If bars don't "
                        "appear, check that its type isn't stuck as text.",
                        "text_id": "Amount harus angka (Modul 2). Kalau batang nggak "
                        "muncul, cek tipenya jangan sampai nyangkut jadi teks.",
                    },
                ],
            },
            {
                "slug": "cards-tables-slicers",
                "title": "Cards, tables, and slicers",
                "minutes": 13,
                "difficulty": "Easy",
                "need_first_en": "Your first chart built.",
                "need_first_id": "Grafik pertamamu sudah jadi.",
                "outcome_en": "add a big-number card and a slicer that filters the "
                "whole page.",
                "outcome_id": "menambah card angka besar dan slicer yang memfilter "
                "seluruh halaman.",
                "dataset": {
                    "name": "Sales and products",
                    "file": "sales-and-products.zip",
                    "desc_en": "Keep working in the same file.",
                    "desc_id": "Lanjut kerja di file yang sama.",
                },
                "intro_en": "A chart alone isn't a dashboard. Add a "
                "<span class='term' title='A visual that shows a single big number, "
                "like a total'>card</span> for the headline number and a "
                "<span class='term' title='A visual full of buttons that filters every "
                "other visual on the page'>slicer</span> so viewers can filter.",
                "intro_id": "Grafik saja belum dashboard. Tambah card untuk angka "
                "utama dan slicer supaya penonton bisa memfilter.",
                "steps": [
                    {
                        "instruction_en": "Click an empty part of the canvas so no "
                        "chart is selected. In Visualizations, click the "
                        "<strong>Card</strong> icon.",
                        "instruction_id": "Klik bagian kosong canvas supaya nggak ada "
                        "grafik terpilih. Di Visualizations, klik ikon "
                        "<strong>Card</strong>.",
                        "menu_path": "Visualizations pane ▸ Card",
                        "image": fig(
                            "/assets/img/vis-card.svg",
                            "The Visualizations pane with the Card visual icon "
                            "highlighted.",
                            [
                                m(1, 50, 30, "The Card icon",
                                  "Ikon Card"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "Tick <strong>Amount</strong>. The card "
                        "shows one big total sales number.",
                        "instruction_id": "Centang <strong>Amount</strong>. Card "
                        "menampilkan satu angka total penjualan yang besar.",
                        "menu_path": None,
                        "image": None,
                    },
                    {
                        "instruction_en": "Click empty canvas again, then click the "
                        "<strong>Slicer</strong> icon in Visualizations.",
                        "instruction_id": "Klik canvas kosong lagi, lalu klik ikon "
                        "<strong>Slicer</strong> di Visualizations.",
                        "menu_path": "Visualizations pane ▸ Slicer",
                        "image": None,
                    },
                    {
                        "instruction_en": "Tick <strong>Product Name</strong>. The "
                        "slicer fills with tick-boxes for each product.",
                        "instruction_id": "Centang <strong>Product Name</strong>. "
                        "Slicer terisi kotak centang untuk tiap produk.",
                        "menu_path": None,
                        "image": fig(
                            "/assets/img/vis-slicer.svg",
                            "A report page with a slicer listing product names, a card "
                            "showing a total, and a bar chart, all together.",
                            [
                                m(1, 18, 45, "The slicer with product tick-boxes",
                                  "Slicer dengan kotak centang produk"),
                                m(2, 78, 25, "The card total",
                                  "Total pada card"),
                                m(3, 60, 60, "The bar chart",
                                  "Bar chart"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "Tick a product in the slicer. Watch the "
                        "card and the chart both update to just that product. One "
                        "slicer filters the whole page.",
                        "instruction_id": "Centang satu produk di slicer. Lihat card "
                        "dan grafik keduanya berubah jadi cuma produk itu. Satu slicer "
                        "memfilter seluruh halaman.",
                        "menu_path": None,
                        "image": None,
                    },
                ],
                "checkpoint_en": "Ticking a product in the slicer instantly changes "
                "both the card number and the bar chart. Untick to see everything "
                "again.",
                "checkpoint_id": "Mencentang satu produk di slicer langsung mengubah "
                "angka card dan bar chart. Batalkan centang untuk melihat semuanya "
                "lagi.",
                "checkpoint_image": fig(
                    "/assets/img/cp-interactive.svg",
                    "The report page with a product selected in the slicer and the "
                    "card and chart both filtered to it.",
                    [],
                ),
                "why_en": "Cards give the headline, slicers give control. Together "
                "they're what makes a page feel like a real, clickable dashboard "
                "instead of a static picture.",
                "why_id": "Card memberi judul angka, slicer memberi kendali. "
                "Bersama-sama itulah yang bikin halaman terasa seperti dashboard "
                "beneran yang bisa diklik, bukan gambar diam.",
                "mistakes": [
                    {
                        "title_en": "Building the slicer on top of a chart",
                        "title_id": "Membangun slicer di atas grafik",
                        "text_en": "Always click empty canvas first. Otherwise you "
                        "change the selected chart instead of making a new visual.",
                        "text_id": "Selalu klik canvas kosong dulu. Kalau nggak, kamu "
                        "mengubah grafik terpilih alih-alih membuat visual baru.",
                    },
                    {
                        "title_en": "Forgetting a slicer selection is still on",
                        "title_id": "Lupa pilihan slicer masih menyala",
                        "text_en": "If numbers look too small, check whether a slicer "
                        "is still filtering. Clear it to see the full picture.",
                        "text_id": "Kalau angka kelihatan terlalu kecil, cek apakah "
                        "slicer masih memfilter. Bersihkan untuk melihat gambaran "
                        "penuh.",
                    },
                ],
            },
            {
                "slug": "formatting-and-layout",
                "title": "Formatting and layout",
                "minutes": 12,
                "difficulty": "Easy",
                "need_first_en": "A card, slicer, and chart on the page.",
                "need_first_id": "Card, slicer, dan grafik ada di halaman.",
                "outcome_en": "give a visual a clear title and line everything up "
                "neatly.",
                "outcome_id": "memberi visual judul yang jelas dan merapikan tata "
                "letaknya.",
                "dataset": {
                    "name": "Sales and products",
                    "file": "sales-and-products.zip",
                    "desc_en": "Same file, keep going.",
                    "desc_id": "File yang sama, lanjut terus.",
                },
                "intro_en": "A tidy page earns trust. We'll title a chart and align "
                "the visuals using the Format pane — the paint-roller icon.",
                "intro_id": "Halaman yang rapi mengundang kepercayaan. Kita bakal "
                "memberi judul grafik dan merapikan visual pakai panel Format — ikon "
                "roller cat.",
                "steps": [
                    {
                        "instruction_en": "Click your bar chart to select it. In the "
                        "Visualizations pane, click the <strong>Format</strong> icon "
                        "(a paint roller).",
                        "instruction_id": "Klik bar chart-mu untuk memilihnya. Di "
                        "panel Visualizations, klik ikon <strong>Format</strong> "
                        "(roller cat).",
                        "menu_path": "Visualizations pane ▸ Format (paint roller)",
                        "image": fig(
                            "/assets/img/format-pane.svg",
                            "The Visualizations pane switched to the Format tab, "
                            "showing formatting options with the paint roller icon "
                            "highlighted.",
                            [
                                m(1, 55, 18, "The Format paint-roller icon",
                                  "Ikon roller cat Format"),
                                m(2, 55, 45, "The Title setting",
                                  "Pengaturan Title"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "Find <strong>General ▸ Title</strong>. "
                        "Turn it on if needed, then type a clear title like "
                        "<code>Sales by product</code>.",
                        "instruction_id": "Temukan <strong>General ▸ Title</strong>. "
                        "Nyalakan kalau perlu, lalu ketik judul jelas seperti "
                        "<code>Sales by product</code>.",
                        "menu_path": "Format ▸ General ▸ Title",
                        "image": None,
                    },
                    {
                        "instruction_en": "Drag the corners of each visual so the "
                        "slicer is narrow on the left and the chart fills the space. "
                        "Line up their top edges.",
                        "instruction_id": "Seret sudut tiap visual supaya slicer "
                        "sempit di kiri dan grafik mengisi ruang. Sejajarkan tepi "
                        "atasnya.",
                        "menu_path": None,
                        "image": None,
                    },
                    {
                        "instruction_en": "Give the whole page a title: Insert ▸ Text "
                        "box, type <code>Coffee sales dashboard</code>, and place it "
                        "at the top.",
                        "instruction_id": "Beri seluruh halaman judul: Insert ▸ Text "
                        "box, ketik <code>Coffee sales dashboard</code>, dan letakkan "
                        "di atas.",
                        "menu_path": "Insert ▸ Text box",
                        "image": None,
                    },
                ],
                "checkpoint_en": "Your page has a heading at the top, a titled chart, "
                "and visuals that line up on a tidy grid instead of overlapping.",
                "checkpoint_id": "Halamanmu punya heading di atas, grafik berjudul, "
                "dan visual yang sejajar di grid rapi alih-alih saling menumpuk.",
                "checkpoint_image": fig(
                    "/assets/img/cp-tidy-page.svg",
                    "A neatly aligned dashboard page with a heading, titled chart, "
                    "card, and slicer.",
                    [],
                ),
                "why_en": "Nobody trusts a messy dashboard, even if the numbers are "
                "right. Ten minutes of tidying is the difference between \"looks "
                "amateur\" and \"looks like the person knows what they're doing.\"",
                "why_id": "Nggak ada yang percaya dashboard berantakan, walau angkanya "
                "benar. Sepuluh menit merapikan adalah beda antara \"kelihatan amatir\" "
                "dan \"kelihatan seperti orang yang tahu apa yang dikerjakan.\"",
                "mistakes": [
                    {
                        "title_en": "Over-decorating with colours and borders",
                        "title_id": "Menghias berlebihan dengan warna dan garis",
                        "text_en": "Restraint reads as professional. A title and clean "
                        "alignment beat rainbow colours every time.",
                        "text_id": "Menahan diri terbaca profesional. Judul dan "
                        "kerapian mengalahkan warna pelangi setiap saat.",
                    },
                    {
                        "title_en": "Leaving the default \"Amount by Product Name\" title",
                        "title_id": "Membiarkan judul bawaan \"Amount by Product Name\"",
                        "text_en": "The auto title is a placeholder. A plain-English "
                        "title tells the reader what they're looking at.",
                        "text_id": "Judul otomatis itu cuma placeholder. Judul "
                        "berbahasa manusia memberi tahu pembaca apa yang mereka lihat.",
                    },
                ],
            },
        ],
    },
    # =====================================================================
    # MODULE 5
    # =====================================================================
    {
        "n": 5,
        "title": "First measures",
        "summary_en": "Go beyond dragging fields. Write your first tiny formula to "
        "calculate totals, counts, and averages on demand.",
        "summary_id": "Melangkah lebih dari sekadar menyeret field. Tulis formula "
        "kecil pertamamu untuk menghitung total, jumlah, dan rata-rata sesuai "
        "kebutuhan.",
        "lessons": [
            {
                "slug": "columns-vs-measures",
                "title": "Columns vs measures",
                "minutes": 9,
                "difficulty": "Medium",
                "need_first_en": "Module 4 finished.",
                "need_first_id": "Modul 4 sudah selesai.",
                "outcome_en": "explain the difference between a column and a measure "
                "in one sentence each.",
                "outcome_id": "menjelaskan beda column dan measure masing-masing dalam "
                "satu kalimat.",
                "dataset": None,
                "intro_en": "So far you've dragged columns. Now meet the "
                "<span class='term' title='A saved calculation, written once, that "
                "recomputes itself for whatever is on screen'>measure</span> — a saved "
                "calculation. Knowing when to use which is a real turning point.",
                "intro_id": "Sejauh ini kamu menyeret column. Sekarang kenalan sama "
                "measure — sebuah perhitungan tersimpan. Tahu kapan pakai yang mana "
                "adalah titik balik yang nyata.",
                "steps": [
                    {
                        "instruction_en": "A <strong>column</strong> is a value that "
                        "exists on every row — like Price on each sale. It's stored, "
                        "row by row.",
                        "instruction_id": "Sebuah <strong>column</strong> adalah nilai "
                        "yang ada di tiap baris — seperti Price di tiap penjualan. Dia "
                        "tersimpan, baris demi baris.",
                        "menu_path": None,
                        "image": None,
                    },
                    {
                        "instruction_en": "A <strong>measure</strong> is a calculation "
                        "done on demand — like Total Sales, which adds every Amount "
                        "and changes when you filter.",
                        "instruction_id": "Sebuah <strong>measure</strong> adalah "
                        "perhitungan yang dilakukan saat dibutuhkan — seperti Total "
                        "Sales, yang menjumlah tiap Amount dan berubah saat kamu "
                        "memfilter.",
                        "menu_path": None,
                        "image": fig(
                            "/assets/img/measure-vs-column.svg",
                            "A split diagram: on the left a column with a value on "
                            "each row; on the right a measure showing a single "
                            "calculated total that recomputes when filtered.",
                            [
                                m(1, 25, 45, "Column: one value per row, stored",
                                  "Column: satu nilai per baris, tersimpan"),
                                m(2, 75, 45, "Measure: calculated on demand",
                                  "Measure: dihitung saat dibutuhkan"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "Rule of thumb: if you want to slice, group, "
                        "or filter by it, it's a column. If you want to add, count, or "
                        "average it, it's a measure.",
                        "instruction_id": "Patokan: kalau kamu mau mengiris, "
                        "mengelompokkan, atau memfilter berdasarkan itu, dia column. "
                        "Kalau kamu mau menjumlah, menghitung, atau merata-rata, dia "
                        "measure.",
                        "menu_path": None,
                        "image": None,
                    },
                ],
                "checkpoint_en": "You can say: \"A column is a value on every row; a "
                "measure is a calculation that runs when I look at it.\"",
                "checkpoint_id": "Kamu bisa bilang: \"Column adalah nilai di tiap "
                "baris; measure adalah perhitungan yang jalan saat aku melihatnya.\"",
                "checkpoint_image": fig(
                    "/assets/img/cp-col-vs-measure.svg",
                    "A summary card contrasting a stored column with an on-demand "
                    "measure.",
                    [],
                ),
                "why_en": "Mixing these up is the single biggest beginner stumble in "
                "Power BI. Getting the distinction now saves you from measures that "
                "won't calculate and columns that won't filter.",
                "why_id": "Mencampur keduanya adalah sandungan pemula terbesar di "
                "Power BI. Paham bedanya sekarang menyelamatkan kamu dari measure yang "
                "nggak mau menghitung dan column yang nggak mau memfilter.",
                "mistakes": [
                    {
                        "title_en": "Trying to filter a slicer by a measure",
                        "title_id": "Mencoba memfilter slicer dengan measure",
                        "text_en": "Slicers need columns, not measures. If a field "
                        "won't go in a slicer, it's probably a measure.",
                        "text_id": "Slicer butuh column, bukan measure. Kalau sebuah "
                        "field nggak mau masuk slicer, kemungkinan dia measure.",
                    },
                    {
                        "title_en": "Making a column when you needed a measure",
                        "title_id": "Membuat column padahal butuh measure",
                        "text_en": "A column can't respond to filters the way a "
                        "measure does. For totals, always reach for a measure.",
                        "text_id": "Column nggak bisa merespons filter seperti "
                        "measure. Untuk total, selalu pakai measure.",
                    },
                ],
            },
            {
                "slug": "your-first-measure",
                "title": "Your first measure",
                "minutes": 13,
                "difficulty": "Medium",
                "need_first_en": "Sales table loaded.",
                "need_first_id": "Tabel Sales sudah dimuat.",
                "outcome_en": "write a Total Sales measure using SUM and show it on a "
                "card.",
                "outcome_id": "menulis measure Total Sales pakai SUM dan "
                "menampilkannya di card.",
                "dataset": {
                    "name": "Sales and products",
                    "file": "sales-and-products.zip",
                    "desc_en": "The linked tables you already know.",
                    "desc_id": "Tabel terhubung yang sudah kamu kenal.",
                },
                "intro_en": "Time to write actual "
                "<span class='term' title='The small formula language used to write "
                "measures in Power BI. Stands for Data Analysis Expressions'>DAX</span> "
                "— Power BI's formula language. Your first one is three words long. "
                "Don't be scared.",
                "intro_id": "Saatnya menulis DAX beneran — bahasa formula Power BI. "
                "Yang pertama cuma tiga kata. Jangan takut.",
                "steps": [
                    {
                        "instruction_en": "In the Fields pane, right-click the "
                        "<strong>Sales</strong> table and choose <strong>New "
                        "measure</strong>.",
                        "instruction_id": "Di panel Fields, klik kanan tabel "
                        "<strong>Sales</strong> dan pilih <strong>New measure</strong>.",
                        "menu_path": "Right-click Sales table ▸ New measure",
                        "image": fig(
                            "/assets/img/new-measure.svg",
                            "The Fields pane right-click menu on the Sales table with "
                            "New measure highlighted.",
                            [
                                m(1, 45, 40, "Right-click the Sales table",
                                  "Klik kanan tabel Sales"),
                                m(2, 60, 60, "Choose New measure",
                                  "Pilih New measure"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "A formula bar appears at the top. Type "
                        "exactly: <code>Total Sales = SUM(Sales[Amount])</code>",
                        "instruction_id": "Formula bar muncul di atas. Ketik persis: "
                        "<code>Total Sales = SUM(Sales[Amount])</code>",
                        "menu_path": None,
                        "image": fig(
                            "/assets/img/measure-formula.svg",
                            "The DAX formula bar showing Total Sales = SUM(Sales[Amount]) "
                            "being typed.",
                            [
                                m(1, 45, 35, "The formula bar",
                                  "Formula bar"),
                                m(2, 40, 55, "Type the measure here",
                                  "Ketik measure di sini"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "As you type <code>Sales[</code>, a "
                        "suggestion list pops up. Pick <strong>Amount</strong> from it "
                        "rather than typing the whole thing. Press Enter to finish.",
                        "instruction_id": "Saat kamu mengetik <code>Sales[</code>, "
                        "daftar saran muncul. Pilih <strong>Amount</strong> dari situ "
                        "daripada mengetik semuanya. Tekan Enter untuk menyelesaikan.",
                        "menu_path": None,
                        "image": None,
                    },
                    {
                        "instruction_en": "Total Sales now appears in the Fields pane "
                        "with a little calculator icon. Add a Card visual and tick "
                        "Total Sales to see it.",
                        "instruction_id": "Total Sales sekarang muncul di panel Fields "
                        "dengan ikon kalkulator kecil. Tambah visual Card dan centang "
                        "Total Sales untuk melihatnya.",
                        "menu_path": None,
                        "image": None,
                    },
                ],
                "checkpoint_en": "Total Sales sits in the Fields pane with a "
                "calculator icon, and a card shows the summed total. Add a product "
                "slicer and the total reacts.",
                "checkpoint_id": "Total Sales ada di panel Fields dengan ikon "
                "kalkulator, dan card menampilkan total yang dijumlah. Tambah slicer "
                "produk dan totalnya bereaksi.",
                "checkpoint_image": fig(
                    "/assets/img/cp-measure-card.svg",
                    "A card showing the Total Sales measure result, with the measure "
                    "visible in the Fields pane.",
                    [],
                ),
                "why_en": "SUM is the measure you'll write more than any other. Once "
                "you've written one measure, every other DAX formula is just a "
                "variation on the same shape.",
                "why_id": "SUM adalah measure yang paling sering kamu tulis. Begitu "
                "kamu menulis satu measure, tiap formula DAX lain cuma variasi dari "
                "bentuk yang sama.",
                "mistakes": [
                    {
                        "title_en": "Typing the column name instead of picking it",
                        "title_id": "Mengetik nama kolom alih-alih memilihnya",
                        "text_en": "One typo and the measure errors. Always choose "
                        "from the suggestion list so the name is exact.",
                        "text_id": "Satu typo dan measure-nya error. Selalu pilih dari "
                        "daftar saran supaya namanya persis.",
                    },
                    {
                        "title_en": "Confusing New measure with New column",
                        "title_id": "Bingung antara New measure dan New column",
                        "text_en": "They sit next to each other in the menu. For "
                        "totals you want New measure, every time.",
                        "text_id": "Keduanya bersebelahan di menu. Untuk total kamu "
                        "mau New measure, tiap saat.",
                    },
                ],
            },
            {
                "slug": "useful-measures",
                "title": "Count and average",
                "minutes": 12,
                "difficulty": "Medium",
                "need_first_en": "Total Sales measure written.",
                "need_first_id": "Measure Total Sales sudah ditulis.",
                "outcome_en": "write a count of orders and an average sale using the "
                "same pattern.",
                "outcome_id": "menulis jumlah order dan rata-rata penjualan pakai pola "
                "yang sama.",
                "dataset": {
                    "name": "Sales and products",
                    "file": "sales-and-products.zip",
                    "desc_en": "Continue in the same file.",
                    "desc_id": "Lanjut di file yang sama.",
                },
                "intro_en": "You know the shape now: <code>Name = FUNCTION(Table"
                "[Column])</code>. Swap SUM for COUNT or AVERAGE and you have two more "
                "measures in minutes.",
                "intro_id": "Kamu sudah tahu bentuknya: <code>Name = FUNCTION(Table"
                "[Column])</code>. Ganti SUM dengan COUNT atau AVERAGE dan kamu punya "
                "dua measure lagi dalam hitungan menit.",
                "steps": [
                    {
                        "instruction_en": "New measure again (right-click Sales ▸ New "
                        "measure). Type: <code>Order Count = COUNT(Sales[Order ID])"
                        "</code>",
                        "instruction_id": "New measure lagi (klik kanan Sales ▸ New "
                        "measure). Ketik: <code>Order Count = COUNT(Sales[Order ID])"
                        "</code>",
                        "menu_path": "Right-click Sales ▸ New measure",
                        "image": None,
                    },
                    {
                        "instruction_en": "One more. New measure, then: "
                        "<code>Average Sale = AVERAGE(Sales[Amount])</code>",
                        "instruction_id": "Satu lagi. New measure, lalu: "
                        "<code>Average Sale = AVERAGE(Sales[Amount])</code>",
                        "menu_path": "Right-click Sales ▸ New measure",
                        "image": None,
                    },
                    {
                        "instruction_en": "Add three cards, one for each measure: "
                        "Total Sales, Order Count, Average Sale. Now you have a "
                        "headline row.",
                        "instruction_id": "Tambah tiga card, satu untuk tiap measure: "
                        "Total Sales, Order Count, Average Sale. Sekarang kamu punya "
                        "baris angka utama.",
                        "menu_path": None,
                        "image": fig(
                            "/assets/img/three-cards.svg",
                            "Three cards in a row showing Total Sales, Order Count, and "
                            "Average Sale.",
                            [
                                m(1, 18, 40, "Total Sales card",
                                  "Card Total Sales"),
                                m(2, 50, 40, "Order Count card",
                                  "Card Order Count"),
                                m(3, 82, 40, "Average Sale card",
                                  "Card Average Sale"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "Click a product in your slicer and watch "
                        "all three cards recalculate at once. That's the power of "
                        "measures.",
                        "instruction_id": "Klik satu produk di slicer-mu dan lihat "
                        "ketiga card menghitung ulang sekaligus. Itulah kekuatan "
                        "measure.",
                        "menu_path": None,
                        "image": None,
                    },
                ],
                "checkpoint_en": "Three cards show a total, a count, and an average. "
                "Filtering with the slicer updates all three together.",
                "checkpoint_id": "Tiga card menampilkan total, jumlah, dan rata-rata. "
                "Memfilter dengan slicer memperbarui ketiganya bersamaan.",
                "checkpoint_image": fig(
                    "/assets/img/cp-headline-row.svg",
                    "A headline row of three measure cards above a bar chart.",
                    [],
                ),
                "why_en": "SUM, COUNT, and AVERAGE cover most of what a beginner "
                "dashboard needs. With these three you can already answer \"how much, "
                "how many, and how big on average\" — the questions every manager "
                "asks.",
                "why_id": "SUM, COUNT, dan AVERAGE menutupi sebagian besar kebutuhan "
                "dashboard pemula. Dengan tiga ini kamu sudah bisa menjawab \"berapa "
                "banyak, berapa jumlahnya, dan rata-rata berapa\" — pertanyaan yang "
                "ditanyakan tiap manajer.",
                "mistakes": [
                    {
                        "title_en": "Using COUNT on a column with blanks",
                        "title_id": "Memakai COUNT pada kolom yang ada kosongnya",
                        "text_en": "COUNT skips blanks. Count an ID column that's "
                        "always filled so the number is honest.",
                        "text_id": "COUNT melewati yang kosong. Hitung kolom ID yang "
                        "selalu terisi supaya angkanya jujur.",
                    },
                    {
                        "title_en": "Averaging something that shouldn't be averaged",
                        "title_id": "Merata-rata sesuatu yang nggak seharusnya",
                        "text_en": "Average a value, not an ID. Averaging Order ID "
                        "gives a meaningless number.",
                        "text_id": "Rata-rata sebuah nilai, bukan ID. Merata-rata "
                        "Order ID memberi angka yang nggak bermakna.",
                    },
                ],
            },
        ],
    },
    # =====================================================================
    # MODULE 6
    # =====================================================================
    {
        "n": 6,
        "title": "Publish and share",
        "summary_en": "Get your finished dashboard off your laptop and in front of "
        "other people, safely.",
        "summary_id": "Bawa dashboard jadimu keluar dari laptop dan tampilkan ke "
        "orang lain, dengan aman.",
        "lessons": [
            {
                "slug": "sign-in-and-publish",
                "title": "Sign in and publish",
                "minutes": 12,
                "difficulty": "Medium",
                "need_first_en": "A finished report and a work or school Microsoft "
                "account.",
                "need_first_id": "Report jadi dan akun Microsoft kantor atau sekolah.",
                "outcome_en": "publish your report to the Power BI Service and open it "
                "in a browser.",
                "outcome_id": "mempublikasikan report-mu ke Power BI Service dan "
                "membukanya di browser.",
                "dataset": None,
                "intro_en": "Publishing sends a copy of your report to Microsoft's "
                "website so you can open it anywhere and share a link. You need a work "
                "or school account — a personal Gmail won't work for publishing.",
                "intro_id": "Publikasi mengirim salinan report-mu ke website Microsoft "
                "supaya kamu bisa membukanya di mana saja dan berbagi link. Kamu butuh "
                "akun kantor atau sekolah — Gmail pribadi nggak bisa buat publikasi.",
                "steps": [
                    {
                        "instruction_en": "First save your file: File ▸ Save, and give "
                        "it a name like <code>Coffee Dashboard</code>. Publishing "
                        "needs a saved file.",
                        "instruction_id": "Simpan dulu file-mu: File ▸ Save, dan beri "
                        "nama seperti <code>Coffee Dashboard</code>. Publikasi butuh "
                        "file yang tersimpan.",
                        "menu_path": "File ▸ Save",
                        "image": None,
                    },
                    {
                        "instruction_en": "Top-right of the window, click "
                        "<strong>Sign in</strong> and enter your work or school "
                        "account.",
                        "instruction_id": "Di kanan atas jendela, klik <strong>Sign "
                        "in</strong> dan masukkan akun kantor atau sekolahmu.",
                        "menu_path": "Top-right ▸ Sign in",
                        "image": fig(
                            "/assets/img/signin.svg",
                            "The top-right corner of Power BI Desktop showing the Sign "
                            "in link.",
                            [
                                m(1, 82, 30, "The Sign in link, top-right",
                                  "Link Sign in, kanan atas"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "On the Home tab, click "
                        "<strong>Publish</strong>. If asked where, choose "
                        "<strong>My workspace</strong>.",
                        "instruction_id": "Di tab Home, klik <strong>Publish</strong>. "
                        "Kalau ditanya ke mana, pilih <strong>My workspace</strong>.",
                        "menu_path": "Home ▸ Publish ▸ My workspace",
                        "image": fig(
                            "/assets/img/publish-button.svg",
                            "The Home ribbon with the Publish button highlighted at "
                            "the far right.",
                            [
                                m(1, 88, 25, "The Publish button",
                                  "Tombol Publish"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "When it finishes, a box shows a link like "
                        "\"Open Coffee Dashboard in Power BI\". Click it to see your "
                        "report live in the browser.",
                        "instruction_id": "Setelah selesai, kotak menampilkan link "
                        "seperti \"Open Coffee Dashboard in Power BI\". Klik untuk "
                        "melihat report-mu langsung di browser.",
                        "menu_path": None,
                        "image": None,
                    },
                ],
                "checkpoint_en": "Your report opens in a web browser at app.powerbi.com, "
                "looking just like it did on the Desktop.",
                "checkpoint_id": "Report-mu terbuka di browser web di app.powerbi.com, "
                "tampil persis seperti di Desktop.",
                "checkpoint_image": fig(
                    "/assets/img/cp-published.svg",
                    "The published report open in a web browser showing the same "
                    "dashboard.",
                    [],
                ),
                "why_en": "A report on your laptop helps nobody but you. Publishing is "
                "the step that turns your work into something a team can actually use. "
                "It's the whole point of the last five modules.",
                "why_id": "Report di laptop cuma membantu kamu sendiri. Publikasi "
                "adalah langkah yang mengubah kerjaanmu jadi sesuatu yang bisa dipakai "
                "tim. Itulah inti dari lima modul terakhir.",
                "mistakes": [
                    {
                        "title_en": "Trying to publish with a personal account",
                        "title_id": "Mencoba publikasi dengan akun pribadi",
                        "text_en": "Publishing needs a work or school account. If you "
                        "don't have one, you can still do everything up to this step.",
                        "text_id": "Publikasi butuh akun kantor atau sekolah. Kalau "
                        "kamu nggak punya, kamu tetap bisa melakukan semuanya sampai "
                        "langkah ini.",
                    },
                    {
                        "title_en": "Forgetting to save before publishing",
                        "title_id": "Lupa menyimpan sebelum publikasi",
                        "text_en": "Power BI will nag you to save first. Just do File "
                        "▸ Save and try Publish again.",
                        "text_id": "Power BI bakal mengingatkan kamu menyimpan dulu. "
                        "Cukup File ▸ Save dan coba Publish lagi.",
                    },
                ],
            },
            {
                "slug": "share-your-dashboard",
                "title": "Share your dashboard",
                "minutes": 10,
                "difficulty": "Easy",
                "need_first_en": "A published report in the Service.",
                "need_first_id": "Report sudah dipublikasi di Service.",
                "outcome_en": "send a colleague a link to your report and understand "
                "who can open it.",
                "outcome_id": "mengirim rekan kerja link ke report-mu dan paham siapa "
                "yang bisa membukanya.",
                "dataset": None,
                "intro_en": "Publishing put your report online. Sharing decides who's "
                "allowed to see it. We'll keep it simple and safe.",
                "intro_id": "Publikasi menaruh report-mu online. Sharing menentukan "
                "siapa yang boleh melihatnya. Kita bikin sederhana dan aman.",
                "steps": [
                    {
                        "instruction_en": "In the browser at app.powerbi.com, open "
                        "your report. Click the <strong>Share</strong> button near the "
                        "top right.",
                        "instruction_id": "Di browser di app.powerbi.com, buka "
                        "report-mu. Klik tombol <strong>Share</strong> di dekat kanan "
                        "atas.",
                        "menu_path": "app.powerbi.com ▸ open report ▸ Share",
                        "image": fig(
                            "/assets/img/share-button.svg",
                            "The Power BI Service toolbar with the Share button "
                            "highlighted near the top right.",
                            [
                                m(1, 80, 20, "The Share button",
                                  "Tombol Share"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "Type a colleague's work email. Leave the "
                        "default permission as view-only unless you truly want them to "
                        "edit.",
                        "instruction_id": "Ketik email kantor rekanmu. Biarkan izin "
                        "bawaan sebagai view-only kecuali kamu benar-benar ingin "
                        "mereka mengedit.",
                        "menu_path": None,
                        "image": None,
                    },
                    {
                        "instruction_en": "Click <strong>Send</strong>. They get an "
                        "email with a link. Only people you add can open it — it's not "
                        "public.",
                        "instruction_id": "Klik <strong>Send</strong>. Mereka menerima "
                        "email berisi link. Hanya orang yang kamu tambahkan yang bisa "
                        "membukanya — nggak publik.",
                        "menu_path": None,
                        "image": None,
                    },
                    {
                        "instruction_en": "Remember: sharing shows people the data too. "
                        "Only share reports whose numbers those people are allowed to "
                        "see.",
                        "instruction_id": "Ingat: sharing juga memperlihatkan datanya. "
                        "Hanya bagikan report yang angkanya boleh dilihat orang-orang "
                        "itu.",
                        "menu_path": None,
                        "image": None,
                    },
                ],
                "checkpoint_en": "A colleague receives a link, opens your report, and "
                "sees the same dashboard — read-only. You've shared safely.",
                "checkpoint_id": "Rekan kerja menerima link, membuka report-mu, dan "
                "melihat dashboard yang sama — read-only. Kamu sudah berbagi dengan "
                "aman.",
                "checkpoint_image": fig(
                    "/assets/img/cp-shared.svg",
                    "The Share dialog with a colleague's email entered and view-only "
                    "permission selected.",
                    [],
                ),
                "why_en": "Knowing that sharing exposes the underlying data is the one "
                "safety rule that keeps beginners out of trouble at work. Share the "
                "view, mind the data.",
                "why_id": "Tahu bahwa sharing membuka data di baliknya adalah satu "
                "aturan keamanan yang menjauhkan pemula dari masalah di kantor. "
                "Bagikan tampilannya, jaga datanya.",
                "mistakes": [
                    {
                        "title_en": "Granting edit access to everyone",
                        "title_id": "Memberi akses edit ke semua orang",
                        "text_en": "View-only is the safe default. Only give edit to "
                        "people who genuinely build the report with you.",
                        "text_id": "View-only adalah default yang aman. Beri edit "
                        "cuma ke orang yang benar-benar membangun report bareng kamu.",
                    },
                    {
                        "title_en": "Sharing sensitive numbers by accident",
                        "title_id": "Berbagi angka sensitif nggak sengaja",
                        "text_en": "Before you hit Send, ask: is this person allowed "
                        "to see these numbers? If unsure, don't share yet.",
                        "text_id": "Sebelum menekan Send, tanya: apakah orang ini "
                        "boleh melihat angka ini? Kalau ragu, jangan bagikan dulu.",
                    },
                ],
            },
        ],
    },
    # =====================================================================
    # MODULE 7
    # =====================================================================
    {
        "n": 7,
        "title": "Capstone",
        "summary_en": "Put all eight modules together and build one complete "
        "dashboard from a blank screen, on your own.",
        "summary_id": "Gabungkan kedelapan modul dan bangun satu dashboard lengkap "
        "dari layar kosong, sendirian.",
        "lessons": [
            {
                "slug": "build-the-dashboard",
                "title": "Build the capstone dashboard",
                "minutes": 40,
                "difficulty": "Medium",
                "need_first_en": "Modules 0 through 6 finished.",
                "need_first_id": "Modul 0 sampai 6 sudah selesai.",
                "outcome_en": "build a complete sales dashboard from a fresh file "
                "without step-by-step hand-holding.",
                "outcome_id": "membangun dashboard penjualan lengkap dari file baru "
                "tanpa dituntun langkah demi langkah.",
                "dataset": {
                    "name": "Capstone superstore",
                    "file": "capstone-superstore.zip",
                    "desc_en": "A fresh set of sales and product files to prove you "
                    "can do it alone.",
                    "desc_id": "Set file penjualan dan produk baru untuk membuktikan "
                    "kamu bisa sendiri.",
                },
                "intro_en": "No new skills here — just all your old ones in a row. "
                "Each step names the module it came from. Peek back whenever you need "
                "to. Take your time.",
                "intro_id": "Nggak ada skill baru di sini — cuma semua skill lamamu "
                "berurutan. Tiap langkah menyebut modul asalnya. Lihat lagi kapan pun "
                "kamu butuh. Santai saja.",
                "steps": [
                    {
                        "instruction_en": "Start fresh: File ▸ New. Then Get data ▸ "
                        "Text/CSV and load both capstone files. "
                        "<em>(Module 1)</em>",
                        "instruction_id": "Mulai dari awal: File ▸ New. Lalu Get data "
                        "▸ Text/CSV dan muat kedua file capstone. <em>(Modul 1)</em>",
                        "menu_path": "File ▸ New · Home ▸ Get data ▸ Text/CSV",
                        "image": None,
                    },
                    {
                        "instruction_en": "Open Power Query. Remove blank rows, fix any "
                        "text-that-should-be-number columns, then Close & Apply. "
                        "<em>(Module 2)</em>",
                        "instruction_id": "Buka Power Query. Hapus baris kosong, "
                        "perbaiki kolom teks-yang-harusnya-angka, lalu Close & Apply. "
                        "<em>(Modul 2)</em>",
                        "menu_path": "Home ▸ Transform data ▸ Close & Apply",
                        "image": None,
                    },
                    {
                        "instruction_en": "In Model view, make sure a relationship "
                        "links the two tables on Product ID. Create it if it's "
                        "missing. <em>(Module 3)</em>",
                        "instruction_id": "Di Model view, pastikan relationship "
                        "menghubungkan kedua tabel lewat Product ID. Buat kalau belum "
                        "ada. <em>(Modul 3)</em>",
                        "menu_path": "Left edge ▸ Model view",
                        "image": None,
                    },
                    {
                        "instruction_en": "Write three measures: Total Sales (SUM), "
                        "Order Count (COUNT), Average Sale (AVERAGE). "
                        "<em>(Module 5)</em>",
                        "instruction_id": "Tulis tiga measure: Total Sales (SUM), "
                        "Order Count (COUNT), Average Sale (AVERAGE). <em>(Modul 5)</em>",
                        "menu_path": "Right-click table ▸ New measure",
                        "image": None,
                    },
                    {
                        "instruction_en": "In Report view, build: three measure cards "
                        "across the top, one bar chart of sales by product, and one "
                        "product slicer. <em>(Module 4)</em>",
                        "instruction_id": "Di Report view, bangun: tiga measure card "
                        "di atas, satu bar chart penjualan per produk, dan satu slicer "
                        "produk. <em>(Modul 4)</em>",
                        "menu_path": None,
                        "image": fig(
                            "/assets/img/capstone-layout.svg",
                            "A target layout for the capstone: a heading, a row of "
                            "three cards, a bar chart, and a slicer arranged on one "
                            "page.",
                            [
                                m(1, 50, 15, "Page heading",
                                  "Judul halaman"),
                                m(2, 50, 32, "Three measure cards",
                                  "Tiga measure card"),
                                m(3, 65, 62, "Bar chart of sales by product",
                                  "Bar chart penjualan per produk"),
                                m(4, 18, 62, "Product slicer",
                                  "Slicer produk"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "Add a page heading, title your chart, and "
                        "line the visuals up neatly. <em>(Module 4)</em>",
                        "instruction_id": "Tambah judul halaman, beri judul grafikmu, "
                        "dan rapikan visualnya. <em>(Modul 4)</em>",
                        "menu_path": "Insert ▸ Text box",
                        "image": None,
                    },
                    {
                        "instruction_en": "Save the file, then Publish to My "
                        "workspace. <em>(Module 6)</em>",
                        "instruction_id": "Simpan file, lalu Publish ke My workspace. "
                        "<em>(Modul 6)</em>",
                        "menu_path": "File ▸ Save · Home ▸ Publish",
                        "image": None,
                    },
                ],
                "checkpoint_en": "You have a published, tidy dashboard: a heading, "
                "three working cards, a titled bar chart, and a slicer that filters "
                "the whole page — built by you, start to finish.",
                "checkpoint_id": "Kamu punya dashboard rapi yang sudah dipublikasi: "
                "judul, tiga card yang bekerja, bar chart berjudul, dan slicer yang "
                "memfilter seluruh halaman — dibuat olehmu, dari awal sampai akhir.",
                "checkpoint_image": fig(
                    "/assets/img/cp-capstone-done.svg",
                    "The finished capstone dashboard with heading, cards, bar chart, "
                    "and slicer, published in the browser.",
                    [],
                ),
                "why_en": "This is what a first day on the job looks like: a blank "
                "file, some data, and a dashboard by the afternoon. If you built this, "
                "you can do the real thing.",
                "why_id": "Beginilah rupa hari pertama kerja: file kosong, sedikit "
                "data, dan dashboard sebelum sore. Kalau kamu membangun ini, kamu bisa "
                "melakukan yang sesungguhnya.",
                "mistakes": [
                    {
                        "title_en": "Skipping the cleaning step because you're excited",
                        "title_id": "Melewati langkah pembersihan karena nggak sabar",
                        "text_en": "Rushing past Power Query is how totals come out "
                        "wrong. Clean first, chart second — every time.",
                        "text_id": "Terburu-buru melewati Power Query bikin total "
                        "keluar salah. Bersihkan dulu, grafik kemudian — tiap saat.",
                    },
                    {
                        "title_en": "Forgetting to check the relationship",
                        "title_id": "Lupa mengecek relationship",
                        "text_en": "If your chart shows the same number for every "
                        "product, the relationship is probably missing. Check Model "
                        "view.",
                        "text_id": "Kalau grafikmu menampilkan angka yang sama untuk "
                        "tiap produk, relationship-nya kemungkinan hilang. Cek Model "
                        "view.",
                    },
                ],
            },
            {
                "slug": "checklist-and-next-steps",
                "title": "Final checklist and where to go next",
                "minutes": 8,
                "difficulty": "Easy",
                "need_first_en": "Capstone dashboard built and published.",
                "need_first_id": "Dashboard capstone sudah dibangun dan dipublikasi.",
                "outcome_en": "check your dashboard against a quality list and know "
                "your three next steps.",
                "outcome_id": "memeriksa dashboard-mu dengan daftar kualitas dan tahu "
                "tiga langkah berikutnya.",
                "dataset": None,
                "intro_en": "You did it — never-opened-it to published dashboard. "
                "Let's run a final quality check and point you at what to learn next, "
                "when you're ready.",
                "intro_id": "Kamu berhasil — dari belum pernah buka sampai dashboard "
                "terpublikasi. Ayo lakukan pengecekan kualitas terakhir dan tunjuk "
                "apa yang dipelajari berikutnya, saat kamu siap.",
                "steps": [
                    {
                        "instruction_en": "Data check: no blank rows, every number "
                        "column is a real number, every date is a real date. "
                        "<em>(Module 2)</em>",
                        "instruction_id": "Cek data: nggak ada baris kosong, tiap "
                        "kolom angka benar-benar angka, tiap tanggal benar-benar "
                        "tanggal. <em>(Modul 2)</em>",
                        "menu_path": None,
                        "image": None,
                    },
                    {
                        "instruction_en": "Model check: your tables are joined on "
                        "Product ID with a 1-to-many line. <em>(Module 3)</em>",
                        "instruction_id": "Cek model: tabelmu tergabung lewat Product "
                        "ID dengan garis 1-to-many. <em>(Modul 3)</em>",
                        "menu_path": None,
                        "image": None,
                    },
                    {
                        "instruction_en": "Visual check: every chart has a plain "
                        "title, the slicer filters everything, nothing overlaps. "
                        "<em>(Module 4)</em>",
                        "instruction_id": "Cek visual: tiap grafik punya judul jelas, "
                        "slicer memfilter semuanya, nggak ada yang menumpuk. "
                        "<em>(Modul 4)</em>",
                        "menu_path": None,
                        "image": fig(
                            "/assets/img/checklist.svg",
                            "A checklist graphic with data, model, and visual items "
                            "ticked off.",
                            [
                                m(1, 20, 30, "Data is clean",
                                  "Data bersih"),
                                m(2, 20, 50, "Model is linked",
                                  "Model terhubung"),
                                m(3, 20, 70, "Visuals are tidy",
                                  "Visual rapi"),
                            ],
                        ),
                    },
                    {
                        "instruction_en": "Three next steps when you want more: learn "
                        "more DAX functions, try a date/calendar table, and explore "
                        "more chart types. But rest first — you earned it.",
                        "instruction_id": "Tiga langkah berikutnya saat kamu mau lebih: "
                        "pelajari lebih banyak fungsi DAX, coba tabel tanggal/kalender, "
                        "dan jelajahi lebih banyak jenis grafik. Tapi istirahat dulu — "
                        "kamu pantas mendapatkannya.",
                        "menu_path": None,
                        "image": None,
                    },
                ],
                "checkpoint_en": "Every box on the quality checklist is ticked, and "
                "you know the three things to explore next. You are, officially, no "
                "longer a beginner.",
                "checkpoint_id": "Tiap kotak di daftar kualitas tercentang, dan kamu "
                "tahu tiga hal yang dijelajahi berikutnya. Kamu, secara resmi, bukan "
                "pemula lagi.",
                "checkpoint_image": fig(
                    "/assets/img/cp-finished.svg",
                    "A completion badge showing all eight modules finished.",
                    [],
                ),
                "why_en": "A checklist habit is what separates reports people trust "
                "from reports people quietly ignore. Run it every time, and your work "
                "will always look deliberate.",
                "why_id": "Kebiasaan memakai checklist adalah yang membedakan report "
                "yang dipercaya orang dari report yang diam-diam diabaikan. Lakukan "
                "tiap saat, dan kerjaanmu akan selalu terlihat matang.",
                "mistakes": [
                    {
                        "title_en": "Rushing to learn advanced DAX too soon",
                        "title_id": "Buru-buru belajar DAX lanjutan terlalu cepat",
                        "text_en": "Solidify SUM, COUNT, and AVERAGE first. Advanced "
                        "formulas make far more sense once the basics are automatic.",
                        "text_id": "Kuatkan SUM, COUNT, dan AVERAGE dulu. Formula "
                        "lanjutan jauh lebih masuk akal setelah dasarnya otomatis.",
                    },
                    {
                        "title_en": "Thinking you're done learning forever",
                        "title_id": "Mengira kamu selesai belajar selamanya",
                        "text_en": "You've got a strong base. Power BI is deep — but "
                        "you now have every foundation you need to keep going.",
                        "text_id": "Kamu punya dasar yang kuat. Power BI itu dalam — "
                        "tapi kamu sekarang punya semua fondasi untuk terus maju.",
                    },
                ],
            },
        ],
    },
]
