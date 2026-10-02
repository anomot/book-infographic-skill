#!/usr/bin/env python3
"""Render 1080px-wide HTML infographics to 2x PNGs via Playwright.

Usage:
    python3 bin/render.py page1.html [page2.html ...] [--out png/]

Needs Playwright + Chromium. If Playwright is missing from the current
interpreter, this script re-execs into the workspace venv that has it.
"""
import os
import sys

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    venv_python = "/home/hatch/workspace/ai-booklist/venv/bin/python"
    if os.path.exists(venv_python) and os.path.abspath(sys.executable) != os.path.abspath(venv_python):
        os.execv(venv_python, [venv_python, os.path.abspath(__file__), *sys.argv[1:]])
    raise SystemExit(
        "Playwright is not installed. Install it (pip install playwright && "
        "python -m playwright install chromium) or run with the workspace venv."
    )

VIEWPORT_W = 1080
SCALE = 2


def main(argv):
    files = []
    out_dir = "png"
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--out" and i + 1 < len(argv):
            out_dir = argv[i + 1]
            i += 2
        elif a.startswith("--"):
            i += 1
        else:
            files.append(a)
            i += 1
    if not files:
        raise SystemExit("usage: render.py page1.html [page2.html ...] [--out png/]")
    os.makedirs(out_dir, exist_ok=True)
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch()
        except Exception:
            browser = p.chromium.launch(executable_path="/opt/meta-chromium/chrome")
        page = browser.new_page(
            viewport={"width": VIEWPORT_W, "height": 900},
            device_scale_factor=SCALE,
        )
        for f in files:
            page.goto("file://" + os.path.abspath(f))
            page.wait_for_timeout(1200)
            out = os.path.join(out_dir, os.path.splitext(os.path.basename(f))[0] + ".png")
            page.screenshot(path=out, full_page=True)
            print("rendered", out, os.path.getsize(out), "bytes")
        browser.close()
    print("ALL DONE")


if __name__ == "__main__":
    main(sys.argv[1:])
