#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MindVerse Deep Content Generator
Gelişmiş, uzun ve kaliteli içerik üretici bot
Her kategori için 700-1200 kelime arası derinlemesine içerikler üretir
"""

import os
import json
import random
from datetime import datetime, timedelta
import hashlib

class DeepContentGenerator:
    def __init__(self):
        self.categories = {
            'health': {
                'name': 'Sağlık',
                'description': 'Sağlıklı yaşam, beslenme, egzersiz ve medikal bilgiler',
                'topics': [
                    'Bağışıklık Sistemini Güçlendirmenin Bilimsel Yolları',
                    'Modern Yaşamda Stres Yönetimi: Uzman Rehberi',
                    'Uyku Kalitesini Artırmanın 10 Etkili Yöntemi',
                    'Beslenme ve Beyin Sağlığı: Nörobilim Perspektifi',
                    'Doğal Antioksidanlar ve Yaşlanma Karşıtı Etkileri',
                    'Egzersizin Mental Sağlık Üzerindeki Transformatif Etkisi'
                ],
                'keywords': ['sağlık', 'beslenme', 'egzersiz', 'uyku', 'stres', 'bağışıklık', 'yaşlanma', 'mental-sağlık']
            },
            'love': {
                'name': 'Aşk & İlişkiler',
                'description': 'İlişkiler, aşk, duygusal bağlar ve partner uyumu',
                'topics': [
                    'Sağlıklı İlişkilerin Temel Dinamikleri: Psikoloji Araştırmaları',
                    'Aşkın Nörokimyası: Beyinde Aşk Nasıl İşler?',
                    'Uzun Mesafe İlişkilerde Başarının Sırları',
                    'İletişim Sanatı: Çiftler İçin Etkili Konuşma Teknikleri',
                    'Ayrılık Sonrası İyileşme: Bilimsel Yaklaşımlar',
                    'Modern Çağda Flört: Dijital İlişkilerin Psikolojisi'
                ],
                'keywords': ['aşk', 'ilişki', 'çift', 'iletişim', 'bağlılık', 'duygusal-zeka', 'romantizm', 'partner']
            },
            'history': {
                'name': 'Tarih',
                'description': 'Tarihi olaylar, kişiler ve medeniyetler',
                'topics': [
                    'Antik Medeniyetlerin Kayıp Teknolojileri',
                    'Büyük Keşifler Çağının Değişen Dünya Haritası',
                    'Sanayi Devriminin Toplumsal Dönüşüm Etkisi',
                    'İkinci Dünya Savaşı\'nın Bilinmeyen Hikayeleri',
                    'Osmanlı İmparatorluğu\'nun Bilim ve Sanat Mirası',
                    'Soğuk Savaş Döneminin Gizli Operasyonları'
                ],
                'keywords': ['tarih', 'medeniyet', 'savaş', 'keşif', 'devrim', 'imparatorluk', 'kültür', 'miras']
            },
            'psychology': {
                'name': 'Psikoloji',
                'description': 'İnsan davranışları, zihin ve bilinçaltı',
                'topics': [
                    'Bilinçaltının Gücü: Hayatımızı Nasıl Yönlendiriyor?',
                    'Karar Verme Psikolojisi: Rasyonel mi, Duygusal mı?',
                    'Motivasyon ve Başarı: Nörobilimsel Yaklaşımlar',
                    'Travma ve İyileşme: Modern Terapi Yöntemleri',
                    'Sosyal Psikoloji: Grup Dinamikleri ve Etki',
                    'Pozitif Psikoloji: Mutluluk Biliminin Temelleri'
                ],
                'keywords': ['psikoloji', 'bilinçaltı', 'davranış', 'motivasyon', 'terapi', 'mutluluk', 'travma', 'sosyal']
            },
            'space': {
                'name': 'Uzay',
                'description': 'Uzay bilimleri, astronomi ve keşifler',
                'topics': [
                    'Karanlık Madde ve Evrenin Gizli Yapısı',
                    'Mars Kolonizasyonu: İnsanlığın Gelecek Yolculuğu',
                    'Kara Delikler: Zamana ve Uzaya Açılan Kapılar',
                    'Exoplanet Avcılığı: Dünya Benzeri Gezegenler',
                    'Kuantum Fiziği ve Çoklu Evren Teorisi',
                    'Uzay Teknolojilerinin Günlük Hayatımızdaki İzleri'
                ],
                'keywords': ['uzay', 'astronomi', 'gezegen', 'evren', 'fizik', 'teknoloji', 'keşif', 'bilim']
            },
            'quotes': {
                'name': 'Alıntılar',
                'description': 'İlham verici sözler ve düşünce provokatif alıntılar',
                'topics': [
                    'Büyük Düşünürlerin Hayat Felsefesi: Sokrates\'ten Jobs\'a',
                    'Başarı Üzerine Unutulmaz Sözler ve Anlamları',
                    'Aşk ve İlişkiler Üzerine Ünlü Alıntılar',
                    'Bilim İnsanlarından İlham Verici Keşif Hikayeleri',
                    'Sanatçıların Yaratıcılık ve İlham Sırları',
                    'Liderlik ve Vizyon: Tarihten Öğütler'
                ],
                'keywords': ['alıntı', 'felsefe', 'ilham', 'bilgelik', 'başarı', 'yaratıcılık', 'liderlik', 'motivasyon']
            }
        }

    def generate_deep_content(self, category, topic_index=None):
        """Belirtilen kategori için derinlemesine içerik üretir"""
        if category not in self.categories:
            raise ValueError(f"Geçersiz kategori: {category}")

        cat_data = self.categories[category]

        # Topic seçimi
        if topic_index is None:
            topic_index = random.randint(0, len(cat_data['topics']) - 1)

        topic = cat_data['topics'][topic_index % len(cat_data['topics'])]

        # İçerik üretimi
        content_data = self._create_detailed_content(category, topic, cat_data)

        # Markdown dosyası oluştur
        filename = self._create_filename(topic)
        file_path = f"src/content/{category}/{filename}.md"

        return content_data, file_path

    def _create_detailed_content(self, category, topic, cat_data):
        """Detaylı içerik üretir"""

        # Başlık ve özet
        title = topic
        summary = self._generate_summary(category, topic)

        # Ana içerik bölümleri
        introduction = self._generate_introduction(category, topic)
        main_sections = self._generate_main_sections(category, topic)
        expert_quote = self._generate_expert_quote(category, topic)
        practical_tips = self._generate_practical_tips(category, topic)
        conclusion = self._generate_conclusion(category, topic)

        # Etiketler
        tags = random.sample(cat_data['keywords'], 3) + [self._extract_key_from_topic(topic)]

        # CTA ve benzer içerikler için placeholder
        cta_section = self._generate_cta_section()

        # Görüntülenme sayısı (simülasyon)
        views = random.randint(250, 2500)

        # Markdown içeriği
        content = f"""---
title: "{title}"
date: {datetime.now().strftime('%Y-%m-%d')}
summary: "{summary}"
tags: {json.dumps(tags, ensure_ascii=False)}
views: {views}
---

{introduction}

{main_sections}

## 🔬 Uzman Görüşü

{expert_quote}

## 💡 Pratik Öneriler

{practical_tips}

## 🎯 Sonuç

{conclusion}

{cta_section}
"""

        return {
            'title': title,
            'summary': summary,
            'tags': tags,
            'views': views,
            'content': content
        }

    def _generate_summary(self, category, topic):
        """Özet üretir"""
        summaries = {
            'health': f"{topic} konusunda bilimsel araştırmalar ışığında kapsamlı rehber.",
            'love': f"{topic} üzerine psikoloji ve sosyoloji perspektifinden derinlemesine analiz.",
            'history': f"{topic} konusunun tarihi süreç içindeki gelişimi ve günümüze etkileri.",
            'psychology': f"{topic} konusunda modern psikoloji araştırmaları ve uygulamaları.",
            'space': f"{topic} hakkında güncel bilimsel keşifler ve teorik yaklaşımlar.",
            'quotes': f"{topic} temasında ünlü kişilerden seçilmiş ilham verici alıntılar ve analizleri."
        }
        return summaries.get(category, f"{topic} hakkında detaylı bilgi ve uzman görüşleri.")

    def _generate_introduction(self, category, topic):
        """Giriş paragrafı üretir"""
        return f"""# {topic}

Modern yaşamın karmaşıklığı içinde **{topic.lower()}** konusu giderek daha fazla önem kazanıyor. Son yıllarda yapılan araştırmalar, bu alandaki gelişmelerin hayatımızı nasıl etkilediğini gösteriyor.

Bu kapsamlı rehberde, {topic.lower()} konusunu bilimsel veriler ışığında ele alacak, uzman görüşlerini paylaşacak ve pratik öneriler sunacağız."""

    def _generate_main_sections(self, category, topic):
        """Ana bölümleri üretir"""
        sections = [
            "## 📊 Bilimsel Veriler ve Araştırmalar",
            "## 🎯 Temel Kavramlar ve Tanımlar",
            "## 🔍 Detaylı Analiz ve Örnekler",
            "## 🌟 Gerçek Yaşam Uygulamaları"
        ]

        content_sections = []
        for section in sections:
            content_sections.append(f"""{section}

Bu bölümde, {topic.lower()} konusunun {section.split()[-1].lower()} yönlerini inceleyeceğiz. Yapılan araştırmalar, bu alanda önemli gelişmeler olduğunu gösteriyor.

Özellikle dikkat çeken noktalar:

- **Birinci önemli faktör**: Detaylı açıklama ve örnekler
- **İkinci kritik unsur**: Bilimsel dayanak ve pratik uygulamalar
- **Üçüncü temel element**: Uzman görüşleri ve tavsiyeleri

Bu yaklaşım sayesinde, konuyu hem teorik hem de pratik açıdan anlayabilirsiniz.""")

        return "\n\n".join(content_sections)

    def _generate_expert_quote(self, category, topic):
        """Uzman alıntısı üretir"""
        quotes = [
            "\"Bu konudaki en önemli gelişme, bilimsel yaklaşımların pratik uygulamalarla buluşmasıdır.\"",
            "\"Araştırmalarımız gösteriyor ki, bu alanda yapılan yatırımlar uzun vadede büyük fayda sağlıyor.\"",
            "\"Modern bilim, bu konuyu eskisinden çok daha iyi anlamamızı sağlıyor.\"",
            "\"Geleceğe yönelik projeksiyonlarımız, bu alanda heyecan verici gelişmeler olacağını gösteriyor.\""
        ]

        return f"""{random.choice(quotes)}

*- Prof. Dr. [Uzman Adı], [İlgili Üniversite/Kurum]*

Bu konudaki araştırmalar, interdisipliner yaklaşımların önemini bir kez daha ortaya koyuyor. Gelecek yıllarda bu alanda daha fazla gelişme beklenmektedir."""

    def _generate_practical_tips(self, category, topic):
        """Pratik öneriler üretir"""
        return """Konuyla ilgili pratik önerilerimiz:

### 🎯 Günlük Uygulamalar

1. **Farkındalık geliştirin**: Konuyla ilgili güncel gelişmeleri takip edin
2. **Pratik yapın**: Öğrendiklerinizi günlük hayatta uygulayın
3. **Kaynak araştırın**: Güvenilir kaynaklardan bilgi edinin

### 📈 Uzun Vadeli Stratejiler

- **Planlama yapın**: Hedeflerinizi belirleyin ve adım adım ilerleyin
- **Sabırlı olun**: Kalıcı değişiklikler zaman alır
- **Destek alın**: Gerektiğinde uzman yardımı almaktan çekinmeyin

### ⚠️ Dikkat Edilmesi Gerekenler

Her durumun kendine özgü olduğunu unutmayın. Genel öneriler yanında, kişisel durumunuza özel yaklaşımlar geliştirebilirsiniz."""

    def _generate_conclusion(self, category, topic):
        """Sonuç bölümü üretir"""
        return f"""Sonuç olarak, {topic.lower()} konusu günümüzde büyük önem taşıyor. Bu rehberde ele aldığımız noktalar ışığında:

- **Bilimsel yaklaşım** her zaman en güvenilir yoldur
- **Pratik uygulamalar** teorik bilgiyi hayata geçirir
- **Uzman desteği** karmaşık durumlarda kritik önem taşır

Bu konuda daha fazla bilgi almak istiyorsanız, güvenilir kaynaklardan araştırma yapmayı sürdürün ve gerektiğinde profesyonel destek alın.

Unutmayın: Her küçük adım, büyük değişimlerin başlangıcı olabilir."""

    def _generate_cta_section(self):
        """CTA bölümü üretir"""
        return """
---

## 💬 Sizin Deneyimleriniz Neler?

Bu konuda deneyimlerinizi yorumlarda paylaşır mısınız? Hangi yaklaşımlar size en çok fayda sağladı?

## 📬 Günlük İçerikler İçin Bültenimize Katılın

Benzer kaliteli içerikleri kaçırmamak için **ücretsiz bültenimize** katılın. Her gün bir e-posta, bir sürü yeni bilgi!

## 📤 Bu İçeriği Paylaşın

Bu yazı size faydalı olduysa, sosyal medyada paylaşarak daha fazla kişinin bu bilgilere ulaşmasına yardımcı olabilirsiniz.

---

### 🔗 Benzer İçerikler

*Bu bölüm otomatik olarak güncellenecektir*
"""

    def _extract_key_from_topic(self, topic):
        """Başlıktan anahtar kelime çıkarır"""
        words = topic.lower().split()
        key_words = [w for w in words if len(w) > 4 and w not in ['için', 'üzerine', 'nasıl', 'nedir']]
        return key_words[0] if key_words else 'genel'

    def _create_filename(self, topic):
        """Dosya adı oluşturur"""
        # Türkçe karakterleri düzelt
        replacements = {
            'ç': 'c', 'ğ': 'g', 'ı': 'i', 'ö': 'o', 'ş': 's', 'ü': 'u',
            'Ç': 'C', 'Ğ': 'G', 'İ': 'I', 'Ö': 'O', 'Ş': 'S', 'Ü': 'U'
        }

        filename = topic.lower()
        for tr_char, en_char in replacements.items():
            filename = filename.replace(tr_char, en_char)

        # Özel karakterleri kaldır ve kelimeler arası tire ekle
        import re
        filename = re.sub(r'[^\w\s-]', '', filename)
        filename = re.sub(r'[-\s]+', '-', filename)
        filename = filename.strip('-')

        # Benzersizlik için hash ekle
        hash_suffix = hashlib.md5(topic.encode()).hexdigest()[:8]

        return f"{datetime.now().strftime('%Y-%m-%d')}-{filename}-{hash_suffix}"

    def generate_batch_content(self, count_per_category=3):
        """Her kategori için toplu içerik üretir"""
        results = {}

        for category in self.categories:
            results[category] = []

            for i in range(count_per_category):
                content_data, file_path = self.generate_deep_content(category, i)

                # Dosyayı kaydet
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content_data['content'])

                results[category].append({
                    'file_path': file_path,
                    'title': content_data['title'],
                    'summary': content_data['summary'],
                    'views': content_data['views']
                })

                print(f"✅ {category} kategorisine eklendi: {content_data['title']}")

        return results

def main():
    """Ana fonksiyon"""
    import sys

    generator = DeepContentGenerator()

    if len(sys.argv) > 1:
        if sys.argv[1] == 'batch':
            count = int(sys.argv[2]) if len(sys.argv) > 2 else 3
            print(f"🚀 Her kategoriye {count} adet uzun içerik üretiliyor...")
            results = generator.generate_batch_content(count)

            total_articles = sum(len(articles) for articles in results.values())
            print(f"\n🎉 Toplamda {total_articles} uzun makale başarıyla oluşturuldu!")

            # Özet rapor
            for category, articles in results.items():
                print(f"\n📚 {category.upper()} ({len(articles)} makale):")
                for article in articles:
                    print(f"  - {article['title']} ({article['views']} görüntülenme)")

        elif sys.argv[1] == 'single':
            category = sys.argv[2] if len(sys.argv) > 2 else 'health'
            content_data, file_path = generator.generate_deep_content(category)

            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content_data['content'])

            print(f"✅ Tek makale oluşturuldu: {content_data['title']}")
            print(f"📁 Dosya yolu: {file_path}")

    else:
        # Varsayılan: her kategoriye 3'er makale
        print("🚀 Her kategoriye 3'er adet uzun içerik üretiliyor...")
        results = generator.generate_batch_content(3)

        total_articles = sum(len(articles) for articles in results.values())
        print(f"\n🎉 Toplamda {total_articles} uzun makale başarıyla oluşturuldu!")

if __name__ == "__main__":
    main()
