#!/usr/bin/env python3
"""
Enhanced SEO Files Generator for MindVerse Blog - Bilingual Edition
Generates comprehensive sitemap.xml, RSS feed, and robots.txt for both Turkish and English content
"""

import os
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
import glob
from pathlib import Path

class BilingualSEOGenerator:
    def __init__(self, base_url="https://www.mindversedaily.com"):
        self.base_url = base_url
        self.current_time = datetime.now(timezone.utc).isoformat()

    def get_all_pages(self):
        """Get comprehensive list of all pages for sitemap"""
        pages = []

        # Turkish Static pages
        turkish_static = [
            ('/', '1.0', 'daily'),
            ('/categories', '0.9', 'weekly'),
            ('/astrology', '0.9', 'daily'),
            ('/astrology/yukselen-burc', '0.8', 'monthly'),
            ('/astrology/sinastri', '0.8', 'monthly'),
            ('/contact', '0.7', 'monthly'),
            ('/faq', '0.6', 'monthly'),
            ('/privacy-policy', '0.5', 'yearly'),
            ('/terms', '0.5', 'yearly'),
            ('/popular', '0.8', 'weekly'),
            ('/search', '0.7', 'weekly'),
            ('/sitemap', '0.6', 'monthly'),
        ]

        # English Static pages
        english_static = [
            ('/en', '1.0', 'daily'),
            ('/en/categories', '0.9', 'weekly'),
            ('/en/astrology', '0.9', 'daily'),
            ('/en/astrology/birth-chart', '0.8', 'monthly'),
            ('/en/astrology/rising-sign', '0.8', 'monthly'),
            ('/en/astrology/synastry', '0.8', 'monthly'),
        ]

        # Add all static pages
        for path, priority, changefreq in turkish_static + english_static:
            pages.append({
                'loc': f"{self.base_url}{path}",
                'priority': priority,
                'changefreq': changefreq,
                'lastmod': self.current_time
            })

        # Content categories
        categories = ['health', 'love', 'history', 'psychology', 'space', 'quotes', 'astrology']

        # Turkish category pages
        for category in categories:
            pages.append({
                'loc': f"{self.base_url}/{category}",
                'priority': '0.8',
                'changefreq': 'weekly',
                'lastmod': self.current_time
            })

        # English category pages
        for category in categories:
            pages.append({
                'loc': f"{self.base_url}/en/{category}",
                'priority': '0.8',
                'changefreq': 'weekly',
                'lastmod': self.current_time
            })

        # English daily horoscope pages
        zodiac_signs = [
            'aries-daily', 'taurus-daily', 'gemini-daily', 'cancer-daily',
            'leo-daily', 'virgo-daily', 'libra-daily', 'scorpio-daily',
            'sagittarius-daily', 'capricorn-daily', 'aquarius-daily', 'pisces-daily'
        ]

        for sign in zodiac_signs:
            pages.append({
                'loc': f"{self.base_url}/en/astrology/{sign}",
                'priority': '0.9',
                'changefreq': 'daily',
                'lastmod': self.current_time
            })

        # Content files from markdown
        content_dir = Path('src/content')
        if content_dir.exists():
            for category in categories:
                category_dir = content_dir / category
                if category_dir.exists():
                    for md_file in category_dir.glob('*.md'):
                        slug = md_file.stem
                        priority = '0.8' if category == 'astrology' else '0.7'

                        # Turkish content
                        pages.append({
                            'loc': f"{self.base_url}/{category}/{slug}",
                            'priority': priority,
                            'changefreq': 'weekly',
                            'lastmod': self.current_time
                        })

                        # English content (auto-generated)
                        pages.append({
                            'loc': f"{self.base_url}/en/{category}/{slug}",
                            'priority': priority,
                            'changefreq': 'weekly',
                            'lastmod': self.current_time
                        })

        return pages

    def generate_sitemap(self):
        """Generate comprehensive sitemap.xml"""
        print("🗺️ Generating bilingual sitemap.xml...")

        # Create root element
        urlset = ET.Element('urlset')
        urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
        urlset.set('xmlns:xhtml', 'http://www.w3.org/1999/xhtml')

        # Get all pages
        pages = self.get_all_pages()

        # Add each page to sitemap
        for page in pages:
            url = ET.SubElement(urlset, 'url')

            loc = ET.SubElement(url, 'loc')
            loc.text = page['loc']

            lastmod = ET.SubElement(url, 'lastmod')
            lastmod.text = page['lastmod']

            changefreq = ET.SubElement(url, 'changefreq')
            changefreq.text = page['changefreq']

            priority = ET.SubElement(url, 'priority')
            priority.text = page['priority']

            # Add hreflang for bilingual content
            if '/en/' in page['loc']:
                # This is an English page, add Turkish alternative
                turkish_url = page['loc'].replace('/en/', '/')
                if not turkish_url.endswith('/'):
                    turkish_url = turkish_url.replace('/en', '')

                # Turkish alternative
                link_tr = ET.SubElement(url, 'xhtml:link')
                link_tr.set('rel', 'alternate')
                link_tr.set('hreflang', 'tr')
                link_tr.set('href', turkish_url)

                # English self-reference
                link_en = ET.SubElement(url, 'xhtml:link')
                link_en.set('rel', 'alternate')
                link_en.set('hreflang', 'en')
                link_en.set('href', page['loc'])

            elif page['loc'] != f"{self.base_url}/" and not any(static in page['loc'] for static in ['/contact', '/faq', '/privacy', '/terms', '/popular', '/search', '/sitemap']):
                # This is a Turkish content page, add English alternative
                english_url = page['loc'].replace(self.base_url, f"{self.base_url}/en")

                # Turkish self-reference
                link_tr = ET.SubElement(url, 'xhtml:link')
                link_tr.set('rel', 'alternate')
                link_tr.set('hreflang', 'tr')
                link_tr.set('href', page['loc'])

                # English alternative
                link_en = ET.SubElement(url, 'xhtml:link')
                link_en.set('rel', 'alternate')
                link_en.set('hreflang', 'en')
                link_en.set('href', english_url)

        # Create tree and write to file
        tree = ET.ElementTree(urlset)
        ET.indent(tree, space="  ", level=0)

        with open('public/sitemap.xml', 'wb') as f:
            tree.write(f, encoding='utf-8', xml_declaration=True)

        print(f"✅ Bilingual sitemap generated with {len(pages)} URLs")
        return len(pages)

    def generate_rss(self):
        """Generate RSS feed with bilingual content"""
        print("📡 Generating bilingual RSS feed...")

        # Create RSS root
        rss = ET.Element('rss')
        rss.set('version', '2.0')
        rss.set('xmlns:atom', 'http://www.w3.org/2005/Atom')

        channel = ET.SubElement(rss, 'channel')

        # Channel info
        title = ET.SubElement(channel, 'title')
        title.text = 'MindVerse Blog - Bilingual Astrology & Lifestyle'

        link = ET.SubElement(channel, 'link')
        link.text = self.base_url

        description = ET.SubElement(channel, 'description')
        description.text = 'Daily horoscopes, astrology insights, and lifestyle content in Turkish and English | Günlük burç yorumları, astroloji analizleri ve yaşam rehberleri'

        language = ET.SubElement(channel, 'language')
        language.text = 'tr-TR'

        pub_date = ET.SubElement(channel, 'pubDate')
        pub_date.text = datetime.now().strftime('%a, %d %b %Y %H:%M:%S %z')

        # Atom self link
        atom_link = ET.SubElement(channel, 'atom:link')
        atom_link.set('href', f'{self.base_url}/rss.xml')
        atom_link.set('rel', 'self')
        atom_link.set('type', 'application/rss+xml')

        # Add featured content
        featured_items = [
            {
                'title': 'Daily Horoscopes - English | Günlük Burç Yorumları',
                'link': f'{self.base_url}/en/astrology',
                'description': 'Get your daily horoscope in English with detailed insights for all zodiac signs.',
                'category': 'astrology'
            },
            {
                'title': 'Rising Sign Calculator | Yükselen Burç Hesaplayıcısı',
                'link': f'{self.base_url}/en/astrology/rising-sign',
                'description': 'Calculate your rising sign and discover its influence on your personality.',
                'category': 'astrology'
            },
            {
                'title': 'Birth Chart Analysis | Doğum Haritası Analizi',
                'link': f'{self.base_url}/en/astrology/birth-chart',
                'description': 'Professional birth chart analysis with planetary positions and interpretations.',
                'category': 'astrology'
            },
            {
                'title': 'Synastry Analysis | Sinastri Analizi',
                'link': f'{self.base_url}/en/astrology/synastry',
                'description': 'Discover relationship compatibility through synastry analysis.',
                'category': 'astrology'
            }
        ]

        for item_data in featured_items:
            item = ET.SubElement(channel, 'item')

            item_title = ET.SubElement(item, 'title')
            item_title.text = item_data['title']

            item_link = ET.SubElement(item, 'link')
            item_link.text = item_data['link']

            item_description = ET.SubElement(item, 'description')
            item_description.text = item_data['description']

            item_category = ET.SubElement(item, 'category')
            item_category.text = item_data['category']

            item_pub_date = ET.SubElement(item, 'pubDate')
            item_pub_date.text = datetime.now().strftime('%a, %d %b %Y %H:%M:%S %z')

            item_guid = ET.SubElement(item, 'guid')
            item_guid.text = item_data['link']
            item_guid.set('isPermaLink', 'true')

        # Write RSS file
        tree = ET.ElementTree(rss)
        ET.indent(tree, space="  ", level=0)

        with open('public/rss.xml', 'wb') as f:
            tree.write(f, encoding='utf-8', xml_declaration=True)

        print(f"✅ Bilingual RSS feed generated with {len(featured_items)} featured items")
        return len(featured_items)

    def generate_robots_txt(self):
        """Generate robots.txt for bilingual site"""
        print("🤖 Generating robots.txt...")

        robots_content = f"""User-agent: *
Allow: /

# Sitemaps
Sitemap: {self.base_url}/sitemap.xml

# Allow all content in both languages
Allow: /astrology/
Allow: /en/astrology/
Allow: /health/
Allow: /en/health/
Allow: /love/
Allow: /en/love/
Allow: /history/
Allow: /en/history/
Allow: /psychology/
Allow: /en/psychology/
Allow: /space/
Allow: /en/space/
Allow: /quotes/
Allow: /en/quotes/

# English site root
Allow: /en/

# Special astrology tools
Allow: /astrology/yukselen-burc
Allow: /astrology/sinastri
Allow: /en/astrology/birth-chart
Allow: /en/astrology/rising-sign
Allow: /en/astrology/synastry

# Daily horoscopes
Allow: /en/astrology/*-daily

# Disallow admin areas (if any exist in future)
Disallow: /admin/
Disallow: /api/
Disallow: /_astro/
Disallow: /node_modules/

# Crawl delay (be nice to servers)
Crawl-delay: 1

# Host directive
Host: {self.base_url.replace('https://', '').replace('http://', '')}
"""

        with open('public/robots.txt', 'w', encoding='utf-8') as f:
            f.write(robots_content)

        print("✅ Bilingual robots.txt generated")

def main():
    """Main function to generate all enhanced SEO files"""
    print("🚀 Generating Enhanced Bilingual SEO files for MindVerse Blog...")
    print("=" * 60)

    # Create public directory if it doesn't exist
    os.makedirs('public', exist_ok=True)

    # Initialize generator
    generator = BilingualSEOGenerator()

    # Generate all files
    try:
        sitemap_urls = generator.generate_sitemap()
        rss_items = generator.generate_rss()
        generator.generate_robots_txt()

        print("=" * 60)
        print("✅ Enhanced SEO file generation completed!")
        print(f"📄 Sitemap: {sitemap_urls} URLs (Turkish + English)")
        print(f"📡 RSS Feed: {rss_items} featured items")
        print("🤖 Robots.txt: Generated with bilingual directives")
        print(f"🌐 Base URL: {generator.base_url}")
        print(f"🌍 Languages: Turkish (tr) + English (en)")
        print(f"🔗 Hreflang: Implemented for language alternatives")
        print("=" * 60)

        return True

    except Exception as e:
        print(f"❌ Error generating enhanced SEO files: {e}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
