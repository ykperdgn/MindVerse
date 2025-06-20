#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import xml.etree.ElementTree as ET
from datetime import datetime
import re

def generate_sitemap():
    """Site haritası oluştur"""

    print("🗺️ Sitemap oluşturuluyor...")

    base_url = "https://www.mindversedaily.com"

    # XML namespace
    urlset = ET.Element("urlset")
    urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

    # Ana sayfa
    url = ET.SubElement(urlset, "url")
    ET.SubElement(url, "loc").text = base_url
    ET.SubElement(url, "lastmod").text = datetime.now().strftime("%Y-%m-%d")
    ET.SubElement(url, "changefreq").text = "daily"
    ET.SubElement(url, "priority").text = "1.0"

    # Statik sayfalar
    static_pages = [
        ("/popular", "weekly", "0.8"),
        ("/categories", "weekly", "0.8"),
        ("/astrology", "daily", "0.9"),
        ("/astrology/yukselen-burc", "monthly", "0.7"),
        ("/astrology/sinastri", "monthly", "0.7"),
        ("/health", "weekly", "0.7"),
        ("/love", "weekly", "0.7"),
        ("/history", "weekly", "0.7"),
        ("/psychology", "weekly", "0.7"),
        ("/space", "weekly", "0.7"),
        ("/quotes", "weekly", "0.7")
    ]

    for page, changefreq, priority in static_pages:
        url = ET.SubElement(urlset, "url")
        ET.SubElement(url, "loc").text = f"{base_url}{page}"
        ET.SubElement(url, "lastmod").text = datetime.now().strftime("%Y-%m-%d")
        ET.SubElement(url, "changefreq").text = changefreq
        ET.SubElement(url, "priority").text = priority

    # Astroloji içerikleri
    astrology_dir = "src/content/astrology"
    if os.path.exists(astrology_dir):
        files = glob.glob(os.path.join(astrology_dir, "*.md"))

        for file_path in files:
            try:
                filename = os.path.basename(file_path)

                # URL oluştur (dosya adından)
                url_path = filename.replace('.md', '')
                # Tarih kısmını çıkar
                url_path = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', url_path)

                url = ET.SubElement(urlset, "url")
                ET.SubElement(url, "loc").text = f"{base_url}/astrology/{url_path}"
                ET.SubElement(url, "lastmod").text = "2025-06-19"
                ET.SubElement(url, "changefreq").text = "weekly"
                ET.SubElement(url, "priority").text = "0.8"

            except Exception as e:
                print(f"⚠️ Error processing {filename}: {e}")

    # Articles (eğer varsa)
    articles_dir = "src/content/articles"
    if os.path.exists(articles_dir):
        files = glob.glob(os.path.join(articles_dir, "*.md"))

        for file_path in files:
            try:
                filename = os.path.basename(file_path)
                url_path = filename.replace('.md', '')

                url = ET.SubElement(urlset, "url")
                ET.SubElement(url, "loc").text = f"{base_url}/articles/{url_path}"
                ET.SubElement(url, "lastmod").text = "2025-06-19"
                ET.SubElement(url, "changefreq").text = "monthly"
                ET.SubElement(url, "priority").text = "0.6"

            except Exception as e:
                print(f"⚠️ Error processing {filename}: {e}")

    # XML'i dosyaya yaz
    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ", level=0)

    sitemap_path = "public/sitemap.xml"
    tree.write(sitemap_path, encoding="utf-8", xml_declaration=True)

    print(f"✅ Sitemap oluşturuldu: {sitemap_path}")

    # İstatistikleri göster
    total_urls = len(urlset.findall("url"))
    print(f"📊 Toplam URL: {total_urls}")

    return sitemap_path

def generate_rss_feed():
    """RSS feed oluştur"""

    print("📡 RSS Feed oluşturuluyor...")

    # RSS XML oluştur
    rss = ET.Element("rss")
    rss.set("version", "2.0")
    rss.set("xmlns:atom", "http://www.w3.org/2005/Atom")

    channel = ET.SubElement(rss, "channel")

    # Channel bilgileri
    ET.SubElement(channel, "title").text = "MindVerse Daily - Astroloji ve Yaşam Rehberi"
    ET.SubElement(channel, "link").text = "https://www.mindversedaily.com"
    ET.SubElement(channel, "description").text = "Günlük burç yorumları, astroloji analizleri ve yaşam rehberliği"
    ET.SubElement(channel, "language").text = "tr-TR"
    ET.SubElement(channel, "lastBuildDate").text = datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")

    # Atom link
    atom_link = ET.SubElement(channel, "atom:link")
    atom_link.set("href", "https://www.mindversedaily.com/rss.xml")
    atom_link.set("rel", "self")
    atom_link.set("type", "application/rss+xml")

    # Astroloji içeriklerini ekle
    astrology_dir = "src/content/astrology"
    if os.path.exists(astrology_dir):
        files = glob.glob(os.path.join(astrology_dir, "*.md"))

        # Son 20 makaleyi ekle
        for file_path in sorted(files, reverse=True)[:20]:
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                # Title ve description çıkar
                title_match = re.search(r'title:\s*["\']([^"\']+)["\']', content)
                desc_match = re.search(r'description:\s*["\']([^"\']+)["\']', content)

                if title_match and desc_match:
                    filename = os.path.basename(file_path)
                    url_path = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', filename.replace('.md', ''))

                    item = ET.SubElement(channel, "item")
                    ET.SubElement(item, "title").text = title_match.group(1)
                    ET.SubElement(item, "link").text = f"https://www.mindversedaily.com/astrology/{url_path}"
                    ET.SubElement(item, "description").text = desc_match.group(1)
                    ET.SubElement(item, "pubDate").text = "Wed, 19 Jun 2025 10:00:00 GMT"
                    ET.SubElement(item, "guid").text = f"https://www.mindversedaily.com/astrology/{url_path}"

            except Exception as e:
                print(f"⚠️ RSS error: {e}")

    # RSS'i dosyaya yaz
    tree = ET.ElementTree(rss)
    ET.indent(tree, space="  ", level=0)

    rss_path = "public/rss.xml"
    tree.write(rss_path, encoding="utf-8", xml_declaration=True)

    print(f"✅ RSS Feed oluşturuldu: {rss_path}")

    return rss_path

if __name__ == "__main__":
    generate_sitemap()
    generate_rss_feed()
    print("\n🎉 SEO dosyaları başarıyla oluşturuldu!")
