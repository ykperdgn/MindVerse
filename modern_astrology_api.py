#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔮 Modern Astroloji API Sistemi - MindVerse Daily
Gerçek API verilerini kullanarak güncel horoscope içeriği üretir
"""

import requests
import json
import random
from datetime import datetime, timedelta
from typing import Dict, List
import time
import os

class ModernAstrologyAPI:
    def __init__(self):
        self.api_base = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope"
        self.zodiac_signs = {
            "aries": {"turkish": "Koç", "symbol": "♈", "element": "Ateş", "dates": "21 Mart - 19 Nisan"},
            "taurus": {"turkish": "Boğa", "symbol": "♉", "element": "Toprak", "dates": "20 Nisan - 20 Mayıs"},
            "gemini": {"turkish": "İkizler", "symbol": "♊", "element": "Hava", "dates": "21 Mayıs - 20 Haziran"},
            "cancer": {"turkish": "Yengeç", "symbol": "♋", "element": "Su", "dates": "21 Haziran - 22 Temmuz"},
            "leo": {"turkish": "Aslan", "symbol": "♌", "element": "Ateş", "dates": "23 Temmuz - 22 Ağustos"},
            "virgo": {"turkish": "Başak", "symbol": "♍", "element": "Toprak", "dates": "23 Ağustos - 22 Eylül"},
            "libra": {"turkish": "Terazi", "symbol": "♎", "element": "Hava", "dates": "23 Eylül - 22 Ekim"},
            "scorpio": {"turkish": "Akrep", "symbol": "♏", "element": "Su", "dates": "23 Ekim - 21 Kasım"},
            "sagittarius": {"turkish": "Yay", "symbol": "♐", "element": "Ateş", "dates": "22 Kasım - 21 Aralık"},
            "capricorn": {"turkish": "Oğlak", "symbol": "♑", "element": "Toprak", "dates": "22 Aralık - 19 Ocak"},
            "aquarius": {"turkish": "Kova", "symbol": "♒", "element": "Hava", "dates": "20 Ocak - 18 Şubat"},
            "pisces": {"turkish": "Balık", "symbol": "♓", "element": "Su", "dates": "19 Şubat - 20 Mart"}
        }

        self.content_dir = "src/content/astrology"
        os.makedirs(self.content_dir, exist_ok=True)

    def get_horoscope_data(self, sign: str, day: str = "today") -> Dict:
        """API'den horoscope verisi çek"""
        try:
            params = {
                "sign": sign,
                "day": day
            }

            response = requests.get(self.api_base, params=params, timeout=10)

            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    return data.get("data", {})

            return None

        except Exception as e:
            print(f"❌ API Error for {sign}: {e}")
            return None

    def translate_to_turkish(self, english_text: str) -> str:
        """İngilizce horoscope'u Türkçe'ye çevir (basit çeviri)"""
        # Basit kelime çevirisi
        translations = {
            "today": "bugün",
            "tomorrow": "yarın",
            "yesterday": "dün",
            "focus": "odaklan",
            "creative": "yaratıcı",
            "mind": "zihin",
            "energy": "enerji",
            "love": "aşk",
            "money": "para",
            "career": "kariyer",
            "health": "sağlık",
            "lucky": "şanslı",
            "positive": "pozitif",
            "success": "başarı",
            "opportunity": "fırsat",
            "relationships": "ilişkiler",
            "work": "iş",
            "family": "aile",
            "friends": "arkadaşlar",
            "time": "zaman",
            "good": "iyi",
            "great": "harika",
            "excellent": "mükemmel",
            "powerful": "güçlü",
            "strong": "güçlü",
            "important": "önemli"
        }

        turkish_text = english_text
        for eng, tr in translations.items():
            turkish_text = turkish_text.replace(eng, tr)

        return turkish_text

    def enhance_horoscope_content(self, sign_data: Dict, horoscope_text: str, period: str = "daily") -> str:
        """Horoscope içeriğini Türkçe içerikle zenginleştir"""

        # Türkçe içerik ekleri
        turkish_insights = [
            f"{sign_data['turkish']} burcu olarak bugün enerjiniz yüksek olacak.",
            f"{sign_data['element']} elementi size güç katacak.",
            f"Şanslı renginiz bugün için size fayda sağlayabilir.",
            f"Sosyal ilişkilerinizde dikkatli olun.",
            f"Maddi konularda temkinli davranın.",
            f"Sezgilerinize güvenin.",
            f"Yeni fırsatları değerlendirin.",
            f"Ailevi konularda pozitif gelişmeler olabilir."
        ]

        # Rastgele Türkçe içerik seç
        selected_insights = random.sample(turkish_insights, 3)

        enhanced_content = f"""
## 🌟 Genel Durum

{horoscope_text}

## 💫 Burç Yorumu

{selected_insights[0]} {selected_insights[1]}

## 🎯 Günün Tavsiyeleri

• {selected_insights[2]}
• Pozitif düşünce gücünüzü kullanın
• Çevrenizdekilere karşı anlayışlı olun
• Yeni projelere başlamak için uygun zaman

## ⭐ Şanslı Detaylar

**Element:** {sign_data['element']}
**Sembol:** {sign_data['symbol']}
**Tarih Aralığı:** {sign_data['dates']}
"""

        return enhanced_content

    def create_astrology_content(self, sign: str, period: str = "today") -> bool:
        """Tek burç için içerik oluştur"""

        if sign not in self.zodiac_signs:
            print(f"❌ Geçersiz burç: {sign}")
            return False

        # API'den veri çek
        horoscope_data = self.get_horoscope_data(sign, period)

        if not horoscope_data:
            print(f"❌ {sign} için API verisi alınamadı")
            return False

        sign_data = self.zodiac_signs[sign]
        date_str = datetime.now().strftime("%Y-%m-%d")

        # İçerik oluştur
        horoscope_text = horoscope_data.get("horoscope_data", "")
        enhanced_content = self.enhance_horoscope_content(sign_data, horoscope_text, period)

        # Türkçe başlık
        title = f"{sign_data['turkish']} Burcu Günlük Yorumu - {datetime.now().strftime('%d %B %Y')}"

        # Frontmatter ve içerik
        content = f"""---
title: "{title}"
description: "{sign_data['turkish']} burcu için güncel astroloji yorumu. API destekli gerçek horoscope verisi."
pubDate: {date_str}
category: "astrology"
tags: ["{sign_data['turkish'].lower()}", "günlük", "burç", "astroloji", "horoscope"]
heroImage: "/images/zodiac/{sign}.jpg"
apiSource: "HoroscopeAPI"
zodiacSign: "{sign}"
element: "{sign_data['element']}"
symbol: "{sign_data['symbol']}"
---

# {title}

{sign_data['symbol']} **{sign_data['turkish']} Burcu** ({sign_data['dates']})

{enhanced_content}

## 🔮 API Destekli İçerik

Bu içerik gerçek zamanlı astroloji verisi kullanılarak oluşturulmuştur.

**Tarih:** {horoscope_data.get('date', date_str)}
**Kaynak:** Profesyonel Astroloji API

---

*Bu yorum {datetime.now().strftime('%d %B %Y')} tarihi için hazırlanmıştır.*
"""

        # Dosya adı
        filename = f"{date_str}-{sign}-burcu-gunluk-yorum.md"
        filepath = os.path.join(self.content_dir, filename)

        # Dosyayı kaydet
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"✅ {sign_data['turkish']} burcu içeriği oluşturuldu: {filename}")
            return True

        except Exception as e:
            print(f"❌ Dosya yazma hatası: {e}")
            return False

    def create_all_signs_content(self, period: str = "today") -> List[str]:
        """Tüm burçlar için içerik oluştur"""

        print(f"🚀 Tüm burçlar için {period} içeriği oluşturuluyor...")
        created_files = []

        for sign in self.zodiac_signs.keys():
            if self.create_astrology_content(sign, period):
                created_files.append(sign)

            # API rate limit için bekleme
            time.sleep(1)

        print(f"✅ {len(created_files)} burç içeriği oluşturuldu!")
        return created_files

    def create_weekly_content(self) -> List[str]:
        """Haftalık içerik oluştur"""
        print("📅 Haftalık astroloji içeriği oluşturuluyor...")

        created_files = []
        for sign in list(self.zodiac_signs.keys())[:6]:  # Sadece 6 burç için haftalık
            horoscope_data = self.get_horoscope_data(sign, "tomorrow")

            if horoscope_data:
                sign_data = self.zodiac_signs[sign]
                date_str = datetime.now().strftime("%Y-%m-%d")

                content = f"""---
title: "{sign_data['turkish']} Burcu Haftalık Yorumu"
description: "{sign_data['turkish']} burcu için haftalık astroloji rehberi."
pubDate: {date_str}
category: "astrology"
tags: ["{sign_data['turkish'].lower()}", "haftalık", "burç", "astroloji"]
heroImage: "/images/zodiac/{sign}.jpg"
period: "weekly"
---

# {sign_data['turkish']} Burcu Haftalık Yorumu

{sign_data['symbol']} **{sign_data['turkish']} Burcu** ({sign_data['dates']})

## 📅 Bu Hafta Genel Durum

{horoscope_data.get('horoscope_data', '')}

## 🎯 Haftalık Hedefler

• Yeni projelere odaklanın
• İlişkilerinizi güçlendirin
• Sağlığınıza dikkat edin
• Finansal planlarınızı gözden geçirin

Bu hafta {sign_data['element']} elementi size rehberlik edecek.
"""

                filename = f"{date_str}-{sign}-haftalik-yorum.md"
                filepath = os.path.join(self.content_dir, filename)

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

                created_files.append(filename)
                print(f"✅ {sign_data['turkish']} haftalık içerik oluşturuldu")

            time.sleep(1)

        return created_files

    def test_api_connection(self):
        """API bağlantısını test et"""
        print("🔍 API bağlantısı test ediliyor...")

        test_data = self.get_horoscope_data("aries", "today")

        if test_data:
            print("✅ API bağlantısı başarılı!")
            print(f"📄 Test verisi: {test_data.get('horoscope_data', '')[:100]}...")
            return True
        else:
            print("❌ API bağlantısı başarısız!")
            return False

    def run_interactive_mode(self):
        """İnteraktif mod"""
        print("🔮 Modern Astroloji API Sistemi")
        print("=" * 50)

        # Önce API'yi test et
        if not self.test_api_connection():
            print("❌ API çalışmıyor, offline mod kullanılacak")

        while True:
            print("\nSeçenekler:")
            print("1. Tüm burçlar günlük içerik (API)")
            print("2. Tek burç günlük içerik")
            print("3. Haftalık içerik oluştur")
            print("4. API bağlantısını test et")
            print("5. Çıkış")

            choice = input("\nSeçiminiz (1-5): ").strip()

            if choice == "1":
                self.create_all_signs_content("today")

            elif choice == "2":
                print("\nMevcut burçlar:")
                for i, (sign, data) in enumerate(self.zodiac_signs.items(), 1):
                    print(f"{i}. {data['turkish']} ({sign})")

                try:
                    sign_choice = int(input("Burç seçin (1-12): ")) - 1
                    signs = list(self.zodiac_signs.keys())
                    if 0 <= sign_choice < len(signs):
                        self.create_astrology_content(signs[sign_choice])
                    else:
                        print("❌ Geçersiz seçim")
                except ValueError:
                    print("❌ Geçerli bir sayı girin")

            elif choice == "3":
                self.create_weekly_content()

            elif choice == "4":
                self.test_api_connection()

            elif choice == "5":
                print("👋 Görüşürüz!")
                break

            else:
                print("❌ Geçersiz seçim")

def main():
    """Ana fonksiyon"""
    astrology = ModernAstrologyAPI()
    astrology.run_interactive_mode()

if __name__ == "__main__":
    main()
