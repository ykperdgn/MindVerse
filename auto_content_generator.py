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
        }

        response = requests.post(
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
        """Template tabanlı içerik üretimi"""
        templates = self.content_templates.get(category, [])
        if not templates:
            # Generic template
            content = f"""
## {topic}

{topic} konusu günümüzde büyük önem taşımaktadır. Bu makalede {topic.lower()} hakkında detaylı bilgiler ve pratik öneriler sunacağız.

### Temel Bilgiler

{topic} ile ilgili temel bilgiler ve güncel yaklaşımlar aşağıda açıklanmaktadır.

### Pratik Öneriler

1. **Araştırma Yapın**: Konuyla ilgili güncel kaynaklardan bilgi edinin
2. **Uzman Görüşü Alın**: Alanında uzman kişilerden tavsiyeleri dinleyin
3. **Adım Adım İlerleyin**: Hedeflerinize aşamalı olarak ulaşın
4. **Sabırlı Olun**: Değişim için zaman tanıyın

### Önemli Noktalar

{topic} konusunda dikkat edilmesi gereken önemli noktalar:

- Bilimsel yaklaşımları tercih edin
- Kanıtlanmış yöntemleri uygulayın
- Bireysel farklılıkları göz önünde bulundurun
- Sürekli öğrenmeye açık olun

### Sonuç

{topic} hakkında edindiğiniz bilgileri pratik hayatınızda uygulayarak olumlu değişiklikler yaratabilirsiniz. Unutmayın ki her bireyin ihtiyaçları farklıdır ve kişiselleştirilmiş yaklaşımlar daha etkili olur.

Bu konuda daha fazla bilgi için diğer makalelerimizi inceleyebilir ve uzman tavsiyeleri alabilirsiniz.
"""
        else:
            template = random.choice(templates)
            topic_item = random.choice(template['topics'])
            content = f"""
## {topic_item}

{topic_item} konusu modern yaşamın önemli bir parçasıdır. Bu rehberde {topic_item.lower()} hakkında kapsamlı bilgiler bulacaksınız.

### Temel Yaklaşımlar

Uzmanlar {topic_item.lower()} konusunda şu temel yaklaşımları önermektedir:

1. **Bilimsel Temeller**: Kanıtlanmış yöntemleri tercih edin
2. **Kişisel Uyum**: Bireysel ihtiyaçlarınıza göre adapte edin
3. **Süreklilik**: Düzenli uygulamaya önem verin
4. **Sabır**: Sonuçlar için zaman tanıyın

### Pratik Uygulamalar

{topic_item} için önerilen praktik uygulamalar:

- Günlük rutinler oluşturun
- Hedeflerinizi belirleyin
- İlerlemenizi takip edin
- Gerektiğinde destek alın

### Yaygın Hatalar

Bu konuda yapılan yaygın hatalardan kaçının:

- Aşırı beklentiler
- Tutarsız uygulama
- Uzman desteğini ihmal etme
- Bireysel farklılıkları görmezden gelme

### Sonuç ve Öneriler

{topic_item} konusunda başarılı olmak için sabırlı, tutarlı ve bilgili yaklaşım sergilemek önemlidir. Bu rehberdeki önerileri hayatınıza adapte ederek olumlu değişiklikler yaratabilirsiniz.
"""

        return content.strip()

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
