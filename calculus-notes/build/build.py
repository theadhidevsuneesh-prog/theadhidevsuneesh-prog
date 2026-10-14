#!/usr/bin/env python3
"""Build the notes PDF.

    python3 build.py                 # full build  -> ../Units_1-3_Calculus_Notes.pdf
    python3 build.py --src ../src    # explicit source dir
    python3 build.py --html-only     # stop after HTML (debug)

Pipeline: markdown --(pandoc + boxes.lua)--> HTML --(KaTeX)--> HTML --(Chromium)--> PDF.
The table of contents is built from the headings and its page numbers are filled in from a
first-pass PDF outline, then the PDF is rendered again.
"""
import argparse
import glob
import os
import re
import subprocess
import sys

from bs4 import BeautifulSoup

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
WORK = os.path.join(HERE, "_work")
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"


def run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        sys.stderr.write(r.stdout + r.stderr)
        raise SystemExit(f"command failed: {' '.join(cmd[:3])}")
    return r.stdout + r.stderr


def build_html(src_dir):
    os.makedirs(WORK, exist_ok=True)
    files = sorted(glob.glob(os.path.join(src_dir, "*.md")))
    if not files:
        raise SystemExit("no markdown files found")
    combined = os.path.join(WORK, "all.md")
    with open(combined, "w", encoding="utf-8") as out:
        for f in files:
            out.write(open(f, encoding="utf-8").read().rstrip() + "\n\n")
    tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read().replace("__ROOT__", ROOT)
    tpl_path = os.path.join(WORK, "template.html")
    open(tpl_path, "w", encoding="utf-8").write(tpl)
    raw = os.path.join(WORK, "raw.html")
    run(["pandoc", combined, "-f",
         "markdown+tex_math_dollars+fenced_divs+raw_html+smart+pipe_tables+header_attributes+implicit_figures+auto_identifiers",
         "-t", "html5", "--katex", "--lua-filter", os.path.join(HERE, "boxes.lua"), "--template", tpl_path,
         "--metadata", "title=Calculus and Linear Algebra Notes - Units I to III", "--no-highlight", "--wrap=none",
         "-o", raw])
    math = os.path.join(WORK, "math.html")
    print(run(["node", os.path.join(HERE, "render_math.js"), raw, math], cwd=HERE).strip())
    return math


def inject_toc(html_path, pages=None):
    soup = BeautifulSoup(open(html_path, encoding="utf-8").read(), "html.parser")
    slot = soup.find(id="toc-slot")
    heads = [h for h in soup.find_all(["h1", "h2"]) if not h.find_parent(class_="cover") and not h.find_parent(class_="toc")]
    if slot is not None:
        ul = soup.new_tag("ul")
        unit = "u0"
        for h in heads:
            level = 1 if h.name == "h1" else 2
            if level == 1:
                classes = h.get("class", [])
                unit = next((c for c in classes if re.fullmatch(r"u\d", c)), "u0")
            li = soup.new_tag("li")
            li["class"] = [f"l{level}", unit] + (["unit"] if "unit-opener" in h.get("class", []) else [])
            a = soup.new_tag("a", href="#" + h.get("id", ""))
            t = soup.new_tag("span", **{"class": "t"})
            t.string = re.sub(r"\s+", " ", h.get_text()).strip()
            d = soup.new_tag("span", **{"class": "dots"})
            p = soup.new_tag("span", **{"class": "pg"})
            p.string = str(pages.get(h.get("id"), "000")) if pages else "000"
            a.extend([t, d, p])
            li.append(a)
            ul.append(li)
        slot.clear()
        slot.append(ul)
        slot["class"] = ["toc"]
        title = soup.new_tag("h1", **{"class": "nobreak u0", "data-eyebrow": "Contents"})
        title.string = "Table of contents"
        slot.insert(0, title)
    out = html_path.replace("math.html", "final.html")
    open(out, "w", encoding="utf-8").write(str(soup))
    return out, [(h.get("id"), re.sub(r"\s+", " ", h.get_text()).strip(), h.name) for h in heads]


def all_headings(html_path):
    soup = BeautifulSoup(open(html_path, encoding="utf-8").read(), "html.parser")
    return [h for h in soup.find_all(re.compile(r"^h[1-6]$")) if not h.find_parent(class_="cover")]


def render_pdf(html_path, pdf_path):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME, args=["--no-sandbox", "--allow-file-access-from-files"])
        page = b.new_page()
        page.goto("file://" + html_path, wait_until="load")
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(600)
        kwargs = dict(path=pdf_path, prefer_css_page_size=True, print_background=True)
        try:
            page.pdf(outline=True, tagged=True, **kwargs)
        except TypeError:
            page.pdf(**kwargs)
        b.close()


def outline_pages(pdf_path):
    from pypdf import PdfReader
    r = PdfReader(pdf_path)
    flat = []

    def walk(items):
        for it in items:
            if isinstance(it, list):
                walk(it)
            else:
                flat.append((it.title, r.get_destination_page_number(it) + 1))
    walk(r.outline)
    return flat, len(r.pages)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=os.path.join(ROOT, "src"))
    ap.add_argument("--out", default=os.path.join(ROOT, "Units_1-3_Calculus_Notes.pdf"))
    ap.add_argument("--html-only", action="store_true")
    a = ap.parse_args()

    math_html = build_html(a.src)
    final, _ = inject_toc(math_html)
    if a.html_only:
        print("HTML at", final)
        return
    tmp_pdf = os.path.join(WORK, "pass1.pdf")
    render_pdf(final, tmp_pdf)
    flat, n = outline_pages(tmp_pdf)
    heads = all_headings(final)
    print(f"pass 1: {n} pages, {len(flat)} outline entries, {len(heads)} headings")
    pages = {}
    if len(flat) == len(heads):
        for h, (_, pg) in zip(heads, flat):
            pages[h.get("id")] = pg
    else:
        # fall back to title matching
        by_title = {}
        for t, pg in flat:
            by_title.setdefault(re.sub(r"\s+", " ", t).strip(), pg)
        for h in heads:
            t = re.sub(r"\s+", " ", h.get_text()).strip()
            if t in by_title:
                pages[h.get("id")] = by_title[t]
    final, _ = inject_toc(math_html, pages)
    render_pdf(final, a.out)
    flat2, n2 = outline_pages(a.out)
    print(f"final: {n2} pages -> {a.out}")
    if n2 != n:
        print("page count changed between passes; re-running once")
        pages = {h.get("id"): pg for h, (_, pg) in zip(all_headings(final), flat2)}
        final, _ = inject_toc(math_html, pages)
        render_pdf(final, a.out)


if __name__ == "__main__":
    main()
