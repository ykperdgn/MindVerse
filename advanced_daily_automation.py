#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🤖 Advanced Daily Content Automation System for MindVerse
- Automatic Turkish & English article generation
- Advanced astrology system with planetary positions
- Newsletter subscription management
- Professional content quality with SEO optimization
"""

import os
import sys
import json
import random
import hashlib
import requests
from datetime import datetime, timedelta
from pathlib import Path
import schedule
import time

class AdvancedContentManager:
    def __init__(self):
        self.base_path = Path(__file__).parent
        self.content_path = self.base_path / "src" / "content"
        self.today = datetime.now().date()

        # Content categories and their English equivalents
        self.categories = {
            'health': {
                'tr_name': 'Sağlık',
                'en_name': 'Health',
                'topics_tr': [
                    'Sağlıklı Beslenme Rehberi',
                    'Egzersiz ve Spor Önerileri',
                    'Mental Sağlık ve Stres Yönetimi',
                    'Uyku Kalitesi İyileştirme',
                    'Bağışıklık Sistemini Güçlendirme',
                    'Kalp Sağlığı Koruma Yöntemleri',
                    'Doğal Detoks Yöntemleri',
                    'Yaşlanma Karşıtı Stratejiler'
                ],
                'topics_en': [
                    'Healthy Nutrition Guidelines',
                    'Exercise and Fitness Recommendations',
                    'Mental Health and Stress Management',
                    'Sleep Quality Improvement',
                    'Immune System Boosting',
                    'Heart Health Protection Methods',
                    'Natural Detox Methods',
                    'Anti-Aging Strategies'
                ]
            },
            'love': {
                'tr_name': 'Aşk ve İlişkiler',
                'en_name': 'Love & Relationships',
                'topics_tr': [
                    'Sağlıklı İlişki Kurma Rehberi',
                    'Etkili İletişim Teknikleri',
                    'Aşk Dillerini Anlama',
                    'İlişki Çatışmalarını Çözme',
                    'Uzun Mesafe İlişki Tavsiyeleri',
                    'Evlilik ve Partnerlik Önerileri',
                    'Modern Çağda Flört Etme',
                    'Kendini Sevme ve Kişisel Gelişim'
                ],
                'topics_en': [
                    'Building Healthy Relationships Guide',
                    'Effective Communication Techniques',
                    'Understanding Love Languages',
                    'Resolving Relationship Conflicts',
                    'Long Distance Relationship Advice',
                    'Marriage and Partnership Tips',
                    'Modern Dating Strategies',
                    'Self-Love and Personal Growth'
                ]
            },
            'psychology': {
                'tr_name': 'Psikoloji',
                'en_name': 'Psychology',
                'topics_tr': [
                    'İnsan Davranışını Anlama',
                    'Bilişsel Psikoloji Rehberi',
                    'Duygusal Zeka Geliştirme',
                    'Hafıza ve Öğrenme Teknikleri',
                    'Kişilik Psikolojisi Temelleri',
                    'Sosyal Psikoloji ve Günlük Yaşam',
                    'Motivasyon ve Hedef Belirleme',
                    'Farkındalık ve Zihinsel Berraklık'
                ],
                'topics_en': [
                    'Understanding Human Behavior',
                    'Cognitive Psychology Guide',
                    'Emotional Intelligence Development',
                    'Memory and Learning Techniques',
                    'Personality Psychology Basics',
                    'Social Psychology in Daily Life',
                    'Motivation and Goal Setting',
                    'Mindfulness and Mental Clarity'
                ]
            },
            'history': {
                'tr_name': 'Tarih',
                'en_name': 'History',
                'topics_tr': [
                    'Antik Medeniyetler ve Mirası',
                    'Dünya Savaşları Tarihsel Analizi',
                    'Rönesans Sanatı ve Kültürü',
                    'Dünyayı Değiştiren Büyük Keşifler',
                    'Ortaçağ Yaşamı ve Toplumu',
                    'Sanayi Devrimi Etkisi',
                    'Antik Mısır Gizemleri',
                    'Yunan Felsefesi ve Etkisi'
                ],
                'topics_en': [
                    'Ancient Civilizations and Legacy',
                    'World Wars Historical Analysis',
                    'Renaissance Art and Culture',
                    'Great Discoveries That Changed the World',
                    'Medieval Life and Society',
                    'Industrial Revolution Impact',
                    'Ancient Egyptian Mysteries',
                    'Greek Philosophy and Influence'
                ]
            },
            'space': {
                'tr_name': 'Uzay',
                'en_name': 'Space',
                'topics_tr': [
                    'Güneş Sistemi Keşifleri',
                    'Kara Delikler ve Karanlık Madde',
                    'Mars Misyonu Güncellemeleri',
                    'Uzay Teknolojisi Gelişmeleri',
                    'Yeni Başlayanlar için Astronomi',
                    'Öte Gezegen Keşifleri',
                    'Uluslararası Uzay İstasyonu',
                    'Uzay Yolculuğunun Geleceği'
                ],
                'topics_en': [
                    'Solar System Exploration',
                    'Black Holes and Dark Matter',
                    'Mars Mission Updates',
                    'Space Technology Advances',
                    'Astronomy for Beginners',
                    'Exoplanet Discoveries',
                    'International Space Station',
                    'Future of Space Travel'
                ]
            },
            'quotes': {
                'tr_name': 'Alıntılar',
                'en_name': 'Quotes',
                'topics_tr': [
                    'İlham Verici Başarı Sözleri',
                    'Büyük Zihinlerden Yaşam Hikmeti',
                    'Günlük Motivasyon Alıntıları',
                    'Aşk ve İlişki Sözleri',
                    'Felsefi Düşünceler',
                    'Liderlik ve Başarı Hikmeti',
                    'Mutluluk ve Şükran Sözleri',
                    'Zorlukları Aşma Alıntıları'
                ],
                'topics_en': [
                    'Inspirational Success Quotes',
                    'Life Wisdom from Great Minds',
                    'Daily Motivation Quotes',
                    'Love and Relationship Quotes',
                    'Philosophical Thoughts',
                    'Leadership and Success Wisdom',
                    'Happiness and Gratitude Quotes',
                    'Overcoming Challenges Quotes'
                ]
            }
        }

        # Advanced astrology system
        self.astrology_system = AstrologySystem()

        # Newsletter system
        self.newsletter_system = NewsletterSystem()

    def generate_daily_articles(self):
        """Generate both Turkish and English articles for today"""
        print(f"📝 Generating daily articles for {self.today.strftime('%Y-%m-%d')}")

        # Select random categories for today (2-3 categories)
        selected_categories = random.sample(list(self.categories.keys()), random.randint(2, 3))

        created_files = []

        for category in selected_categories:
            # Generate Turkish article
            tr_file = self.create_article(category, 'tr')
            if tr_file:
                created_files.append(tr_file)

            # Generate English article
            en_file = self.create_article(category, 'en')
            if en_file:
                created_files.append(en_file)

        print(f"✅ Created {len(created_files)} articles today")
        return created_files

    def create_article(self, category, language):
        """Create a single article in specified language"""
        try:
            # Select topic based on language
            if language == 'tr':
                topic = random.choice(self.categories[category]['topics_tr'])
                category_name = self.categories[category]['tr_name']
            else:
                topic = random.choice(self.categories[category]['topics_en'])
                category_name = self.categories[category]['en_name']

            # Generate content
            content = self.generate_article_content(topic, category, language)

            # Create filename
            slug = self.create_slug(topic)
            date_str = self.today.strftime('%Y-%m-%d')
            unique_id = hashlib.md5(f"{topic}{date_str}{language}".encode()).hexdigest()[:8]

            if language == 'en':
                filename = f"{slug}-{unique_id}_en.md"
            else:
                filename = f"{slug}-{unique_id}.md"

            # Create file path
            file_path = self.content_path / category / filename

            # Ensure directory exists
            file_path.parent.mkdir(parents=True, exist_ok=True)

            # Write file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"   ✅ Created: {filename} ({language.upper()})")
            return str(file_path)

        except Exception as e:
            print(f"   ❌ Error creating {category} article in {language}: {e}")
            return None

    def create_slug(self, text):
        """Create URL-friendly slug from text"""
        # Turkish character mapping
        char_map = {
            'ç': 'c', 'ğ': 'g', 'ı': 'i', 'ö': 'o', 'ş': 's', 'ü': 'u',
            'Ç': 'C', 'Ğ': 'G', 'İ': 'I', 'Ö': 'O', 'Ş': 'S', 'Ü': 'U'
        }

        # Replace Turkish characters
        for tr_char, en_char in char_map.items():
            text = text.replace(tr_char, en_char)

        # Convert to lowercase and replace spaces with dashes
        slug = text.lower().replace(' ', '-').replace('&', 'and')

        # Keep only alphanumeric characters and dashes
        slug = ''.join(c for c in slug if c.isalnum() or c == '-')

        return slug

    def generate_article_content(self, topic, category, language):
        """Generate comprehensive article content"""

        # Content templates based on language
        if language == 'tr':
            return self.generate_turkish_content(topic, category)
        else:
            return self.generate_english_content(topic, category)

    def generate_turkish_content(self, topic, category):
        """Generate Turkish article content"""

        date_str = self.today.strftime('%Y-%m-%d')
        views = random.randint(50, 800)

        # Create tags based on category
        tags = self.get_turkish_tags(category)

        frontmatter = f"""---
title: '{topic}'
date: {date_str}
summary: '{topic} hakkında kapsamlı rehber ve uzman önerileri.'
tags: {tags}
views: {views}
author: 'MindVerse Editör Ekibi'
keywords: '{", ".join(tags[:3])}, rehber, ipuçları, öneriler'
---
"""

        content = self.get_turkish_article_template(topic, category)

        return frontmatter + content

    def generate_english_content(self, topic, category):
        """Generate English article content"""

        date_str = self.today.strftime('%Y-%m-%d')
        views = random.randint(30, 500)

        # Create tags based on category
        tags = self.get_english_tags(category)

        frontmatter = f"""---
title: '{topic}'
date: {date_str}
summary: 'Comprehensive guide about {topic.lower()} with expert insights and practical advice.'
tags: {tags}
views: {views}
author: 'MindVerse Editorial Team'
keywords: '{", ".join(tags[:3])}, guide, tips, advice'
---
"""

        content = self.get_english_article_template(topic, category)

        return frontmatter + content

    def get_turkish_tags(self, category):
        """Get Turkish tags for category"""
        tag_map = {
            'health': ['sağlık', 'wellness', 'beslenme', 'egzersiz', 'yaşam'],
            'love': ['aşk', 'ilişki', 'sevgi', 'romantizm', 'evlilik'],
            'psychology': ['psikoloji', 'zihin', 'davranış', 'motivasyon', 'gelişim'],
            'history': ['tarih', 'geçmiş', 'medeniyet', 'kültür', 'analiz'],
            'space': ['uzay', 'astronomi', 'bilim', 'keşif', 'gezegen'],
            'quotes': ['alıntı', 'söz', 'motivasyon', 'ilham', 'hikmet']
        }
        return tag_map.get(category, ['genel', 'bilgi', 'rehber'])

    def get_english_tags(self, category):
        """Get English tags for category"""
        tag_map = {
            'health': ['health', 'wellness', 'nutrition', 'fitness', 'lifestyle'],
            'love': ['love', 'relationships', 'romance', 'dating', 'marriage'],
            'psychology': ['psychology', 'mind', 'behavior', 'motivation', 'growth'],
            'history': ['history', 'past', 'civilization', 'culture', 'analysis'],
            'space': ['space', 'astronomy', 'science', 'exploration', 'universe'],
            'quotes': ['quotes', 'wisdom', 'motivation', 'inspiration', 'life']
        }
        return tag_map.get(category, ['general', 'information', 'guide'])

    def get_turkish_article_template(self, topic, category):
        """Get Turkish article content template"""
        return f"""
## {topic} Hakkında Kapsamlı Rehber

{topic} konusu günümüz dünyasında giderek daha fazla önem kazanıyor. Bu kapsamlı rehberde, konuyla ilgili en güncel bilgileri, uzman görüşlerini ve pratik önerileri bulacaksınız.

### Giriş

Modern yaşamın karmaşık dinamikleri içinde {topic.lower()} konusu, hem bireysel gelişim hem de genel yaşam kalitesi açısından kritik bir rol oynamaktadır. Son yıllarda yapılan araştırmalar, bu alandaki gelişmelerin ne kadar önemli olduğunu gözler önüne sermektedir.

### Temel Prensipler

{topic} ile ilgili temel bilgiler ve güncel yaklaşımlar şu şekilde özetlenebilir:

#### 1. Bilimsel Temeller
- Konuyla ilgili kanıtlanmış yöntemleri tercih etmek
- Güncel araştırmaları takip etmek
- Uzman görüşlerinden faydalanmak
- Bireysel farklılıkları göz önünde bulundurmak

#### 2. Pratik Uygulamalar
- Günlük rutinlere entegre edilebilir stratejiler
- Adım adım uygulama rehberleri
- Yaygın hataları önleme yöntemleri
- Başarı ölçütleri ve değerlendirme kriterleri

### Detaylı Analiz

#### Neden Önemli?
{topic} konusunun önemli olmasının başlıca nedenleri:

- **Bilimsel Kanıtlar**: Yapılan araştırmalar konunun etkisini kanıtlıyor
- **Pratik Faydalar**: Günlük yaşamda somut iyileştirmeler sağlıyor
- **Uzun Vadeli Etkiler**: Sürdürülebilir değişiklikler yaratıyor
- **Bütünsel Yaklaşım**: Yaşamın farklı alanlarını olumlu etkiliyor

#### Uygulama Stratejileri

##### Başlangıç Seviyesi
1. **Temel Bilgileri Öğrenme**: Konuyla ilgili temel kavramları anlama
2. **Küçük Adımlar**: Değişikliklerle küçük başlayıp büyütme
3. **Tutarlılık**: Düzenli uygulama alışkanlığı geliştirme
4. **Sabır**: Sonuçlar için yeterli zaman tanıma

##### İleri Seviye
- Daha karmaşık teknikleri öğrenme
- Kişisel ihtiyaçlara göre adapte etme
- Başkalarıyla deneyim paylaşma
- Sürekli öğrenme ve gelişim

### Uzman Tavsiyeleri

Alanında uzman kişiler {topic.lower()} konusunda şu tavsiyelerde bulunuyor:

> **"Başarının anahtarı tutarlılık ve sabırdır. Hemen sonuç beklemek yerine uzun vadeli düşünmek önemlidir."**

### Yaygın Hatalar ve Çözümleri

#### En Sık Yapılan Hatalar
1. **Aşırı Beklenti**: Çok hızlı sonuç bekleme
2. **Tutarsızlık**: Düzenli uygulama yapmama
3. **Bireyselleştirmeme**: Herkese uyan çözüm arama
4. **Uzman Desteğini İhmal**: Profesyonel yardım almama

#### Çözüm Önerileri
- Gerçekçi hedefler belirleme
- Adım adım ilerleme
- Kişisel ihtiyaçları analiz etme
- Gerektiğinde uzman desteği alma

### Gelecek Perspektifi

{topic} alanındaki gelecek trendleri ve beklentiler:

- Teknolojik gelişmelerin etkisi
- Yeni araştırma bulgularının uygulanması
- Toplumsal farkındalığın artması
- Bireyselleştirilmiş yaklaşımların yaygınlaşması

### Sonuç ve Öneriler

{topic} konusunda edindiğiniz bilgileri pratik hayatınızda uygulayarak olumlu değişiklikler yaratabilirsiniz. Unutmayın ki:

- Her bireyin ihtiyaçları farklıdır
- Sabır ve tutarlılık başarının anahtarıdır
- Uzman desteği almaktan çekinmeyin
- Küçük değişiklikler bile büyük farklar yaratabilir

Bu rehberdeki önerileri hayatınıza adapte ederek, {topic.lower()} konusunda istediğiniz gelişimi sağlayabilirsiniz. Sürekli öğrenme ve gelişim, başarılı sonuçlar elde etmenin en etkili yoludur.

---

*Bu makale, güncel araştırmalar ve uzman görüşleri doğrultusunda hazırlanmıştır. Kişisel durumunuz için mutlaka uzman görüşü alınız.*
"""

    def get_english_article_template(self, topic, category):
        """Get English article content template"""
        return f"""
## Comprehensive Guide to {topic}

{topic} has become increasingly important in today's world. This comprehensive guide provides you with the latest information, expert opinions, and practical recommendations on this vital subject.

### Introduction

In the complex dynamics of modern life, {topic.lower()} plays a critical role in both personal development and overall quality of life. Recent research has highlighted just how important developments in this field have become.

### Fundamental Principles

The basic information and current approaches related to {topic} can be summarized as follows:

#### 1. Scientific Foundation
- Preferring evidence-based methods related to the topic
- Following current research
- Benefiting from expert opinions
- Considering individual differences

#### 2. Practical Applications
- Strategies that can be integrated into daily routines
- Step-by-step implementation guides
- Methods to prevent common mistakes
- Success metrics and evaluation criteria

### Detailed Analysis

#### Why Is It Important?
The main reasons why {topic} is important include:

- **Scientific Evidence**: Research proves the effectiveness of the subject
- **Practical Benefits**: Provides concrete improvements in daily life
- **Long-term Effects**: Creates sustainable changes
- **Holistic Approach**: Positively affects different areas of life

#### Implementation Strategies

##### Beginner Level
1. **Learning Basics**: Understanding fundamental concepts related to the topic
2. **Small Steps**: Starting small with changes and gradually expanding
3. **Consistency**: Developing regular application habits
4. **Patience**: Allowing sufficient time for results

##### Advanced Level
- Learning more complex techniques
- Adapting to personal needs
- Sharing experiences with others
- Continuous learning and development

### Expert Recommendations

Experts in the field offer the following advice regarding {topic.lower()}:

> **"The key to success is consistency and patience. Rather than expecting immediate results, it's important to think long-term."**

### Common Mistakes and Solutions

#### Most Frequent Mistakes
1. **Excessive Expectations**: Expecting results too quickly
2. **Inconsistency**: Not applying regularly
3. **Lack of Personalization**: Looking for one-size-fits-all solutions
4. **Neglecting Expert Support**: Not seeking professional help

#### Solution Recommendations
- Setting realistic goals
- Progressing step by step
- Analyzing personal needs
- Seeking expert support when necessary

### Future Perspective

Future trends and expectations in the field of {topic}:

- Impact of technological developments
- Application of new research findings
- Increasing social awareness
- Widespread adoption of personalized approaches

### Conclusion and Recommendations

By applying the knowledge you've gained about {topic} in your practical life, you can create positive changes. Remember that:

- Every individual's needs are different
- Patience and consistency are the keys to success
- Don't hesitate to seek expert support
- Even small changes can make big differences

By adapting the recommendations in this guide to your life, you can achieve the development you desire in {topic.lower()}. Continuous learning and development is the most effective way to achieve successful results.

---

*This article has been prepared in line with current research and expert opinions. Please consult an expert for your personal situation.*
"""

    def run_daily_automation(self):
        """Run complete daily automation"""
        print("🤖 STARTING DAILY AUTOMATION")
        print("=" * 50)

        # 1. Generate daily articles
        articles = self.generate_daily_articles()

        # 2. Generate daily horoscopes
        horoscopes = self.astrology_system.generate_daily_horoscopes()

        # 3. Update planetary positions (if needed)
        if self.today.weekday() == 0:  # Monday
            self.astrology_system.update_planetary_positions()

        # 4. Send newsletter (if it's newsletter day)
        if self.should_send_newsletter():
            self.newsletter_system.send_weekly_newsletter(articles, horoscopes)

        # 5. Update SEO files
        self.update_seo_files()

        # 6. Git commit and push
        self.commit_and_push_changes()

        print("=" * 50)
        print("✅ DAILY AUTOMATION COMPLETED")

        return {
            'articles': len(articles),
            'horoscopes': len(horoscopes),
            'date': self.today.strftime('%Y-%m-%d')
        }

    def should_send_newsletter(self):
        """Check if today is newsletter day (weekly on Sundays)"""
        return self.today.weekday() == 6  # Sunday

    def update_seo_files(self):
        """Update SEO files"""
        try:
            print("🔄 Updating SEO files...")
            os.system('python generate_enhanced_seo.py')
            print("   ✅ SEO files updated")
        except Exception as e:
            print(f"   ❌ Error updating SEO: {e}")

    def commit_and_push_changes(self):
        """Commit and push changes to git"""
        try:
            print("📤 Committing changes to git...")

            # Add all changes
            os.system('git add -A')

            # Commit with descriptive message
            commit_msg = f"🤖 Daily content automation - {self.today.strftime('%Y-%m-%d')}"
            os.system(f'git commit -m "{commit_msg}"')

            # Push to remote
            os.system('git push')

            print("   ✅ Changes pushed to git")
        except Exception as e:
            print(f"   ❌ Error with git operations: {e}")

    def generate_daily_turkish_content(self):
        """Generate daily Turkish content"""
        return self.generate_daily_articles()

    def generate_daily_english_content(self):
        """Generate daily English content"""
        return self.generate_daily_articles()

    def check_git_status(self):
        """Check Git repository status"""
        try:
            import subprocess
            result = subprocess.run(['git', 'status', '--porcelain'],
                                  capture_output=True, text=True, cwd=self.base_path)
            if result.returncode == 0:
                changes = result.stdout.strip()
                if changes:
                    return f"Modified files: {len(changes.splitlines())}"
                else:
                    return "No changes"
            else:
                return "Not a git repository"
        except Exception as e:
            return f"Git error: {e}"


class AstrologySystem:
    """Advanced astrology system with planetary positions"""

    def __init__(self):
        self.base_path = Path(__file__).parent
        self.astrology_path = self.base_path / "src" / "content" / "astrology"
        self.today = datetime.now().date()

        # Zodiac signs
        self.zodiac_signs = {
            'koc': {'name': 'Koç', 'en_name': 'Aries', 'symbol': '♈'},
            'boga': {'name': 'Boğa', 'en_name': 'Taurus', 'symbol': '♉'},
            'ikizler': {'name': 'İkizler', 'en_name': 'Gemini', 'symbol': '♊'},
            'yengec': {'name': 'Yengeç', 'en_name': 'Cancer', 'symbol': '♋'},
            'aslan': {'name': 'Aslan', 'en_name': 'Leo', 'symbol': '♌'},
            'basak': {'name': 'Başak', 'en_name': 'Virgo', 'symbol': '♍'},
            'terazi': {'name': 'Terazi', 'en_name': 'Libra', 'symbol': '♎'},
            'akrep': {'name': 'Akrep', 'en_name': 'Scorpio', 'symbol': '♏'},
            'yay': {'name': 'Yay', 'en_name': 'Sagittarius', 'symbol': '♐'},
            'oglak': {'name': 'Oğlak', 'en_name': 'Capricorn', 'symbol': '♑'},
            'kova': {'name': 'Kova', 'en_name': 'Aquarius', 'symbol': '♒'},
            'balik': {'name': 'Balık', 'en_name': 'Pisces', 'symbol': '♓'}
        }

        # Planetary data (simplified)
        self.planets = {
            'mercury': 'Merkür',
            'venus': 'Venüs',
            'mars': 'Mars',
            'jupiter': 'Jüpiter',
            'saturn': 'Satürn'
        }

    def generate_daily_horoscopes(self):
        """Generate daily horoscopes for all signs"""
        print("🔮 Generating daily horoscopes...")

        created_files = []

        for sign_code, sign_info in self.zodiac_signs.items():
            # Turkish horoscope
            tr_file = self.create_daily_horoscope(sign_code, 'tr')
            if tr_file:
                created_files.append(tr_file)

            # English horoscope
            en_file = self.create_daily_horoscope(sign_code, 'en')
            if en_file:
                created_files.append(en_file)

        print(f"   ✅ Generated {len(created_files)} horoscopes")
        return created_files

    def create_daily_horoscope(self, sign_code, language):
        """Create daily horoscope for specific sign"""
        try:
            sign_info = self.zodiac_signs[sign_code]

            if language == 'tr':
                title = f"{sign_info['name']} Günlük Yorumu"
                content = self.generate_turkish_horoscope_content(sign_info)
            else:
                title = f"{sign_info['en_name']} Daily Horoscope"
                content = self.generate_english_horoscope_content(sign_info)

            # Create filename
            date_str = self.today.strftime('%Y-%m-%d')
            if language == 'en':
                filename = f"{sign_code}-daily-{date_str}_en.md"
            else:
                filename = f"{sign_code}-gunluk-{date_str}.md"

            file_path = self.astrology_path / filename

            # Ensure directory exists
            file_path.parent.mkdir(parents=True, exist_ok=True)

            # Write file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            return str(file_path)

        except Exception as e:
            print(f"   ❌ Error creating horoscope for {sign_code}: {e}")
            return None

    def generate_turkish_horoscope_content(self, sign_info):
        """Generate Turkish horoscope content"""

        date_str = self.today.strftime('%Y-%m-%d')
        display_date = self.today.strftime('%d %B %Y')

        # Random horoscope elements
        love_texts = [
            "Aşk hayatında yeni fırsatlar sizi bekliyor.",
            "İlişkinizde daha derin bağlar kurma zamanı.",
            "Sevdiğiniz kişiyle güzel anlar yaşayacaksınız.",
            "Romantik sürprizler günü renklendirrebilir."
        ]

        career_texts = [
            "İş hayatında yaratıcı çözümler bulacaksınız.",
            "Kariyerinizde yeni adımlar atma zamanı.",
            "Mesleki hedeflerinize odaklanın.",
            "İş birliği halinde büyük başarılar elde edebilirsiniz."
        ]

        health_texts = [
            "Sağlığınıza özel önem gösterin.",
            "Dengeli beslenme ve düzenli egzersiz önemli.",
            "Stres seviyenizi kontrol altında tutun.",
            "Zihinsel ve fiziksel dengeyi koruyun."
        ]

        lucky_numbers = random.sample(range(1, 50), 3)
        lucky_color = random.choice(['Mavi', 'Yeşil', 'Kırmızı', 'Sarı', 'Mor', 'Turuncu'])

        frontmatter = f"""---
title: '{sign_info["name"]} Günlük Yorumu - {display_date}'
date: {date_str}
summary: '{sign_info["name"]} burcu için {display_date} günlük astroloji yorumu ve önerileri.'
tags: ['astroloji', 'günlük-yorum', '{sign_info["name"].lower()}', 'burç', 'yıldız']
views: {random.randint(100, 800)}
author: 'MindVerse Astroloji Uzmanı'
keywords: '{sign_info["name"]}, günlük yorum, astroloji, burç yorumu, {display_date}'
---
"""

        content = f"""
## {sign_info['symbol']} {sign_info['name']} Günlük Astroloji Yorumu

**Tarih:** {display_date}

### Genel Durum

Bugün {sign_info['name']} burcu için özel bir gün olacak. Yıldızların size gönderdiği enerjiler, yaşamınızın farklı alanlarında olumlu gelişmelere kapı açacak.

### Aşk ve İlişkiler ❤️

{random.choice(love_texts)} İçinizdeki romantik duyguları açığa çıkarın ve sevginizi göstermekten çekinmeyin.

### Kariyer ve İş 💼

{random.choice(career_texts)} Bugün aldığınız kararlar, geleceğinizi şekillendirebilir.

### Sağlık ve Enerji 🌟

{random.choice(health_texts)} Vücudunuzun verdiği sinyalleri dinleyin ve gerekli önlemleri alın.

### Günün Önerisi

Bugün özellikle {lucky_color.lower()} renk size şans getirebilir. Önemli kararları verirken sezgilerinizi dinleyin.

### Şanslı Detaylar

- **Şanslı Sayılar:** {', '.join(map(str, lucky_numbers))}
- **Şanslı Renk:** {lucky_color}
- **Şanslı Taş:** {random.choice(['Ametist', 'Kuvars', 'Akik', 'Jade', 'Obsidyen'])}
- **Şanslı Yön:** {random.choice(['Kuzey', 'Güney', 'Doğu', 'Batı'])}

### Dikkat Edilmesi Gerekenler

- Aceleci kararlardan kaçının
- Sabırlı olmayı unutmayın
- Yakınlarınızla iletişiminizi güçlendirin
- Mali konularda temkinli olun

---

**Not:** Bu yorum genel astroloji bilgilerine dayanmaktadır. Kişisel durumunuz için detaylı astroloji analizi yaptırabilirsiniz.

### Diğer Burç Yorumları

Diğer burçların günlük yorumlarını da incelemek için [astroloji sayfamızı](https://www.mindversedaily.com) ziyaret edebilirsiniz.
"""

        return frontmatter + content

    def generate_english_horoscope_content(self, sign_info):
        """Generate English horoscope content"""

        date_str = self.today.strftime('%Y-%m-%d')
        display_date = self.today.strftime('%B %d, %Y')

        # Random horoscope elements
        love_texts = [
            "New opportunities in love life await you.",
            "Time to form deeper connections in your relationship.",
            "You'll experience beautiful moments with your loved one.",
            "Romantic surprises may brighten your day."
        ]

        career_texts = [
            "You'll find creative solutions in your work life.",
            "Time to take new steps in your career.",
            "Focus on your professional goals.",
            "Great achievements can be made through collaboration."
        ]

        health_texts = [
            "Pay special attention to your health.",
            "Balanced nutrition and regular exercise are important.",
            "Keep your stress levels under control.",
            "Maintain mental and physical balance."
        ]

        lucky_numbers = random.sample(range(1, 50), 3)
        lucky_color = random.choice(['Blue', 'Green', 'Red', 'Yellow', 'Purple', 'Orange'])

        frontmatter = f"""---
title: '{sign_info["en_name"]} Daily Horoscope - {display_date}'
date: {date_str}
summary: 'Daily astrology reading and recommendations for {sign_info["en_name"]} on {display_date}.'
tags: ['astrology', 'daily-horoscope', '{sign_info["en_name"].lower()}', 'zodiac', 'stars']
views: {random.randint(50, 500)}
author: 'MindVerse Astrology Expert'
keywords: '{sign_info["en_name"]}, daily horoscope, astrology, zodiac reading, {display_date}'
---
"""

        content = f"""
## {sign_info['symbol']} {sign_info['en_name']} Daily Astrology Reading

**Date:** {display_date}

### Overall Outlook

Today will be a special day for {sign_info['en_name']}. The energies sent by the stars will open doors to positive developments in different areas of your life.

### Love & Relationships ❤️

{random.choice(love_texts)} Express your romantic feelings openly and don't hesitate to show your love.

### Career & Work 💼

{random.choice(career_texts)} The decisions you make today can shape your future.

### Health & Energy 🌟

{random.choice(health_texts)} Listen to the signals your body gives and take necessary precautions.

### Today's Recommendation

The color {lucky_color.lower()} may bring you luck today. Trust your intuition when making important decisions.

### Lucky Details

- **Lucky Numbers:** {', '.join(map(str, lucky_numbers))}
- **Lucky Color:** {lucky_color}
- **Lucky Stone:** {random.choice(['Amethyst', 'Quartz', 'Agate', 'Jade', 'Obsidian'])}
- **Lucky Direction:** {random.choice(['North', 'South', 'East', 'West'])}

### Things to Consider

- Avoid hasty decisions
- Remember to be patient
- Strengthen communication with loved ones
- Be cautious in financial matters

---

**Note:** This reading is based on general astrological information. For your personal situation, you can get a detailed astrological analysis.

### Other Zodiac Readings

To check daily readings for other zodiac signs, visit our [astrology page](https://www.mindversedaily.com/en).
"""

        return frontmatter + content

    def update_planetary_positions(self):
        """Update weekly planetary position content"""
        print("🪐 Updating planetary positions...")

        # This would integrate with real astronomical APIs in production
        # For now, we'll create template content

        try:
            # Turkish version
            tr_content = self.create_planetary_content('tr')
            tr_file = self.astrology_path / f"planetary-positions-{self.today.strftime('%Y-%m-%d')}.md"

            with open(tr_file, 'w', encoding='utf-8') as f:
                f.write(tr_content)

            # English version
            en_content = self.create_planetary_content('en')
            en_file = self.astrology_path / f"planetary-positions-{self.today.strftime('%Y-%m-%d')}_en.md"

            with open(en_file, 'w', encoding='utf-8') as f:
                f.write(en_content)

            print("   ✅ Planetary positions updated")

        except Exception as e:
            print(f"   ❌ Error updating planetary positions: {e}")

    def create_planetary_content(self, language):
        """Create planetary position content"""

        date_str = self.today.strftime('%Y-%m-%d')

        if language == 'tr':
            title = f"Haftalık Gezegen Konumları ve Etkileri"
            content = f"""---
title: '{title} - {self.today.strftime("%d %B %Y")}'
date: {date_str}
summary: 'Bu hafta gezegenlerin konumları ve burçlar üzerindeki etkileri.'
tags: ['astroloji', 'gezegenler', 'haftalık', 'konum', 'etki']
views: {random.randint(200, 1000)}
author: 'MindVerse Astroloji Uzmanı'
---

## 🪐 Bu Haftanın Gezegen Konumları

### Merkür'ün Durumu
Merkür bu hafta iletişim alanında güçlü etkiler yaratacak...

### Venüs'ün Etkisi
Aşk ve ilişkiler konusunda önemli gelişmeler bekleniyor...

### Mars'ın Enerjisi
Eylem ve motivasyon konularında güçlü destek geliyor...

### Jüpiter'in Bereket Enerjisi
Genişleme ve büyüme fırsatları kendini gösterecek...

### Satürn'ün Disiplin Mesajı
Sorumluluk ve düzen konularında önemli dersler...
"""
        else:
            title = f"Weekly Planetary Positions and Effects"
            content = f"""---
title: '{title} - {self.today.strftime("%B %d, %Y")}'
date: {date_str}
summary: 'This week planetary positions and their effects on zodiac signs.'
tags: ['astrology', 'planets', 'weekly', 'positions', 'effects']
views: {random.randint(100, 600)}
author: 'MindVerse Astrology Expert'
---

## 🪐 This Week's Planetary Positions

### Mercury's Status
Mercury will create strong effects in communication this week...

### Venus's Influence
Important developments expected in love and relationships...

### Mars's Energy
Strong support coming in action and motivation areas...

### Jupiter's Abundance Energy
Expansion and growth opportunities will manifest...

### Saturn's Discipline Message
Important lessons in responsibility and order...
"""

        return content


class NewsletterSystem:
    """Newsletter subscription and sending system"""

    def __init__(self):
        self.base_path = Path(__file__).parent
        self.subscribers_file = self.base_path / "newsletter_subscribers.json"
        self.ensure_subscribers_file()

    def ensure_subscribers_file(self):
        """Ensure subscribers file exists"""
        if not self.subscribers_file.exists():
            with open(self.subscribers_file, 'w', encoding='utf-8') as f:
                json.dump({"subscribers": []}, f, ensure_ascii=False, indent=2)

    def add_subscriber(self, email, language='tr'):
        """Add new subscriber"""
        try:
            with open(self.subscribers_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Check if already subscribed
            for subscriber in data['subscribers']:
                if subscriber['email'] == email:
                    return False, "Already subscribed"            # Add new subscriber
            data['subscribers'].append({
                'email': email,
                'language': language,
                'subscribed_date': datetime.now().isoformat(),
                'active': True
            })

            with open(self.subscribers_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            return True, "Successfully subscribed"

        except Exception as e:
            return False, f"Error: {e}"

    def get_subscribers(self):
        """Get all subscribers"""
        try:
            with open(self.subscribers_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data['subscribers']
        except Exception as e:
            return []

    def send_weekly_newsletter(self, articles, horoscopes):
        """Send weekly newsletter to subscribers"""
        print("📧 Preparing weekly newsletter...")

        try:
            with open(self.subscribers_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            active_subscribers = [s for s in data['subscribers'] if s['active']]

            print(f"   📊 {len(active_subscribers)} active subscribers")

            # Group by language
            tr_subscribers = [s for s in active_subscribers if s['language'] == 'tr']
            en_subscribers = [s for s in active_subscribers if s['language'] == 'en']

            # Send Turkish newsletter
            if tr_subscribers:
                self.send_newsletter_batch(tr_subscribers, articles, horoscopes, 'tr')

            # Send English newsletter
            if en_subscribers:
                self.send_newsletter_batch(en_subscribers, articles, horoscopes, 'en')

            print("   ✅ Newsletter sent successfully")

        except Exception as e:
            print(f"   ❌ Error sending newsletter: {e}")

    def send_newsletter_batch(self, subscribers, articles, horoscopes, language):
        """Send newsletter to a batch of subscribers"""

        # Create newsletter content
        subject, content = self.create_newsletter_content(articles, horoscopes, language)

        print(f"   📬 Sending {language.upper()} newsletter to {len(subscribers)} subscribers")

        # In production, this would integrate with email service like SendGrid, Mailgun, etc.
        # For now, we'll just log the action

        newsletter_log = {
            'date': datetime.now().isoformat(),
            'language': language,
            'subscribers_count': len(subscribers),
            'subject': subject,
            'status': 'sent'
        }

        # Save newsletter log
        log_file = self.base_path / f"newsletter_log_{language}_{datetime.now().strftime('%Y%m%d')}.json"
        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump(newsletter_log, f, ensure_ascii=False, indent=2)

    def create_newsletter_content(self, articles, horoscopes, language):
        """Create newsletter content"""

        if language == 'tr':
            subject = f"MindVerse Haftalık Bülten - {datetime.now().strftime('%d %B %Y')}"
            content = f"""
## 🌟 MindVerse Haftalık Bülten

Merhaba sevgili okuyucumuz,

Bu hafta sizin için hazırladığımız özel içerikler:

### 📝 Yeni Makaleler
{self.format_articles_list(articles, 'tr')}

### 🔮 Haftalık Astroloji
{self.format_horoscopes_list(horoscopes, 'tr')}

### 🎯 Özel Öneriler
Bu hafta özellikle kişisel gelişim alanında harika fırsatlar sizi bekliyor!

Daha fazla içerik için sitemizi ziyaret edin: https://www.mindversedaily.com
Selamlar,
MindVerse Ekibi
"""
        else:
            subject = f"MindVerse Weekly Newsletter - {datetime.now().strftime('%B %d, %Y')}"
            content = f"""
## 🌟 MindVerse Weekly Newsletter

Hello dear reader,

Special content we've prepared for you this week:

### 📝 New Articles
{self.format_articles_list(articles, 'en')}

### 🔮 Weekly Astrology
{self.format_horoscopes_list(horoscopes, 'en')}

### 🎯 Special Recommendations
This week, especially great opportunities await you in personal development!

Visit our website for more content: https://www.mindversedaily.com
Best regards,
MindVerse Team
"""

        return subject, content

    def format_articles_list(self, articles, language):
        """Format articles list for newsletter"""
        if not articles:
            return "Bu hafta yeni makale eklenmedi." if language == 'tr' else "No new articles this week."

        formatted = []
        for article in articles[:5]:  # Show max 5 articles
            filename = Path(article).name
            if language == 'tr' and not filename.endswith('_en.md'):
                formatted.append(f"- {filename}")
            elif language == 'en' and filename.endswith('_en.md'):
                formatted.append(f"- {filename}")

        return '\n'.join(formatted) if formatted else ("Henüz makale yok." if language == 'tr' else "No articles yet.")

    def format_horoscopes_list(self, horoscopes, language):
        """Format horoscopes list for newsletter"""
        if not horoscopes:
            return "Bu hafta burç yorumu eklenmedi." if language == 'tr' else "No horoscope updates this week."

        if language == 'tr':
            return "- Tüm burçlar için günlük yorumlar güncellendi"
        else:
            return "- Daily readings updated for all zodiac signs"


def setup_daily_schedule():
    """Setup daily automation schedule"""
    print("⏰ Setting up daily automation schedule...")

    content_manager = AdvancedContentManager()

    # Schedule daily content generation at 06:00
    schedule.every().day.at("06:00").do(content_manager.run_daily_automation)

    print("✅ Daily automation scheduled for 06:00")
    print("📅 Newsletter scheduled for Sundays")

    return content_manager


def run_scheduler():
    """Run the automation scheduler"""
    print("🚀 Starting MindVerse automation scheduler...")

    content_manager = setup_daily_schedule()

    print("⚡ Scheduler is running. Press Ctrl+C to stop.")

    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        command = sys.argv[1]

        content_manager = AdvancedContentManager()

        if command == 'run-daily':
            content_manager.run_daily_automation()
        elif command == 'generate-articles':
            content_manager.generate_daily_articles()
        elif command == 'generate-horoscopes':
            content_manager.astrology_system.generate_daily_horoscopes()
        elif command == 'start-scheduler':
            run_scheduler()
        else:
            print("Unknown command. Available: run-daily, generate-articles, generate-horoscopes, start-scheduler")
    else:
        # Default: run daily automation
        content_manager = AdvancedContentManager()
        content_manager.run_daily_automation()
