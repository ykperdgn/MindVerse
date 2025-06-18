#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MindVerse Tam Otomatik Sosyal Medya Sistemi
Ücretsiz araçlarla sosyal medya paylaşımlarını tamamen otomatikleştir
"""

import json
import os
import requests
import schedule
import time
from datetime import datetime, timedelta
import tweepy
import subprocess
from pathlib import Path

class AutoSocialMediaPoster:
    def __init__(self):
        self.base_url = "https://www.mindversedaily.com"
        self.automation_tools = {
            'buffer': {
                'free_limit': '3 hesap, 10 post/ay',
                'api_available': True,
                'cost': 'Ücretsiz',
                'platforms': ['Twitter', 'Facebook', 'LinkedIn', 'Instagram']
            },
            'hootsuite': {
                'free_limit': '3 sosyal ağ, 5 post/ay',
                'api_available': True,
                'cost': 'Ücretsiz',
                'platforms': ['Twitter', 'Facebook', 'LinkedIn', 'Instagram']
            },
            'later': {
                'free_limit': '30 post/ay, 1 social set',
                'api_available': True,
                'cost': 'Ücretsiz',
                'platforms': ['Instagram', 'Twitter', 'Facebook', 'Pinterest']
            },
            'zapier': {
                'free_limit': '100 task/ay',
                'api_available': True,
                'cost': 'Ücretsiz',
                'platforms': ['Hepsi (webhook ile)']
            }
        }

    def create_buffer_integration_guide(self):
        """Buffer ile tam otomasyon rehberi"""
        guide = f"""
# 🤖 Buffer ile Tam Otomatik Sosyal Medya Rehberi

## 1. Buffer Hesap Kurulumu (ÜCRETSİZ)

### A. Hesap Oluşturma
1. https://buffer.com adresine git
2. "Get started for free" tıkla
3. Email ile kayıt ol
4. Email doğrulama yap

### B. Ücretsiz Plan Limitleri
- **3 sosyal hesap** bağlayabilirsin
- **10 post** aylık limit
- **1 kullanıcı**
- Temel analytics
- Taslak post özelliği

## 2. Sosyal Medya Hesaplarını Bağla

### Twitter Bağlantısı
1. Buffer dashboard'da "Connect Account" tıkla
2. Twitter seç
3. @mindverse_tr hesabını bağla
4. İzinleri onayla

### Instagram Bağlantısı
1. Instagram Business hesabına geç
2. Facebook Page'e bağla
3. Buffer'da Instagram seç
4. Facebook izinleri ver

### LinkedIn Bağlantısı
1. LinkedIn Company Page oluştur: "MindVerse"
2. Buffer'da LinkedIn seç
3. Company page'i seç
4. İzinleri onayla

## 3. Otomatik İçerik Yükleme

### A. Manuel Yükleme (Başlangıç)
Buffer'a günlük 1-2 post yükle:

**Sabah Postu (09:00):**
```
🌟 Günün motivasyonu: "Bilgi, paylaştıkça çoğalan tek şeydir."

📚 Bugünün önerisi: {self.base_url}/popular

#eğitim #motivasyon #bilgi #blog
```

**Akşam Postu (19:00):**
```
📖 Bugün ne öğrendiniz?

Bizden öneri: {self.base_url}/[kategori]

💬 Yorumlarda paylaşın!

#öğrenme #gelişim #soru
```

### B. Bulk Upload (Toplu Yükleme)
1. CSV dosyası hazırla:
```csv
Platform,Content,Scheduled Time,Image URL
Twitter,"Sağlık bilgisi: ...",2025-06-19 09:00,
Facebook,"Detaylı sağlık rehberi...",2025-06-19 13:00,
LinkedIn,"Profesyonel gelişim...",2025-06-19 15:00,
```

2. Buffer'da "Bulk Upload" kullan
3. CSV'yi yükle
4. Schedule'ı onayla

## 4. RSS Feed Otomasyonu

### A. Buffer RSS Özelliği (Pro gerektirir)
Buffer Pro'da RSS feed ekleyerek otomatik post:

1. Settings → RSS Feeds
2. Feed URL ekle: `{self.base_url}/sitemap.xml`
3. Post template belirle:
```
📝 Yeni makale: {{title}}

{{summary}}

👉 Devamı: {{link}}

#blog #yenimakale #{{category}}
```

### B. Zapier ile RSS Otomasyonu (ÜCRETSİZ 100 task/ay)

**Webhook Setup:**
1. Zapier hesabı aç
2. "Make a Zap" tıkla
3. Trigger: RSS by Zapier
4. RSS URL: `{self.base_url}/sitemap.xml`
5. Action: Buffer → Create Post

**Zap Template:**
```
Trigger: New RSS item
Action: Buffer post oluştur
Content: "📝 {{title}} - {{summary}} 👉 {{link}} #blog"
Schedule: Immediate
```

## 5. Canva ile Görsel Otomasyonu

### A. Canva + Buffer Entegrasyonu
1. Canva'da template oluştur
2. "Share" → "Schedule with Buffer"
3. Buffer'da otomatik post oluşturulur

### B. Toplu Görsel Hazırlama
**Template'lar hazırla:**
- Quote cards (Alıntılar kategorisi için)
- Tip cards (Liste makaleler için)
- Category headers (Her kategori için)
- Statistics cards (Rakam içeren postlar için)

## 6. IFTTT ile Ek Otomasyon

### A. IFTTT Applets (Ücretsiz)
1. https://ifttt.com hesabı aç
2. "Create" tıkla
3. Useful applets:

**Yeni Blog Post → Twitter:**
```
IF: RSS feed has new item
THEN: Twitter'da post at
Content: "🆕 {{EntryTitle}} 👉 {{EntryUrl}} #blog #{{category}}"
```

**Instagram Post → Twitter:**
```
IF: Instagram'da yeni post
THEN: Twitter'da paylaş
Content: "📸 Instagram'da yeni: {{Caption}} 🔗 {{Url}}"
```

## 7. Scheduling Best Practices

### A. Optimal Posting Times
**Twitter:** 09:00, 12:00, 17:00, 20:00
**Instagram:** 11:00, 14:00, 17:00, 20:00
**LinkedIn:** 08:00, 12:00, 14:00, 17:00
**Facebook:** 13:00, 15:00, 19:00

### B. Content Mix (30 günlük cycle)
- **50%** Blog promotion posts
- **20%** Motivational/Quote posts
- **15%** Engagement questions
- **10%** Behind-the-scenes
- **5%** Retweets/shares

## 8. Analytics ve Optimization

### A. Buffer Analytics (Free)
Track edilen metrikler:
- Reach
- Engagement
- Clicks
- Best performing times
- Top content

### B. Weekly Review Process
**Her Pazar:**
1. Buffer analytics incelenecek
2. En iyi performing content analizi
3. Gelecek hafta content'i planlanacak
4. Posting times optimization

## 9. Advanced Automation (Webhooks)

### A. MindVerse → Buffer Webhook
Yeni makale yayınlandığında otomatik post:

```python
import requests

def auto_post_new_article(title, category, url):
    buffer_api_url = "https://api.bufferapp.com/1/updates/create.json"

    content = f"""
📝 Yeni {category} makalesi!

{title}

👉 {url}

#{category} #blog #mindverse
"""

    payload = {{
        'access_token': 'YOUR_BUFFER_TOKEN',
        'profile_ids[]': 'PROFILE_ID',
        'text': content,
        'shorten': 'false'
    }}

    response = requests.post(buffer_api_url, data=payload)
    return response.json()
```

### B. Schedule Optimization Script
```python
import schedule
import time

def daily_content_check():
    # Yeni content var mı kontrol et
    # Buffer queue'sini kontrol et
    # Gerekirse yeni post ekle
    pass

schedule.every().day.at("08:00").do(daily_content_check)

while True:
    schedule.run_pending()
    time.sleep(3600)  # Her saat kontrol
```

## 10. Emergency & Backup Plans

### A. Content Backlog
Her zaman 1 haftalık content hazır tut:
- 7 günlük post queue
- Emergency motivational posts
- Generic category posts

### B. Platform Downtime Backup
Buffer down olursa:
1. Native scheduler kullan (Twitter, LinkedIn)
2. Manuel posting
3. Later.com backup account

## 🚀 Implementation Timeline

### Hafta 1: Setup
- [ ] Buffer hesabı aç
- [ ] 3 platform bağla
- [ ] İlk 10 post yükle

### Hafta 2: Automation
- [ ] Zapier/IFTTT setup
- [ ] RSS feed bağlantısı
- [ ] Canva templates

### Hafta 3: Optimization
- [ ] Analytics review
- [ ] Posting time optimization
- [ ] Content mix adjustment

### Hafta 4: Scale
- [ ] Webhook integration
- [ ] Advanced automation
- [ ] Backup systems

---

**Sonuç:** Bu rehberle sosyal medya paylaşımların %90 otomatik olacak!

Only manual work: Content creation + strategy adjustment (Weekly 30 dakika)

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
"""

        with open('buffer_automation_guide.md', 'w', encoding='utf-8') as f:
            f.write(guide)

        return guide

    def create_twitter_api_automation(self):
        """Twitter API ile doğrudan otomasyon"""
        twitter_script = f'''
import tweepy
import json
import schedule
import time
from datetime import datetime

class TwitterAutoPoster:
    def __init__(self):
        # Twitter API credentials (FREE tier)
        self.api_key = "YOUR_API_KEY"
        self.api_secret = "YOUR_API_SECRET"
        self.access_token = "YOUR_ACCESS_TOKEN"
        self.access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

        # Twitter API v2 authentication
        self.client = tweepy.Client(
            consumer_key=self.api_key,
            consumer_secret=self.api_secret,
            access_token=self.access_token,
            access_token_secret=self.access_token_secret
        )

    def tweet_daily_content(self):
        """Günlük içerik tweeti"""
        tweets = [
            "🌟 Günün motivasyonu: Bilgi, paylaştıkça çoğalan tek şeydir! 📚 {self.base_url}/popular #motivasyon #bilgi",
            "🧠 Psikoloji dünyasından: Başarı zihniyeti nasıl geliştirilir? 👉 {self.base_url}/psychology #psikoloji",
            "❤️ İlişkiler: Sağlıklı iletişimin 5 altın kuralı 💕 {self.base_url}/love #ilişkiler #aşk",
            "🏥 Sağlık ipucu: Bağışıklığı güçlendiren doğal yöntemler ✨ {self.base_url}/health #sağlık",
            "🚀 Uzay merakı: Kara delikler hakkında şaşırtıcı gerçekler 🌌 {self.base_url}/space #uzay",
            "📚 Tarihten bugüne: Antik medeniyetlerin kayıp teknolojileri 🏛️ {self.base_url}/history #tarih"
        ]

        import random
        tweet_content = random.choice(tweets)

        try:
            response = self.client.create_tweet(text=tweet_content)
            print(f"Tweet posted: {{response.data['id']}}")
        except Exception as e:
            print(f"Error posting tweet: {{e}}")

    def schedule_tweets(self):
        """Tweet programlama"""
        # Günde 3 tweet
        schedule.every().day.at("09:00").do(self.tweet_daily_content)
        schedule.every().day.at("14:00").do(self.tweet_daily_content)
        schedule.every().day.at("19:00").do(self.tweet_daily_content)

        print("Tweet scheduler başlatıldı...")

        while True:
            schedule.run_pending()
            time.sleep(60)  # Her dakika kontrol

if __name__ == "__main__":
    poster = TwitterAutoPoster()
    poster.schedule_tweets()
'''

        with open('twitter_auto_poster.py', 'w', encoding='utf-8') as f:
            f.write(twitter_script)

        return twitter_script

    def create_instagram_automation_guide(self):
        """Instagram otomasyonu için rehber"""
        guide = f"""
# 📸 Instagram Tam Otomatik Posting Rehberi

## 🚨 Instagram API Kısıtlamaları
Instagram API'si kısıtlı olduğu için ücretsiz otomatik posting zor.
Alternatif çözümler:

## 1. Creator Studio ile Manuel-Otomatik Hybrid

### A. Facebook Creator Studio (ÜCRETSİZ)
1. Facebook Business hesabı aç
2. Instagram Business'a geç
3. Facebook Page oluştur: "MindVerse"
4. Instagram'ı Facebook Page'e bağla
5. Creator Studio: https://business.facebook.com/creatorstudio

### B. Bulk Upload Process
1. Creator Studio → "Create Post"
2. Instagram seç
3. Multiple posts oluştur
4. Schedule için tarih/saat seç
5. "Schedule" tıkla

### C. Content Templates

**Daily Quote Card:**
```
🌟 Günün İlham Sözü

"[ALINTI]"

📚 Daha fazlası için: {self.base_url}

#motivasyon #ilham #alıntı #mindverse
```

**Category Spotlight:**
```
🧠 Psikoloji Köşesi

[KATEGORİ BİLGİSİ - 2-3 cümle]

🔗 Link bio'da

#psikoloji #zihin #gelişim
```

## 2. Later.com ile Instagram Automation

### A. Later Free Plan (30 post/ay)
1. https://later.com hesabı aç
2. Instagram Business bağla
3. Visual Calendar kullan
4. Auto-posting aktifleştir

### B. Content Calendar Setup
**Pazartesi:** Sağlık içeriği
**Salı:** Psikoloji insights
**Çarşamba:** İlişki tavsiyeleri
**Perşembe:** Tarih bilgileri
**Cuma:** Uzay merakları
**Cumartesi:** Motivasyon sözleri
**Pazar:** Haftalık özet

## 3. Canva + Scheduling Workflow

### A. Bulk Visual Creation
1. Canva'da MindVerse branded template oluştur
2. 30 günlük content batch oluştur
3. Canva → Later integration kullan
4. Otomatik schedule

### B. Template Library
- **Quote cards:** 7 farklı stil
- **Tip graphics:** Liste formatı
- **Category headers:** 6 kategori için
- **Behind scenes:** Süreç görselleri

## 4. Stories Automation

### A. Instagram Stories Scheduler
Later ile:
1. Stories tab aç
2. Multiple stories hazırla
3. Schedule → Auto-post

### B. Story Content Ideas
- **Polls:** "Bugün hangi konuda okumak istersiniz?"
- **Questions:** "Sağlık hakkında merak ettikleriniz?"
- **Quick Tips:** Günlük 1 ipucu
- **BTS:** Content creation process

---
**Sonuç:** Instagram %80 otomatik olabilir (Stories hariç)
Manual work: Story interactions + community management
"""

        with open('instagram_automation_guide.md', 'w', encoding='utf-8') as f:
            f.write(guide)

        return guide

    def create_complete_automation_dashboard(self):
        """Tüm platform otomasyonu için dashboard"""
        dashboard = {
            "automation_status": {
                "twitter": {
                    "method": "Buffer + Twitter API",
                    "automation_level": "95%",
                    "manual_tasks": ["Community management", "Trend hijacking"],
                    "cost": "Free"
                },
                "instagram": {
                    "method": "Later + Creator Studio",
                    "automation_level": "80%",
                    "manual_tasks": ["Stories interaction", "Comment responses"],
                    "cost": "Free (30 posts/month)"
                },
                "linkedin": {
                    "method": "Buffer + Native scheduler",
                    "automation_level": "90%",
                    "manual_tasks": ["Professional networking", "Article sharing"],
                    "cost": "Free"
                },
                "facebook": {
                    "method": "Creator Studio + Buffer",
                    "automation_level": "85%",
                    "manual_tasks": ["Group participation", "Community building"],
                    "cost": "Free"
                }
            },
            "posting_schedule": {
                "monday": {
                    "09:00": "Twitter - Motivational quote",
                    "11:00": "Instagram - Health post",
                    "13:00": "Facebook - Weekly preview",
                    "15:00": "LinkedIn - Professional insight",
                    "19:00": "Twitter - Blog promotion"
                },
                "tuesday": {
                    "09:00": "Twitter - Psychology tip",
                    "11:00": "Instagram - Quote card",
                    "14:00": "LinkedIn - Industry news",
                    "19:00": "Twitter - Engagement question"
                }
                # ... diğer günler
            },
            "automation_tools": {
                "primary": "Buffer (3 accounts, 10 posts/month)",
                "secondary": "Later (Instagram, 30 posts/month)",
                "backup": "Native schedulers",
                "content_creation": "Canva (free templates)",
                "analytics": "Native platform analytics"
            },
            "weekly_manual_tasks": [
                "Buffer queue replenishment (30 min)",
                "Analytics review (15 min)",
                "Community engagement (45 min)",
                "Content calendar update (20 min)"
            ],
            "success_metrics": {
                "posts_per_week": 21,
                "automation_percentage": 87,
                "manual_time_required": "2 hours/week",
                "cost": "0 TL/month"
            }
        }

        with open('social_automation_dashboard.json', 'w', encoding='utf-8') as f:
            json.dump(dashboard, f, ensure_ascii=False, indent=2)

        return dashboard

def main():
    automator = AutoSocialMediaPoster()

    print("🤖 Tam Otomatik Sosyal Medya Sistemi Kuruluyor...")

    # Buffer rehberi oluştur
    buffer_guide = automator.create_buffer_integration_guide()

    # Twitter API script
    twitter_script = automator.create_twitter_api_automation()

    # Instagram rehberi
    instagram_guide = automator.create_instagram_automation_guide()

    # Automation dashboard
    dashboard = automator.create_complete_automation_dashboard()

    print(f"""
🎯 TAM OTOMATİK SOSYAl MEDYA SİSTEMİ HAZIR!

📊 Otomasyon Seviyeleri:
┌─────────────────────────────────────┐
│ Twitter:   95% otomatik ✅          │
│ Instagram: 80% otomatik ⚡          │
│ LinkedIn:  90% otomatik ✅          │
│ Facebook:  85% otomatik ⚡          │
└─────────────────────────────────────┘

🔧 Kullanılacak Araçlar (ÜCRETSİZ):
✅ Buffer: 3 hesap, 10 post/ay
✅ Later: Instagram için 30 post/ay
✅ Creator Studio: Instagram + Facebook
✅ Zapier: 100 automation/ay
✅ IFTTT: Sınırsız applet

📅 Otomatik Posting Schedule:
- Twitter: Günde 3 tweet (09:00, 14:00, 19:00)
- Instagram: Günde 1 post (11:00)
- LinkedIn: Haftada 3 post
- Facebook: Haftada 2 post

⏰ Haftalık Manuel İş: Sadece 2 saat!
- Buffer queue doldurma: 30 dakika
- Community management: 45 dakika
- Analytics review: 15 dakika
- Content planning: 20 dakika

🚀 Kurulum Adımları:
1. Buffer hesabı aç (buffer.com)
2. Sosyal medya hesaplarını bağla
3. İlk 10 post'u yükle ve schedule et
4. Zapier ile RSS feed automation kur
5. Later'da Instagram automation başlat

📈 Beklenen Sonuçlar:
- Haftalık 21 otomatik post
- %87 otomasyon oranı
- 0 TL aylık maliyet
- Consistent brand presence

💡 PRO TİP:
Buffer'ın ücretsiz planı ile başla,
büyüdükçe Pro'ya geç (aylık 15$)

🎯 1 hafta içinde tam otomatik sosyal medya!
""")

if __name__ == "__main__":
    main()
