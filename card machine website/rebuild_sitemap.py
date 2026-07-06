"""Rebuild sitemap.xml from all HTML files in the directory."""
import os, glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://www.paymentcardservices.co.uk"

# Manual priority map — slug prefix -> priority
def priority(slug):
    if slug == "/": return "1.0"
    if slug.startswith("free-card-machine-for-") and "-in-" in slug: return "0.75"
    if slug.startswith("free-card-machine-"): return "0.90"
    if slug.startswith("card-machine-for-"): return "0.85"
    if slug.startswith("dojo-vs-"): return "0.85"
    if slug in ("how-much-does-a-card-machine-cost","best-card-machine-for-small-business","do-i-need-a-card-machine","card-machine-transaction-fees-explained"): return "0.80"
    if slug == "industries": return "0.80"
    return "0.70"

lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">', '']
lines.append('  <!-- Homepage -->')
lines.append(f'  <url><loc>{DOMAIN}/</loc><lastmod>2026-07-06</lastmod><changefreq>monthly</changefreq><priority>1.0</priority></url>')
lines.append('')

# Collect all HTML files
html_files = sorted(glob.glob(os.path.join(BASE_DIR, "*.html")))
slugs = []
for f in html_files:
    name = os.path.basename(f).replace(".html","")
    if name == "index": continue  # homepage handled above
    slugs.append(name)

# Group by type
city_pages = [s for s in slugs if s.startswith("free-card-machine-") and not s.startswith("free-card-machine-for-")]
industry_pages = [s for s in slugs if s.startswith("card-machine-for-")]
combo_pages = [s for s in slugs if s.startswith("free-card-machine-for-")]
comparison_pages = [s for s in slugs if s.startswith("dojo-vs-")]
blog_pages = [s for s in slugs if s in ("how-much-does-a-card-machine-cost","best-card-machine-for-small-business","do-i-need-a-card-machine","card-machine-transaction-fees-explained")]
other_pages = [s for s in slugs if s not in city_pages+industry_pages+combo_pages+comparison_pages+blog_pages]

def add_section(label, page_list, lastmod="2026-07-06"):
    lines.append(f'  <!-- {label} -->')
    for s in sorted(page_list):
        p = priority(s)
        lines.append(f'  <url><loc>{DOMAIN}/{s}</loc><lastmod>{lastmod}</lastmod><changefreq>monthly</changefreq><priority>{p}</priority></url>')
    lines.append('')

add_section("City landing pages", city_pages)
add_section("Industry landing pages", industry_pages)
add_section("City x Industry combo pages", combo_pages)
add_section("Comparison pages", comparison_pages)
add_section("Blog and FAQ pages", blog_pages)
add_section("Other pages", other_pages)

lines.append('</urlset>')

out = "\n".join(lines)
with open(os.path.join(BASE_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(out)

total = len(city_pages)+len(industry_pages)+len(combo_pages)+len(comparison_pages)+len(blog_pages)+len(other_pages)+1
print(f"Sitemap rebuilt — {total} URLs total")
print(f"  City pages: {len(city_pages)}")
print(f"  Industry pages: {len(industry_pages)}")
print(f"  Combo pages: {len(combo_pages)}")
print(f"  Comparison pages: {len(comparison_pages)}")
print(f"  Blog pages: {len(blog_pages)}")
print(f"  Other: {len(other_pages)}")
