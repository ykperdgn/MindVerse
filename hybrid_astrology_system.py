#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 Hibrit Astroloji Sistemi - API + Offline
Prokerola API ile gerçek veriler + premium offline içerik
"""

import requests
import json
import random
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import os
from premium_astrology_system import PremiumAstrologySystem

class HybridAstrologySystem:
    def __init__(self):
        self.api_key = "your_prokerala_api_key"  # API key'i buraya ekleyecek
        self.base_url = "https://api.prokerala.com/v2"
        self.premium_system = PremiumAstrologySystem()

        # API kullanım takibi
        self.daily_api_calls = 0
        self.max_daily_calls = 166  # Günde 166 kişi limit (5000/30)
        self.last_call_time = 0
        self.rate_limit_delay = 12  # Dakikada 5 istek = 12 saniye arayla

        # Burç isimleri çevirisi
        self.sign_mapping = {
            "koc": "aries", "boga": "taurus", "ikizler": "gemini",
            "yengec": "cancer", "aslan": "leo", "basak": "virgo",
            "terazi": "libra", "akrep": "scorpio", "yay": "sagittarius",
            "oglak": "capricorn", "kova": "aquarius", "balik": "pisces"
        }

    def _rate_limit_check(self):
        """Rate limiting kontrolü"""
        current_time = time.time()
        if current_time - self.last_call_time < self.rate_limit_delay:
            sleep_time = self.rate_limit_delay - (current_time - self.last_call_time)
            time.sleep(sleep_time)
        self.last_call_time = time.time()

    def get_api_horoscope(self, sign: str, period: str = "today") -> Optional[Dict]:
        """Prokerala API'den horoscope verisi çek"""
        if self.daily_api_calls >= self.max_daily_calls:
            print(f"⚠️ Günlük API limiti aşıldı ({self.max_daily_calls})")
            return None

        try:
            self._rate_limit_check()

            english_sign = self.sign_mapping.get(sign, sign)
            url = f"{self.base_url}/horoscope/{english_sign}/{period}"

            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code == 200:
                self.daily_api_calls += 1
                print(f"✅ API çağrısı başarılı - Kalan: {self.max_daily_calls - self.daily_api_calls}")
                return response.json()
            else:
                print(f"❌ API Hatası: {response.status_code}")
                return None

        except Exception as e:
            print(f"❌ API Bağlantı Hatası: {e}")
            return None

    def create_hybrid_content(self, sign: str, use_api: bool = True) -> Dict[str, str]:
        """Hibrit içerik oluştur - API + Premium sistem"""

        # Premium sistem ile temel içerik oluştur
        premium_content = self.premium_system.generate_daily_content(sign)

        if use_api and self.daily_api_calls < self.max_daily_calls:
            # API'den gerçek horoscope verisi al
            api_data = self.get_api_horoscope(sign)

            if api_data and "data" in api_data:
                # API verisini premium içerikle birleştir
                enhanced_content = self._merge_api_premium(premium_content, api_data)
                return enhanced_content

        # API yok veya limit aşıldıysa premium içerik kullan
        return premium_content

    def _merge_api_premium(self, premium_content: Dict, api_data: Dict) -> Dict[str, str]:
        """API verisini premium içerikle birleştir"""

        api_horoscope = api_data.get("data", {}).get("horoscope_data", "")

        if api_horoscope:
            # Premium içeriğin başına API verisini ekle
            lines = premium_content["content"].split("\n")

            # "## 🌟 Günün Genel Enerjisi" bölümünü bul ve API verisini ekle
            for i, line in enumerate(lines):
                if "## 🌟 Günün Genel Enerjisi" in line:
                    # API verisini ekle
                    lines.insert(i + 2, f"**🔮 Astroloji Uzmanından:** {api_horoscope}")
                    lines.insert(i + 3, "")
                    break

            premium_content["content"] = "\n".join(lines)
            premium_content["title"] += " (Pro)"

        return premium_content

    def generate_daily_batch(self, use_api_ratio: float = 0.3) -> List[str]:
        """Günlük toplu içerik üret - API kullanımını optimize et"""
        created_files = []
        signs = list(self.premium_system.zodiac_data.keys())

        # Sadece %30'u için API kullan (kredi tasarrufu)
        api_count = int(len(signs) * use_api_ratio)
        api_signs = random.sample(signs, api_count)

        print(f"🚀 {len(signs)} burç için hibrit içerik oluşturuluyor...")
        print(f"📡 API kullanılacak burçlar: {api_count}")
        print(f"🔧 Offline sistem kullanılacak burçlar: {len(signs) - api_count}")

        for sign in signs:
            use_api = sign in api_signs
            content_data = self.create_hybrid_content(sign, use_api)

            filepath = self.premium_system.create_content_file(content_data)
            created_files.append(filepath)

            status = "🌐 API" if use_api else "💾 Offline"
            print(f"✅ {self.premium_system.zodiac_data[sign]['name']} - {status}")

            # Rate limiting için kısa bekleme
            if use_api:
                time.sleep(1)

        print(f"✅ {len(created_files)} hibrit içerik oluşturuldu!")
        return created_files

    def generate_birth_chart_content(self, name: str, birth_date: str, birth_time: str, birth_place: str) -> Optional[Dict]:
        """Doğum haritası içeriği oluştur (Premium özellik)"""

        if self.daily_api_calls >= self.max_daily_calls:
            return {"error": "Günlük API limiti aşıldı"}

        try:
            self._rate_limit_check()

            url = f"{self.base_url}/birth-chart"
            data = {
                "datetime": birth_date + "T" + birth_time,
                "coordinates": birth_place  # Koordinat formatında
            }

            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            response = requests.post(url, json=data, headers=headers, timeout=15)

            if response.status_code == 200:
                self.daily_api_calls += 4  # Doğum haritası 4 kredi tüketir
                return response.json()
            else:
                return {"error": f"API Hatası: {response.status_code}"}

        except Exception as e:
            return {"error": f"Bağlantı Hatası: {e}"}

    def get_compatibility_analysis(self, sign1: str, sign2: str) -> Optional[Dict]:
        """Burç uyumluluk analizi (Premium özellik)"""

        if self.daily_api_calls >= self.max_daily_calls:
            return {"error": "Günlük API limiti aşıldı"}

        try:
            self._rate_limit_check()

            english_sign1 = self.sign_mapping.get(sign1, sign1)
            english_sign2 = self.sign_mapping.get(sign2, sign2)

            url = f"{self.base_url}/compatibility/{english_sign1}/{english_sign2}"

            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code == 200:
                self.daily_api_calls += 5  # Compatibility 5 kredi tüketir
                return response.json()
            else:
                return {"error": f"API Hatası: {response.status_code}"}

        except Exception as e:
            return {"error": f"Bağlantı Hatası: {e}"}

    def save_api_usage_stats(self):
        """API kullanım istatistiklerini kaydet"""
        stats = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "daily_calls": self.daily_api_calls,
            "remaining_calls": self.max_daily_calls - self.daily_api_calls,
            "usage_percentage": (self.daily_api_calls / self.max_daily_calls) * 100
        }

        with open("api_usage_stats.json", "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=2, ensure_ascii=False)

        print(f"📊 API kullanım istatistikleri kaydedildi: {stats}")

    def run_interactive_mode(self):
        """İnteraktif hibrit sistem"""
        print("🚀 Hibrit Astroloji Sistemi - API + Premium")
        print("=" * 60)
        print(f"📡 Günlük API kullanımı: {self.daily_api_calls}/{self.max_daily_calls}")

        while True:
            print("\nSeçenekler:")
            print("1. Hibrit günlük içerik oluştur (API + Offline)")
            print("2. Sadece premium offline içerik")
            print("3. API durumu kontrol et")
            print("4. Doğum haritası oluştur (Premium)")
            print("5. Burç uyumluluk analizi (Premium)")
            print("6. API kullanım istatistikleri")
            print("7. Çıkış")

            choice = input("\nSeçiminiz (1-7): ").strip()

            if choice == "1":
                ratio = float(input("API kullanım oranı (0.1-1.0, önerilen: 0.3): ") or "0.3")
                self.generate_daily_batch(ratio)

            elif choice == "2":
                self.premium_system.generate_all_daily_content()

            elif choice == "3":
                print(f"📡 API Durumu:")
                print(f"   Bugün yapılan çağrı: {self.daily_api_calls}")
                print(f"   Kalan limit: {self.max_daily_calls - self.daily_api_calls}")
                print(f"   Kullanım oranı: {(self.daily_api_calls/self.max_daily_calls)*100:.1f}%")

            elif choice == "4":
                print("🌟 Doğum Haritası Oluştur")
                name = input("İsim: ")
                birth_date = input("Doğum tarihi (YYYY-MM-DD): ")
                birth_time = input("Doğum saati (HH:MM): ")
                birth_place = input("Doğum yeri koordinatları: ")

                result = self.generate_birth_chart_content(name, birth_date, birth_time, birth_place)
                if result:
                    print(f"✅ Doğum haritası oluşturuldu: {json.dumps(result, indent=2)}")

            elif choice == "5":
                print("💕 Burç Uyumluluk Analizi")
                print("Mevcut burçlar:", ", ".join(self.sign_mapping.keys()))
                sign1 = input("İlk burç: ").lower()
                sign2 = input("İkinci burç: ").lower()

                result = self.get_compatibility_analysis(sign1, sign2)
                if result:
                    print(f"✅ Uyumluluk analizi: {json.dumps(result, indent=2)}")

            elif choice == "6":
                self.save_api_usage_stats()

            elif choice == "7":
                self.save_api_usage_stats()
                print("👋 Hibrit sistem kapatılıyor...")
                break

            else:
                print("❌ Geçersiz seçim")

def main():
    """Ana fonksiyon"""
    system = HybridAstrologySystem()

    print("🌟 Hibrit Astroloji Sistemi Başlatılıyor...")
    print("📡 API + 💎 Premium Offline Sistem")
    print("⚡ Akıllı kredi yönetimi ile optimize edilmiş")

    system.run_interactive_mode()

if __name__ == "__main__":
    main()
