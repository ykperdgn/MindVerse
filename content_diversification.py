#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MindVerse İçerik Çeşitlendirme Sistemi
Trafik artışı için çeşitli içerik formatları oluşturur
"""

import json
import os
import random
from datetime import datetime, timedelta
from pathlib import Path

class ContentDiversificationSystem:
    def __init__(self):
        self.base_url = "https://www.mindversedaily.com"
        self.categories = {
            'health': {
                'emoji': '🏥',
                'color': 'green',
                'topics': ['beslenme', 'egzersiz', 'mental sağlık', 'uyku', 'bağışıklık']
            },
            'love': {
                'emoji': '❤️',
                'color': 'red',
                'topics': ['ilişki', 'aşk psikolojisi', 'evlilik', 'dating', 'iletişim']
            },
            'history': {
                'emoji': '📚',
                'color': 'yellow',
                'topics': ['antik çağ', 'modern tarih', 'savaşlar', 'keşifler', 'kültürler']
            },
            'psychology': {
                'emoji': '🧠',
                'color': 'purple',
                'topics': ['motivasyon', 'zihin', 'davranış', 'bilinçaltı', 'başarı']
            },
            'space': {
                'emoji': '🚀',
                'color': 'blue',
                'topics': ['gezegenler', 'yıldızlar', 'uzay keşfi', 'astronomi', 'evren']
            },
            'quotes': {
                'emoji': '💭',
                'color': 'gray',
                'topics': ['motivasyon', 'ilham', 'başarı', 'hayat', 'sevgi']
            }
        }

    def create_faq_pages(self):
        """Sık sorulan sorular sayfaları (Featured Snippet için)"""
        faq_content = {}

        for category, info in self.categories.items():
            faqs = self.generate_category_faqs(category, info)

            # FAQ sayfası oluştur
            faq_page = f"""---
title: "{category.title()} Hakkında Sık Sorulan Sorular"
date: {datetime.now().strftime('%Y-%m-%d')}
summary: "{category.title()} kategorisinde en çok merak edilen sorular ve detaylı cevapları."
tags: ["faq", "{category}", "sorular", "rehber"]
views: 0
---

# {info['emoji']} {category.title()} - Sık Sorulan Sorular

{category.title()} konusunda en çok merak edilen soruları derledik. Aradığınız cevap burada!

## 📋 İçindekiler
{chr(10).join([f"- [{faq['question']}](#{self.slugify(faq['question'])})" for faq in faqs[:5]])}

---

"""

            for i, faq in enumerate(faqs, 1):
                faq_page += f"""
## {i}. {faq['question']} {{#{self.slugify(faq['question'])}}}

**Kısa Cevap:** {faq['short_answer']}

**Detaylı Açıklama:**
{faq['detailed_answer']}

**İlgili Kaynaklar:**
{chr(10).join([f"- [{source}]({self.base_url}/{category})" for source in faq['sources']])}

---
"""

            faq_page += f"""
## 💡 Daha Fazla Bilgi

{category.title()} konusunda daha fazla bilgi için:
- [{category.title()} kategorisindeki tüm içeriklerimiz]({self.base_url}/{category})
- [En popüler {category} yazılarımız]({self.base_url}/popular)
- [Site içi arama]({self.base_url}/search)

## 🤔 Sorunuz mu Var?

Aklınıza takılan başka sorular varsa yorumlarda belirtebilir veya [bültenimize]({self.base_url}) katılarak güncel içeriklerimizden haberdar olabilirsiniz.
"""

            # Dosyayı kaydet
            faq_filename = f"src/content/{category}/faq-{category}.md"
            os.makedirs(os.path.dirname(faq_filename), exist_ok=True)

            with open(faq_filename, 'w', encoding='utf-8') as f:
                f.write(faq_page)

            faq_content[category] = faqs

        # FAQ index sayfası
        self.create_faq_index_page()

        print("✅ FAQ sayfaları oluşturuldu (Featured Snippet için)")
        return faq_content

    def generate_category_faqs(self, category, info):
        """Kategori bazlı FAQ'ler oluştur"""
        faq_templates = {
            'health': [
                {
                    'question': 'Sağlıklı yaşam için en önemli faktörler nelerdir?',
                    'short_answer': 'Dengeli beslenme, düzenli egzersiz, kaliteli uyku ve stres yönetimi.',
                    'detailed_answer': 'Sağlıklı yaşamın temel taşları beslenme, hareket, dinlenme ve zihinsel sağlıktır. Dengeli beslenme vücut fonksiyonlarını destekler, düzenli egzersiz kardiyovasküler sistemi güçlendirir, kaliteli uyku vücudun onarım süreçlerini başlatır, stres yönetimi ise genel yaşam kalitesini artırır.',
                    'sources': ['Beslenme Rehberi', 'Egzersiz Programları', 'Uyku Hijyeni']
                },
                {
                    'question': 'Bağışıklık sistemini doğal yollarla nasıl güçlendirebilirim?',
                    'short_answer': 'C vitamini, D vitamini, çinko alımı, düzenli egzersiz ve yeterli uyku.',
                    'detailed_answer': 'Bağışıklık sistemi güçlendirmek için vitamin ve mineral açısından zengin beslenme, düzenli fiziksel aktivite, 7-9 saat kaliteli uyku, stres yönetimi ve probiyotik gıdalar tüketmek etkilidir. Özellikle turunçgiller, yeşil yapraklılar ve fermente gıdalar faydalıdır.',
                    'sources': ['Bağışıklık Rehberi', 'Vitamin Rehberi', 'Beslenme Önerileri']
                }
            ],
            'love': [
                {
                    'question': 'Sağlıklı ilişkinin temel unsurları nelerdir?',
                    'short_answer': 'İletişim, güven, saygı, empati ve ortak değerler.',
                    'detailed_answer': 'Sağlıklı ilişkilerde açık iletişim, karşılıklı güven ve saygı, empati kurabilme, bireysel alanları koruma ve ortak hedefler bulunur. Çiftler problem çözme becerilerini geliştirmeli ve birbirlerinin gelişimini desteklemelidir.',
                    'sources': ['İlişki Rehberi', 'İletişim Teknikleri', 'Çift Terapisi']
                }
            ],
            'psychology': [
                {
                    'question': 'Motivasyon nasıl artırılır?',
                    'short_answer': 'Net hedefler, küçük adımlar, ödül sistemi ve pozitif çevre.',
                    'detailed_answer': 'Motivasyon artırmak için SMART hedefler belirleme, büyük hedefleri küçük adımlara bölme, başarıları ödüllendirme, pozitif çevreyle kuşatma ve ilerleme kaydetme etkilidir. Ayrıca neden-sonuç ilişkisini anlamak ve içsel motivasyon kaynaklarını keşfetmek önemlidir.',
                    'sources': ['Motivasyon Teknikleri', 'Hedef Belirleme', 'Başarı Psikolojisi']
                }
            ]
        }

        return faq_templates.get(category, [
            {
                'question': f'{category.title()} hakkında bilmeniz gerekenler nelerdir?',
                'short_answer': f'{category.title()} konusunda temel bilgiler ve pratik öneriler.',
                'detailed_answer': f'{category.title()} alanında güncel bilgiler ve uzman tavsiyeleri ile kapsamlı rehberler sunuyoruz.',
                'sources': ['Temel Rehber', 'Uzman Önerileri', 'Güncel Araştırmalar']
            }
        ])

    def create_faq_index_page(self):
        """Ana FAQ index sayfası"""
        faq_index = f"""---
title: "Sık Sorulan Sorular - MindVerse"
date: {datetime.now().strftime('%Y-%m-%d')}
summary: "MindVerse'te en çok merak edilen sorular ve detaylı cevapları. Tüm kategorilerde uzman rehberleri."
tags: ["faq", "sorular", "rehber", "yardım"]
views: 0
---

# 🤔 Sık Sorulan Sorular

MindVerse topluluğumuzun en çok merak ettiği sorular ve detaylı cevapları burada!

## 📚 Kategorilere Göre FAQ'ler

### 🏥 Sağlık
- [Sağlık konusunda sık sorulan sorular]({self.base_url}/health/faq-health)
- Beslenme, egzersiz, mental sağlık rehberleri

### ❤️ Aşk & İlişkiler
- [İlişkiler konusunda sık sorulan sorular]({self.base_url}/love/faq-love)
- İletişim, aşk psikolojisi, evlilik önerileri

### 📚 Tarih
- [Tarih konusunda sık sorulan sorular]({self.base_url}/history/faq-history)
- Antik çağlar, keşifler, kültürel miras

### 🧠 Psikoloji
- [Psikoloji konusunda sık sorulan sorular]({self.base_url}/psychology/faq-psychology)
- Motivasyon, zihin, davranış analizi

### 🚀 Uzay
- [Uzay konusunda sık sorulan sorular]({self.base_url}/space/faq-space)
- Astronomi, gezegen bilimi, uzay keşifleri

### 💭 Alıntılar
- [Alıntılar konusunda sık sorulan sorular]({self.base_url}/quotes/faq-quotes)
- Motivasyonel sözler, ilham kaynakları

## 🔍 Hızlı Arama

Aradığınızı bulamadınız mı? [Site içi arama]({self.base_url}/search) ile tüm içeriklerimizde arama yapabilirsiniz.

## 📧 Soru Gönderin

Aklınıza takılan sorular için:
- Yorumlar bölümünde soru sorabilirsiniz
- [Bültenimize]({self.base_url}) katılarak güncel içeriklerden haberdar olabilirsiniz
- Sosyal medya hesaplarımızdan bize ulaşabilirsiniz

---
*Bu sayfa düzenli olarak güncellenmektedir. En son güncellenme: {datetime.now().strftime('%d.%m.%Y')}*
"""

        with open('src/pages/faq.astro', 'w', encoding='utf-8') as f:
            f.write(f"""---
import Layout from '../components/Layout.astro';
---

<Layout title="Sık Sorulan Sorular - MindVerse">
  <div class="container mx-auto px-4 py-8">
    <div class="prose prose-lg max-w-none">
{faq_index}
    </div>
  </div>
</Layout>""")

        print("✅ FAQ index sayfası oluşturuldu: src/pages/faq.astro")

    def create_listicle_templates(self):
        """Listicle (liste) formatında içerik şablonları"""
        listicle_ideas = []

        for category, info in self.categories.items():
            category_listicles = [
                {
                    'title': f"{category.title()} Hakkında 10 Şaşırtıcı Gerçek",
                    'type': 'facts',
                    'items': 10,
                    'target_words': 1200
                },
                {
                    'title': f"{category.title()} İçin 15 Pratik İpucu",
                    'type': 'tips',
                    'items': 15,
                    'target_words': 1500
                },
                {
                    'title': f"{category.title()} Alanında 7 Yaygın Hata",
                    'type': 'mistakes',
                    'items': 7,
                    'target_words': 1000
                },
                {
                    'title': f"{category.title()} Başlangıç Rehberi: 5 Temel Adım",
                    'type': 'beginner',
                    'items': 5,
                    'target_words': 800
                }
            ]

            listicle_ideas.extend([{
                'category': category,
                'emoji': info['emoji'],
                **listicle
            } for listicle in category_listicles])

        # Listicle template örneği oluştur
        self.create_sample_listicle(listicle_ideas[0])

        with open('listicle_content_ideas.json', 'w', encoding='utf-8') as f:
            json.dump(listicle_ideas, f, ensure_ascii=False, indent=2)

        print("✅ Listicle içerik fikirleri: listicle_content_ideas.json")
        return listicle_ideas

    def create_sample_listicle(self, listicle_data):
        """Örnek listicle içeriği oluştur"""
        category = listicle_data['category']
        title = listicle_data['title']
        emoji = listicle_data['emoji']

        sample_content = f"""---
title: "{title}"
date: {datetime.now().strftime('%Y-%m-%d')}
summary: "{title} - Uzmanlar tarafından derlenen kapsamlı liste rehberi."
tags: ["{category}", "liste", "ipucu", "rehber", "pratik"]
views: 0
---

# {emoji} {title}

{category.title()} konusunda bilmeniz gereken en önemli noktaları liste halinde derledik. Bu rehberle konuya hakim olacaksınız!

## 📋 İçindekiler
1. [Giriş](#giris)
2. [Ana Liste](#ana-liste)
3. [Sonuç ve Öneriler](#sonuc)

## Giriş {{#giris}}

{category.title()} alanında başarılı olmak için doğru bilgilere sahip olmak kritik önem taşır. Bu makalede uzmanlar tarafından önerilen en etkili yöntemleri bulacaksınız.

## Ana Liste {{#ana-liste}}

"""

        # Liste öğelerini oluştur
        for i in range(1, listicle_data['items'] + 1):
            sample_content += f"""
### {i}. [Liste Öğesi {i} Başlığı]

**Özet:** Bu bölümde ana nokta kısaca özetlenir.

**Detaylı Açıklama:**
Bu kısımda konu detaylı bir şekilde işlenir. Örnekler, açıklamalar ve pratik öneriler yer alır. Her liste öğesi 80-120 kelime arasında olmalıdır.

**Pratik İpucu:** Konuyla ilgili uygulanabilir bir öneri.

---
"""

        sample_content += f"""
## Sonuç ve Öneriler {{#sonuc}}

{title} konusunu ele aldığımız bu rehberde en önemli noktaları öğrendiniz. Bu bilgileri günlük hayatınızda uygulayarak {category.title()} alanında gelişim gösterebilirsiniz.

### 🎯 Hemen Uygulayabileceğiniz 3 Adım:
1. **İlk adım:** Temel bilgileri pekiştirin
2. **İkinci adım:** Pratik uygulamalara başlayın
3. **Üçüncü adım:** Düzenli takip ve gelişim

### 📚 İlgili İçerikler:
- [{category.title()} kategorisindeki diğer yazılarımız]({self.base_url}/{category})
- [En popüler {category} içerikleri]({self.base_url}/popular)
- [Site içi arama]({self.base_url}/search)

## 💬 Sizin Deneyimleriniz Neler?

Bu konuda deneyimlerinizi yorumlarda paylaşır mısınız? Hangi yöntemler size en çok fayda sağladı?

## 📬 Günlük İçerikler İçin Bültenimize Katılın

Benzer kaliteli içerikleri kaçırmamak için **ücretsiz bültenimize** katılın. Her gün bir e-posta, bir sürü yeni bilgi!

## 📤 Bu İçeriği Paylaşın

Bu faydalı rehberi arkadaşlarınızla paylaşmayı unutmayın! Sosyal medya butonlarını kullanarak kolayca paylaşabilirsiniz.
"""

        filename = f"src/content/{category}/sample-listicle-{category}.md"
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(sample_content)

        print(f"✅ Örnek listicle oluşturuldu: {filename}")

    def create_interactive_content_ideas(self):
        """İnteraktif içerik fikirleri (engagement artırımı için)"""
        interactive_ideas = {
            'polls_surveys': [
                {
                    'title': 'Hangi sağlık konusunda daha fazla içerik görmek istersiniz?',
                    'options': ['Beslenme', 'Egzersiz', 'Mental Sağlık', 'Uyku Hijyeni'],
                    'category': 'health'
                },
                {
                    'title': 'İlişkilerde en zorlandığınız konu hangisi?',
                    'options': ['İletişim', 'Güven', 'Zaman Yönetimi', 'Empati'],
                    'category': 'love'
                }
            ],
            'quizzes': [
                {
                    'title': 'Sağlık Bilginizi Test Edin',
                    'questions': 10,
                    'category': 'health',
                    'reward': 'Kişiselleştirilmiş beslenme önerileri'
                },
                {
                    'title': 'Hangi Tarihsel Döneme Aitsiniz?',
                    'questions': 8,
                    'category': 'history',
                    'reward': 'Kişilik analizi raporu'
                }
            ],
            'challenges': [
                {
                    'title': '30 Günlük Sağlıklı Yaşam Challenge',
                    'duration': '30 gün',
                    'daily_tasks': True,
                    'category': 'health'
                },
                {
                    'title': '7 Günlük Pozitif Düşünce Challenge',
                    'duration': '7 gün',
                    'daily_tasks': True,
                    'category': 'psychology'
                }
            ],
            'calculators': [
                {
                    'title': 'BMI Hesaplayıcı',
                    'inputs': ['boy', 'kilo'],
                    'output': 'BMI değeri ve öneriler',
                    'category': 'health'
                },
                {
                    'title': 'Günlük Kalori İhtiyacı Hesaplayıcı',
                    'inputs': ['yaş', 'cinsiyet', 'aktivite_seviyesi'],
                    'output': 'Önerilen kalori miktarı',
                    'category': 'health'
                }
            ]
        }

        with open('interactive_content_ideas.json', 'w', encoding='utf-8') as f:
            json.dump(interactive_ideas, f, ensure_ascii=False, indent=2)

        return interactive_ideas

    def create_content_series_ideas(self):
        """İçerik serisi fikirleri (uzun dönem engagement için)"""
        series_ideas = []

        for category, info in self.categories.items():
            category_series = {
                'category': category,
                'emoji': info['emoji'],
                'series': [
                    {
                        'title': f'{category.title()} Temelleri Serisi',
                        'episodes': 5,
                        'frequency': 'haftalık',
                        'target_audience': 'başlangıç',
                        'goal': 'temel bilgi aktarımı'
                    },
                    {
                        'title': f'İleri Seviye {category.title()} Serisi',
                        'episodes': 8,
                        'frequency': '2 haftada bir',
                        'target_audience': 'ileri',
                        'goal': 'derinlemesine analiz'
                    },
                    {
                        'title': f'{category.title()} Case Study Serisi',
                        'episodes': 6,
                        'frequency': 'aylık',
                        'target_audience': 'tüm seviyeler',
                        'goal': 'gerçek örnekler'
                    }
                ]
            }
            series_ideas.append(category_series)

        # Çapraz kategori serileri
        cross_category_series = [
            {
                'title': 'Yaşam Kalitesi Artırma Serisi',
                'categories': ['health', 'psychology', 'love'],
                'episodes': 12,
                'goal': 'holistik yaklaşım'
            },
            {
                'title': 'Bilim ve Tarih Kesişimi Serisi',
                'categories': ['history', 'space', 'psychology'],
                'episodes': 8,
                'goal': 'interdisipliner perspektif'
            }
        ]

        series_data = {
            'category_series': series_ideas,
            'cross_category_series': cross_category_series,
            'implementation_guide': {
                'planning': 'Her seri için detaylı içerik takvimi oluştur',
                'consistency': 'Yayın programına sıkı sıkıya bağlı kal',
                'promotion': 'Her bölümde önceki ve sonraki bölümlere link ver',
                'engagement': 'Seri boyunca okuyucu feedback\'i topla'
            }
        }

        with open('content_series_ideas.json', 'w', encoding='utf-8') as f:
            json.dump(series_data, f, ensure_ascii=False, indent=2)

        return series_data

    def create_seasonal_content_calendar(self):
        """Mevsimsel içerik takvimi"""
        seasonal_calendar = {
            'spring': {
                'months': ['mart', 'nisan', 'mayıs'],
                'themes': ['yenilenme', 'başlangıçlar', 'doğa'],
                'content_ideas': {
                    'health': ['Bahar detoksu', 'Açık hava sporları', 'Alerjiler'],
                    'psychology': ['Motivasyon artırma', 'Yeni hedefler', 'Pozitif enerji'],
                    'love': ['Yeni ilişkiler', 'Romantik aktiviteler', 'İletişim'],
                    'history': ['Tarihte bahar', 'Yeniden doğuş hikayeleri'],
                    'space': ['Bahar takımyıldızları', 'Gezegen gözlemleri'],
                    'quotes': ['Yenilenme sözleri', 'Motivasyon alıntıları']
                }
            },
            'summer': {
                'months': ['haziran', 'temmuz', 'ağustos'],
                'themes': ['enerji', 'aktivite', 'sosyalleşme'],
                'content_ideas': {
                    'health': ['Yaz beslenme', 'Su tüketimi', 'Güneş koruması'],
                    'psychology': ['Sosyal psikoloji', 'Tatil psikolojisi', 'Mutluluk'],
                    'love': ['Yaz aşkları', 'Tatil ilişkileri', 'Açık hava randevuları'],
                    'history': ['Yaz savaşları', 'Antik olimpiyatlar'],
                    'space': ['Yaz gökyüzü', 'Meteor yağmurları'],
                    'quotes': ['Özgürlük sözleri', 'Macera alıntıları']
                }
            }
        }

        with open('seasonal_content_calendar.json', 'w', encoding='utf-8') as f:
            json.dump(seasonal_calendar, f, ensure_ascii=False, indent=2)

        return seasonal_calendar

    def slugify(self, text):
        """String'i URL slug'ına çevir"""
        import re
        text = text.lower()
        text = re.sub(r'[^a-z0-9\s-]', '', text)
        text = re.sub(r'\s+', '-', text)
        return text.strip('-')

def main():
    diversifier = ContentDiversificationSystem()

    print("🎨 MindVerse İçerik Çeşitlendirme Sistemi Başlatılıyor...")

    # FAQ sayfaları oluştur (Featured Snippet için)
    faq_content = diversifier.create_faq_pages()

    # Listicle şablonları
    listicle_ideas = diversifier.create_listicle_templates()

    # İnteraktif içerik fikirleri
    interactive_ideas = diversifier.create_interactive_content_ideas()

    # İçerik serisi fikirleri
    series_ideas = diversifier.create_content_series_ideas()

    # Mevsimsel takvim
    seasonal_calendar = diversifier.create_seasonal_content_calendar()

    print(f"""
🎯 İçerik Çeşitlendirme Sistemi Aktif!

📁 Oluşturulan İçerikler:
- FAQ sayfaları: {len(diversifier.categories)} kategori (Featured Snippet için)
- Listicle fikirleri: {len(listicle_ideas)} farklı format
- İnteraktif içerik: Quiz, anket, hesaplayıcı fikirleri
- İçerik serileri: Uzun dönem engagement planı
- Mevsimsel takvim: Yıl boyunca tema önerileri

🎪 İçerik Formatları:
✅ FAQ sayfaları (Google Featured Snippet hedefli)
✅ Listicle'lar (viral potential yüksek)
✅ How-to rehberleri (uzun kuyruk SEO)
✅ İnteraktif araçlar (engagement boost)
✅ İçerik serileri (retention artışı)

📈 Trafik Artış Stratejisi:
1. FAQ sayfaları → Featured Snippet trafiği
2. Listicle'lar → Sosyal paylaşım artışı
3. İnteraktif içerik → Time on site artışı
4. Seri içerikler → Return visitor artışı
5. Mevsimsel içerik → Trend yakalama

🚀 Bu Hafta Odağı:
- FAQ sayfalarını deploy et
- İlk listicle'ı yaz
- İnteraktif quiz prototipi oluştur

🎯 30 Gün Hedefi: İçerik çeşitliliği ile trafik %50 artış!
""")

if __name__ == "__main__":
    main()
