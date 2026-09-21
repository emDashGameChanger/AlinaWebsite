#!/usr/bin/env python3
"""Render summary-source.html to site-v2/downloads/alina-ren-docking-summary.pdf (Letter, must stay 1 page)."""
from pathlib import Path
from playwright.sync_api import sync_playwright

here = Path(__file__).resolve().parent
out = here.parents[1] / "site-v2" / "downloads" / "alina-ren-docking-summary.pdf"
out.parent.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto((here / "summary-source.html").as_uri())
    pg.wait_for_timeout(500)
    pg.pdf(path=str(out), format="Letter", prefer_css_page_size=True, print_background=True)
    b.close()
print("wrote", out)
