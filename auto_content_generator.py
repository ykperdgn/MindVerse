#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MindVerse Otomatik İçerik Üreticisi
Hibrit sistem: Ücretsiz AI + Template + Scheduling
"""

import os
import json
import random
import schedule
import time
import requests
import subprocess
from datetime import datetime, timedelta
import hashlib

class AutoContentGenerator:
    def __init__(self):
        self.base_path = "src/content"
        self.base_url = "https://www.mindversedaily.com"
        self.categories = ["health", "love", "history", "psychology", "space", "quotes"]

        # Ücretsiz AI API seçenekleri
        self.ai_apis = {
            'huggingface': {
                'url': 'https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium',
                'free_limit': 30000,  # chars/month
                'token_required': True
            },
            'cohere': {
                'url': 'https://api.cohere.ai/v1/generate',
                'free_limit': 100,  # calls/month
                'token_required': True
            },
            'groq': {
                'url': 'https://api.groq.com/openai/v1/chat/completions',
                'free_limit': 'daily',
                'token_required': True
            }
        }

        # Template-based backup system
        self.content_templates = {
            'health': [
                {
                    'title_template': '{topic} için Uzman Önerileri',
                    'topics': [
                        'Bağışıklık Sistemini Güçlendirme',
                        'Kalp Sağlığını Koruma',
                        'Stres Yönetimi Teknikleri',
                        'Sağlıklı Beslenme Alışkanlıkları',
                        'Düzenli Egzersizin Faydaları',
                        'Uyku Kalitesini İyileştirme'
                    ],
                    'content_structure': [
                        "## Giriş\n\n{topic} konusu günümüzde büyük önem taşımaktadır.",
                        "## Ana Noktalar\n\n### 1. Temel Prensipler\n{detail1}\n\n### 2. Pratik Uygulamalar\n{detail2}",
                        "## Uzman Tavsiyeleri\n\n{expert_advice}",
                        "## Sonuç\n\n{conclusion}"
                    ]
                }
            ],
            'psychology': [
                {
                    'title_template': '{topic}: Psikolojik Yaklaşımlar',
                    'topics': [
                        'Motivasyon Artırma Yöntemleri',
                        'Özgüven Geliştirme Teknikleri',
                        'Anksiyete ile Başa Çıkma',
                        'Pozitif Düşünce Alışkanlıkları',
                        'Duygusal Zeka Geliştirme',
                        'Mindfulness ve Meditasyon'
                    ]
                }
            ],
            'love': [
                {
                    'title_template': 'İlişkilerde {topic}',
                    'topics': [
                        'Etkili İletişim Kurma',
                        'Güven İnşa Etme Yolları',
                        'Çatışma Çözüme Yaklaşımları',
                        'Romantizmi Canlı Tutma',
                        'Duygusal Bağ Güçlendirme',
                        'Karşılıklı Anlayış Geliştirme'
                    ]
                }
            ]
        }

    def setup_ai_api(self, provider='huggingface', api_key=None):
        """AI API kurulumu"""
        if api_key:
            os.environ[f'{provider.upper()}_API_KEY'] = api_key
            return True
        return False

    def generate_content_with_ai(self, topic, category, provider='template'):
        """AI ile içerik üretimi"""
        if provider == 'template':
            return self.generate_template_content(topic, category)

        # Gerçek AI API entegrasyonu için placeholder
        try:
            if provider == 'huggingface':
                return self.call_huggingface_api(topic, category)
            elif provider == 'cohere':
                return self.call_cohere_api(topic, category)
            elif provider == 'groq':
                return self.call_groq_api(topic, category)
        except Exception as e:
            print(f"AI API hatası: {e}")
            # Fallback to template
            return self.generate_template_content(topic, category)

    def call_huggingface_api(self, topic, category):
        """Hugging Face API çağrısı (ücretsiz)"""
        api_key = os.getenv('HUGGINGFACE_API_KEY')
        if not api_key:
            return self.generate_template_content(topic, category)

        headers = {"Authorization": f"Bearer {api_key}"}

        prompt = f"""
        Türkçe olarak {category} kategorisinde "{topic}" başlıklı 500-700 kelimelik bir blog makalesi yaz.
        Makale SEO-friendly olsun ve şu yapıya sahip olsun:
        1. Giriş paragrafı
        2. 3-4 ana bölüm
        3. Sonuç paragrafı
        """

        payload = {
            "inputs": prompt,
            "parameters": {
                "max_length": 800,
                "temperature": 0.7
            }
        }        response = requests.post(
            self.ai_apis['huggingface']['url'],
            headers=headers,
            json=payload,
            timeout=30
        )

        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                return result[0].get('generated_text', '').replace(prompt, '').strip()

        # Fallback to template
        return self.generate_template_content(topic, category)

    def generate_template_content(self, topic, category):
        """Template tabanlı içerik üretimi - Her zaman uzun ve detaylı makaleler"""

        # Her kategori için zengin topic listesi
        category_topics = {
            'health': [
                'Bağışıklık Sistemini Güçlendirme',
                'Kalp Sağlığını Koruma',
                'Stres Yönetimi Teknikleri',
                'Sağlıklı Beslenme Alışkanlıkları',
                'Düzenli Egzersizin Faydaları',
                'Uyku Kalitesini İyileştirme',
                'Mental Sağlık ve Fiziksel Aktivite',
                'Detoksifikasyon ve Temizlik',
                'Yaşlanma Karşıtı Stratejiler'
            ],
            'psychology': [
                'Motivasyon Artırma Yöntemleri',
                'Özgüven Geliştirme Teknikleri',
                'Anksiyete ile Başa Çıkma',
                'Pozitif Düşünce Alışkanlıkları',
                'Duygusal Zeka Geliştirme',
                'Mindfulness ve Meditasyon',
                'Karar Verme Psikolojisi',
                'Sosyal Beceri Geliştirme',
                'Öfke Yönetimi Stratejileri'
            ],
            'love': [
                'Etkili İletişim Kurma',
                'Güven İnşa Etme Yolları',
                'Çatışma Çözüme Yaklaşımları',
                'Romantizmi Canlı Tutma',
                'Duygusal Bağ Güçlendirme',
                'Karşılıklı Anlayış Geliştirme',
                'İlişkilerde Sınır Belirleme',
                'Aşkın Nörokimyası',
                'Uzun Mesafeli İlişkiler'
            ],
            'history': [
                'Antik Medeniyetler',
                'Tarihi Keşifler',
                'Büyük Savaşlar',
                'Kültürel Dönüşümler',
                'Bilimsel Devrimler',
                'İmparatorlukların Yükselişi',
                'Teknolojik İlerlemeler',
                'Sosyal Hareketler'
            ],
            'space': [
                'Gezegen Keşifleri',
                'Uzay Teknolojileri',
                'Astronomi Gözlemleri',
                'Mars Misyonları',
                'Kara Delik Araştırmaları',
                'Galaksi Sistemleri',
                'Uzaydaki Yaşam Arayışı',
                'Kuantum Fiziği'
            ],
            'quotes': [
                'Motivasyonel Alıntılar',
                'Felsefe Sözleri',
                'Başarı Alıntıları',
                'Yaşam Hikmeti',
                'İlham Verici Sözler',
                'Büyük Düşünürler',
                'Modern Motivasyon',
                'Antik Hikmetler'
            ]
        }

        # Seçilen kategoriden rastgele topic al veya verilen topic'i kullan
        if topic in category_topics.get(category, []):
            selected_topic = topic
        else:
            # Eğer verilen topic listede yoksa, kategoriye uygun rastgele birini seç
            selected_topic = random.choice(category_topics.get(category, [topic]))

        # Her zaman uzun ve detaylı makale üret
        content = f"""
## {selected_topic}

{selected_topic} konusu günümüzde büyük önem taşımaktadır. Bu kapsamlı rehberde {selected_topic.lower()} hakkında derinlemesine bilgiler, uzman önerileri ve pratik çözümler sunacağız.

### Giriş

Modern yaşamın karmaşık dinamikleri içinde {selected_topic.lower()} konusu, hem bireysel gelişim hem de genel yaşam kalitesi açısından kritik bir rol oynamaktadır. Son yıllarda yapılan araştırmalar, bu alandaki gelişmelerin ne kadar önemli olduğunu gözler önüne sermektedir.

### Temel Prensipler ve Bilimsel Yaklaşım

{selected_topic} ile ilgili temel bilgiler ve güncel bilimsel yaklaşımlar şu şekilde özetlenebilir:

#### 1. Teorik Temeller
- Konuyla ilgili temel kavramları anlamak
- Bilimsel literatürdeki son gelişmeleri takip etmek
- Farklı perspektiflerden konuya yaklaşmak
- Eleştirel düşünme becerileri geliştirmek

#### 2. Pratik Uygulamalar
- Günlük hayatta uygulanabilir stratejiler
- Adım adım uygulama rehberleri
- Yaygın hataları önleme yöntemleri
- Başarı ölçütleri ve değerlendirme kriterleri

### Detaylı Öneriler ve Stratejiler

#### A. Başlangıç Seviyesi İçin:

1. **Temel Araştırma Yapın**
   - Konuyla ilgili güncel ve güvenilir kaynaklardan bilgi edinin
   - Akademik makaleler, uzman görüşleri ve vaka çalışmalarını inceleyin
   - Farklı görüşleri karşılaştırarak objektif bir yaklaşım benimseyin

2. **Uzman Görüşü Alın**
   - Alanında deneyimli kişilerden tavsiyeleri dinleyin
   - Mentörlük ilişkileri kurarak sürekli öğrenim sağlayın
   - Profesyonel ağlarınızı genişleterek bilgi paylaşımında bulunun

3. **Adım Adım İlerleyin**
   - Büyük hedeflerinizi küçük, yönetilebilir parçalara bölün
   - Her aşamada somut başarılar elde etmeye odaklanın
   - İlerlemenizi düzenli olarak değerlendirin ve gerektiğinde ayarlamalar yapın

#### B. İleri Seviye Uygulamalar:

1. **Derinlemesine Analiz**
   - Konunun farklı boyutlarını kapsamlı şekilde inceleyin
   - Neden-sonuç ilişkilerini analiz edin
   - Uzun vadeli etkileri değerlendirin

2. **Yenilikçi Yaklaşımlar**
   - Geleneksel yöntemlerin yanı sıra yaratıcı çözümler geliştirin
   - Teknoloji destekli araçları etkin şekilde kullanın
   - Sürekli iyileştirme anlayışını benimseyin

### Önemli Hususlar ve Dikkat Edilmesi Gerekenler

{selected_topic} konusunda dikkat edilmesi gereken kritik noktalar:

- **Bilimsel Yaklaşım:** Kanıtlanmış yöntemleri tercih edin ve spekülatif bilgilerden kaçının
- **Bireyselleştirme:** Her bireyin farklı ihtiyaçları olduğunu göz önünde bulundurun
- **Süreklilik:** Düzenli uygulama ve sabır gerektiren bir süreç olduğunu unutmayın
- **Esneklik:** Değişen koşullara adapte olabilecek esnek stratejiler geliştirin
- **Sürekli Öğrenme:** Bu alanda sürekli gelişen bilgiye açık olun

### Yaygın Hatalar ve Çözüm Önerileri

Bu alanda sıkça karşılaşılan hatalar ve bunlara yönelik çözüm önerileri:

1. **Acele Etmek:** Sonuçları hemen beklemek yerine sabırlı olmak
2. **Tek Boyutlu Yaklaşım:** Konuyu sadece bir açıdan değerlendirmek
3. **Süreklilik Eksikliği:** Düzenli uygulama yapmamak
4. **Uzman Desteğini İhmal Etmek:** Kendi kendine çözmeye çalışmak

### Gelecek Perspektifleri ve Trendler

{selected_topic} alanında gelecekte beklenen gelişmeler:

- Teknolojik yeniliklerin rolü
- Bilimsel araştırmalardaki yeni bulgular
- Toplumsal değişimlerin etkileri
- Küresel trendler ve yerel uygulamalar

### Kategori Özel İçerik - {category.title()}

{self._get_category_specific_content(category, selected_topic)}

### Sonuç ve Eylem Planı

{selected_topic} hakkında edindiğiniz bu kapsamlı bilgileri pratik hayatınızda uygulamaya geçirmek için:

1. **Kısa Vadeli Hedefler (1-3 ay):**
   - Temel kavramları öğrenin
   - Basit uygulamaları hayatınıza entegre edin
   - İlk sonuçları gözlemleyin

2. **Orta Vadeli Hedefler (3-12 ay):**
   - Daha karmaşık stratejileri uygulayın
   - Uzman desteği alın
   - Sürekli iyileştirmeler yapın

3. **Uzun Vadeli Hedefler (1+ yıl):**
   - Konuda uzmanlaşın
   - Deneyimlerinizi başkalarıyla paylaşın
   - Sürekli öğrenme ve gelişim sürecini devam ettirin

Unutmayın ki her bireyin ihtiyaçları farklıdır ve kişiselleştirilmiş yaklaşımlar her zaman daha etkili sonuçlar verir. Bu konuda daha fazla bilgi için diğer makalelerimizi inceleyebilir, uzman tavsiyeleri alabilir ve sürekli öğrenme yolculuğunuza devam edebilirsiniz.

**Önemli Not:** Bu rehberdeki öneriler genel bilgilendirme amaçlıdır. Spesifik durumlar için mutlaka uzman görüşü alınmalıdır.
"""

        return content.strip()

    def _get_category_specific_content(self, category, topic):
        """Kategori-spesifik içerik üretir"""
        category_content = {
            'health': f"""
#### Sağlık Uzmanlarının Önerileri

{topic} konusunda sağlık uzmanları şu önerilerde bulunmaktadır:

- **Beslenme:** Dengeli ve sağlıklı beslenme alışkanlıkları
- **Egzersiz:** Düzenli fiziksel aktivite programları
- **Uyku:** Kaliteli ve yeterli uyku düzeni
- **Stres Yönetimi:** Etkili stres azaltma teknikleri
- **Periyodik Kontrol:** Düzenli sağlık muayeneleri

#### Bilimsel Araştırmalar

Son araştırmaların gösterdiği üzere, {topic.lower()} konusunda yapılan çalışmalar umut verici sonuçlar ortaya koymaktadır. Özellikle:

- Kapsamlı veri analizleri
- Uzun vadeli gözlem çalışmaları
- Klinik test sonuçları
- Meta-analiz bulguları""",

            'psychology': f"""
#### Psikolojik Yaklaşımlar

{topic} konusunda psikoloji alanından öneriler:

- **Bilişsel Terapi:** Düşünce kalıplarını yeniden yapılandırma
- **Davranışsal Teknikler:** Pozitif alışkanlık oluşturma
- **Mindfulness:** Farkındalık ve meditasyon pratikleri
- **Sosyal Destek:** İnsan ilişkilerinin önemi
- **Kişisel Gelişim:** Sürekli öğrenme ve büyüme

#### Psikolojik Araştırmalar

Yapılan psikolojik araştırmalar {topic.lower()} konusunda şu sonuçları ortaya koymaktadır:

- Nörolojik etki mekanizmaları
- Davranışsal değişim modelleri
- Sosyal psikoloji bulguları
- Gelişimsel psikoloji perspektifleri""",

            'love': f"""
#### İlişki Uzmanlarının Tavsiyeleri

{topic} konusunda ilişki uzmanları şu önerilerde bulunmaktadır:

- **İletişim:** Açık ve dürüst iletişim kurma
- **Empati:** Karşılıklı anlayış geliştirme
- **Kalite Zaman:** Birlikte geçirilen anlamlı zamanlar
- **Güven:** Karşılıklı güven inşa etme
- **Büyüme:** Birlikte gelişim ve büyüme

#### Aşk ve İlişki Araştırmaları

Modern araştırmalar {topic.lower()} konusunda şu bulgulara işaret etmektedir:

- Nörobiyolojik süreçler
- Bağlanma teorileri
- İletişim kalıpları
- Uzun vadeli ilişki başarı faktörleri""",

            'history': f"""
#### Tarihçi Perspektifleri

{topic} konusunda tarih uzmanları şu yaklaşımları benimser:

- **Kaynak Analizi:** Birincil ve ikincil kaynakların incelenmesi
- **Bağlam:** Tarihsel olayların çağdaş koşullar içinde değerlendirilmesi
- **Karşılaştırmalı Analiz:** Farklı dönem ve bölgelerle karşılaştırma
- **Süreklilik:** Tarihsel süreçlerin günümüze etkileri
- **Objektiflik:** Önyargısız ve bilimsel yaklaşım

#### Tarihsel Araştırmalar

{topic.lower()} konusundaki son tarihsel araştırmalar:

- Arkeolojik bulgular
- Yeni keşfedilen belgeler
- Teknolojik analiz yöntemleri
- İnterdisipliner çalışmalar""",

            'space': f"""
#### Uzay Bilimcilerinin Görüşleri

{topic} konusunda uzay bilimcileri şu yaklaşımları önerir:

- **Gözlem:** Sistematik ve teknoloji destekli gözlemler
- **Teorik Modeller:** Matematiksel ve fiziksel modelleme
- **Deneysel Araştırma:** Laboratuvar ve uzay misyonları
- **Teknolojik Yenilik:** Sürekli teknoloji geliştirme
- **Uluslararası İşbirliği:** Küresel bilimsel ortaklıklar

#### Uzay Araştırmaları

{topic.lower()} alanındaki güncel araştırmalar:

- Teleskop gözlemleri
- Uzay misyonu verileri
- Teorik fizik çalışmaları
- Teknolojik gelişimler""",

            'quotes': f"""
#### Büyük Düşünürlerin Sözleri

{topic} konusunda tarih boyunca büyük düşünürler şu sözleri söylemiştir:

- **Antik Filozoflar:** Yaşam hikmeti ve değerler
- **Modern Myasgalarımızler:** Çağdaş görüşler ve perspektifler
- **Bilim İnsanları:** Akıl ve mantık temelli yaklaşımlar
- **Sanatçılar:** Yaratıcılık ve ilham
- **Liderler:** Vizyoner düşünce ve liderlik

#### Motivasyonel Araştırmalar

{topic.lower()} konusundaki motivasyon araştırmaları:

- Psikolojik etki mekanizmaları
- Davranışsal değişim süreçleri
- Başarı hikayeleri analizi
- Kişisel gelişim modelleri"""
        }

        return category_content.get(category, f"""
#### Uzman Değerlendirmeleri

{topic} konusunda uzmanlar genel olarak şu yaklaşımları önermektedir:

- Bilimsel temelli yaklaşımlar
- Kanıtlanmış metodolojiler
- Sürekli öğrenme anlayışı
- Pratik uygulama becerileri
- Eleştirel düşünme yetenekleri

#### Araştırma Sonuçları

Bu alandaki son araştırmalar umut verici sonuçlar göstermektedir ve {topic.lower()} konusunda yeni perspektifler sunmaktadır.
""")

    def create_article_file(self, title, content, category):
        """Makale dosyası oluşturma"""
        # Tarih ve unique ID
        now = datetime.now()
        date_str = now.strftime('%Y-%m-%d')
        unique_id = hashlib.md5(f"{title}{now}".encode()).hexdigest()[:8]        # Slug oluşturma
        slug = title.lower()
        slug = slug.replace(' ', '-')
        slug = slug.replace('ı', 'i').replace('ğ', 'g').replace('ü', 'u')
        slug = slug.replace('ş', 's').replace('ö', 'o').replace('ç', 'c')
        slug = ''.join(c for c in slug if c.isalnum() or c == '-')

        # Front matter (views kaldırıldı)
        frontmatter = f"""---
title: '{title}'
date: {now.strftime('%Y-%m-%d')}
summary: '{title} hakkında detaylı rehber ve uzman önerileri.'
tags: ['{category}', 'rehber', 'uzman-tavsiyeleri']
---

"""

        # Tam içerik
        full_content = frontmatter + content

        # Dosya yolu
        filename = f"{date_str}-{slug}-{unique_id}.md"
        file_path = os.path.join(self.base_path, category, filename)

        # Dizin oluştur
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Dosyayı yaz
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(full_content)

        print(f"✅ Yeni makale oluşturuldu: {filename}")

        # Git commit ve push (otomatik yayınlama için)
        self.auto_deploy_article(filename, title, category)

        return file_path

    def auto_deploy_article(self, filename, title, category):
        """Otomatik Git commit ve deploy"""
        try:
            # Git add
            subprocess.run(['git', 'add', '.'], check=True, cwd='.')

            # Git commit
            commit_message = f"🤖 Otomatik makale: {title} ({category})"
            subprocess.run(['git', 'commit', '-m', commit_message], check=True, cwd='.')

            # Git push (Vercel otomatik deploy)
            subprocess.run(['git', 'push'], check=True, cwd='.')

            print(f"🚀 Site otomatik güncellendi: {filename}")
            print(f"📡 Vercel'de build başlatıldı...")

        except subprocess.CalledProcessError as e:
            print(f"⚠️ Git işlemi başarısız: {e}")
            print("📝 Makale oluşturuldu ama manuel commit gerekiyor")

    def generate_daily_content(self):
        """Günlük içerik üretimi"""
        print(f"🤖 Günlük içerik üretimi başlıyor... {datetime.now().strftime('%Y-%m-%d %H:%M')}")

        # Rastgele kategori seç
        category = random.choice(self.categories)

        # Kategori için topic listesi
        topics = {
            'health': [
                'Sağlıklı Beslenme Rehberi',
                'Egzersiz Programı Hazırlama',
                'Stres Yönetimi Teknikleri',
                'Uyku Düzeni Optimizasyonu',
                'Bağışıklık Sistemi Güçlendirme'
            ],
            'psychology': [
                'Motivasyon Artırma Yöntemleri',
                'Özgüven Geliştirme',
                'Mindfulness Teknikleri',
                'Duygusal Zeka Geliştirme',
                'Pozitif Düşünce Alışkanlıkları'
            ],
            'love': [
                'Sağlıklı İlişki Kurma',
                'Etkili İletişim Teknikleri',
                'Çift Terapisi Yöntemleri',
                'Romantizmi Canlı Tutma',
                'İlişkilerde Güven İnşası'
            ],
            'history': [
                'Antik Medeniyetler',
                'Tarihi Keşifler',
                'Dünya Savaşları',
                'Kültürel Dönüşümler',
                'Bilimsel Devrimler'
            ],
            'space': [
                'Gezegen Keşifleri',
                'Uzay Teknolojileri',
                'Astronomi Gözlemleri',
                'Mars Misyonları',
                'Kara Delik Araştırmaları'
            ],
            'quotes': [
                'Motivasyonel Alıntılar',
                'Felsefe Sözleri',
                'Başarı Alıntıları',
                'Yaşam Hikmeti',
                'İlham Verici Sözler'
            ]
        }        # Rastgele topic seç
        topic = random.choice(topics.get(category, ['Genel Konu']))

        # İçerik üret
        content = self.generate_content_with_ai(topic, category, 'template')

        # Makale dosyası oluştur
        self.create_article_file(topic, content, category)

        print(f"✅ {category} kategorisinde '{topic}' makalesi oluşturuldu!")

    def schedule_content_generation(self):
        """İçerik üretimi programlama"""        # TEST - 3 dakika sonra
        schedule.every().day.at("23:20").do(self.generate_daily_content)

        # Normal çalışma saati
        schedule.every().day.at("23:00").do(self.generate_daily_content)

        # Hafta sonu ekstra makale
        schedule.every().saturday.at("15:00").do(self.generate_daily_content)

        print("📅 Otomatik içerik üretimi programlandı:")
        print("   - TEST: Bugün 23:20 (3 dakika sonra!)")
        print("   - Normal: Her gün 23:00")
        print("   - Cumartesi 15:00: Ekstra makale")

        while True:
            schedule.run_pending()
            time.sleep(60)  # Her dakika kontrol

    def generate_weekly_batch(self):
        """Haftalık toplu içerik üretimi"""
        print("🚀 Haftalık toplu içerik üretimi başlıyor...")

        # Her kategoriden 1-2 makale
        for category in self.categories:
            topics = {
                'health': ['Sağlıklı Yaşam Rehberi', 'Beslenme Önerileri'],
                'psychology': ['Zihinsel Sağlık', 'Motivasyon Teknikleri'],
                'love': ['İlişki Tavsiyeleri', 'İletişim Becerileri'],
                'history': ['Tarihi Olaylar', 'Medeniyetler'],
                'space': ['Uzay Keşifleri', 'Astronomi'],
                'quotes': ['İlham Sözleri', 'Motivasyon']
            }

            for topic in topics.get(category, ['Genel Konu']):
                content = self.generate_content_with_ai(topic, category, 'template')
                self.create_article_file(topic, content, category)
                time.sleep(1)  # API rate limit için

        print("✅ Haftalık içerik üretimi tamamlandı!")

def main():
    generator = AutoContentGenerator()

    print("""
🤖 MindVerse Otomatik İçerik Üreticisi

Seçenekler:
1. Tek makale üret (test)
2. Haftalık toplu üretim
3. Otomatik program başlat (günlük)
4. AI API kurulumu
""")

    choice = input("Seçiminiz (1-4): ").strip()

    if choice == '1':
        generator.generate_daily_content()
    elif choice == '2':
        generator.generate_weekly_batch()
    elif choice == '3':
        generator.schedule_content_generation()
    elif choice == '4':
        print("""
AI API Kurulumu:

1. Hugging Face (Ücretsiz): https://huggingface.co/settings/tokens
2. Cohere (Ücretsiz trial): https://dashboard.cohere.ai/api-keys
3. Groq (Ücretsiz): https://console.groq.com/keys

API key aldıktan sonra:
generator.setup_ai_api('huggingface', 'your_api_key_here')
""")
    else:
        print("❌ Geçersiz seçim!")

if __name__ == "__main__":
    main()
