"""Keep the three photo strips responsive and ready before they start moving."""
import json
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent


def optimize_carousels(markup):
    entries = json.loads((ROOT / 'lib/carousel-images.json').read_text())
    lookup = {name: item for item in entries for name in (item['original'], Path(item['master']).name)}

    def strip(match):
        desktop = {'gallery-strip': 640, 'about-marquee': 498, 'training-scroll-inner': 534}[match[1]]
        sizes = f'(max-width:350px) 200px, (max-width:450px) 57vw, (max-width:767px) 256px, {desktop}px'

        def image(img):
            tag = img[0]
            source = re.search(r'\bsrc="([^"]+)"', tag)
            item = lookup.get(Path(unquote(source[1])).name) if source else None
            if not item:
                return tag
            # Only replace image attributes; preserve lightbox actions and alt text.
            for attr in ('src', 'srcset', 'sizes', 'width', 'height', 'loading', 'decoding', 'fetchpriority'):
                tag = re.sub(r'\s+' + attr + r'="[^"]*"', '', tag)
            srcset = ', '.join(f"{v['url']} {v['width']}w" for v in item['variants'])
            return tag[:-1] + f' src="{item["master"]}" srcset="{srcset}" sizes="{sizes}" width="{item["width"]}" height="{item["height"]}" loading="eager" fetchpriority="low" decoding="async">'

        return re.sub(r'<img\b[^>]*>', image, match[0])

    pattern = r'<div class="(gallery-strip|about-marquee|training-scroll-inner)">[\s\S]*?</div>'
    if not re.search(pattern, markup):
        return markup
    markup = re.sub(pattern, strip, markup)
    if '/Styles/carousel-images.css' not in markup:
        markup = markup.replace('</head>', '<link rel="stylesheet" href="/Styles/carousel-images.css?v=1">\n<script defer src="/Script/carousel-images.js?v=1"></script>\n</head>', 1)
    return markup
