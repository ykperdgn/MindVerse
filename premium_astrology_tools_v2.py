#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌟 Premium Astroloji Araçları v2.0 - Gelişmiş Özellikler
MindVerse Daily için premium astroloji özellikleri
Premium Özellik 4: Haftalık Astroloji Raporu
Premium Özellik 5: Yıllık Astroloji Tahmini
"""

import random
import json
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import os
from calendar import monthrange

class PremiumAstrologyToolsV2:
    def __init__(self):
        self.content_dir = "src/content/astrology"
        os.makedirs(self.content_dir, exist_ok=True)

        # Gelişmiş burç bilgileri
        self.zodiac_data = {
            "koc": {"name": "Koç", "english": "Aries", "symbol": "♈", "element": "Ateş", "quality": "Öncü", "ruling_planet": "Mars", "dates": (3, 21, 4, 19)},
            "boga": {"name": "Boğa", "english": "Taurus", "symbol": "♉", "element": "Toprak", "quality": "Sabit", "ruling_planet": "Venüs", "dates": (4, 20, 5, 20)},
            "ikizler": {"name": "İkizler", "english": "Gemini", "symbol": "♊", "element": "Hava", "quality": "Değişken", "ruling_planet": "Merkür", "dates": (5, 21, 6, 20)},
            "yengec": {"name": "Yengeç", "english": "Cancer", "symbol": "♋", "element": "Su", "quality": "Öncü", "ruling_planet": "Ay", "dates": (6, 21, 7, 22)},
            "aslan": {"name": "Aslan", "english": "Leo", "symbol": "♌", "element": "Ateş", "quality": "Sabit", "ruling_planet": "Güneş", "dates": (7, 23, 8, 22)},
            "basak": {"name": "Başak", "english": "Virgo", "symbol": "♍", "element": "Toprak", "quality": "Değişken", "ruling_planet": "Merkür", "dates": (8, 23, 9, 22)},
            "terazi": {"name": "Terazi", "english": "Libra", "symbol": "♎", "element": "Hava", "quality": "Öncü", "ruling_planet": "Venüs", "dates": (9, 23, 10, 22)},
            "akrep": {"name": "Akrep", "english": "Scorpio", "symbol": "♏", "element": "Su", "quality": "Sabit", "ruling_planet": "Plüton", "dates": (10, 23, 11, 21)},
            "yay": {"name": "Yay", "english": "Sagittarius", "symbol": "♐", "element": "Ateş", "quality": "Değişken", "ruling_planet": "Jüpiter", "dates": (11, 22, 12, 21)},
            "oglak": {"name": "Oğlak", "english": "Capricorn", "symbol": "♑", "element": "Toprak", "quality": "Öncü", "ruling_planet": "Satürn", "dates": (12, 22, 1, 19)},
            "kova": {"name": "Kova", "english": "Aquarius", "symbol": "♒", "element": "Hava", "quality": "Sabit", "ruling_planet": "Uranüs", "dates": (1, 20, 2, 18)},
            "balik": {"name": "Balık", "english": "Pisces", "symbol": "♓", "element": "Su", "quality": "Değişken", "ruling_planet": "Neptün", "dates": (2, 19, 3, 20)}
        }

        # Haftalık astroloji konuları
        self.weekly_themes = [
            "Aşk ve İlişkiler", "Kariyer ve Para", "Sağlık ve Enerji", "Aile ve Ev",
            "Yaratıcılık ve Hobi", "Arkadaşlık ve Sosyal", "Manevi Gelişim", "Seyahat ve Macera"
        ]

        # Yıllık dönemler
        self.yearly_periods = {
            "İlkbahar": {"months": [3, 4, 5], "theme": "Yenilenme ve Başlangıçlar"},
            "Yaz": {"months": [6, 7, 8], "theme": "Büyüme ve Başarı"},
            "Sonbahar": {"months": [9, 10, 11], "theme": "Hasat ve Değerlendirme"},
            "Kış": {"months": [12, 1, 2], "theme": "İç Gözlem ve Hazırlık"}
        }

        # Astrolojik yönler
        self.aspects = {
            "conjunction": {"name": "Kavuşum", "effect": "güçlendirici", "score": 90},
            "trine": {"name": "Üçgen", "effect": "uyumlu", "score": 85},
            "sextile": {"name": "Altıgen", "effect": "destekleyici", "score": 75},
            "square": {"name": "Kare", "effect": "zorlu", "score": 45},
            "opposition": {"name": "Karşıtlık", "effect": "dengeleyici", "score": 55}
        }

    def create_weekly_astrology_report(self) -> str:
        """Premium Özellik 4: Haftalık Astroloji Raporu"""
        today = datetime.now()
        week_start = today - timedelta(days=today.weekday())
        week_end = week_start + timedelta(days=6)

        theme = random.choice(self.weekly_themes)
        main_planet = random.choice(["Merkür", "Venüs", "Mars", "Jüpiter", "Satürn"])

        date_str = week_start.strftime("%Y-%m-%d")
        week_range = f"{week_start.strftime('%d %B')} - {week_end.strftime('%d %B %Y')}"

        title = f"Haftalık Astroloji Raporu - {week_range}"
        filename = f"haftalik-astroloji-raporu-{date_str}.md"

        # Haftalık genel tahmin
        general_forecast = self.generate_weekly_general_forecast(theme, main_planet)

        # Her burç için haftalık yorum
        weekly_signs = self.generate_weekly_signs_forecast()

        content = f"""---
title: "{title}"
description: "{week_range} haftası için detaylı astroloji raporu ve burç yorumları."
pubDate: {date_str}
category: "astrology"
tags: ["haftalık", "astroloji raporu", "{theme.lower()}", "burç yorumları"]
heroImage: "/images/weekly-astrology.jpg"
type: "weekly-report"
featured: true
weekly_theme: "{theme}"
main_planet: "{main_planet}"
week_start: "{week_start.strftime('%Y-%m-%d')}"
week_end: "{week_end.strftime('%Y-%m-%d')}"
---

# 🌟 {title}

## 📅 Hafta Genel Görünümü

Bu hafta **{theme}** konularında önemli gelişmeler yaşanacak. {main_planet} gezegeninin etkisi altında geçecek olan bu dönemde, astrolojik enerjiler özellikle şu alanlarda hissedilecek:

{general_forecast}

---

## 🔮 Haftalık Burç Yorumları

{weekly_signs}

---

## 🌙 Haftalık Önemli Tarihler

### Pazartesi ({week_start.strftime('%d.%m')})
- **Ay Evresi:** {self.get_moon_phase(week_start)}
- **Önemli Açı:** {random.choice(list(self.aspects.values()))['name']}
- **Odak:** Hafta başı enerjisi ve yeni projeler

### Çarşamba ({(week_start + timedelta(days=2)).strftime('%d.%m')})
- **Hızlı Gezegen:** {random.choice(["Merkür", "Venüs"])} hareketi
- **Enerji:** Orta haftanın dönüşüm enerjisi
- **Tavsiye:** İletişim ve düşünce netliği

### Cuma ({(week_start + timedelta(days=4)).strftime('%d.%m')})
- **Sosyal Enerji:** Venüs etkisi güçlü
- **Aktivite:** Sosyal buluşmalar ve romantik anlar
- **Şans:** Mali konularda dikkatli olun

### Pazar ({week_end.strftime('%d.%m')})
- **Dinlenme:** Hafta sonu refleksiyonu
- **Ay Enerjisi:** İç dünya ve rüyalar
- **Hazırlık:** Gelecek hafta için planning

---

## 💫 Haftalık Astroloji Tavsiyeleri

### 🌟 Genel Tavsiyeler
- **En İyi Günler:** Çarşamba ve Cuma
- **Dikkat Edilecek:** Pazartesi ve Perşembe
- **Şanslı Renkler:** {random.choice(['Mavi', 'Yeşil', 'Mor', 'Turuncu'])} ve {random.choice(['Altın', 'Gümüş', 'Beyaz'])}
- **Şanslı Sayılar:** {random.randint(1, 9)}, {random.randint(10, 19)}, {random.randint(20, 31)}

### 💝 Aşk ve İlişkiler
Bu hafta {theme.lower()} temasının etkisiyle, ilişkilerde derin bağlar kurma zamanı. Özellikle {random.choice(['su', 'toprak', 'ateş', 'hava'])} burçları için romantik fırsatlar.

### 💼 Kariyer ve Finans
{main_planet} etkisi altında, profesyonel hayatta yeni kapılar açılabilir. Mali konularda {random.choice(['temkinli', 'cesur', 'dengeli'])} yaklaşım sergilemek önemli.

### 🏥 Sağlık ve Enerji
Enerji seviyeniz bu hafta {random.choice(['yüksek', 'değişken', 'dengeli'])} olacak. {random.choice(['Yoga', 'Meditasyon', 'Doğa yürüyüşü'])} gibi aktiviteler önerilir.

---

*🔮 Bu haftalık rapor, genel astrolojik eğilimleri yansıtır. Kişisel doğum haritanız için özel danışmanlık alabilirsiniz.*

**Sonraki Hafta:** Daha detaylı tahminler için takipte kalın!

---

### 📚 İlgili İçerikler
- [Günlük Burç Yorumları](/astrology/gunluk-burç-yorumlari)
- [Kişisel Doğum Haritası](/astrology/dogum-haritasi)
- [Burç Uyumluluğu](/astrology/uyumluluk-analizi)
"""

        filepath = os.path.join(self.content_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ Haftalık astroloji raporu oluşturuldu: {filename}")
        return filepath

    def generate_weekly_general_forecast(self, theme: str, main_planet: str) -> str:
        """Haftalık genel tahmin oluştur"""
        forecasts = [
            f"**{main_planet}** gezegeninin güçlü etkisi altında, {theme.lower()} alanında önemli gelişmeler bekleniyor.",
            f"Bu dönemde evrensel enerjiler {theme.lower()} konularına odaklanıyor.",
            f"Astrolojik açıdan bakıldığında, {theme.lower()} temasında dönüşümler yaşanacak.",
            f"Kozmik enerjiler bu hafta özellikle {theme.lower()} alanında hissedilecek."
        ]

        return random.choice(forecasts) + f"\n\n**{main_planet} Etkisi:** Bu gezegen özellikle iletişim, düşünce ve karar verme süreçlerinizi etkileyecek. Önemli kararları bu dönemde almanız avantajlı olabilir."

    def generate_weekly_signs_forecast(self) -> str:
        """Haftalık burç yorumları oluştur"""
        signs_content = ""

        for sign_key, sign_data in self.zodiac_data.items():
            weekly_score = random.randint(65, 95)
            lucky_day = random.choice(['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi', 'Pazar'])

            areas = {
                "Aşk": random.randint(60, 90),
                "Kariyer": random.randint(65, 95),
                "Sağlık": random.randint(70, 90),
                "Para": random.randint(55, 85)
            }

            forecast_texts = [
                f"Bu hafta enerjiniz {weekly_score}% seviyesinde olacak.",
                f"Özellikle {lucky_day} günü şanslı gününüz.",
                f"{sign_data['element']} elementi size güç katacak.",
                f"Yönetici gezegen {sign_data['ruling_planet']} olumlu etki yapacak."
            ]

            signs_content += f"""
### {sign_data['symbol']} {sign_data['name']} Burcu
**Haftalık Enerji:** %{weekly_score} | **Şanslı Gün:** {lucky_day}

{random.choice(forecast_texts)}

**Detay Puanlar:**
- 💕 Aşk: %{areas['Aşk']}
- 💼 Kariyer: %{areas['Kariyer']}
- 🏥 Sağlık: %{areas['Sağlık']}
- 💰 Para: %{areas['Para']}

{self.generate_weekly_advice(sign_data)}

---
"""

        return signs_content

    def generate_weekly_advice(self, sign_data: Dict) -> str:
        """Haftalık tavsiye oluştur"""
        advices = [
            f"**Tavsiye:** {sign_data['element']} enerjisini kullanarak dengeli kalın.",
            f"**Dikkat:** {sign_data['quality']} özelliğiniz bu hafta avantaj sağlayacak.",
            f"**Fırsat:** {sign_data['ruling_planet']} etkisiyle yeni kapılar açılabilir.",
            f"**Odak:** {sign_data['name']} enerjisini en iyi şekilde değerlendirin."
        ]

        return random.choice(advices)

    def create_yearly_astrology_forecast(self) -> str:
        """Premium Özellik 5: Yıllık Astroloji Tahmini"""
        year = datetime.now().year + 1  # Gelecek yıl tahmini

        title = f"{year} Yılı Detaylı Astroloji Tahmini"
        filename = f"yillik-astroloji-tahmini-{year}.md"
        date_str = datetime.now().strftime("%Y-%m-%d")

        # Yıllık ana temalar
        main_themes = self.generate_yearly_themes(year)

        # Dönemlik tahminler
        seasonal_forecasts = self.generate_seasonal_forecasts(year)

        # Burç bazında yıllık tahminler
        zodiac_yearly = self.generate_zodiac_yearly_forecasts(year)

        content = f"""---
title: "{title}"
description: "{year} yılı için kapsamlı astroloji tahmini, dönemlik analizler ve burç yorumları."
pubDate: {date_str}
category: "astrology"
tags: ["yıllık tahmin", "{year}", "astroloji", "gelecek", "dönemlik analiz"]
heroImage: "/images/yearly-forecast.jpg"
type: "yearly-forecast"
featured: true
forecast_year: {year}
main_themes: {json.dumps(main_themes, ensure_ascii=False)}
---

# 🌟 {title}

## 🔮 Yıl Genel Görünümü

{year} yılı, astrolojik açıdan **dönüşüm ve büyüme** yılı olarak öne çıkıyor. Bu yıl boyunca yaşanacak olan önemli astrolojik hareketler, hem bireysel hem de toplumsal düzeyde derin değişimlere işaret ediyor.

### 📅 Yılın Ana Temaları

{self.format_yearly_themes(main_themes)}

---

## 🌍 Dönemlik Astroloji Tahminleri

{seasonal_forecasts}

---

## 🔮 Burç Bazında {year} Yılı Tahminleri

{zodiac_yearly}

---

## 🌙 {year} Yılının Önemli Astrolojik Olayları

### Ayın Ek Detayları
- **Süper Ay:** {random.choice(['Mart', 'Haziran', 'Eylül', 'Aralık'])}
- **Mavi Ay:** {random.choice(['Mayıs', 'Ağustos', 'Kasım'])}
- **Ay Tutulması:** {random.choice(['Nisan-Ekim', 'Mayıs-Kasım', 'Haziran-Aralık'])}
- **Güneş Tutulması:** {random.choice(['Mart-Eylül', 'Nisan-Ekim', 'Mayıs-Kasım'])}

### Gezegen Gerilemelerı
- **Merkür Geriler:** 3-4 kez (İletişim ve teknoloji)
- **Venüs Geriler:** 1 kez (Aşk ve finans)
- **Mars Geriler:** {random.choice(['Yok', '1 kez'])} (Enerji ve eylem)

---

## 💫 {year} Yılı İçin Genel Tavsiyeler

### 🌟 En İyi Dönemler
1. **İlkbahar ({random.choice(['Mart', 'Nisan', 'Mayıs'])}):** Yeni başlangıçlar için ideal
2. **Yaz ({random.choice(['Haziran', 'Temmuz', 'Ağustos'])}):** Büyüme ve başarı dönemi
3. **Sonbahar ({random.choice(['Eylül', 'Ekim', 'Kasım'])}):** Hasat ve değerlendirme zamanı

### ⚠️ Dikkatli Olunacak Dönemler
- **Merkür Geri Dönemleri:** İletişimde dikkat
- **Tutulma Dönemleri:** Ani değişimlere hazır olun
- **Gezegen Kavuşumları:** Yoğun enerji dönemleri

### 💎 Yıllık Şans Faktörleri
- **Şanslı Aylar:** {random.choice(['Nisan, Haziran, Eylül', 'Mayıs, Temmuz, Ekim', 'Mart, Ağustos, Kasım'])}
- **Şanslı Günler:** {random.choice(['Çarşamba, Cuma', 'Salı, Perşembe', 'Pazartesi, Cumartesi'])}
- **Şanslı Renkler:** {random.choice(['Mavi, Yeşil', 'Mor, Altın', 'Turuncu, Gümüş'])}
- **Şanslı Sayılar:** {random.choice(['3, 7, 11', '2, 6, 9', '4, 8, 12'])}

---

## 💝 Aşk ve İlişkiler - {year}

Bu yıl aşk hayatında **{random.choice(['derin bağlar', 'yeni başlangıçlar', 'dönüşümler'])}** yaşanacak. Özellikle {random.choice(['su', 'toprak', 'ateş', 'hava'])} burçları için romantik dönem.

**En İyi Aşk Dönemleri:**
- {random.choice(['İlkbahar', 'Yaz', 'Sonbahar'])}: Yeni ilişkiler
- {random.choice(['Yaz', 'Sonbahar', 'Kış'])}: Mevcut ilişkilerde derinleşme

---

## 💼 Kariyer ve Finans - {year}

Profesyonel hayatta **{random.choice(['büyük fırsatlar', 'karıyer değişimleri', 'finansal büyüme'])}** yılı. Özellikle {random.choice(['dijital', 'yaratıcı', 'hizmet', 'teknoloji'])} sektörlerde gelişmeler.

**Mali Tavsiyeler:**
- **Yatırım:** {random.choice(['İlkbahar', 'Yaz', 'Sonbahar'])} döneminde değerlendir
- **Harcama:** {random.choice(['Kış', 'Sonbahar', 'İlkbahar'])} aylarında dikkatli ol
- **Gelir:** Yıl ortasından itibaren artış bekleniyor

---

## 🏥 Sağlık ve Enerji - {year}

Bu yıl sağlık konusunda **{random.choice(['dengeli yaklaşım', 'yenilenme', 'güçlenme'])}** ön planda. Özellikle mental sağlık ve enerji yönetimine odaklanın.

**Sağlık Tavsiyeleri:**
- **Beslenme:** Mevsimsel beslenme modeli
- **Egzersiz:** Düzenli ve keyifli aktiviteler
- **Mental:** Meditasyon ve stres yönetimi

---

*🔮 Bu yıllık tahmin, genel astrolojik eğilimleri yansıtır. Kişisel doğum haritanız için özel danışmanlık alabilirsiniz.*

**Gelecek Yıl:** {year + 1} yılı tahminleri için takipte kalın!

---

### 📚 İlgili İçerikler
- [Haftalık Astroloji Raporu](/astrology/haftalik-rapor)
- [Aylık Burç Yorumları](/astrology/aylik-burc-yorumlari)
- [Kişisel Doğum Haritası](/astrology/dogum-haritasi)
"""

        filepath = os.path.join(self.content_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ {year} yılı astroloji tahmini oluşturuldu: {filename}")
        return filepath

    def generate_yearly_themes(self, year: int) -> List[str]:
        """Yıllık ana temalar oluştur"""
        themes = [
            "Dijital Dönüşüm ve Teknoloji",
            "Sürdürülebilirlik ve Çevre",
            "Manevi Gelişim ve İç Yolculuk",
            "İnovasyonlarve Yaratıcılık",
            "İnsan İlişkileri ve Sosyal Bağlar",
            "Kariyer ve Profesyonel Gelişim",
            "Sağlık ve Yaşam Kalitesi",
            "Finansal Bağımsızlık"
        ]

        return random.sample(themes, 3)

    def format_yearly_themes(self, themes: List[str]) -> str:
        """Yıllık temaları formatla"""
        formatted = ""
        for i, theme in enumerate(themes, 1):
            descriptions = {
                "Dijital Dönüşüm ve Teknoloji": "Bu yıl teknolojik ilerlemeler hayatımızda büyük rol oynayacak.",
                "Sürdürülebilirlik ve Çevre": "Çevre bilinci ve sürdürülebilir yaşam ön plana çıkacak.",
                "Manevi Gelişim ve İç Yolculuk": "İç dünyamızı keşfetme ve manevi gelişim önem kazanacak.",
                "İnovasyonlarve Yaratıcılık": "Yaratıcı projeler ve yenilikçi çözümler dönem olacak.",
                "İnsan İlişkileri ve Sosyal Bağlar": "İlişkiler ve sosyal bağlantılar güçlenecek.",
                "Kariyer ve Profesyonel Gelişim": "Mesleki gelişim ve kariyer değişimleri ön planda.",
                "Sağlık ve Yaşam Kalitesi": "Sağlıklı yaşam ve yaşam kalitesi artırımı önemli.",
                "Finansal Bağımsızlık": "Mali özgürlük ve finansal planlama önem kazanacak."
            }

            formatted += f"**{i}. {theme}**\n"
            formatted += f"{descriptions.get(theme, 'Bu tema yıl boyunca öne çıkacak.')}\n\n"

        return formatted

    def generate_seasonal_forecasts(self, year: int) -> str:
        """Dönemlik tahminler oluştur"""
        seasons_content = ""

        for season, data in self.yearly_periods.items():
            months_names = {
                1: "Ocak", 2: "Şubat", 3: "Mart", 4: "Nisan",
                5: "Mayıs", 6: "Haziran", 7: "Temmuz", 8: "Ağustos",
                9: "Eylül", 10: "Ekim", 11: "Kasım", 12: "Aralık"
            }

            season_months = [months_names[m] for m in data['months']]
            energy_level = random.randint(70, 90)

            forecasts = [
                f"Bu dönemde enerji seviyeniz %{energy_level} olacak.",
                f"{data['theme']} teması hayatınızda ön plana çıkacak.",
                f"Önemli değişimler ve fırsatlar sizi bekliyor.",
                f"Astrolojik enerjiler size destek olacak."
            ]

            seasons_content += f"""
### 🌿 {season} Dönemi ({', '.join(season_months)})
**Tema:** {data['theme']} | **Enerji:** %{energy_level}

{random.choice(forecasts)}

**Öne Çıkan Konular:**
- {random.choice(['Yeni projeler', 'İlişki gelişimi', 'Kariyer fırsatları', 'Sağlık iyileşmesi'])}
- {random.choice(['Finansal gelişim', 'Yaratıcı projeler', 'Sosyal aktiviteler', 'İç gelişim'])}
- {random.choice(['Seyahat fırsatları', 'Eğitim ve öğrenme', 'Aile zamanı', 'Hobi geliştirme'])}

**Dikkat Edilecek:**
- {random.choice(['Aşırı hıza kapılma', 'Mali konularda aceleci olma', 'İletişim sorunları', 'Enerji dağılımı'])}

---
"""

        return seasons_content

    def generate_zodiac_yearly_forecasts(self, year: int) -> str:
        """Burç bazında yıllık tahminler"""
        zodiac_content = ""

        for sign_key, sign_data in self.zodiac_data.items():
            yearly_score = random.randint(75, 95)
            lucky_months = random.sample(['Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım'], 3)

            life_areas = {
                "Aşk ve İlişkiler": random.randint(70, 90),
                "Kariyer ve İş": random.randint(75, 95),
                "Sağlık ve Enerji": random.randint(80, 95),
                "Finans ve Para": random.randint(65, 85),
                "Aile ve Ev": random.randint(70, 90),
                "Sosyal Hayat": random.randint(75, 90)
            }

            zodiac_content += f"""
### {sign_data['symbol']} {sign_data['name']} Burcu - {year}
**Yıllık Enerji:** %{yearly_score} | **Şanslı Aylar:** {', '.join(lucky_months)}

Bu yıl {sign_data['name']} burcu için **{random.choice(['büyüme', 'dönüşüm', 'başarı', 'dengeleme'])}** yılı olacak. {sign_data['ruling_planet']} gezeni size özel destek sağlayacak.

**Yaşam Alanları Puanları:**
"""

            for area, score in life_areas.items():
                zodiac_content += f"- {area}: %{score}\n"

            # Dönemlik öneriler
            best_period = random.choice(['İlkbahar', 'Yaz', 'Sonbahar', 'Kış'])
            zodiac_content += f"""
**En İyi Dönem:** {best_period} - {self.yearly_periods[best_period]['theme']}

**Yıllık Tavsiyeler:**
- {random.choice(['Cesur adımlar atın', 'Sabırlı olun', 'Değişime açık olun', 'Dengeyi koruyun'])}
- {random.choice(['İlişkilere yatırım yapın', 'Kariyere odaklanın', 'Sağlığınızı öncelik yapın', 'Finansal planlama yapın'])}
- {random.choice(['Yaratıcılığınızı kullanın', 'Sosyal bağlar kurun', 'İç sesinizi dinleyin', 'Öğrenmeye devam edin'])}

---
"""

        return zodiac_content

    def get_moon_phase(self, date: datetime) -> str:
        """Ay evresi hesapla (basit yaklaşım)"""
        phases = ["Yeni Ay", "Hilal", "İlk Dördün", "Dolunay", "Son Dördün"]
        # Basit döngüsel hesaplama
        day_of_year = date.timetuple().tm_yday
        phase_index = (day_of_year // 7) % len(phases)
        return phases[phase_index]

    def create_content_file(self, content_data: Dict) -> str:
        """İçerik dosyası oluştur"""
        filename = content_data.get('filename', f"content-{datetime.now().strftime('%Y%m%d%H%M%S')}.md")
        filepath = os.path.join(self.content_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content_data['content'])

        return filepath

    def run_interactive_mode(self):
        """İnteraktif mod v2.0"""
        print("🌟 Premium Astroloji Araçları v2.0")
        print("=" * 60)

        while True:
            print("\nPremium Özellikler:")
            print("1. Kişiselleştirilmiş Doğum Haritası")
            print("2. Burç Uyumluluk Analizi")
            print("3. Rastgele doğum haritası oluştur (demo)")
            print("4. Rastgele uyumluluk analizi oluştur (demo)")
            print("5. Premium içerik istatistikleri")
            print("6. 🆕 Haftalık Astroloji Raporu")
            print("7. 🆕 Yıllık Astroloji Tahmini")
            print("8. Çıkış")

            choice = input("\nSeçiminiz (1-8): ").strip()

            if choice == "6":
                # Premium Özellik 4: Haftalık Astroloji Raporu
                try:
                    filepath = self.create_weekly_astrology_report()
                    print(f"📄 Dosya konumu: {filepath}")
                except Exception as e:
                    print(f"❌ Hata: {e}")

            elif choice == "7":
                # Premium Özellik 5: Yıllık Astroloji Tahmini
                try:
                    year = input(f"Hangi yıl için tahmin? (varsayılan: {datetime.now().year + 1}): ").strip()
                    if not year:
                        year = datetime.now().year + 1
                    else:
                        year = int(year)

                    # Geçici olarak create_yearly_astrology_forecast'ı çağır
                    filepath = self.create_yearly_astrology_forecast()
                    print(f"📄 Dosya konumu: {filepath}")
                except ValueError:
                    print("❌ Geçerli bir yıl girin")
                except Exception as e:
                    print(f"❌ Hata: {e}")

            elif choice == "5":
                files = [f for f in os.listdir(self.content_dir) if f.endswith('.md')]
                birth_charts = [f for f in files if 'dogum-haritasi' in f]
                compatibility = [f for f in files if 'uyumluluk' in f]
                weekly_reports = [f for f in files if 'haftalik-astroloji' in f]
                yearly_forecasts = [f for f in files if 'yillik-astroloji' in f]

                print(f"📊 Premium İçerik İstatistikleri:")
                print(f"🔮 Doğum Haritaları: {len(birth_charts)} adet")
                print(f"💕 Uyumluluk Analizleri: {len(compatibility)} adet")
                print(f"📅 Haftalık Raporlar: {len(weekly_reports)} adet")
                print(f"🎯 Yıllık Tahminler: {len(yearly_forecasts)} adet")
                print(f"📄 Toplam Premium İçerik: {len(birth_charts) + len(compatibility) + len(weekly_reports) + len(yearly_forecasts)} adet")

            elif choice == "8":
                print("👋 Premium araçlar v2.0 kapatılıyor...")
                break

            else:
                print("❌ Geçersiz seçim (1-8 arası seçin)")

def main():
    """Ana fonksiyon"""
    tools = PremiumAstrologyToolsV2()
    tools.run_interactive_mode()

if __name__ == "__main__":
    main()
