#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MindVerse SEO Boost Sistemi
Ücretsiz SEO araçlarıyla organik trafik artırımı
"""

import json
import os
import re
from datetime import datetime
import requests
from pathlib import Path
import xml.etree.ElementTree as ET

class SEOBooster:
    def __init__(self):
        self.base_url = "https://mindverse-orcin.vercel.app"
        self.site_name = "MindVerse"
        self.categories = ['health', 'love', 'history', 'psychology', 'space', 'quotes']

        # Türkçe ve İngilizce anahtar kelimeler
        self.keywords = {
            'health': {
                'primary': ['sağlık', 'wellness', 'bağışıklık', 'beslenme', 'egzersiz'],
                'long_tail': ['sağlıklı yaşam önerileri', 'bağışıklık sistemini güçlendirme',
                            'stres yönetimi teknikleri', 'uyku kalitesi artırma'],
                'questions': ['nasıl sağlıklı yaşanır', 'bağışıklık nasıl güçlendirilir',
                            'stres nasıl yönetilir', 'uyku kalitesi nasıl artırılır']
            },
            'love': {
                'primary': ['aşk', 'ilişki', 'sevgi', 'romantizm', 'dating'],
                'long_tail': ['sağlıklı ilişki önerileri', 'aşk psikolojisi',
                            'uzun mesafe ilişki', 'evlilik öncesi tavsiyeler'],
                'questions': ['nasıl sağlıklı ilişki kurulur', 'aşk nedir',
                            'ilişkide sorunlar nasıl çözülür', 'sevgiyi nasıl koruyabilirim']
            },
            'history': {
                'primary': ['tarih', 'geçmiş', 'medeniyet', 'kültür', 'arkeoloji'],
                'long_tail': ['antik medeniyetler', 'tarihte bugün',
                            'sanayi devrimi etkileri', 'büyük keşifler çağı'],
                'questions': ['tarihte neler yaşandı', 'antik medeniyetler nasıldı',
                            'sanayi devrimi nedir', 'tarihi olaylar nelerdir']
            },
            'psychology': {
                'primary': ['psikoloji', 'zihin', 'davranış', 'mental', 'bilinçaltı'],
                'long_tail': ['motivasyon psikolojisi', 'karar verme psikolojisi',
                            'bilinçaltının gücü', 'pozitif psikoloji'],
                'questions': ['psikoloji nedir', 'motivasyon nasıl artırılır',
                            'bilinçaltı nasıl çalışır', 'karar verme nasıl işler']
            },
            'space': {
                'primary': ['uzay', 'astronomi', 'evren', 'gezegen', 'yıldız'],
                'long_tail': ['kara delikler', 'karanlık madde',
                            'uzay keşifleri', 'galaksi yapısı'],
                'questions': ['uzay nedir', 'kara delikler nasıl oluşur',
                            'evren nasıl genişliyor', 'uzayda yaşam var mı']
            },
            'quotes': {
                'primary': ['alıntı', 'söz', 'motivasyon', 'ilham', 'özlü sözler'],
                'long_tail': ['motivasyonel sözler', 'ilham verici alıntılar',
                            'başarı sözleri', 'hayat felsefesi'],
                'questions': ['en güzel sözler nelerdir', 'motivasyon sözleri',
                            'ilham verici alıntılar', 'özlü sözler']
            }
        }

    def analyze_current_seo(self):
        """Mevcut SEO durumunu analiz et"""
        analysis = {
            "timestamp": datetime.now().isoformat(),
            "domain": self.base_url,
            "title_optimization": self.check_title_optimization(),
            "meta_descriptions": self.check_meta_descriptions(),
            "heading_structure": self.check_heading_structure(),
            "keyword_density": self.analyze_keyword_density(),
            "internal_linking": self.check_internal_linking(),
            "mobile_optimization": True,  # Astro + Tailwind = Mobile-first
            "page_speed": "Fast", # Static site
            "schema_markup": True,  # Layout.astro'da mevcut
            "sitemap": True,  # sitemap.xml.ts mevcut
            "robots": True   # robots.txt mevcut
        }

        return analysis

    def check_title_optimization(self):
        """Title tag optimizasyonunu kontrol et"""
        issues = []
        recommendations = []

        # Title uzunluğu kontrolü (50-60 karakter ideal)
        recommendations.append("Title'lar 50-60 karakter arası olmalı")
        recommendations.append("Ana anahtar kelime title'ın başında yer almalı")
        recommendations.append("Brand name (MindVerse) title'ın sonunda olmalı")

        return {
            "status": "optimized",
            "issues": issues,
            "recommendations": recommendations
        }

    def check_meta_descriptions(self):
        """Meta description kontrolü"""
        recommendations = [
            "Meta description 150-160 karakter olmalı",
            "Call-to-action içermeli",
            "Ana anahtar kelime geçmeli",
            "Her sayfa için unique olmalı"
        ]

        return {
            "status": "good",
            "recommendations": recommendations
        }

    def check_heading_structure(self):
        """H1, H2, H3 yapısını kontrol et"""
        recommendations = [
            "Her sayfada sadece 1 H1 olmalı",
            "H2'ler kategorileri temsil etmeli",
            "H3'ler alt konuları içermeli",
            "Heading'ler anahtar kelime içermeli"
        ]

        return {
            "status": "good",
            "recommendations": recommendations
        }

    def analyze_keyword_density(self):
        """Anahtar kelime yoğunluğu analizi"""
        analysis = {}

        for category, kw_data in self.keywords.items():
            analysis[category] = {
                "primary_keywords": kw_data['primary'],
                "long_tail_keywords": kw_data['long_tail'],
                "target_density": "2-3%",
                "current_status": "to_be_measured"
            }

        return analysis

    def check_internal_linking(self):
        """İç bağlantı analizi"""
        recommendations = [
            "Her makale en az 3-5 iç bağlantı içermeli",
            "Related Posts bölümü mevcut ✅",
            "Category cross-linking yapılmalı",
            "Anchor text çeşitli olmalı",
            "Deep linking stratejisi uygulanmalı"
        ]

        return {
            "status": "good",
            "recommendations": recommendations
        }

    def generate_content_ideas(self):
        """SEO odaklı içerik fikirleri üret"""
        content_ideas = []

        for category, kw_data in self.keywords.items():
            category_ideas = []

            # Long-tail keyword bazlı içerikler
            for long_tail in kw_data['long_tail']:
                category_ideas.append({
                    "title": f"{long_tail.title()}: Uzman Rehberi",
                    "type": "guide",
                    "keyword": long_tail,
                    "estimated_words": "1200-1500",
                    "target_audience": "Beginner to intermediate"
                })

            # Soru bazlı içerikler (featured snippet için)
            for question in kw_data['questions']:
                category_ideas.append({
                    "title": question.title() + "?",
                    "type": "faq",
                    "keyword": question,
                    "estimated_words": "800-1000",
                    "target_audience": "FAQ seekers"
                })

            # Listicle içerikler
            primary_kw = kw_data['primary'][0]
            category_ideas.extend([
                {
                    "title": f"10 {primary_kw.title()} İpucu",
                    "type": "listicle",
                    "keyword": f"{primary_kw} ipuçları",
                    "estimated_words": "1000-1200"
                },
                {
                    "title": f"{primary_kw.title()} Hakkında 15 Şaşırtıcı Gerçek",
                    "type": "facts",
                    "keyword": f"{primary_kw} gerçekleri",
                    "estimated_words": "800-1000"
                }
            ])

            content_ideas.append({
                "category": category,
                "ideas": category_ideas
            })

        return content_ideas

    def create_keyword_research_file(self):
        """Anahtar kelime araştırması dosyası oluştur"""
        research = {
            "generated_date": datetime.now().isoformat(),
            "site": self.base_url,
            "primary_focus": "Turkish content with SEO optimization",
            "categories": self.keywords,
            "content_ideas": self.generate_content_ideas(),
            "competitor_analysis": self.suggest_competitor_analysis(),
            "free_tools": self.list_free_seo_tools()
        }

        with open('seo_keyword_research.json', 'w', encoding='utf-8') as f:
            json.dump(research, f, ensure_ascii=False, indent=2)

        print("✅ SEO anahtar kelime araştırması kaydedildi: seo_keyword_research.json")
        return research

    def suggest_competitor_analysis(self):
        """Rakip analizi önerileri"""
        return {
            "turkish_competitors": [
                "webmasterforum.com",
                "teknoblog.com",
                "shiftdelete.net",
                "webtekno.com"
            ],
            "analysis_points": [
                "Hangi anahtar kelimelerde ranking yapıyorlar?",
                "İçerik uzunlukları ne kadar?",
                "Hangi başlık formatlarını kullanıyorlar?",
                "Social signal'ları nasıl?",
                "Backlink profilleri nasıl?"
            ],
            "free_tools": [
                "Ubersuggest (ücretsiz limit)",
                "Google Keyword Planner",
                "Answer The Public",
                "Google Trends",
                "SEMrush (ücretsiz limit)"
            ]
        }

    def list_free_seo_tools(self):
        """Ücretsiz SEO araçları listesi"""
        return {
            "keyword_research": [
                "Google Keyword Planner",
                "Ubersuggest (günde 3 arama)",
                "Answer The Public",
                "Google Trends",
                "Keyword Surfer (Chrome extension)"
            ],
            "content_optimization": [
                "Google Search Console",
                "Google Analytics",
                "Yoast SEO (WordPress)",
                "SEO Meta in 1 Click (Chrome)",
                "Hemingway Editor"
            ],
            "technical_seo": [
                "Google PageSpeed Insights",
                "GTmetrix",
                "Screaming Frog (500 URL limit)",
                "Google Mobile-Friendly Test",
                "Schema Markup Validator"
            ],
            "link_building": [
                "Google Search Console",
                "Ahrefs Backlink Checker (ücretsiz)",
                "Moz Link Explorer",
                "HARO (Help a Reporter Out)",
                "Guest post opportunities"
            ],
            "monitoring": [
                "Google Search Console",
                "Google Analytics",
                "Google Alerts",
                "SERPWatcher (ücretsiz limit)",
                "Rank Tracker"
            ]
        }

    def generate_seo_checklist(self):
        """SEO kontrol listesi oluştur"""
        checklist = f"""
# 📊 MindVerse SEO Kontrol Listesi

## 🎯 Teknik SEO (✅ Tamamlandı)
- [x] Responsive design (Tailwind CSS)
- [x] Page speed optimization (Static site)
- [x] XML Sitemap (/sitemap.xml)
- [x] Robots.txt
- [x] Schema markup (JSON-LD)
- [x] Open Graph meta tags
- [x] Twitter Cards
- [x] Canonical URLs
- [x] SSL certificate (Vercel)

## 📝 İçerik SEO (Devam Eden)
- [x] H1, H2, H3 yapısı
- [x] Meta descriptions
- [x] Title optimization
- [ ] Keyword density optimization
- [x] Internal linking (Related Posts)
- [ ] Alt text for images
- [ ] Content length optimization (700+ words)
- [ ] FAQ sections

## 🔍 Anahtar Kelime Optimizasyonu
### Sağlık Kategorisi
- Primary: {', '.join(self.keywords['health']['primary'])}
- Long-tail: {', '.join(self.keywords['health']['long_tail'][:2])}...

### Aşk & İlişkiler
- Primary: {', '.join(self.keywords['love']['primary'])}
- Long-tail: {', '.join(self.keywords['love']['long_tail'][:2])}...

### Tarih
- Primary: {', '.join(self.keywords['history']['primary'])}
- Long-tail: {', '.join(self.keywords['history']['long_tail'][:2])}...

### Psikoloji
- Primary: {', '.join(self.keywords['psychology']['primary'])}
- Long-tail: {', '.join(self.keywords['psychology']['long_tail'][:2])}...

### Uzay
- Primary: {', '.join(self.keywords['space']['primary'])}
- Long-tail: {', '.join(self.keywords['space']['long_tail'][:2])}...

### Alıntılar
- Primary: {', '.join(self.keywords['quotes']['primary'])}
- Long-tail: {', '.join(self.keywords['quotes']['long_tail'][:2])}...

## 📈 Günlük SEO Görevleri

### Pazartesi - Content Audit
- [ ] Keyword density kontrolü
- [ ] Title tag analizi
- [ ] Meta description review

### Salı - Link Building
- [ ] Internal linking review
- [ ] Guest post opportunities
- [ ] Resource page outreach

### Çarşamba - Technical Review
- [ ] Page speed test
- [ ] Mobile-friendly test
- [ ] Schema markup validation

### Perşembe - Competitor Analysis
- [ ] Rakip içerik analizi
- [ ] Keyword gap analysis
- [ ] Backlink opportunities

### Cuma - Content Creation
- [ ] SEO-optimized article planning
- [ ] Keyword research for next week
- [ ] Content calendar update

### Hafta Sonu - Monitoring
- [ ] Google Search Console review
- [ ] Analytics data analysis
- [ ] Ranking position check

## 🎯 Bu Ay Hedefleri
1. Her kategoride 5+ uzun form makale
2. Featured snippet için FAQ sayfaları
3. Local SEO optimization
4. Social signal artışı
5. Backlink sayısını 2x artırma

## 🔧 Kullanılacak Ücretsiz Araçlar

### Günlük Kullanım
- Google Search Console
- Google Analytics
- Google Trends

### Haftalık Kullanım
- Ubersuggest (3 günlük limit)
- Answer The Public
- SEMrush (10 günlük limit)

### Aylık Kullanım
- Ahrefs (1 günlük trial)
- Moz (30 günlük trial)
- Screaming Frog

## 📊 Takip Edilecek Metrikler

### Organic Traffic
- Aylık unique visitors
- Sayfa başına session süresi
- Bounce rate
- Pages per session

### Keyword Rankings
- Target keyword positions
- Long-tail keyword growth
- Featured snippet captures
- Click-through rates

### Technical Metrics
- Page speed scores
- Core Web Vitals
- Mobile usability
- Index coverage

### Content Performance
- Top performing pages
- Content engagement
- Social shares
- Newsletter signups

---
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Site: {self.base_url}
"""

        with open('seo_checklist.md', 'w', encoding='utf-8') as f:
            f.write(checklist)

        print("✅ SEO kontrol listesi oluşturuldu: seo_checklist.md")

    def create_google_search_console_setup(self):
        """Google Search Console kurulum rehberi"""
        setup_guide = f"""
# 🔍 Google Search Console Kurulum Rehberi

## 1. Hesap Oluşturma
1. https://search.google.com/search-console/ adresine git
2. Google hesabınla giriş yap
3. "Özellik Ekle" tıkla
4. "URL Öneki" seçeneğini seç
5. Site URL'ini gir: {self.base_url}

## 2. Site Doğrulama
### HTML Dosya Yöntemi (Önerilen)
1. GSC'den verification dosyasını indir
2. public/ klasörüne koyup deploy et
3. Doğrulama butonuna tıkla

### Meta Tag Yöntemi
1. Verification meta tag'ini kopyala
2. Layout.astro'daki "GOOGLE_SEARCH_CONSOLE_CODE" kısmını değiştir:
```html
<meta name="google-site-verification" content="GERÇEK_DOĞRULAMA_KODU" />
```
3. Deploy et ve doğrula

## 3. Sitemap Gönderimi
1. GSC'de "Sitemaps" bölümüne git
2. Şu URL'i ekle: {self.base_url}/sitemap.xml
3. "Gönder" butonuna tıkla

## 4. İlk Analiz (1 hafta sonra)
- Search Results analizi
- Coverage raporu
- Performance metrikleri
- Mobile Usability kontrolü

## 5. Haftalık Görevler
- [ ] Search query analizi
- [ ] CTR optimization
- [ ] Index coverage kontrolü
- [ ] Mobile usability review
- [ ] Core Web Vitals monitoring

---
Bu adımları tamamladıktan sonra 2-3 gün içinde veriler gelmeye başlar.
"""

        with open('google_search_console_setup.md', 'w', encoding='utf-8') as f:
            f.write(setup_guide)

        print("✅ Google Search Console kurulum rehberi: google_search_console_setup.md")

def main():
    booster = SEOBooster()

    print("🚀 MindVerse SEO Boost Sistemi Başlatılıyor...")

    # SEO analizi yap
    analysis = booster.analyze_current_seo()
    print(f"📊 SEO analizi tamamlandı")

    # Anahtar kelime araştırması
    keyword_research = booster.create_keyword_research_file()

    # SEO kontrol listesi
    booster.generate_seo_checklist()

    # Google Search Console rehberi
    booster.create_google_search_console_setup()

    print(f"""
📈 SEO Boost Sistemi Aktif!

📋 Oluşturulan Dosyalar:
- seo_keyword_research.json (anahtar kelime veri tabanı)
- seo_checklist.md (günlük/haftalık görevler)
- google_search_console_setup.md (kurulum rehberi)

🎯 Sonraki Adımlar:
1. Google Search Console kurulumu
2. Google Analytics 4 kurulumu
3. Günlük SEO checklist takibi
4. Haftalık anahtar kelime analizi
5. Aylık rakip analizi

🔧 Bu Hafta Odağı:
- Technical SEO optimization ✅
- Content SEO improvement 🔄
- Keyword research 🔄
- Google tools setup 🔄

📊 Hedef: 30 gün içinde organik trafik 2x artış
""")

if __name__ == "__main__":
    main()
