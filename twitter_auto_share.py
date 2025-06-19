#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Twitter Otomatik Paylaşım Sistemi
@MindVerseDaily hesabı için otomatik tweet atma
"""

import tweepy
import os
import json
import time
import hashlib
from datetime import datetime
import schedule
from pathlib import Path

class TwitterAutoShare:
    def __init__(self):
        self.username = "MindVerseDaily"
        self.hashtags = ["#mindversedaily", "#blog", "#bilgi", "#gelişim", "#eğitim"]
        self.base_url = "https://www.mindversedaily.com"
        
        # Twitter API credentials (environment variables'dan alınacak)
        self.api_key = os.getenv('TWITTER_API_KEY')
        self.api_secret = os.getenv('TWITTER_API_SECRET')
        self.access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        self.access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        self.bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
        
        # Paylaşılan makaleleri takip etmek için
        self.shared_articles_file = "shared_articles.json"
        
    def setup_twitter_api(self):
        """Twitter API bağlantısını kurar"""
        try:
            # Twitter API v2 client
            self.client = tweepy.Client(
                bearer_token=self.bearer_token,
                consumer_key=self.api_key,
                consumer_secret=self.api_secret,
                access_token=self.access_token,
                access_token_secret=self.access_token_secret,
                wait_on_rate_limit=True
            )
            
            # API v1.1 for media upload (if needed)
            auth = tweepy.OAuth1UserHandler(
                self.api_key,
                self.api_secret,
                self.access_token,
                self.access_token_secret
            )
            self.api_v1 = tweepy.API(auth)
            
            print("✅ Twitter API bağlantısı başarılı!")
            return True
            
        except Exception as e:
            print(f"❌ Twitter API bağlantı hatası: {e}")
            return False
    
    def load_shared_articles(self):
        """Daha önce paylaşılan makaleleri yükler"""
        try:
            if os.path.exists(self.shared_articles_file):
                with open(self.shared_articles_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Shared articles dosyası okunamadı: {e}")
        return []
    
    def save_shared_articles(self, shared_list):
        """Paylaşılan makaleleri kaydet"""
        try:
            with open(self.shared_articles_file, 'w', encoding='utf-8') as f:
                json.dump(shared_list, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Shared articles dosyası kaydedilemedi: {e}")
    
    def get_latest_articles(self, limit=5):
        """En son eklenen makaleleri getirir"""
        articles = []
        content_dir = Path("src/content")
        
        for category_dir in content_dir.iterdir():
            if category_dir.is_dir() and category_dir.name != "__pycache__":
                for article_file in category_dir.glob("*.md"):
                    # Sadece bugün eklenen makaleler
                    today = datetime.now().strftime('%Y-%m-%d')
                    if today in article_file.name:
                        articles.append({
                            'file': str(article_file),
                            'category': category_dir.name,
                            'filename': article_file.name,
                            'created': article_file.stat().st_mtime
                        })
        
        # En yeni makaleler önce
        articles.sort(key=lambda x: x['created'], reverse=True)
        return articles[:limit]
    
    def extract_article_info(self, article_path):
        """Makale dosyasından bilgileri çıkarır"""
        try:
            with open(article_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Front matter'dan title ve summary çıkar
            lines = content.split('\n')
            title = ""
            summary = ""
            
            in_frontmatter = False
            for line in lines:
                if line.strip() == '---':
                    in_frontmatter = not in_frontmatter
                    continue
                    
                if in_frontmatter:
                    if line.startswith('title:'):
                        title = line.replace('title:', '').strip().strip('"\'')
                    elif line.startswith('summary:'):
                        summary = line.replace('summary:', '').strip().strip('"\'')
            
            return title, summary
            
        except Exception as e:
            print(f"Makale bilgileri çıkarılamadı: {e}")
            return None, None
    
    def create_tweet_text(self, title, category, article_url):
        """Tweet metni oluşturur"""
        # Kategori emojileri
        category_emojis = {
            'health': '🏥',
            'psychology': '🧠',
            'love': '❤️',
            'history': '📚',
            'space': '🚀',
            'quotes': '💭'
        }
        
        emoji = category_emojis.get(category, '📖')
        
        # Tweet formatları
        formats = [
            f"{emoji} {title}\n\n{article_url}",
            f"📖 Yeni makale: {title}\n\n{article_url}",
            f"{emoji} {title}\n\nDetaylı rehber ve uzman önerileri 👇\n{article_url}",
            f"📚 {category.title()} kategorisinde yeni içerik:\n\n{title}\n\n{article_url}"
        ]
        
        # Rastgele format seç
        import random
        tweet_text = random.choice(formats)
        
        # Hashtag ekle (280 karakter limitini aşmayacak şekilde)
        hashtags_text = " ".join(self.hashtags[:3])  # İlk 3 hashtag
        
        if len(tweet_text + " " + hashtags_text) <= 280:
            tweet_text += " " + hashtags_text
        
        return tweet_text
    
    def create_article_url(self, category, filename):
        """Makale URL'ini oluşturur"""
        # Filename'den slug çıkar
        slug = filename.replace('.md', '')
        return f"{self.base_url}/{category}/{slug}"
    
    def share_article(self, article_info):
        """Makaleyi Twitter'da paylaşır"""
        try:
            title, summary = self.extract_article_info(article_info['file'])
            if not title:
                print(f"❌ Makale başlığı alınamadı: {article_info['file']}")
                return False
            
            # URL oluştur
            article_url = self.create_article_url(
                article_info['category'], 
                article_info['filename']
            )
            
            # Tweet metni oluştur
            tweet_text = self.create_tweet_text(title, article_info['category'], article_url)
            
            print(f"🐦 Tweet hazırlanıyor:")
            print(f"   📝 İçerik: {tweet_text[:100]}...")
            print(f"   🔗 URL: {article_url}")
            
            # Tweet gönder
            if self.api_key and self.client:
                response = self.client.create_tweet(text=tweet_text)
                print(f"✅ Tweet başarıyla gönderildi! ID: {response.data['id']}")
                return True
            else:
                print("⚠️ Twitter API credentials bulunamadı. Simülasyon modu.")
                print(f"📤 Gönderilecek tweet: {tweet_text}")
                return True
                
        except Exception as e:
            print(f"❌ Tweet gönderim hatası: {e}")
            return False
    
    def auto_share_new_articles(self):
        """Yeni makaleleri otomatik paylaş"""
        print(f"\n🤖 Otomatik Twitter paylaşımı başlıyor... {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        
        # Daha önce paylaşılanları yükle
        shared_articles = self.load_shared_articles()
        
        # Yeni makaleleri al
        new_articles = self.get_latest_articles(limit=3)
        
        if not new_articles:
            print("📰 Paylaşılacak yeni makale bulunamadı.")
            return
        
        shared_count = 0
        for article in new_articles:
            article_id = hashlib.md5(article['filename'].encode()).hexdigest()
            
            # Daha önce paylaşılmış mı kontrol et
            if article_id not in shared_articles:
                success = self.share_article(article)
                if success:
                    shared_articles.append(article_id)
                    shared_count += 1
                    
                    # Rate limit için bekleme
                    if shared_count < len(new_articles):
                        print("⏳ Rate limit için 30 saniye bekleniyor...")
                        time.sleep(30)
                else:
                    print(f"❌ Paylaşım başarısız: {article['filename']}")
            else:
                print(f"ℹ️ Daha önce paylaşılmış: {article['filename']}")
        
        # Güncellenen listeyi kaydet
        self.save_shared_articles(shared_articles)
        
        print(f"✅ {shared_count} makale Twitter'da paylaşıldı!")
    
    def schedule_auto_sharing(self):
        """Otomatik paylaşımı zamanla"""
        # Günde 3 kez paylaşım
        schedule.every().day.at("09:00").do(self.auto_share_new_articles)  # Sabah
        schedule.every().day.at("15:00").do(self.auto_share_new_articles)  # Öğleden sonra
        schedule.every().day.at("21:00").do(self.auto_share_new_articles)  # Akşam
        
        print("📅 Twitter otomatik paylaşımı programlandı:")
        print("   - Sabah: 09:00")
        print("   - Öğleden sonra: 15:00") 
        print("   - Akşam: 21:00")
        print("   - Zamanlamayı durdurmak için Ctrl+C")
        
        while True:
            schedule.run_pending()
            time.sleep(60)

def main():
    twitter_bot = TwitterAutoShare()
    
    print("""
🐦 MindVerse Twitter Otomatik Paylaşım
@MindVerseDaily hesabı için otomatik tweet sistemi

Önemli: Twitter API credentials gerekli!
1. https://developer.twitter.com'da uygulama oluşturun
2. Environment variables ayarlayın:
   - TWITTER_API_KEY
   - TWITTER_API_SECRET  
   - TWITTER_ACCESS_TOKEN
   - TWITTER_ACCESS_TOKEN_SECRET
   - TWITTER_BEARER_TOKEN

Seçenekler:
1. Tek paylaşım (test)
2. Otomatik zamanlayıcı başlat
3. API setup rehberi göster
""")
    
    choice = input("Seçiminiz (1-3): ").strip()
    
    if choice == '1':
        success = twitter_bot.setup_twitter_api()
        if success or not twitter_bot.api_key:  # Simülasyon da kabul
            twitter_bot.auto_share_new_articles()
    elif choice == '2':
        success = twitter_bot.setup_twitter_api()
        if success or not twitter_bot.api_key:  # Simülasyon da kabul
            twitter_bot.schedule_auto_sharing()
    elif choice == '3':
        print("""
🔧 Twitter API Setup Rehberi:

1. https://developer.twitter.com/en/portal/dashboard adresine gidin
2. "Create App" ile yeni uygulama oluşturun
3. App permissions: "Read and Write" seçin
4. Keys and tokens sekmesinden değerleri alın:
   - API Key (Consumer Key)
   - API Secret Key (Consumer Secret)
   - Access Token
   - Access Token Secret
   - Bearer Token

5. Environment variables olarak ayarlayın:
   PowerShell:
   $env:TWITTER_API_KEY="your_api_key"
   $env:TWITTER_API_SECRET="your_api_secret"
   $env:TWITTER_ACCESS_TOKEN="your_access_token"
   $env:TWITTER_ACCESS_TOKEN_SECRET="your_access_token_secret"
   $env:TWITTER_BEARER_TOKEN="your_bearer_token"

6. tweepy kütüphanesini yükleyin:
   pip install tweepy
""")
    else:
        print("❌ Geçersiz seçim!")

if __name__ == "__main__":
    main()
