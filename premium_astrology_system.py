#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌟 Premium Astroloji İçerik Sistemi - MindVerse Daily
Offline çalışan, gelişmiş şablon sistemi ile profesyonel içerik üretir
"""

import random
import json
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import os

class PremiumAstrologySystem:
    def __init__(self):
        self.content_dir = "src/content/astrology"
        os.makedirs(self.content_dir, exist_ok=True)

        # Kapsamlı burç bilgileri
        self.zodiac_data = {
            "koc": {
                "name": "Koç", "english": "Aries", "symbol": "♈", "element": "Ateş",
                "dates": "21 Mart - 19 Nisan", "ruling_planet": "Mars",
                "colors": ["Kırmızı", "Turuncu"], "lucky_numbers": [1, 8, 17],
                "personality": ["Girişken", "Cesur", "Lider", "Enerjik", "Kararlı"],
                "strengths": ["Liderlik", "Cesaret", "Girişkenlik", "Bağımsızlık"],
                "challenges": ["Sabırsızlık", "Düşüncesizlik", "Öfke kontrol"],
                "compatible": ["Aslan", "Yay", "İkizler", "Kova"],
                "career": ["Yöneticilik", "Girişimcilik", "Spor", "Satış"]
            },
            "boga": {
                "name": "Boğa", "english": "Taurus", "symbol": "♉", "element": "Toprak",
                "dates": "20 Nisan - 20 Mayıs", "ruling_planet": "Venüs",
                "colors": ["Yeşil", "Pembe"], "lucky_numbers": [2, 6, 9, 24],
                "personality": ["Güvenilir", "Sabırlı", "Pratik", "Sadık"],
                "strengths": ["Güvenilirlik", "Sabır", "Kararlılık", "Sadakat"],
                "challenges": ["İnatçılık", "Değişime direnç", "Kıskançlık"],
                "compatible": ["Başak", "Oğlak", "Yengeç", "Balık"],
                "career": ["Bankacılık", "Emlak", "Sanat", "Tarım"]
            },
            "ikizler": {
                "name": "İkizler", "english": "Gemini", "symbol": "♊", "element": "Hava",
                "dates": "21 Mayıs - 20 Haziran", "ruling_planet": "Merkür",
                "colors": ["Sarı", "Açık Mavi"], "lucky_numbers": [5, 7, 14, 23],
                "personality": ["İletişimci", "Zeki", "Meraklı", "Sosyal"],
                "strengths": ["İletişim", "Zeka", "Adaptasyon", "Çok yönlülük"],
                "challenges": ["Kararsızlık", "Yüzeysellik", "Sabırsızlık"],
                "compatible": ["Terazi", "Kova", "Koç", "Aslan"],
                "career": ["Gazetecilik", "Öğretmenlik", "Teknoloji"]
            },
            "yengec": {
                "name": "Yengeç", "english": "Cancer", "symbol": "♋", "element": "Su",
                "dates": "21 Haziran - 22 Temmuz", "ruling_planet": "Ay",
                "colors": ["Gümüş", "Beyaz", "Deniz Mavisi"], "lucky_numbers": [2, 7, 11, 16],
                "personality": ["Duygusal", "Koruyucu", "Sezgisel", "Aileci"],
                "strengths": ["Empati", "Sadakat", "Sezgi", "Duygusal zeka"],
                "challenges": ["Aşırı duyarlılık", "Geçmişe takılma", "Değişken ruh hali"],
                "compatible": ["Akrep", "Balık", "Boğa", "Başak"],
                "career": ["Hemşirelik", "Psikoloji", "Eğitim", "Beslenme"]
            },
            "aslan": {
                "name": "Aslan", "english": "Leo", "symbol": "♌", "element": "Ateş",
                "dates": "23 Temmuz - 22 Ağustos", "ruling_planet": "Güneş",
                "colors": ["Altın", "Turuncu", "Kırmızı"], "lucky_numbers": [1, 3, 10, 19],
                "personality": ["Karizmatik", "Yaratıcı", "Cömert", "Gururlu"],
                "strengths": ["Karizma", "Yaratıcılık", "Liderlik", "Optimizm"],
                "challenges": ["Ego", "Drama", "Dikkat arayışı", "Kibir"],
                "compatible": ["Koç", "Yay", "İkizler", "Terazi"],
                "career": ["Oyunculuk", "Sanat", "Eğlence", "Yöneticilik"]
            },
            "basak": {
                "name": "Başak", "english": "Virgo", "symbol": "♍", "element": "Toprak",
                "dates": "23 Ağustos - 22 Eylül", "ruling_planet": "Merkür",
                "colors": ["Kahverengi", "Yeşil", "Lacivert"], "lucky_numbers": [6, 14, 18, 24],
                "personality": ["Mükemmeliyetçi", "Analitik", "Detaycı", "Yardımsever"],
                "strengths": ["Analitik düşünce", "Detay odağı", "Güvenilirlik"],
                "challenges": ["Aşırı eleştiri", "Endişe", "Mükemmeliyetçilik"],
                "compatible": ["Boğa", "Oğlak", "Yengeç", "Akrep"],
                "career": ["Sağlık", "Muhasebe", "Araştırma", "Hukuk"]
            },
            "terazi": {
                "name": "Terazi", "english": "Libra", "symbol": "♎", "element": "Hava",
                "dates": "23 Eylül - 22 Ekim", "ruling_planet": "Venüs",
                "colors": ["Pembe", "Açık Mavi", "Pastel Yeşil"], "lucky_numbers": [4, 6, 13, 15],
                "personality": ["Dengeli", "Diplomatik", "Estetik", "Sosyal"],
                "strengths": ["Diplomasi", "Adalet duygusu", "Estetik anlayışı"],
                "challenges": ["Kararsızlık", "Çelişki korkusu", "Bağımlılık"],
                "compatible": ["İkizler", "Kova", "Aslan", "Yay"],
                "career": ["Hukuk", "Diplomasi", "Sanat", "İnsan kaynakları"]
            },
            "akrep": {
                "name": "Akrep", "english": "Scorpio", "symbol": "♏", "element": "Su",
                "dates": "23 Ekim - 21 Kasım", "ruling_planet": "Plüton",
                "colors": ["Bordo", "Siyah", "Koyu Kırmızı"], "lucky_numbers": [8, 11, 18, 22],
                "personality": ["Yoğun", "Gizemli", "Tutkulu", "Güçlü"],
                "strengths": ["Güçlü irade", "Sezgi", "Sadakat", "Kararlılık"],
                "challenges": ["Kıskançlık", "İntikamcılık", "Şüphecilik"],
                "compatible": ["Yengeç", "Balık", "Başak", "Oğlak"],
                "career": ["Psikoloji", "Araştırma", "Tıp", "Finans"]
            },
            "yay": {
                "name": "Yay", "english": "Sagittarius", "symbol": "♐", "element": "Ateş",
                "dates": "22 Kasım - 21 Aralık", "ruling_planet": "Jüpiter",
                "colors": ["Mor", "Turkuaz", "Turuncu"], "lucky_numbers": [3, 9, 15, 21],
                "personality": ["Özgür", "Maceraperest", "Felsefi", "İyimser"],
                "strengths": ["İyimserlik", "Özgürlük sevgisi", "Macera ruhu"],
                "challenges": ["Sabırsızlık", "Düşüncesizlik", "Sorumluluktan kaçış"],
                "compatible": ["Koç", "Aslan", "Terazi", "Kova"],
                "career": ["Turizm", "Eğitim", "Yayıncılık", "Spor"]
            },
            "oglak": {
                "name": "Oğlak", "english": "Capricorn", "symbol": "♑", "element": "Toprak",
                "dates": "22 Aralık - 19 Ocak", "ruling_planet": "Satürn",
                "colors": ["Siyah", "Kahverengi", "Koyu Yeşil"], "lucky_numbers": [6, 8, 10, 26],
                "personality": ["Disiplinli", "Hırslı", "Sorumlu", "Pratik"],
                "strengths": ["Disiplin", "Hırs", "Sorumluluk", "Kararlılık"],
                "challenges": ["Katılık", "Karamsar", "Aşırı ciddiyet"],
                "compatible": ["Boğa", "Başak", "Akrep", "Balık"],
                "career": ["Yöneticilik", "Mühendislik", "Bankacılık", "Siyaset"]
            },
            "kova": {
                "name": "Kova", "english": "Aquarius", "symbol": "♒", "element": "Hava",
                "dates": "20 Ocak - 18 Şubat", "ruling_planet": "Uranüs",
                "colors": ["Elektrik Mavisi", "Gümüş", "Mor"], "lucky_numbers": [4, 7, 11, 22],
                "personality": ["Bağımsız", "Yenilikçi", "Özgün", "Vizyoner"],
                "strengths": ["Yenilikçilik", "Bağımsızlık", "İnsancıllık", "Vizyon"],
                "challenges": ["Duygusal mesafe", "İnatçılık", "Aşırı idealizm"],
                "compatible": ["İkizler", "Terazi", "Koç", "Yay"],
                "career": ["Teknoloji", "Bilim", "Sosyal hizmet", "Araştırma"]
            },
            "balik": {
                "name": "Balık", "english": "Pisces", "symbol": "♓", "element": "Su",
                "dates": "19 Şubat - 20 Mart", "ruling_planet": "Neptün",
                "colors": ["Deniz Yeşili", "Lavanta", "Gümüş"], "lucky_numbers": [3, 9, 12, 15],
                "personality": ["Sezgisel", "Yaratıcı", "Duygusal", "Empatik"],
                "strengths": ["Sezgi", "Empati", "Yaratıcılık", "Şefkat"],
                "challenges": ["Aşırı duyarlılık", "Kaçış eğilimi", "Sınır eksikliği"],
                "compatible": ["Yengeç", "Akrep", "Boğa", "Oğlak"],
                "career": ["Sanat", "Müzik", "Psikoloji", "Sağlık"]
            }
        }

        # Gelişmiş içerik şablonları
        self.content_templates = {
            "daily_themes": [
                "Yeni Başlangıçlar", "İç Huzur Arayışı", "Yaratıcı Enerji", "Aşk Fısıltıları",
                "Kariyer Atılımı", "Ruhsal Gelişim", "Mali Fırsatlar", "Cesaret ve Güç",
                "Duygusal Denge", "İlham Veren Anlar", "Pozitif Değişim", "Güçlü Sezgiler"
            ],
            "weekly_themes": [
                "Dönüşüm Haftası", "Yaratıcılığın Zirvesi", "İlişkilerde Derinlik",
                "Kariyer Fırsatları", "Ruhsal Yolculuk", "Maddi Bolluk", "İçsel Keşif"
            ],
            "monthly_themes": [
                "Büyük Dönüşümler", "Aşkın Gücü", "Kariyer Zirvesi", "Ruhsal Uyanış",
                "Bolluk ve Bereket", "İç Yolculuk", "Kozmik Enerji", "Yaşam Dönüşümü"
            ]
        }

        # Astrolojik konular
        self.astrological_content = {
            "planets": {
                "Mars": ["enerji", "cesaret", "girişkenlik", "rekabet", "tutku"],
                "Venüs": ["aşk", "güzellik", "sanat", "uyum", "romantizm"],
                "Merkür": ["iletişim", "zeka", "teknoloji", "öğrenme"],
                "Jüpiter": ["şans", "genişleme", "felsefe", "bereket"],
                "Satürn": ["disiplin", "sorumluluk", "olgunluk", "sabır"],
                "Uranüs": ["değişim", "özgürlük", "yaratıcılık", "sürpriz"],
                "Neptün": ["rüyalar", "sanat", "spiritüalite", "sezgi"],
                "Plüton": ["dönüşüm", "güç", "yeniden doğuş"]
            },
            "aspects": [
                "Yeni Ay etkisi ile yeni başlangıçlar",
                "Dolunay'ın güçlü enerjisi",
                "Artan Ay'ın büyüme etkisi",
                "Azalan Ay'ın temizlenme gücü"
            ]
        }

    def generate_daily_content(self, sign_key: str) -> Dict[str, str]:
        """Günlük burç yorumu oluştur"""
        sign_data = self.zodiac_data[sign_key]
        theme = random.choice(self.content_templates["daily_themes"])
        planet = random.choice(list(self.astrological_content["planets"].keys()))
        planet_effects = self.astrological_content["planets"][planet]
        aspect = random.choice(self.astrological_content["aspects"])

        date_str = datetime.now().strftime("%Y-%m-%d")
        date_display = datetime.now().strftime("%d %B %Y")

        title = f"{sign_data['name']} Burcu Günlük Yorumu - {theme}"

        # Detaylı içerik oluştur
        content = f"""---
title: "{title}"
description: "{sign_data['name']} burcu için {date_display} günlük astroloji yorumu. {theme} teması ile rehberlik."
pubDate: {date_str}
category: "astrology"
tags: ["{sign_data['name'].lower()}", "günlük", "burç", "astroloji", "{theme.lower()}"]
heroImage: "/images/zodiac/{sign_data['english'].lower()}.jpg"
zodiacSign: "{sign_key}"
element: "{sign_data['element']}"
symbol: "{sign_data['symbol']}"
theme: "{theme}"
---

# {title}

{sign_data['symbol']} **{sign_data['name']} Burcu** ({sign_data['dates']})

## 🌟 Günün Genel Enerjisi

Bugün {sign_data['name']} burcu için **{planet}** gezeninizin etkisiyle {theme.lower()} yaşayacağınız bereketli bir gün olacak. {sign_data['element']} elementi size güç katarken, doğal {random.choice(sign_data['personality']).lower()} özelliğiniz ön plana çıkacak.

{aspect}. Bu kozmik enerji sizin için özellikle {random.choice(planet_effects)} konusunda faydalı olacak.

## 💕 Aşk ve İlişkiler

**💖 Bekar {sign_data['name']}lar:** {random.choice(['Sosyal ortamlarda', 'İş yerinde', 'Hobilerle uğraşırken', 'Spor yaparken'])} dikkatinizi çekecek biriyle tanışabilirsiniz. {sign_data['ruling_planet']} gezeninizin pozitif etkisi altında samimi bağlantılar kurabilirsiniz.

**💑 İlişkisi Olan {sign_data['name']}lar:** Partnerinizle daha derin bağlar kurabilir, {random.choice(['romantik', 'özel', 'anlamlı', 'duygusal'])} anlar yaşayabilirsiniz. {random.choice(sign_data['colors'])} rengi bugün aşk hayatınızda şans getirebilir.

**🌹 İlişki Önerileri:**
• Duygularınızı samimi şekilde paylaşın
• Küçük jestlerle sevginizi gösterin
• Geçmiş sorunları geride bırakın
• Partnerinizin fikirlerini dinleyin

## 💼 Kariyer ve İş Hayatı

**🚀 İş Hayatı:** {random.choice(sign_data['strengths'])} özelliğiniz sayesinde bugün dikkat çekeceksiniz. {random.choice(sign_data['career'])} alanında yeni fırsatlar değerlendirilebilir.

**💰 Mali Durum:** Maddi konularda {random.choice(['temkinli', 'planlı', 'akıllıca', 'stratejik'])} davranın. Bugün {random.choice(['yatırım', 'tasarruf', 'alışveriş', 'finansal planlama'])} konularında doğru kararlar alabilirsiniz.

**📈 Öneriler:**
• Yeni projelere başlamak için uygun zaman
• {random.choice(['İş birliği', 'Takım çalışması', 'Networking', 'Görüşmeler'])} odaklanın
• Yaratıcı fikirlerinizi paylaşın

## 🏃‍♀️ Sağlık ve Enerji

**{sign_data['element']} elementi size bugün özel bir güç verecek:**

{self._get_health_advice(sign_data['element'])}

**⚖️ Genel Sağlık:** Enerji seviyeniz {random.choice(['yüksek', 'dengeli', 'iyi', 'pozitif'])} olacak. {random.choice(['Spor', 'Yürüyüş', 'Meditasyon', 'Nefes egzersizleri'])} yaparak kendinizi daha iyi hissedebilirsiniz.

## 🎯 Günün Tavsiyeleri

1. **{random.choice(sign_data['strengths'])}** özelliğinizi aktif kullanın
2. **{random.choice(sign_data['colors'])}** rengi bugün şansınızı artıracak
3. **{random.choice(sign_data['lucky_numbers'])}** sayısı size rehberlik edebilir
4. **{random.choice(sign_data['compatible'])}** burcu ile pozitif etkileşimler kurun
5. Sezgilerinize güvenin ve pozitif düşünün

## 🔮 Şanslı Elementler

**🎨 Şanslı Renkler:** {', '.join(sign_data['colors'])}
**🔢 Şanslı Sayılar:** {', '.join(map(str, sign_data['lucky_numbers']))}
**🌟 Güçlü Saatler:** {random.choice(['09:00-11:00', '14:00-16:00', '19:00-21:00'])}
**💫 Uyumlu Burçlar:** {', '.join(sign_data['compatible'])}

## 💫 Sonuç

Bugün {sign_data['name']} burcu için {theme.lower()} yaşayacağınız, kişisel gelişiminizi destekleyecek güzel bir gün olacak. {sign_data['ruling_planet']} gezeninizin desteği ile doğal yeteneklerinizi kullanarak başarılı adımlar atabilirsiniz.

---

*{sign_data['name']} burcu olarak doğal {random.choice(sign_data['personality']).lower()} özelliğiniz bugün size büyük avantaj sağlayacak.*

**Astroloji Notu:** Bu yorum {date_display} tarihi için hazırlanmıştır. Kişisel gelişiminiz için bir rehber olarak kullanın.
"""

        slug = f"{date_str}-{sign_key}-burcu-gunluk-yorum"

        return {
            "title": title,
            "content": content,
            "slug": slug,
            "sign": sign_key,
            "period": "günlük",
            "theme": theme
        }

    def _get_health_advice(self, element: str) -> str:
        """Element bazlı sağlık tavsiyesi"""
        health_advice = {
            "Ateş": "🔥 Enerji seviyeniz yüksek olacak. Aktif sporları tercih edin, ancak aşırıya kaçmayın. Protein açısından zengin beslenme size iyi gelecek.",
            "Toprak": "🌱 Vücudunuzla uyum içinde olacaksınız. Doğal beslenmeye önem verin. Yürüyüş ve yoga gibi aktiviteler ideal olacak.",
            "Hava": "💨 Zihinsel aktiviteniz artacak. Nefes egzerzilerine zaman ayırın. Açık havada vakit geçirmek size enerji verecek.",
            "Su": "💧 Duygusal dengeniz önemli. Bol su içmeyi unutmayın. Su sporları ve meditasyon faydalı olacak."
        }
        return health_advice.get(element, "Genel sağlık durumunuz iyi olacak.")

    def create_weekly_content(self, sign_key: str) -> Dict[str, str]:
        """Haftalık burç yorumu oluştur"""
        sign_data = self.zodiac_data[sign_key]
        theme = random.choice(self.content_templates["weekly_themes"])

        date_str = datetime.now().strftime("%Y-%m-%d")

        content = f"""---
title: "{sign_data['name']} Burcu Haftalık Yorumu - {theme}"
description: "{sign_data['name']} burcu için detaylı haftalık astroloji rehberi."
pubDate: {date_str}
category: "astrology"
tags: ["{sign_data['name'].lower()}", "haftalık", "burç", "astroloji"]
heroImage: "/images/zodiac/{sign_data['english'].lower()}.jpg"
period: "weekly"
---

# {sign_data['name']} Burcu Haftalık Yorumu

{sign_data['symbol']} **{sign_data['name']} Burcu** ({sign_data['dates']})

Bu hafta {sign_data['name']} burcu için {theme.lower()} yaşayacağınız transformatif bir dönem başlıyor...

[Haftalık detaylı içerik buraya gelecek]
"""

        slug = f"{date_str}-{sign_key}-haftalik-yorum"

        return {
            "title": f"{sign_data['name']} Burcu Haftalık Yorumu",
            "content": content,
            "slug": slug,
            "sign": sign_key,
            "period": "haftalık",
            "theme": theme
        }

    def create_content_file(self, content_data: Dict[str, str]) -> str:
        """İçeriği dosyaya kaydet"""
        filename = f"{content_data['slug']}.md"
        filepath = os.path.join(self.content_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content_data['content'])

        return filepath

    def generate_all_daily_content(self) -> List[str]:
        """Tüm burçlar için günlük içerik oluştur"""
        print("🚀 Tüm burçlar için günlük içerik oluşturuluyor...")
        created_files = []

        for sign_key in self.zodiac_data.keys():
            content_data = self.generate_daily_content(sign_key)
            filepath = self.create_content_file(content_data)
            created_files.append(filepath)
            print(f"✅ {self.zodiac_data[sign_key]['name']} burcu günlük yorumu oluşturuldu")

        print(f"✅ {len(created_files)} günlük yorum oluşturuldu!")
        return created_files

    def run_interactive_mode(self):
        """İnteraktif mod"""
        print("🌟 Premium Astroloji İçerik Sistemi")
        print("=" * 50)

        while True:
            print("\nSeçenekler:")
            print("1. Tüm burçlar günlük içerik oluştur")
            print("2. Tek burç günlük içerik")
            print("3. Haftalık içerik oluştur (pilot)")
            print("4. İçerik istatistikleri")
            print("5. Çıkış")

            choice = input("\nSeçiminiz (1-5): ").strip()

            if choice == "1":
                self.generate_all_daily_content()

            elif choice == "2":
                print("\nMevcut burçlar:")
                for i, (key, data) in enumerate(self.zodiac_data.items(), 1):
                    print(f"{i:2d}. {data['name']} ({key})")

                try:
                    sign_choice = int(input("\nBurç seçin (1-12): ")) - 1
                    signs = list(self.zodiac_data.keys())
                    if 0 <= sign_choice < len(signs):
                        sign_key = signs[sign_choice]
                        content_data = self.generate_daily_content(sign_key)
                        filepath = self.create_content_file(content_data)
                        print(f"✅ {self.zodiac_data[sign_key]['name']} içeriği oluşturuldu: {filepath}")
                    else:
                        print("❌ Geçersiz seçim")
                except ValueError:
                    print("❌ Geçerli bir sayı girin")

            elif choice == "3":
                print("📅 Haftalık içerik sistemi geliştirme aşamasında...")

            elif choice == "4":
                files = [f for f in os.listdir(self.content_dir) if f.endswith('.md')]
                print(f"📊 Toplam astroloji içeriği: {len(files)} dosya")

            elif choice == "5":
                print("👋 Görüşürüz!")
                break

            else:
                print("❌ Geçersiz seçim")

def main():
    """Ana fonksiyon"""
    system = PremiumAstrologySystem()
    system.run_interactive_mode()

if __name__ == "__main__":
    main()
