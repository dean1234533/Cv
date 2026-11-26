#!/usr/bin/env python3
"""Audit public static pages, built tool pages and their sitemap; optionally check live URLs."""
import argparse
import json
import re
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
DOMAIN = 'https://dbworkouts.co.uk'


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.title = []
        self.h1 = []
        self.meta = defaultdict(list)
        self.canonical = []
        self.jsonld = []
        self.assets = []
        self.links = []
        self._capture = None
        self._text = ''
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ('title', 'h1'):
            self._capture, self._text = tag, ''
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self._capture, self._text = 'script', ''
        if tag == 'meta':
            key = attrs.get('name', attrs.get('property', '')).lower()
            self.meta[key].append(attrs.get('content', ''))
            if key in ('og:image', 'twitter:image'):
                self.assets.append(attrs.get('content', ''))
        if tag == 'link':
            rel = attrs.get('rel', '').split()
            if 'canonical' in rel:
                self.canonical.append(attrs.get('href', ''))
            if any(key in rel for key in ('icon', 'apple-touch-icon')):
                self.assets.append(attrs.get('href', ''))
        if tag == 'img':
            self.assets.append(attrs.get('src', ''))
            if not attrs.get('srcset', '').startswith('data:'):
                self.assets.extend(part.strip().split()[0] for part in attrs.get('srcset', '').split(',') if part.strip())
        if tag == 'a':
            self.links.append(attrs.get('href', ''))

    def handle_data(self, data):
        if self._capture:
            self._text += data

    def handle_endtag(self, tag):
        if tag == self._capture:
            value = ' '.join(self._text.split()) if tag != 'script' else self._text
            {'title': self.title, 'h1': self.h1, 'script': self.jsonld}[tag].append(value)
            self._capture = None


def objects(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from objects(child)
    elif isinstance(value, list):
        for child in value:
            yield from objects(child)


def audit(tools_dir, live=False):
    issues, notes, pages = [], [], []
    redirects = {}
    for line in (ROOT / '_redirects').read_text().splitlines():
        fields = line.split()
        if len(fields) == 3 and fields[2] in ('301', '302') and '*' not in fields[0]:
            redirects[fields[0]] = fields[1]

    def issue(kind, page, detail):
        issues.append({'kind': kind, 'page': page, 'detail': detail})

    def asset_exists(url):
        parsed = urlsplit(url)
        if not url or parsed.scheme == 'data' or (parsed.netloc and parsed.netloc != 'dbworkouts.co.uk'):
            return True
        path = unquote(parsed.path).lstrip('/')
        if path.startswith('tools/'):
            return (tools_dir / path.removeprefix('tools/')).is_file()
        return (ROOT / path).is_file()

    for file in sorted(ROOT.glob('*.html')):
        if file.name.startswith('._') or file.name in ('instagram-posts.html', 'online_video_modal.html'):
            continue
        url = DOMAIN + ('/' if file.stem == 'index' else '/' + file.stem)
        pages.append((file, url, Page(file.read_text())))
    built_tools = [file for file in sorted(tools_dir.glob('*.html')) if not file.name.startswith('._')]
    for file in built_tools:
        url = DOMAIN + '/tools' + ('' if file.stem == 'index' else '/' + file.stem)
        pages.append((file, url, Page(file.read_text())))
    if len(built_tools) != 12:
        issue('tool_build', 'tools', 'Expected 12 built HTML tool routes')

    indexable, titles, descriptions, schema_types = {}, defaultdict(list), defaultdict(list), Counter()
    for file, url, page in pages:
        noindex = any('noindex' in value.lower() for value in page.meta['robots'])
        redirected = urlsplit(url).path in redirects
        if noindex or redirected:
            notes.append({'page': url, 'indexing': 'redirect' if redirected else 'noindex'})
            continue
        indexable[url] = page
        for key, values in [('title', page.title), ('description', page.meta['description']), ('canonical', page.canonical), ('h1', page.h1)]:
            if len(values) != 1 or not values[0]:
                issue(key, url, f'Expected one nonempty {key}, got {len(values)}')
        if page.canonical != [url]:
            issue('canonical_target', url, page.canonical)
        if page.title:
            titles[page.title[0]].append(url)
        if page.meta['description']:
            descriptions[page.meta['description'][0]].append(url)
        for key in ('og:title', 'og:description', 'og:url', 'og:image', 'twitter:card'):
            if len(page.meta[key]) != 1 or not page.meta[key][0]:
                issue('social_metadata', url, key)
        if page.meta['og:url'] and page.meta['og:url'][0] != url:
            issue('social_url', url, page.meta['og:url'])
        for asset in page.assets:
            if not asset_exists(asset):
                issue('missing_asset', url, asset)
        for href in page.links:
            parsed = urlsplit(href)
            if parsed.scheme in ('mailto', 'tel', 'javascript') or (parsed.netloc and parsed.netloc != 'dbworkouts.co.uk'):
                continue
            path = unquote(parsed.path)
            if not path or path in redirects:
                continue
            if path == '/tools' or path.startswith('/tools/'):
                local = tools_dir / (path.removeprefix('/tools').strip('/') or 'index')
            else:
                local = ROOT / (path.lstrip('/') or 'index')
            if not local.suffix:
                local = local.with_suffix('.html')
            if not local.is_file():
                issue('broken_internal_link', url, href)
        parsed_schemas = []
        for raw in page.jsonld:
            try:
                schema = json.loads(raw)
            except json.JSONDecodeError as error:
                issue('invalid_jsonld', url, str(error))
                continue
            parsed_schemas.append(schema)
            for obj in objects(schema):
                types = obj.get('@type', [])
                types = types if isinstance(types, list) else [types]
                schema_types.update(types)
                for key in ('image', 'logo', 'contentUrl', 'thumbnailUrl'):
                    value = obj.get(key)
                    values = value if isinstance(value, list) else [value]
                    for asset in values:
                        if isinstance(asset, str) and not asset_exists(asset):
                            issue('missing_schema_asset', url, asset)
                if 'ImageObject' in types and isinstance(obj.get('url'), str) and not asset_exists(obj['url']):
                    issue('missing_schema_asset', url, obj['url'])
        if '/tools' in urlsplit(url).path:
            expected = 'CollectionPage' if url.endswith('/tools') else 'WebApplication'
            if not any(obj.get('@type') == expected for schema in parsed_schemas for obj in objects(schema)):
                issue('tool_schema', url, f'Missing static {expected}')

    for kind, groups in [('duplicate_title', titles), ('duplicate_description', descriptions)]:
        for value, urls in groups.items():
            if len(urls) > 1:
                issue(kind, urls, value)
    xml = ET.parse(ROOT / 'sitemap.xml')
    sitemap_urls = [node.text for node in xml.findall('.//{*}loc')]
    for url in set(indexable) - set(sitemap_urls):
        issue('missing_sitemap_url', url, 'Indexable page absent from sitemap')
    for url in set(sitemap_urls) - set(indexable):
        issue('unexpected_sitemap_url', url, 'Not an indexable public page in this build')
    for url, count in Counter(sitemap_urls).items():
        if count > 1:
            issue('duplicate_sitemap_url', url, count)
    for node in xml.findall('.//{*}lastmod'):
        if node.text[:10] > date.today().isoformat():
            issue('future_sitemap_date', 'sitemap.xml', node.text)
    robots = (ROOT / 'robots.txt').read_text()
    if f'Sitemap: {DOMAIN}/sitemap.xml' not in robots:
        issue('robots_sitemap', 'robots.txt', 'Missing canonical sitemap reference')

    live_results = []
    if live:
        def fetch(url):
            try:
                with urlopen(Request(url, headers={'User-Agent': "DBWorkouts-SEO-Audit/1.0"}), timeout=20) as response:
                    document = Page(response.read().decode('utf-8', 'replace'))
                    return {'url': url, 'status': response.status, 'final_url': response.url,
                            'canonical': document.canonical, 'title': document.title,
                            'noindex': any('noindex' in v.lower() for v in document.meta['robots']),
                            'x_robots_tag': response.headers.get('X-Robots-Tag', ''),
                            'h1_count': len(document.h1),
                            'jsonld_blocks': len(document.jsonld),
                            'local_title_matches': document.title == indexable[url].title}
            except Exception as error:
                return {'url': url, 'error': str(error)}
        with ThreadPoolExecutor(max_workers=4) as pool:
            live_results = list(pool.map(fetch, sorted(indexable)))
    return {
        'summary': {'checked_pages': len(pages), 'indexable_pages': len(indexable),
                    'excluded_pages': len(notes), 'sitemap_urls': len(sitemap_urls),
                    'issue_count': len(issues), 'schema_types': dict(schema_types)},
        'issues': issues, 'indexing_exclusions': notes, 'live_results': live_results,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--tools-dir', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--live', action='store_true')
    args = parser.parse_args()
    result = audit(args.tools_dir, args.live)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result['summary'], indent=2))
    if result['issues']:
        print(json.dumps(result['issues'], indent=2))
