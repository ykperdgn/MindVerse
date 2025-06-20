#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced Astrology Content Manager v1.0
Content scheduling, organization, and automated publishing pipeline
"""

import os
import json
import random
from datetime import datetime, timedelta
from typing import Dict, List, Tuple

# Try to import from enhanced or fallback to basic generator
try:
    from enhanced_astrology_generator import EnhancedAstrologyGenerator
except ImportError:
    print("Enhanced generator not found, using basic astrology generator...")
    from astrology_content_generator import AdvancedAstrologyGenerator as EnhancedAstrologyGenerator

class AstrologyContentManager:
    def __init__(self):
        self.generator = EnhancedAstrologyGenerator()
        self.content_dir = "src/content/astrology"
        self.schedule_file = "astrology_content_schedule.json"

        # Load existing schedule
        self.schedule = self.load_schedule()

    def load_schedule(self) -> Dict:
        """Mevcut içerik programını yükle."""
        if os.path.exists(self.schedule_file):
            with open(self.schedule_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            "daily_schedule": {},
            "weekly_schedule": {},
            "monthly_schedule": {},
            "generated_content": [],
            "last_updated": datetime.now().isoformat()
        }

    def save_schedule(self):
        """İçerik programını kaydet."""
        self.schedule["last_updated"] = datetime.now().isoformat()
        with open(self.schedule_file, 'w', encoding='utf-8') as f:
            json.dump(self.schedule, f, indent=2, ensure_ascii=False)

    def get_existing_content(self) -> List[str]:
        """Mevcut içerikleri listele."""
        if not os.path.exists(self.content_dir):
            return []

        files = []
        for filename in os.listdir(self.content_dir):
            if filename.endswith('.md'):
                files.append(filename)
        return sorted(files)

    def analyze_content_gaps(self) -> Dict[str, List[str]]:
        """İçerik boşluklarını analiz et."""
        existing_files = self.get_existing_content()
        all_signs = list(self.generator.zodiac_signs.keys())
        periods = ["gunluk", "haftalik", "aylik"]

        gaps = {
            "missing_daily": [],
            "missing_weekly": [],
            "missing_monthly": [],
            "sign_coverage": {}
        }

        # Her burç için analiz
        for sign in all_signs:
            sign_files = [f for f in existing_files if f.startswith(f"2025-06-19-{sign}-burcu-")]

            daily_exists = any("gunluk" in f for f in sign_files)
            weekly_exists = any("haftalik" in f for f in sign_files)
            monthly_exists = any("aylik" in f for f in sign_files)

            if not daily_exists:
                gaps["missing_daily"].append(sign)
            if not weekly_exists:
                gaps["missing_weekly"].append(sign)
            if not monthly_exists:
                gaps["missing_monthly"].append(sign)

            gaps["sign_coverage"][sign] = {
                "daily": daily_exists,
                "weekly": weekly_exists,
                "monthly": monthly_exists,
                "total_files": len(sign_files)
            }

        return gaps

    def generate_missing_content(self, max_items: int = 10) -> List[str]:
        """Eksik içerikleri oluştur."""
        gaps = self.analyze_content_gaps()
        created_files = []
        count = 0

        print("🔍 İçerik boşlukları analiz ediliyor...")
        print(f"📊 Eksik günlük: {len(gaps['missing_daily'])} burç")
        print(f"📊 Eksik haftalık: {len(gaps['missing_weekly'])} burç")
        print(f"📊 Eksik aylık: {len(gaps['missing_monthly'])} burç")

        # Önce eksik günlük içerikleri oluştur
        for sign in gaps["missing_daily"]:
            if count >= max_items:
                break
            print(f"📝 {self.generator.zodiac_signs[sign]['name']} günlük yorumu oluşturuluyor...")
            content_data = self.generator.generate_daily_content(sign)
            filepath = self.generator.create_content_file(content_data)
            created_files.append(filepath)
            count += 1

        # Sonra eksik haftalık içerikleri oluştur
        for sign in gaps["missing_weekly"]:
            if count >= max_items:
                break
            print(f"📝 {self.generator.zodiac_signs[sign]['name']} haftalık yorumu oluşturuluyor...")
            content_data = self.generator.generate_weekly_content(sign)
            filepath = self.generator.create_content_file(content_data)
            created_files.append(filepath)
            count += 1

        # Son olarak eksik aylık içerikleri oluştur
        for sign in gaps["missing_monthly"]:
            if count >= max_items:
                break
            print(f"📝 {self.generator.zodiac_signs[sign]['name']} aylık yorumu oluşturuluyor...")
            content_data = self.generator.generate_monthly_content(sign)
            filepath = self.generator.create_content_file(content_data)
            created_files.append(filepath)
            count += 1

        # Programı güncelle
        for filepath in created_files:
            self.schedule["generated_content"].append({
                "file": filepath,
                "generated_date": datetime.now().isoformat(),
                "type": "gap_fill"
            })

        self.save_schedule()
        return created_files

    def create_future_schedule(self, days_ahead: int = 30) -> Dict:
        """Gelecek için içerik programı oluştur."""
        future_schedule = {}
        start_date = datetime.now()

        for day in range(days_ahead):
            current_date = start_date + timedelta(days=day)
            date_key = current_date.strftime("%Y-%m-%d")

            # Her gün için rastgele 1-2 burç seç
            daily_signs = random.sample(list(self.generator.zodiac_signs.keys()),
                                      random.randint(1, 2))

            # Haftanın başında haftalık içerik
            weekly_content = []
            if current_date.weekday() == 0:  # Pazartesi
                weekly_signs = random.sample(list(self.generator.zodiac_signs.keys()),
                                           random.randint(1, 3))
                weekly_content = weekly_signs

            # Ayın başında aylık içerik
            monthly_content = []
            if current_date.day == 1:  # Ayın ilk günü
                monthly_signs = random.sample(list(self.generator.zodiac_signs.keys()),
                                            random.randint(2, 4))
                monthly_content = monthly_signs

            future_schedule[date_key] = {
                "daily": daily_signs,
                "weekly": weekly_content,
                "monthly": monthly_content,
                "total_planned": len(daily_signs) + len(weekly_content) + len(monthly_content)
            }

        return future_schedule

    def generate_content_for_date(self, date_str: str) -> List[str]:
        """Belirli bir tarih için içerik oluştur."""
        if date_str not in self.schedule.get("daily_schedule", {}):
            print(f"❌ {date_str} için program bulunamadı")
            return []

        day_plan = self.schedule["daily_schedule"][date_str]
        created_files = []

        # Günlük içerikler
        for sign in day_plan.get("daily", []):
            content_data = self.generator.generate_daily_content(sign)
            filepath = self.generator.create_content_file(content_data)
            created_files.append(filepath)
            print(f"✅ {self.generator.zodiac_signs[sign]['name']} günlük yorumu oluşturuldu")

        # Haftalık içerikler
        for sign in day_plan.get("weekly", []):
            content_data = self.generator.generate_weekly_content(sign)
            filepath = self.generator.create_content_file(content_data)
            created_files.append(filepath)
            print(f"✅ {self.generator.zodiac_signs[sign]['name']} haftalık yorumu oluşturuldu")

        # Aylık içerikler
        for sign in day_plan.get("monthly", []):
            content_data = self.generator.generate_monthly_content(sign)
            filepath = self.generator.create_content_file(content_data)
            created_files.append(filepath)
            print(f"✅ {self.generator.zodiac_signs[sign]['name']} aylık yorumu oluşturuldu")

        return created_files

    def create_specialized_content(self, content_type: str) -> List[str]:
        """Özel içerik türleri oluştur."""
        created_files = []

        if content_type == "love_special":
            # Aşk temalı özel içerikler
            love_signs = ["boga", "yengec", "terazi", "balik"]  # Aşka yatkın burçlar

            for sign in love_signs:
                theme = random.choice([
                    "Aşkta Büyük Dönüşüm", "Kalp Fısıltıları",
                    "Romantik Rüyalar", "Sonsuz Aşk Enerjisi"
                ])

                content_data = self.generator.generate_daily_content(sign)
                # Başlığı özelleştir
                content_data["title"] = f"{theme} - {self.generator.zodiac_signs[sign]['name']} Burcu Özel Yorumu"

                filepath = self.generator.create_content_file(content_data)
                created_files.append(filepath)
                print(f"💖 {self.generator.zodiac_signs[sign]['name']} aşk özel yorumu oluşturuldu")

        elif content_type == "career_boost":
            # Kariyer temalı özel içerikler
            career_signs = ["koc", "aslan", "basak", "oglak"]  # Kariyere odaklı burçlar

            for sign in career_signs:
                theme = random.choice([
                    "Kariyer Zirvesi", "İş Hayatında Başarı",
                    "Liderlik Enerjisi", "Mali Bolluk Dönemi"
                ])

                content_data = self.generator.generate_weekly_content(sign)
                content_data["title"] = f"{theme} - {self.generator.zodiac_signs[sign]['name']} Burcu Kariyer Rehberi"

                filepath = self.generator.create_content_file(content_data)
                created_files.append(filepath)
                print(f"💼 {self.generator.zodiac_signs[sign]['name']} kariyer özel yorumu oluşturuldu")

        return created_files

    def generate_content_report(self) -> Dict:
        """İçerik raporunu oluştur."""
        existing_files = self.get_existing_content()
        gaps = self.analyze_content_gaps()

        report = {
            "total_files": len(existing_files),
            "content_gaps": gaps,
            "coverage_percentage": {},
            "recommendations": []
        }

        # Kapsam yüzdelerini hesapla
        total_signs = len(self.generator.zodiac_signs)
        report["coverage_percentage"] = {
            "daily": ((total_signs - len(gaps["missing_daily"])) / total_signs) * 100,
            "weekly": ((total_signs - len(gaps["missing_weekly"])) / total_signs) * 100,
            "monthly": ((total_signs - len(gaps["missing_monthly"])) / total_signs) * 100
        }

        # Öneriler
        if len(gaps["missing_daily"]) > 0:
            report["recommendations"].append(f"🎯 {len(gaps['missing_daily'])} burç için günlük yorum eksik")

        if len(gaps["missing_weekly"]) > 0:
            report["recommendations"].append(f"🎯 {len(gaps['missing_weekly'])} burç için haftalık yorum eksik")

        if len(gaps["missing_monthly"]) > 0:
            report["recommendations"].append(f"🎯 {len(gaps['missing_monthly'])} burç için aylık yorum eksik")

        if report["coverage_percentage"]["daily"] == 100:
            report["recommendations"].append("✅ Tüm burçlar için günlük yorumlar tamamlandı!")

        return report

    def run_manager_interface(self):
        """Yönetici arayüzünü çalıştır."""
        print("🌟 Gelişmiş Astroloji İçerik Yöneticisi")
        print("=" * 50)

        while True:
            print("\nSeçenekler:")
            print("1. İçerik analizi ve rapor")
            print("2. Eksik içerikleri tamamla")
            print("3. Özel aşk içerikleri oluştur")
            print("4. Özel kariyer içerikleri oluştur")
            print("5. Rastgele 5 içerik oluştur")
            print("6. Gelecek program oluştur")
            print("7. Çıkış")

            choice = input("\nSeçiminiz (1-7): ").strip()

            if choice == "1":
                print("\n📊 İçerik Analizi Yapılıyor...")
                report = self.generate_content_report()

                print(f"\n📈 RAPOR:")
                print(f"Toplam Dosya: {report['total_files']}")
                print(f"Günlük Kapsam: {report['coverage_percentage']['daily']:.1f}%")
                print(f"Haftalık Kapsam: {report['coverage_percentage']['weekly']:.1f}%")
                print(f"Aylık Kapsam: {report['coverage_percentage']['monthly']:.1f}%")

                print(f"\n💡 ÖNERİLER:")
                for rec in report['recommendations']:
                    print(f"  {rec}")

            elif choice == "2":
                print("\n🔧 Eksik İçerikler Tamamlanıyor...")
                files = self.generate_missing_content(10)
                print(f"✅ {len(files)} eksik içerik oluşturuldu!")

            elif choice == "3":
                print("\n💖 Özel Aşk İçerikleri Oluşturuluyor...")
                files = self.create_specialized_content("love_special")
                print(f"✅ {len(files)} aşk temalı içerik oluşturuldu!")

            elif choice == "4":
                print("\n💼 Özel Kariyer İçerikleri Oluşturuluyor...")
                files = self.create_specialized_content("career_boost")
                print(f"✅ {len(files)} kariyer temalı içerik oluşturuldu!")

            elif choice == "5":
                print("\n🎲 Rastgele İçerikler Oluşturuluyor...")
                from batch_astrology_generator import generate_bulk_astrology_content
                generate_bulk_astrology_content()

            elif choice == "6":
                print("\n📅 30 Günlük Program Oluşturuluyor...")
                future_schedule = self.create_future_schedule(30)
                self.schedule["daily_schedule"] = future_schedule
                self.save_schedule()
                print("✅ 30 günlük içerik programı oluşturuldu!")

            elif choice == "7":
                print("👋 Görüşürüz!")
                break

            else:
                print("❌ Geçersiz seçim. Lütfen 1-7 arası bir sayı girin.")

if __name__ == "__main__":
    manager = AstrologyContentManager()
    manager.run_manager_interface()
