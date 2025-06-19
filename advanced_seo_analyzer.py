#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import glob
from collections import defaultdict

def analyze_seo_performance():
    """SEO performansını analiz et ve öneriler sun"""

    print("🔍 MindVerse Daily SEO Analizi Başlatılıyor...\n")

    # İçerik dizinleri
    content_dirs = [
        "src/content/articles",
        "src/content/astrology",
        "src/pages"
    ]

    all_files = []
    for content_dir in content_dirs:
        if os.path.exists(content_dir):
            files = glob.glob(os.path.join(content_dir, "*.md")) + glob.glob(os.path.join(content_dir, "*.astro"))
            all_files.extend(files)

    print(f"📁 Toplam {len(all_files)} dosya analiz ediliyor...\n")

    # Analiz sonuçları
    seo_issues = defaultdict(list)
    content_stats = {
        'short_content': [],
        'missing_meta': [],
        'duplicate_titles': defaultdict(list),
        'missing_images': [],
        'poor_headings': [],
        'keyword_density': [],
        'good_content': []
    }

    for file_path in all_files:
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            filename = os.path.basename(file_path)
            analyze_file_seo(file_path, content, content_stats, seo_issues)

        except Exception as e:
            print(f"❌ Hata: {file_path} - {e}")

    # Sonuçları raporla
    generate_seo_report(content_stats, seo_issues)
    generate_optimization_suggestions()

def analyze_file_seo(file_path, content, stats, issues):
    """Tek dosya SEO analizi"""
    filename = os.path.basename(file_path)

    # Meta bilgileri çıkar
    title_match = re.search(r'title:\s*["\']([^"\']+)["\']', content)
    description_match = re.search(r'description:\s*["\']([^"\']+)["\']', content)
    keywords_match = re.search(r'keywords:\s*["\']([^"\']+)["\']', content)

    title = title_match.group(1) if title_match else None
    description = description_match.group(1) if description_match else None
    keywords = keywords_match.group(1) if keywords_match else None

    # İçerik uzunluğu
    text_content = re.sub(r'---.*?---', '', content, flags=re.DOTALL)  # Frontmatter'ı çıkar
    text_content = re.sub(r'<[^>]+>', '', text_content)  # HTML etiketlerini çıkar
    word_count = len(text_content.split())

    # Title analizi
    if title:
        if len(title) < 30:
            issues['short_titles'].append(f"{filename}: '{title}' ({len(title)} karakter)")
        elif len(title) > 60:
            issues['long_titles'].append(f"{filename}: '{title}' ({len(title)} karakter)")

        # Duplicate title kontrolü
        stats['duplicate_titles'][title].append(filename)
    else:
        stats['missing_meta'].append(f"{filename}: Title eksik")

    # Description analizi
    if description:
        if len(description) < 120:
            issues['short_descriptions'].append(f"{filename}: {len(description)} karakter")
        elif len(description) > 160:
            issues['long_descriptions'].append(f"{filename}: {len(description)} karakter")
    else:
        stats['missing_meta'].append(f"{filename}: Description eksik")

    # Keywords analizi
    if not keywords:
        stats['missing_meta'].append(f"{filename}: Keywords eksik")

    # İçerik uzunluğu analizi
    if word_count < 300:
        stats['short_content'].append(f"{filename}: {word_count} kelime")
    elif word_count > 800:
        stats['good_content'].append(f"{filename}: {word_count} kelime")

    # Heading yapısı analizi
    h1_count = len(re.findall(r'^#\s+', content, re.MULTILINE))
    h2_count = len(re.findall(r'^##\s+', content, re.MULTILINE))

    if h1_count == 0:
        stats['poor_headings'].append(f"{filename}: H1 eksik")
    elif h1_count > 1:
        stats['poor_headings'].append(f"{filename}: Çoklu H1 ({h1_count})")

    if h2_count == 0:
        stats['poor_headings'].append(f"{filename}: H2 eksik")

    # Image analizi
    img_count = len(re.findall(r'!\[.*?\]\(.*?\)', content))
    if img_count == 0 and word_count > 200:
        stats['missing_images'].append(f"{filename}: Görsel eksik")

def generate_seo_report(stats, issues):
    """SEO raporu oluştur"""
    print("=" * 60)
    print("🎯 SEO PERFORMANS RAPORU")
    print("=" * 60)

    # Genel istatistikler
    total_files = len(stats['short_content']) + len(stats['good_content'])
    good_ratio = len(stats['good_content']) / total_files * 100 if total_files > 0 else 0

    print(f"📊 GENEL İSTATİSTİKLER")
    print(f"   • Toplam içerik: {total_files}")
    print(f"   • Kaliteli içerik: {len(stats['good_content'])} (%{good_ratio:.1f})")
    print(f"   • Kısa içerik: {len(stats['short_content'])}")
    print(f"   • Meta bilgi eksiklikleri: {len(stats['missing_meta'])}")
    print()

    # Kritik sorunlar
    print("🚨 KRİTİK SORUNLAR")

    if stats['short_content']:
        print(f"   📝 Kısa İçerikler ({len(stats['short_content'])} adet):")
        for item in stats['short_content'][:5]:  # İlk 5'ini göster
            print(f"      - {item}")
        if len(stats['short_content']) > 5:
            print(f"      ... ve {len(stats['short_content']) - 5} adet daha")
        print()

    if stats['missing_meta']:
        print(f"   📋 Meta Bilgi Eksiklikleri ({len(stats['missing_meta'])} adet):")
        for item in stats['missing_meta'][:5]:
            print(f"      - {item}")
        if len(stats['missing_meta']) > 5:
            print(f"      ... ve {len(stats['missing_meta']) - 5} adet daha")
        print()

    # Duplicate title kontrolü
    duplicates = {title: files for title, files in stats['duplicate_titles'].items() if len(files) > 1}
    if duplicates:
        print(f"   🔄 Tekrarlanan Title'lar ({len(duplicates)} adet):")
        for title, files in list(duplicates.items())[:3]:
            print(f"      - '{title}': {', '.join(files)}")
        print()

    # Title uzunluk sorunları
    if issues['short_titles']:
        print(f"   📏 Kısa Title'lar ({len(issues['short_titles'])} adet):")
        for item in issues['short_titles'][:3]:
            print(f"      - {item}")
        print()

    if issues['long_titles']:
        print(f"   📏 Uzun Title'lar ({len(issues['long_titles'])} adet):")
        for item in issues['long_titles'][:3]:
            print(f"      - {item}")
        print()

def generate_optimization_suggestions():
    """SEO optimizasyon önerileri"""
    print("=" * 60)
    print("💡 SEO OPTİMİZASYON ÖNERİLERİ")
    print("=" * 60)

    suggestions = [
        {
            "title": "🎯 İçerik Uzunluğu Optimizasyonu",
            "items": [
                "300 kelimeden az içerikleri genişletin",
                "Her makaleye en az 2-3 paragraf ekleyin",
                "İlgili alt başlıklar ve detaylar ekleyin",
                "Pratik örnekler ve uygulamalar ekleyin"
            ]
        },
        {
            "title": "📋 Meta Bilgi Tamamlama",
            "items": [
                "Eksik title'ları ekleyin (30-60 karakter)",
                "Description'ları yazın (120-160 karakter)",
                "Keywords ekleyin (3-5 anahtar kelime)",
                "OG:image ve Twitter card meta'ları ekleyin"
            ]
        },
        {
            "title": "🔗 İç Linkler ve Yapı",
            "items": [
                "İlgili makaleler arası linkler ekleyin",
                "Breadcrumb navigasyon ekleyin",
                "Site haritası oluşturun",
                "Category sayfalarını optimize edin"
            ]
        },
        {
            "title": "🖼️ Görsel Optimizasyonu",
            "items": [
                "Her makaleye en az 1 görsel ekleyin",
                "Alt text'leri anahtar kelimelerle yazın",
                "Görselleri WebP formatına çevirin",
                "Lazy loading uygulayın"
            ]
        },
        {
            "title": "⚡ Teknik SEO",
            "items": [
                "Site hızını optimize edin",
                "Mobile-first dizayn uygulayın",
                "Schema markup ekleyin",
                "SSL sertifikasını kontrol edin"
            ]
        },
        {
            "title": "🎭 Astroloji SEO Stratejisi",
            "items": [
                "Günlük burç aramalarını hedefleyin",
                "Uzun kuyruk anahtar kelimeler kullanın",
                "Seasonal content (dolunay, yeniay) ekleyin",
                "Local astroloji aramaları optimize edin"
            ]
        }
    ]

    for suggestion in suggestions:
        print(f"\n{suggestion['title']}")
        for item in suggestion['items']:
            print(f"   • {item}")

    print("\n" + "=" * 60)
    print("🚀 ÖNCELİKLİ AKSIYONLAR")
    print("=" * 60)

    priorities = [
        "1. 300 kelimeden kısa tüm içerikleri genişletin",
        "2. Eksik meta description'ları ekleyin",
        "3. Duplicate title'ları düzeltin",
        "4. Ana kategorilere landing page'ler ekleyin",
        "5. Site haritası ve robot.txt oluşturun"
    ]

    for priority in priorities:
        print(f"   {priority}")

    print(f"\n📈 Hedef: 3 ay içinde organik trafik %200 artış!")

if __name__ == "__main__":
    analyze_seo_performance()
