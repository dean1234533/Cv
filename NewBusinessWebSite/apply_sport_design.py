#!/usr/bin/env python3
"""Apply the approved public-site design to static pages, including regenerated pages."""
from pathlib import Path
import re
import json
from urllib.parse import unquote, urlsplit
from html import unescape

ROOT = Path(__file__).resolve().parent
EXCLUDED = {'index.html', 'instagram-posts.html', 'online_video_modal.html'}
DIMENSIONS = json.loads((ROOT / 'lib/image-dimensions.json').read_text())
FONT = 'https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap'


def clean_arrows(markup):
    # Only alter markup; leave JavaScript operators and embedded data untouched.
    parts = re.split(r'(<script\b[^>]*>[\s\S]*?</script>|<style\b[^>]*>[\s\S]*?</style>)', markup, flags=re.I)
    for i in range(0, len(parts), 2):
        text = parts[i]
        # The logo is the home link; do not reintroduce visible breadcrumb trails.
        text = re.sub(r'\s*<(div|nav|ol)\b[^>]*class="[^"\n]*\bbreadcrumb[^"\n]*"[^>]*>[\s\S]*?</\1>', '', text, flags=re.I)
        text = re.sub(r'(<button\b[^>]*aria-label="([^"]+)"[^>]*>)\s*[←→↗↓↑]\s*(</button>)', lambda m: m[1] + ('Previous' if 'prev' in m[2].lower() else 'Next' if 'next' in m[2].lower() else m[2]) + m[3], text)
        text = re.sub(r'\s*<span\b[^>]*>\s*(?:[↗↘→←↓↑]|&(?:rarr|larr|nearr|darr);)\s*</span>', '', text)
        text = re.sub(r'\s*(?:[↗↘→←↓↑]|&(?:rarr|larr|nearr|darr);)(?=\s*</(?:a|button)>)', '', text)
        parts[i] = text
    return ''.join(parts)


def fix_image_dimensions(markup):
    def image_tag(match):
        tag = match[0]
        source = re.search(r'\bsrc=["\']([^"\']+)["\']', tag)
        width = re.search(r'\bwidth="(\d+)"', tag)
        height = re.search(r'\bheight="(\d+)"', tag)
        if not source or not width or not height:
            return tag
        url = urlsplit(unescape(source[1]))
        if url.scheme or url.netloc:
            return tag
        key = unquote(url.path).removeprefix('./').lstrip('/')
        size = DIMENSIONS.get(key)
        if not size or abs((int(width[1]) / int(height[1])) / (size[0] / size[1]) - 1) <= .01:
            return tag
        tag = re.sub(r'\bwidth="\d+"', f'width="{size[0]}"', tag, count=1)
        return re.sub(r'\bheight="\d+"', f'height="{size[1]}"', tag, count=1)
    return re.sub(r'<img\b[^>]*>', image_tag, markup, flags=re.I)



def label_comparison_tables(markup):
    def table(match):
        text = match[0]
        head = re.search(r'<thead\b[^>]*>([\s\S]*?)</thead>', text)
        if not head:
            return text
        labels = [unescape(re.sub(r'<[^>]+>', '', value)).strip() for value in re.findall(r'<th\b[^>]*>([\s\S]*?)</th>', head[1])]
        def row(match):
            index = -1
            def cell(match):
                nonlocal index
                index += 1
                tag = match[0]
                if index and index < len(labels) and 'data-label=' not in tag:
                    label = labels[index].replace('&', '&amp;').replace('"', '&quot;')
                    tag = tag[:-1] + f' data-label="{label}">'
                return tag
            return re.sub(r'<td\b[^>]*>', cell, match[0])
        text = re.sub(r'<tr\b[^>]*>[\s\S]*?</tr>', row, text)
        text = text.replace('class="compare-check"', 'class="compare-check" role="img" aria-label="Included"')
        text = text.replace('class="compare-cross"', 'class="compare-cross" role="img" aria-label="Not included"')
        # Keep this decorator idempotent.
        text = text.replace(' role="img" aria-label="Included" role="img" aria-label="Included"', ' role="img" aria-label="Included"')
        text = text.replace(' role="img" aria-label="Not included" role="img" aria-label="Not included"', ' role="img" aria-label="Not included"')
        return text
    return re.sub(r'<table\b[^>]*class="compare-table"[^>]*>[\s\S]*?</table>', table, markup)



def size_header_logo(markup):
    def header(match):
        tag = re.sub(r'\s(?:width|height)="[^"]*"', '', match[2])
        return match[1] + tag[:-1] + ' width="72" height="72">'
    markup = re.sub(r'(<a\b[^>]*class="primary-brand"[^>]*>\s*)(<img\b[^>]*>)', header, markup)
    def logo(match):
        tag = match[0]
        source = re.search(r'\bsrc="([^"]*)"', tag)
        if not source:
            return tag
        url = urlsplit(unescape(source[1]))
        key = unquote(url.path).removeprefix('./').lstrip('/')
        if url.scheme or url.netloc or key not in {
            'logo.png', 'logo-136.png', 'pics/optimized/logo-160.webp',
            'pics/optimized/logo-320.webp', 'pics/optimized/logo-3d-160.webp',
            'pics/optimized/logo-3d-320.webp', 'pics/optimized/logo-3d-matte-160.webp',
            'pics/optimized/logo-3d-matte-320.webp',
        }:
            return tag
        width = re.search(r'\bwidth="(\d+)"', tag)
        size = width[1] if width else '72'
        tag = tag[:source.start(1)] + '/pics/optimized/logo-3d-matte-160.webp' + tag[source.end(1):]
        tag = re.sub(r'\s(?:srcset|sizes)="[^"]*"', '', tag)
        return tag[:-1] + f' srcset="/pics/optimized/logo-3d-matte-160.webp 160w, /pics/optimized/logo-3d-matte-320.webp 320w" sizes="{size}px">'
    return re.sub(r'<img\b[^>]*>', logo, markup)


def apply_page(path):
    old = path.read_text()
    if '<head' not in old.lower() or '<body' not in old.lower():
        return False
    text = old
    page_class = 'sport-' + path.stem
    def body(match):
        tag = match[0]
        existing = re.search(r'\bclass="([^"]*)"', tag)
        classes = existing[1].split() if existing else []
        for name in ['sport-site', page_class]:
            if name not in classes:
                classes.append(name)
        value = 'class="' + ' '.join(classes) + '"'
        return tag[:existing.start()] + value + tag[existing.end():] if existing else tag[:-1] + ' ' + value + '>'
    text = re.sub(r'<body\b[^>]*>', body, text, count=1, flags=re.I)
    if 'id="sport-fonts"' not in text:
        text = re.sub(r'<link\b[^>]*href=["\']https://fonts\.googleapis\.com/css[^>]*>\s*', '', text)
        text = text.replace('</head>', f'<link id="sport-fonts" rel="stylesheet" href="{FONT}">\n<link id="sport-design" rel="stylesheet" href="/Styles/sport-system.css?v=30">\n</head>', 1)
    # Main-page headers each own their photograph; location templates keep theirs.
    main_header_images = {
        'active-living-3.html': (
            './pics/IMG_8096.JPG',
            '/pics/IMG_7865%203.jpg',
            'Outdoor fitness equipment beside the park tennis courts',
        ),
        'park-guide.html': (
            './pics/IMG_7933.jpg',
            '/pics/victoria-park-london.jpg',
            'Trees, grass and a fountain in Victoria Park, East London',
        ),
        'pair-personal-training-east-london.html': (
            '/pics/optimized/training-8096.webp',
            '/pics/IMG_7911_SnapseedCopy.jpg',
            'Clients training together on exercise mats in an East London park',
        ),
        'online-personal-training.html': (
            '/pics/optimized/dean-portrait.webp',
            '/pics/optimized/training-7883.webp',
            'DB’s Workouts clients practising core exercises on individual mats',
        ),
        'personal-training-for-beginners-east-london.html': (
            '/pics/optimized/training-7856.webp',
            '/pics/optimized/training-7859.webp',
            'Two clients stretching on exercise mats during a park training session',
        ),
        'mobile-personal-trainer-east-london.html': (
            '/pics/optimized/training-7856.webp',
            '/pics/IMG_7855%203.JPG',
            'A client doing a press-up beside portable dumbbells and a skipping rope',
        ),
        'personal-trainer-east-london-areas.html': (
            '/pics/optimized/training-7856.webp',
            '/pics/IMG_7861%203.jpg',
            'Outdoor fitness equipment at Stratford Park',
        ),
    }
    if path.name in main_header_images:
        previous, source, alt = main_header_images[path.name]
        def unique_header(match):
            tag = match[0].replace(previous, source)
            tag = re.sub(r'alt="[^"]*"', f'alt="{alt}"', tag)
            width, height = DIMENSIONS[unquote(source).lstrip('/')]
            tag = re.sub(r'\s(?:width|height)="[^"]*"', '', tag)
            return tag[:-1] + f' width="{width}" height="{height}">'
        def hero(match):
            image_source = r'(?:' + re.escape(previous) + '|' + re.escape(source) + ')'
            return re.sub(r'<img\b[^>]*src="' + image_source + r'"[^>]*>', unique_header, match[0], count=1)
        text = re.sub(r'<(?:section|header)\b[^>]*class="[^"\n]*(?:seo-hero|article-hero)[^"\n]*"[^>]*>[\s\S]*?</(?:section|header)>', hero, text, count=1)
    # Keep coach-biography photography consistent after regenerating online pages.
    def coach_portrait(match):
        return re.sub(r'<img\b[^>]*src="/pics/optimized/hero-dean.webp"[^>]*>', '<img src="/pics/optimized/dean-portrait.webp" alt="Dean Burt, your DB’s Workouts personal trainer" width="599" height="800" loading="lazy" decoding="async">', match[0], count=1)
    text = re.sub(r'<section class="seo-proof seo-section"[^>]*>[\s\S]*?</section>', coach_portrait, text)
    style_version = '26'
    text = re.sub(r'(/Styles/sport-system\.css\?v=)\d+', lambda m: m[1] + style_version, text)
    text = size_header_logo(label_comparison_tables(fix_image_dimensions(clean_arrows(text))))
    text = re.sub(r'(<a\b[^>]*class="mb-call"[^>]*>)[^<]*(</a>)', r'\1Call Dean\2', text)
    text = re.sub(r'(<a\b[^>]*class="mb-book"[^>]*>)[^<]*(</a>)', r'\1Book a call\2', text)

    if path.name == 'programs.html':
        # Show the page title before the legacy article-page navigation.
        text = re.sub(r'(<div class="content-container">)\s*(<nav aria-label="Page navigation example">[\s\S]*?</nav>)\s*(<h1\b[^>]*>[\s\S]*?</h1>)', r'\1\n\3\n\2', text, count=1)

    if path.name == 'about.html':
        # Keep first-screen proof values correct and stable from the first paint.
        text = re.sub(r"  var co=new IntersectionObserver[^\n]*\n\s*document\.querySelectorAll\('\[data-count\]'\)[^\n]*", '  // Stats display their final values immediately.', text, count=1)
        # Match the approved homepage gallery: landscape images only, including loop copies.
        text = re.sub(r'\s*<img[^>]+src="\./pics/IMG_8723\.JPG"[^>]*>', '', text)

    if text != old:
        path.write_text(text)
        return True
    return False


def main():
    pages = [p for p in sorted(ROOT.glob('*.html')) if p.name not in EXCLUDED]
    changed = sum(apply_page(p) for p in pages)
    print(f'Sports design: {len(pages)} inner pages covered; {changed} updated.')


if __name__ == '__main__':
    main()
