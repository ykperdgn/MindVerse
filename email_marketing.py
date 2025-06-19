#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MindVerse Email Marketing Sistemi
Ücretsiz email servislerle newsletter otomasyonu
"""

import json
import os
import csv
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

class EmailMarketingSystem:
    def __init__(self):
        self.base_url = "https://mindverse-orcin.vercel.app"
        self.site_name = "MindVerse"
        self.categories = ['health', 'love', 'history', 'psychology', 'space', 'quotes']

        # Email templates
        self.email_templates = {
            'welcome': {
                'subject': '🌟 MindVerse\'e Hoş Geldiniz! İlk Hediyeniz İçeride',
                'category': 'onboarding'
            },
            'daily_digest': {
                'subject': '📚 Günlük Bilgi Dozu - {date}',
                'category': 'content'
            },
            'weekly_roundup': {
                'subject': '🔥 Bu Haftanın En Popüler İçerikleri',
                'category': 'engagement'
            },
            'category_spotlight': {
                'subject': '🎯 {category} Kategorisinde Yeni İçerikler',
                'category': 'targeted'
            }
        }

        # Ücretsiz email servisleri
        self.free_services = {
            'mailchimp': {
                'limit': '2000 contact, 10000 email/month',
                'features': ['automation', 'templates', 'analytics'],
                'setup_url': 'https://mailchimp.com'
            },
            'sendinblue': {
                'limit': '300 email/day (unlimited contacts)',
                'features': ['smtp', 'templates', 'automation'],
                'setup_url': 'https://sendinblue.com'
            },
            'mailjet': {
                'limit': '6000 email/month, 200 email/day',
                'features': ['api', 'templates', 'tracking'],
                'setup_url': 'https://mailjet.com'
            },
            'gmail_smtp': {
                'limit': '500 email/day',
                'features': ['smtp', 'free', 'easy_setup'],
                'setup_url': 'Google Account'
            }
        }

    def create_welcome_email_template(self):
        """Hoş geldin email şablonu"""
        template = f"""
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MindVerse'e Hoş Geldiniz!</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f8f9fa;
            margin: 0;
            padding: 20px;
        }}
        .container {{
            max-width: 600px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px 20px;
            text-align: center;
        }}
        .content {{
            padding: 30px 20px;
        }}
        .button {{
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 12px 24px;
            text-decoration: none;
            border-radius: 6px;
            margin: 10px 5px;
        }}
        .category-card {{
            background: #f8f9fa;
            border-left: 4px solid #667eea;
            padding: 15px;
            margin: 15px 0;
            border-radius: 4px;
        }}
        .footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            font-size: 14px;
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌟 MindVerse'e Hoş Geldiniz!</h1>
            <p>Bilginin sonsuz evrenine hoş geldiniz</p>
        </div>

        <div class="content">
            <h2>Merhaba!</h2>
            <p>MindVerse ailesine katıldığınız için çok mutluyuz! Artık her gün kaliteli, araştırma temelli içeriklerimize özel erişiminiz var.</p>

            <h3>🎯 Size Özel İçeriklerimiz:</h3>

            <div class="category-card">
                <strong>🏥 Sağlık</strong><br>
                Bilimsel temelli sağlık önerileri, beslenme rehberleri ve wellness ipuçları.
            </div>

            <div class="category-card">
                <strong>❤️ Aşk & İlişkiler</strong><br>
                İlişki psikolojisi, aşk bilimleri ve duygusal zeka geliştirme.
            </div>

            <div class="category-card">
                <strong>📚 Tarih</strong><br>
                Antik medeniyetler, tarihi keşifler ve kültürel miras.
            </div>

            <div class="category-card">
                <strong>🧠 Psikoloji</strong><br>
                Zihin bilimi, motivasyon teknikleri ve kişisel gelişim.
            </div>

            <div class="category-card">
                <strong>🚀 Uzay</strong><br>
                Astronomi, uzay keşifleri ve evrenin sırları.
            </div>

            <div class="category-card">
                <strong>💭 Alıntılar</strong><br>
                İlham verici sözler, motivasyonel alıntılar ve bilge öğütler.
            </div>

            <h3>🎁 İlk Hediyeniz:</h3>
            <p>Sizin için özel olarak seçtiklerimiz:</p>

            <a href="{self.base_url}/popular" class="button">🔥 En Popüler İçerikler</a>
            <a href="{self.base_url}/search" class="button">🔍 İlgi Alanınızı Keşfedin</a>

            <h3>📧 Neler Bekleyebilirsiniz?</h3>
            <ul>
                <li><strong>Günlük İçerik:</strong> Her gün yeni bir makale</li>
                <li><strong>Haftalık Özet:</strong> Haftanın en popüler içerikleri</li>
                <li><strong>Özel Seriler:</strong> Derinlemesine araştırma yazıları</li>
                <li><strong>İnteraktif İçerik:</strong> Anketler ve yorumlar</li>
            </ul>

            <p><strong>Bir sonraki emailimiz:</strong> Yarın saat 09:00'da günlük bilgi dozunuz gelecek!</p>
        </div>

        <div class="footer">
            <p>Bu emaili almak istemiyorsanız <a href="#">buradan</a> çıkabilirsiniz.</p>
            <p>© 2025 MindVerse. Tüm hakları saklıdır.</p>
            <p>Web: <a href="{self.base_url}">{self.base_url}</a></p>
        </div>
    </div>
</body>
</html>
"""

        with open('email_templates/welcome_email.html', 'w', encoding='utf-8') as f:
            f.write(template)

        return template

    def create_daily_digest_template(self):
        """Günlük özet email şablonu"""
        template = f"""
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Günlük Bilgi Dozu</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f8f9fa;
            margin: 0;
            padding: 20px;
        }}
        .container {{
            max-width: 600px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            text-align: center;
        }}
        .content {{
            padding: 20px;
        }}
        .article-card {{
            border: 1px solid #e9ecef;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
            background: #fff;
        }}
        .button {{
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 6px;
            margin-top: 10px;
        }}
        .category-badge {{
            background: #e9ecef;
            color: #495057;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: bold;
        }}
        .footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            font-size: 14px;
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📚 Günlük Bilgi Dozu</h1>
            <p>{{date}} - Sizin için seçtiklerimiz</p>
        </div>

        <div class="content">
            <h2>Merhaba!</h2>
            <p>Bugün sizin için özenle seçtiğimiz içerikler burada. Keyifli okumalar!</p>

            <!-- Ana makale -->
            <div class="article-card">
                <span class="category-badge">{{main_category}}</span>
                <h3>{{main_title}}</h3>
                <p>{{main_summary}}</p>
                <a href="{self.base_url}/{{main_category}}/{{main_slug}}" class="button">Devamını Oku →</a>
            </div>

            <!-- İkinci makale -->
            <div class="article-card">
                <span class="category-badge">{{second_category}}</span>
                <h3>{{second_title}}</h3>
                <p>{{second_summary}}</p>
                <a href="{self.base_url}/{{second_category}}/{{second_slug}}" class="button">Devamını Oku →</a>
            </div>

            <h3>🔥 Bu Hafta Popüler Olan:</h3>
            <ul>
                <li><a href="{self.base_url}/{{popular1_category}}/{{popular1_slug}}">{{popular1_title}}</a></li>
                <li><a href="{self.base_url}/{{popular2_category}}/{{popular2_slug}}">{{popular2_title}}</a></li>
                <li><a href="{self.base_url}/{{popular3_category}}/{{popular3_slug}}">{{popular3_title}}</a></li>
            </ul>

            <h3>💡 Günün İpucu:</h3>
            <p><em>{{daily_tip}}</em></p>

            <p style="text-align: center; margin-top: 30px;">
                <a href="{self.base_url}" class="button">Tüm İçerikleri Gör</a>
            </p>
        </div>

        <div class="footer">
            <p>Yarın aynı saatte yeni içeriklerle buradayız!</p>
            <p>Bu emaili almak istemiyorsanız <a href="#">buradan</a> çıkabilirsiniz.</p>
            <p>© 2025 MindVerse. Web: <a href="{self.base_url}">{self.base_url}</a></p>
        </div>
    </div>
</body>
</html>
"""

        with open('email_templates/daily_digest.html', 'w', encoding='utf-8') as f:
            f.write(template)

        return template

    def create_weekly_roundup_template(self):
        """Haftalık özet email şablonu"""
        template = f"""
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Haftalık Özet</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f8f9fa;
            margin: 0;
            padding: 20px;
        }}
        .container {{
            max-width: 600px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .header {{
            background: linear-gradient(135deg, #ff6b6b 0%, #ffa726 100%);
            color: white;
            padding: 20px;
            text-align: center;
        }}
        .content {{
            padding: 20px;
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin: 20px 0;
        }}
        .stat-card {{
            background: #f8f9fa;
            padding: 15px;
            text-align: center;
            border-radius: 8px;
            border-left: 4px solid #ff6b6b;
        }}
        .top-articles {{
            background: #fff3cd;
            border: 1px solid #ffeaa7;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
        }}
        .article-item {{
            padding: 10px 0;
            border-bottom: 1px solid #e9ecef;
        }}
        .button {{
            display: inline-block;
            background: #ff6b6b;
            color: white;
            padding: 12px 24px;
            text-decoration: none;
            border-radius: 6px;
            margin: 10px 5px;
        }}
        .footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            font-size: 14px;
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔥 Bu Haftanın En İyileri</h1>
            <p>{{week_start}} - {{week_end}} Özeti</p>
        </div>

        <div class="content">
            <h2>Merhaba!</h2>
            <p>Bu hafta MindVerse'te neler oldu? İşte öne çıkanlar:</p>

            <div class="stats-grid">
                <div class="stat-card">
                    <h3>{{total_views}}</h3>
                    <p>Toplam Okuma</p>
                </div>
                <div class="stat-card">
                    <h3>{{new_articles}}</h3>
                    <p>Yeni Makale</p>
                </div>
            </div>

            <div class="top-articles">
                <h3>🏆 Bu Haftanın En Çok Okunanları</h3>

                <div class="article-item">
                    <strong>1. {{top1_title}}</strong><br>
                    <small>{{top1_category}} • {{top1_views}} okuma</small>
                </div>

                <div class="article-item">
                    <strong>2. {{top2_title}}</strong><br>
                    <small>{{top2_category}} • {{top2_views}} okuma</small>
                </div>

                <div class="article-item">
                    <strong>3. {{top3_title}}</strong><br>
                    <small>{{top3_category}} • {{top3_views}} okuma</small>
                </div>

                <div class="article-item">
                    <strong>4. {{top4_title}}</strong><br>
                    <small>{{top4_category}} • {{top4_views}} okuma</small>
                </div>

                <div class="article-item">
                    <strong>5. {{top5_title}}</strong><br>
                    <small>{{top5_category}} • {{top5_views}} okuma</small>
                </div>
            </div>

            <h3>📊 Kategori Analizi</h3>
            <p>Bu hafta en çok ilgi gören kategori: <strong>{{trending_category}}</strong></p>

            <h3>🎯 Gelecek Hafta</h3>
            <p>{{next_week_preview}}</p>

            <p style="text-align: center; margin-top: 30px;">
                <a href="{self.base_url}/popular" class="button">Popüler İçerikler</a>
                <a href="{self.base_url}/categories" class="button">Tüm Kategoriler</a>
            </p>
        </div>

        <div class="footer">
            <p>Bir sonraki haftalık özet 7 gün sonra gelecek!</p>
            <p>Bu emaili almak istemiyorsanız <a href="#">buradan</a> çıkabilirsiniz.</p>
            <p>© 2025 MindVerse. Web: <a href="{self.base_url}">{self.base_url}</a></p>
        </div>
    </div>
</body>
</html>
"""

        with open('email_templates/weekly_roundup.html', 'w', encoding='utf-8') as f:
            f.write(template)

        return template

    def create_email_automation_sequences(self):
        """Email otomasyon sıralamaları"""
        sequences = {
            "onboarding_sequence": {
                "name": "Yeni Abone Karşılama Serisi",
                "duration_days": 7,
                "emails": [
                    {
                        "day": 0,
                        "subject": "🌟 MindVerse'e Hoş Geldiniz! İlk Hediyeniz İçeride",
                        "template": "welcome_email",
                        "goal": "brand_introduction"
                    },
                    {
                        "day": 1,
                        "subject": "📚 İlk Günlük Bilgi Dozunuz Hazır",
                        "template": "daily_digest",
                        "goal": "content_engagement"
                    },
                    {
                        "day": 3,
                        "subject": "🎯 Hangi Konularda Uzmanlaşmak İstiyorsunuz?",
                        "template": "preference_survey",
                        "goal": "personalization"
                    },
                    {
                        "day": 7,
                        "subject": "🔥 İlk Haftanızın Özeti ve Özel Öneri",
                        "template": "week_one_summary",
                        "goal": "retention"
                    }
                ]
            },
            "engagement_sequence": {
                "name": "Etkileşim Artırma Serisi",
                "trigger": "low_engagement",
                "emails": [
                    {
                        "subject": "😊 Sizi Özledik! Geri Dönmeniz İçin Özel İçerikler",
                        "template": "re_engagement",
                        "goal": "win_back"
                    },
                    {
                        "subject": "🎁 Size Özel: En Popüler İçeriklerimizden Seçmeler",
                        "template": "special_curated",
                        "goal": "value_delivery"
                    }
                ]
            },
            "content_series": {
                "name": "Tematik İçerik Serileri",
                "frequency": "weekly",
                "series": [
                    {
                        "name": "Sağlık Serisi",
                        "duration_weeks": 4,
                        "category": "health",
                        "topics": ["Bağışıklık", "Beslenme", "Egzersiz", "Mental Sağlık"]
                    },
                    {
                        "name": "Psikoloji Serisi",
                        "duration_weeks": 4,
                        "category": "psychology",
                        "topics": ["Motivasyon", "Karar Verme", "İletişim", "Başarı"]
                    }
                ]
            }
        }

        with open('email_automation_sequences.json', 'w', encoding='utf-8') as f:
            json.dump(sequences, f, ensure_ascii=False, indent=2)

        return sequences

    def create_mailchimp_integration_guide(self):
        """Mailchimp entegrasyon rehberi"""
        guide = f"""
# 📧 Mailchimp Entegrasyon Rehberi

## 1. Mailchimp Hesap Kurulumu (ÜCRETSİZ)
1. https://mailchimp.com adresine git
2. "Sign Up Free" butonuna tıkla
3. Email, username ve şifre belirle
4. Hesabını doğrula

### Ücretsiz Plan Limitleri:
- 2,000 contact
- 10,000 email/month
- Basic templates
- Email automation
- Analytics

## 2. Audience (Liste) Oluşturma
1. Dashboard'da "Audience" tıkla
2. "Create Audience" seç
3. Liste bilgilerini doldur:
   - **List name:** MindVerse Newsletter
   - **Default from email:** info@yourdomain.com
   - **Default from name:** MindVerse
   - **Default subject:** MindVerse Günlük Bilgi Dozu

## 3. Signup Form (Kayıt Formu) Oluşturma
1. "Audience" → "Signup forms"
2. "Embedded forms" seç
3. Form tasarımını özelleştir
4. Generated kodu kopyala
5. MindVerse'e entegre et

### CTASection.astro Entegrasyonu:
```html
<!-- Mevcut form yerine Mailchimp form -->
<div id="mc_embed_signup">
<form action="https://yourdomain.us1.list-manage.com/subscribe/post?u=USER_ID&amp;id=LIST_ID"
      method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form"
      class="validate" target="_blank" novalidate>
    <div id="mc_embed_signup_scroll">
        <input type="email" value="" name="EMAIL" class="email"
               placeholder="E-posta adresiniz..." required>
        <div style="position: absolute; left: -5000px;" aria-hidden="true">
            <input type="text" name="b_USER_ID_LIST_ID" tabindex="-1" value="">
        </div>
        <div class="clear">
            <input type="submit" value="Bültene Katıl" name="subscribe"
                   id="mc-embedded-subscribe" class="button">
        </div>
    </div>
</form>
</div>
```

## 4. Email Templates Oluşturma
1. "Templates" bölümüne git
2. "Create Template" tıkla
3. "Code your own" seç
4. HTML template'ları kopyala/yapıştır

### Template Listesi:
- Welcome Email (Hoş geldin)
- Daily Digest (Günlük özet)
- Weekly Roundup (Haftalık özet)
- Re-engagement (Geri kazanım)

## 5. Automation Kurulumu
1. "Automations" tıkla
2. "Create" → "Email"
3. "Welcome new subscribers" seç

### Automation Akışı:
```
Abone olur → Hoş geldin email (0 gün)
           → Günlük digest (1 gün)
           → Anket email (3 gün)
           → Haftalık özet (7 gün)
```

## 6. Campaign Oluşturma (Günlük/Haftalık)
1. "Campaigns" tıkla
2. "Create Campaign" → "Email"
3. "Regular" seç
4. Template seç ve içerik ekle
5. Schedule veya Send

## 7. Newsletter Analytics
### Takip Edilecek Metrikler:
- **Open Rate:** %20+ (iyi)
- **Click Rate:** %3+ (iyi)
- **Unsubscribe Rate:** %2'nin altı
- **Growth Rate:** Aylık %10+

### Optimizasyon:
- A/B test subject lines
- Send time optimization
- Content personalization
- Mobile optimization

## 8. Segment Oluşturma
İleri seviye targeting için:
1. "Audience" → "Segments"
2. "Create Segment" tıkla
3. Kriterleri belirle:
   - Engagement level
   - Signup date
   - Geographic location
   - Email activity

## 9. API Entegrasyonu (Gelişmiş)
Newsletter admin paneli için:

```javascript
// Mailchimp API v3.0
const listId = 'YOUR_LIST_ID';
const apiKey = 'YOUR_API_KEY';
const serverPrefix = 'us1'; // API key'den çıkar

async function addSubscriber(email) {{
    const url = `https://${{serverPrefix}}.api.mailchimp.com/3.0/lists/${{listId}}/members`;

    const response = await fetch(url, {{
        method: 'POST',
        headers: {{
            'Authorization': `Basic ${{btoa(`anystring:${{apiKey}}`)}}`
            'Content-Type': 'application/json'
        }},
        body: JSON.stringify({{
            email_address: email,
            status: 'subscribed'
        }})
    }});

    return response.json();
}}
```

## 10. Günlük Workflow
### Pazartesi - Campaign Planning
- [ ] Haftalık content calendar
- [ ] Subject line ideas
- [ ] Segment analysis

### Salı-Cuma - Daily Digest
- [ ] Content selection
- [ ] Template customization
- [ ] Schedule sending (09:00)

### Cuma - Weekly Roundup
- [ ] Week performance analysis
- [ ] Top content compilation
- [ ] Next week preview

### Analytics Review (Haftalık)
- [ ] Open rates analysis
- [ ] Click-through optimization
- [ ] A/B test results
- [ ] List growth review

---
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Site: {self.base_url}
"""

        with open('mailchimp_integration_guide.md', 'w', encoding='utf-8') as f:
            f.write(guide)

        print("✅ Mailchimp entegrasyon rehberi: mailchimp_integration_guide.md")

    def create_email_templates_folder(self):
        """Email template klasörü ve dosyaları oluştur"""
        os.makedirs('email_templates', exist_ok=True)

        # Template'ları oluştur
        self.create_welcome_email_template()
        self.create_daily_digest_template()
        self.create_weekly_roundup_template()

        print("✅ Email template'ları oluşturuldu: email_templates/")

    def generate_email_content_calendar(self):
        """30 günlük email içerik takvimi"""
        calendar = {}

        # Email türleri ve frekansları
        daily_digest_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        weekly_roundup_day = 'sunday'

        for day in range(30):
            date = (datetime.now() + timedelta(days=day)).strftime('%Y-%m-%d')
            weekday = (datetime.now() + timedelta(days=day)).strftime('%A').lower()

            calendar[date] = {
                'date': date,
                'weekday': weekday,
                'emails': []
            }

            # Günlük digest (hafta içi)
            if weekday in daily_digest_days:
                calendar[date]['emails'].append({
                    'type': 'daily_digest',
                    'time': '09:00',
                    'subject': f'📚 Günlük Bilgi Dozu - {date}',
                    'template': 'daily_digest'
                })

            # Haftalık özet (pazar)
            if weekday == weekly_roundup_day:
                calendar[date]['emails'].append({
                    'type': 'weekly_roundup',
                    'time': '10:00',
                    'subject': '🔥 Bu Haftanın En Popüler İçerikleri',
                    'template': 'weekly_roundup'
                })

            # Özel kampanyalar (2 haftada bir çarşamba)
            if weekday == 'wednesday' and day % 14 == 0:
                calendar[date]['emails'].append({
                    'type': 'special_campaign',
                    'time': '14:00',
                    'subject': '🎯 Size Özel İçerik Önerileri',
                    'template': 'special_curated'
                })

        with open('email_content_calendar.json', 'w', encoding='utf-8') as f:
            json.dump(calendar, f, ensure_ascii=False, indent=2)

        return calendar

def main():
    email_system = EmailMarketingSystem()

    print("📧 MindVerse Email Marketing Sistemi Başlatılıyor...")

    # Email template'larını oluştur
    email_system.create_email_templates_folder()

    # Otomasyon sıralarını oluştur
    sequences = email_system.create_email_automation_sequences()

    # Mailchimp entegrasyon rehberi
    email_system.create_mailchimp_integration_guide()

    # 30 günlük email takvimi
    calendar = email_system.generate_email_content_calendar()

    print(f"""
📬 Email Marketing Sistemi Hazır!

📁 Oluşturulan Dosyalar:
- email_templates/ (3 HTML template)
- email_automation_sequences.json (otomasyon akışları)
- mailchimp_integration_guide.md (kurulum rehberi)
- email_content_calendar.json (30 günlük takvim)

🎯 Kurulum Adımları:
1. Mailchimp hesabı oluştur (ücretsiz)
2. Email template'ları yükle
3. Automation akışlarını kur
4. CTASection.astro'yu güncelle
5. Newsletter admin panelini Mailchimp API'ye bağla

📊 Hedefler:
- İlk 30 gün: 100 abone
- Açılma oranı: %25+
- Tıklama oranı: %5+
- Aylık büyüme: %20+

💡 Ücretsiz Alternatifler:
- Mailchimp: 2000 contact, 10K email/ay
- Sendinblue: 300 email/gün, sınırsız contact
- Mailjet: 6000 email/ay, 200/gün
- Gmail SMTP: 500 email/gün

🚀 Bu Hafta Görevi: Mailchimp kurulumu ve ilk campaign!
""")

if __name__ == "__main__":
    main()
