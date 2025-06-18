#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MindVerse Sosyal Medya Otomasyonu
Ücretsiz hesaplar kullanarak sosyal medya paylaşımlarını otomatikleştirir
"""

import json
import os
import random
from datetime import datetime, timedelta
import hashlib
import requests
from pathlib import Path

class SocialMediaAutomator:
    def __init__(self):
        self.base_url = "https://mindverse-orcin.vercel.app"
        self.categories = {
            'health': {'emoji': '🏥', 'hashtags': ['#sağlık', '#wellness', '#health', '#sağlıklıyaşam', '#tıp']},
            'love': {'emoji': '❤️', 'hashtags': ['#aşk', '#ilişkiler', '#love', '#relationship', '#dating']},
            'history': {'emoji': '📚', 'hashtags': ['#tarih', '#history', '#kültür', '#geçmiş', '#bilgi']},
            'psychology': {'emoji': '🧠', 'hashtags': ['#psikoloji', '#psychology', '#zihin', '#mental', '#davranış']},
            'space': {'emoji': '🚀', 'hashtags': ['#uzay', '#space', '#astronomi', '#bilim', '#keşif']},
            'quotes': {'emoji': '💭', 'hashtags': ['#alıntılar', '#quotes', '#motivasyon', '#ilham', '#söz']}
        }
        
    def generate_tweets(self, count=50):
        """Twitter için otomatik tweet'ler oluştur"""
        tweets = []
        
        # Günlük motivasyon tweet'leri
        motivation_tweets = [
            f"🌟 Bugün kendinizi geliştirmek için ne yapacaksınız? {self.base_url}/popular #motivasyon #gelişim",
            f"💡 Bilgi güçtür, paylaşılan bilgi ise çifte güçtür! {self.base_url} #bilgi #eğitim",
            f"🎯 Her gün yeni bir şey öğrenmek, hayatı zenginleştirir. {self.base_url}/categories #öğrenme",
            f"🔥 En popüler içeriklerimize göz attınız mı? {self.base_url}/popular #trending",
            f"📖 Bugün hangi konuda bilgi edinmek istiyorsunız? {self.base_url} #soru #merak"
        ]
        
        # Kategori bazlı tweet'ler
        for category, info in self.categories.items():
            hashtags = ' '.join(info['hashtags'][:3])
            tweets.extend([
                f"{info['emoji']} {category.title()} konusunda yeni içerikler! {self.base_url}/{category} {hashtags}",
                f"🔍 {category.title()} kategorisinde aradığınızı bulamıyor musunuz? {self.base_url}/search {hashtags}",
                f"📊 {category.title()} alanında en çok okunan yazılar: {self.base_url}/{category} {hashtags}"
            ])
        
        # Etkileşim artırıcı sorular
        engagement_tweets = [
            f"❓ Hangi konuda daha fazla içerik görmek istersiniz? Yorumlarda belirtin! {self.base_url} #soru",
            f"💬 En çok hangi kategoriye ilgi duyuyorsunuz? {self.base_url}/categories #anket",
            f"🤔 Bilgi edinirken en çok hangi kaynaklara güveniyorsunuz? {self.base_url} #güven",
            f"📝 Yeni bir şey öğrendiğinizde ilk kim ile paylaşıyorsunuz? {self.base_url} #paylaşım",
            f"⭐ Favori içerik türünüz hangisi? {self.base_url}/popular #favoriler"
        ]
        
        tweets.extend(motivation_tweets)
        tweets.extend(engagement_tweets)
        
        # Hashtag optimizasyonu ekle
        trending_hashtags = ['#eğitim', '#bilim', '#kültür', '#gelişim', '#öğrenme', '#araştırma', '#blog', '#içerik']
        
        for i, tweet in enumerate(tweets):
            if len(tweets[i]) < 200:  # Twitter karakter limiti
                extra_hashtag = random.choice(trending_hashtags)
                if extra_hashtag not in tweet:
                    tweets[i] += f" {extra_hashtag}"
        
        return tweets[:count]
    
    def generate_facebook_posts(self, count=30):
        """Facebook için uzun format postlar"""
        posts = []
        
        post_templates = [
            {
                "title": "🧠 Psikoloji Dünyasından İlginç Gerçekler",
                "content": """Psikoloji alanındaki en son araştırmalar şaşırtıcı sonuçlar ortaya çıkarıyor! 

🔍 Bilincaltımızın günlük kararlarımıza etkisi
💭 Motivasyon mekanizmalarının bilimsel temelleri  
🎯 Başarıya giden zihinsel stratejiler

Daha fazlası için: {url}/psychology

#psikoloji #zihin #motivasyon #başarı #bilim""",
                "category": "psychology"
            },
            {
                "title": "🏥 Sağlıklı Yaşamın Bilimsel Temelleri",
                "content": """Modern yaşamda sağlığımızı korumak için neleri bilmeliyiz?

✅ Bağışıklık sistemini güçlendiren yöntemler
✅ Stres yönetimi teknikleri
✅ Uyku kalitesini artırmanın yolları

Uzman tavsiyeleri ve bilimsel verilerle: {url}/health

#sağlık #wellness #bağışıklık #stres #uyku""",
                "category": "health"
            },
            {
                "title": "🚀 Uzayın Gizemli Dünyası",
                "content": """Evrenin sırları her geçen gün biraz daha açığa çıkıyor!

🌌 Karanlık maddenin gizemli yapısı
🕳️ Kara deliklerin zaman üzerindeki etkisi
⭐ Yıldızların yaşam döngüleri

Uzay bilimlerindeki son keşifler: {url}/space

#uzay #astronomi #bilim #keşif #evren""",
                "category": "space"
            }
        ]
        
        for template in post_templates:
            posts.append({
                "title": template["title"],
                "content": template["content"].format(url=self.base_url),
                "category": template["category"],
                "hashtags": self.categories[template["category"]]["hashtags"]
            })
        
        return posts * (count // len(post_templates) + 1)[:count]
    
    def generate_instagram_posts(self, count=40):
        """Instagram için görsel odaklı postlar"""
        posts = []
        
        for category, info in self.categories.items():
            # Her kategori için 6-7 post
            category_posts = [
                {
                    "caption": f"{info['emoji']} {category.title()} dünyasından ilham verici içerikler!\n\n📖 Blog: {self.base_url}/{category}\n\n{' '.join(info['hashtags'])} #blog #içerik #bilgi",
                    "image_suggestion": f"Kategori: {category} - Minimalist tasarım, {info['emoji']} emoji, modern tipografi",
                    "category": category
                },
                {
                    "caption": f"💡 Bugünün konusu: {category.title()}!\n\n🔍 Detaylar: {self.base_url}/{category}\n\n{' '.join(info['hashtags'][:3])} #günün konusu",
                    "image_suggestion": f"Konu başlığı kartı - {category}",
                    "category": category
                }
            ]
            posts.extend(category_posts)
        
        # Genel motivasyon postları
        motivation_posts = [
            {
                "caption": f"🌟 Her gün yeni bir şey öğrenmek, hayatın en büyük hediyesi!\n\n📚 {self.base_url}\n\n#öğrenme #gelişim #bilgi #motivasyon #eğitim",
                "image_suggestion": "Motivasyonel quote tasarımı",
                "category": "general"
            },
            {
                "caption": f"🎯 Bilgi paylaştıkça çoğalır!\n\n🔗 {self.base_url}/popular\n\n#paylaşım #bilgi #topluluk #gelişim",
                "image_suggestion": "Community/paylaşım temalı görsel",
                "category": "general"
            }
        ]
        
        posts.extend(motivation_posts)
        return posts[:count]
    
    def generate_linkedin_posts(self, count=25):
        """LinkedIn için profesyonel içerikler"""
        posts = []
        
        professional_templates = [
            {
                "title": "Psikoloji ve İş Hayatı",
                "content": """İş dünyasında psikolojik faktörlerin önemi her geçen gün artıyor.

🎯 Liderlik psikolojisi
🤝 Takım dinamikleri  
💼 Motivasyon teknikleri
📈 Performans optimizasyonu

Detaylı analiz: {url}/psychology

#leadership #psychology #business #motivation #performance""",
                "category": "psychology"
            },
            {
                "title": "Sağlıklı Çalışma Hayatı",
                "content": """Modern çalışma yaşamında sağlığımızı korumak kritik bir beceri haline geldi.

⚡ Stres yönetimi stratejileri
🧘 Mindfulness teknikleri
💪 Fiziksel sağlık ipuçları
😴 Uyku hijyeni

Profesyonel rehber: {url}/health

#worklifebalance #health #productivity #wellness #stress""",
                "category": "health"
            }
        ]
        
        for template in professional_templates:
            posts.append({
                "title": template["title"],
                "content": template["content"].format(url=self.base_url),
                "category": template["category"]
            })
        
        return posts * (count // len(professional_templates) + 1)[:count]
    
    def save_social_content(self):
        """Tüm sosyal medya içeriklerini kaydet"""
        social_content = {
            "generated_date": datetime.now().isoformat(),
            "twitter": self.generate_tweets(),
            "facebook": self.generate_facebook_posts(),
            "instagram": self.generate_instagram_posts(),
            "linkedin": self.generate_linkedin_posts(),
            "posting_schedule": self.generate_posting_schedule()
        }
        
        # JSON dosyasına kaydet
        with open('social_media_content.json', 'w', encoding='utf-8') as f:
            json.dump(social_content, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Sosyal medya içerikleri kaydedildi: social_media_content.json")
        return social_content
    
    def generate_posting_schedule(self):
        """7 günlük paylaşım programı oluştur"""
        schedule = {}
        platforms = ['twitter', 'facebook', 'instagram', 'linkedin']
        
        # En iyi paylaşım saatleri
        best_times = {
            'twitter': ['09:00', '12:00', '17:00', '20:00'],
            'facebook': ['13:00', '15:00', '19:00'],
            'instagram': ['11:00', '14:00', '17:00', '20:00'],
            'linkedin': ['08:00', '12:00', '14:00', '17:00']
        }
        
        for day in range(7):
            date = (datetime.now() + timedelta(days=day)).strftime('%Y-%m-%d')
            schedule[date] = {}
            
            for platform in platforms:
                posts_per_day = {
                    'twitter': 4,
                    'facebook': 1,
                    'instagram': 2,
                    'linkedin': 1
                }[platform]
                
                times = random.sample(best_times[platform], min(posts_per_day, len(best_times[platform])))
                schedule[date][platform] = times
        
        return schedule
    
    def create_social_media_guide(self):
        """Sosyal medya kullanım rehberi oluştur"""
        guide = f"""
# 📱 MindVerse Sosyal Medya Rehberi

## 🎯 Platform Stratejileri

### Twitter (@mindverse_blog)
- Günde 3-4 tweet
- Etkileşim odaklı
- Hashtag kullanımı: 2-3 adet
- En iyi saatler: 09:00, 12:00, 17:00, 20:00

### Facebook (MindVerse Blog)
- Günde 1 uzun post
- Görsel ile destekle
- Community building odaklı
- En iyi saatler: 13:00, 15:00, 19:00

### Instagram (@mindverse_tr)
- Günde 1-2 görsel post
- Story kullanımı: günde 3-5
- Reels potansiyeli yüksek
- En iyi saatler: 11:00, 14:00, 17:00, 20:00

### LinkedIn (MindVerse)
- Haftada 3-4 profesyonel post
- Endüstri insights
- Thought leadership
- En iyi saatler: 08:00, 12:00, 14:00, 17:00

## 📈 Ücretsiz Büyüme Taktikleri

### 1. Hashtag Stratejisi
- Ana hashtag'ler: #eğitim #bilgi #blog #öğrenme
- Niche hashtag'ler: kategori bazlı
- Trending hashtag'leri takip et

### 2. Etkileşim Artırma
- Sorular sor
- Anketler düzenle
- User generated content teşvik et
- Diğer hesaplarla etkileşim kur

### 3. İçerik Çeşitlendirme
- Behind the scenes
- Tips & tricks
- Motivational quotes
- Industry news commentary

### 4. Cross-Platform Promotion
- Her platformda diğerlerine yönlendir
- Newsletter signup'ı teşvik et
- Website trafiğini artır

## 🤖 Otomasyon Araçları (Ücretsiz)

1. **Buffer** (ücretsiz plan): 3 hesap, 10 post
2. **Hootsuite** (ücretsiz): 3 sosyal ağ
3. **Later** (ücretsiz): 30 post/ay
4. **Canva** (ücretsiz): görsel tasarım
5. **Google Analytics**: trafik takibi

## 📊 Takip Edilecek Metrikler

### Twitter
- Impression, engagement rate
- Profile visits, follower growth
- Link clicks, mentions

### Facebook  
- Reach, engagement
- Page likes, post shares
- Website clicks

### Instagram
- Reach, impressions
- Profile visits, website clicks
- Hashtag performance

### LinkedIn
- Impression, engagement
- Profile views, connection requests
- Article views

## 🎨 Görsel İçerik Önerileri

### Canva Şablonları (Ücretsiz)
- Quote cards: motivasyonel sözler
- Tip cards: kısa öneriler  
- Statistics: istatistik paylaşımları
- Behind the scenes: süreç görselleri

### Unsplash/Pexels (Ücretsiz Stok Fotoğraflar)
- Eğitim temalı
- Bilim/teknoloji
- Kitap/okuma
- Çalışma masası setup'ları

Site URL: {self.base_url}
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
"""
        
        with open('social_media_guide.md', 'w', encoding='utf-8') as f:
            f.write(guide)
        
        print("✅ Sosyal medya rehberi oluşturuldu: social_media_guide.md")

def main():
    automator = SocialMediaAutomator()
    
    print("🚀 MindVerse Sosyal Medya Otomasyonu Başlatılıyor...")
    
    # İçerikleri oluştur ve kaydet
    content = automator.save_social_content()
    
    # Rehber oluştur
    automator.create_social_media_guide()
    
    # Özet bilgi
    print(f"""
📊 Oluşturulan İçerik Özeti:
- Twitter: {len(content['twitter'])} tweet
- Facebook: {len(content['facebook'])} post  
- Instagram: {len(content['instagram'])} post
- LinkedIn: {len(content['linkedin'])} post

📅 7 günlük paylaşım programı oluşturuldu
📋 Sosyal medya rehberi hazırlandı

🎯 Sonraki Adımlar:
1. Sosyal medya hesapları oluştur
2. Buffer/Hootsuite ile programla
3. Canva ile görseller tasarla
4. Günlük etkileşime başla
""")

if __name__ == "__main__":
    main()
