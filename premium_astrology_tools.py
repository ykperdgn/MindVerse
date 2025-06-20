#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌟 Premium Astroloji Araçları - Doğum Haritası & Uyumluluk
MindVerse Daily için gelişmiş premium özellikler
"""

import random
import json
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import os

class PremiumAstrologyTools:
    def __init__(self):
        self.content_dir = "src/content/astrology"
        os.makedirs(self.content_dir, exist_ok=True)

        # Gelişmiş burç bilgileri
        self.zodiac_data = {
            "koc": {"name": "Koç", "english": "Aries", "symbol": "♈", "element": "Ateş", "quality": "Öncü", "ruling_planet": "Mars"},
            "boga": {"name": "Boğa", "english": "Taurus", "symbol": "♉", "element": "Toprak", "quality": "Sabit", "ruling_planet": "Venüs"},
            "ikizler": {"name": "İkizler", "english": "Gemini", "symbol": "♊", "element": "Hava", "quality": "Değişken", "ruling_planet": "Merkür"},
            "yengec": {"name": "Yengeç", "english": "Cancer", "symbol": "♋", "element": "Su", "quality": "Öncü", "ruling_planet": "Ay"},
            "aslan": {"name": "Aslan", "english": "Leo", "symbol": "♌", "element": "Ateş", "quality": "Sabit", "ruling_planet": "Güneş"},
            "basak": {"name": "Başak", "english": "Virgo", "symbol": "♍", "element": "Toprak", "quality": "Değişken", "ruling_planet": "Merkür"},
            "terazi": {"name": "Terazi", "english": "Libra", "symbol": "♎", "element": "Hava", "quality": "Öncü", "ruling_planet": "Venüs"},
            "akrep": {"name": "Akrep", "english": "Scorpio", "symbol": "♏", "element": "Su", "quality": "Sabit", "ruling_planet": "Plüton"},
            "yay": {"name": "Yay", "english": "Sagittarius", "symbol": "♐", "element": "Ateş", "quality": "Değişken", "ruling_planet": "Jüpiter"},
            "oglak": {"name": "Oğlak", "english": "Capricorn", "symbol": "♑", "element": "Toprak", "quality": "Öncü", "ruling_planet": "Satürn"},
            "kova": {"name": "Kova", "english": "Aquarius", "symbol": "♒", "element": "Hava", "quality": "Sabit", "ruling_planet": "Uranüs"},
            "balik": {"name": "Balık", "english": "Pisces", "symbol": "♓", "element": "Su", "quality": "Değişken", "ruling_planet": "Neptün"}
        }

    def create_birth_chart_content(self, name: str, sign_key: str, birth_details: Dict) -> Dict[str, str]:
        """Detaylı doğum haritası içeriği oluştur"""
        sign_data = self.zodiac_data[sign_key]
        date_str = datetime.now().strftime("%Y-%m-%d")

        title = f"{name} İçin Detaylı Doğum Haritası Analizi"

        content = f"""---
title: "{title}"
description: "{name} için kişiselleştirilmiş doğum haritası analizi ve astrolojik rehberlik."
pubDate: {date_str}
category: "astrology"
tags: ["doğum haritası", "{sign_data['name'].lower()}", "kişisel analiz", "astroloji"]
heroImage: "/images/birth-chart.jpg"
type: "birth-chart"
featured: true
---

# {title}

## 🌟 Kişisel Bilgiler

**👤 İsim:** {name}
**🌅 Ana Burç:** {sign_data['symbol']} {sign_data['name']}
**🌍 Element:** {sign_data['element']}
**⚡ Kalite:** {sign_data['quality']}
**🪐 Yönetici Gezegen:** {sign_data['ruling_planet']}

---

## 🔮 Detaylı Doğum Haritası Analizi

### Ana Kişilik Yapısı

{sign_data['symbol']} **{sign_data['name']} burcu** olarak doğmuş olan {name}, doğal olarak {self._get_personality_traits(sign_data)} özelliklere sahiptir. {sign_data['element']} elementi, yaşama bakış açınızı ve enerji akışınızı belirleyen temel faktördür.

### 🏠 Astrolojik Ev Analizleri

#### 1. Ev - Kişilik ve Kimlik
**{sign_data['ruling_planet']} Etkisi:** {self._get_house_analysis(1, sign_data)}

#### 2. Ev - Değerler ve Kaynaklar
**Mali Durum:** {self._get_house_analysis(2, sign_data)}

#### 7. Ev - İlişkiler ve Partnerlik
**Aşk Hayatı:** {self._get_house_analysis(7, sign_data)}

#### 10. Ev - Kariyer ve Toplumsal Statü
**Meslek Hayatı:** {self._get_house_analysis(10, sign_data)}

### 🌙 Ay Etkisi ve Duygusal Yapı

{self._get_moon_analysis(sign_data)}

### ⭐ Yükselen Burç Etkisi

{self._get_rising_sign_analysis(sign_data)}

### 🪐 Gezegen Pozisyonları

{self._get_planetary_positions(sign_data)}

## 💫 Yaşam Rehberi

### Güçlü Yönleriniz
{self._get_strengths_analysis(sign_data)}

### Gelişim Alanlarınız
{self._get_development_areas(sign_data)}

### Kariyer Tavsiyeleri
{self._get_career_guidance(sign_data)}

### İlişki Rehberi
{self._get_relationship_guidance(sign_data)}

## 🎯 2025 Yılı Özel Tahminleri

### Bu Yıl Sizin İçin Özel
{self._get_yearly_predictions(sign_data)}

### Önemli Tarihler
{self._get_important_dates(sign_data)}

## 🔮 Sonuç ve Öneriler

{name}, doğum haritanız sizin benzersiz potansiyelinizi gösteriyor. {sign_data['name']} burcu olarak sahip olduğunuz {sign_data['element'].lower()} elementi enerjisi, yaşamınızda güçlü bir rehber olacak.

**En Önemli Tavsiyeler:**
- {sign_data['ruling_planet']} gezeninizin enerjisini pozitif yönde kullanın
- {sign_data['element']} elementi özelliklerinizi geliştirin
- Doğal {sign_data['quality'].lower()} kalitenizi avantaja çevirin

---

*Bu analiz {name} için özel olarak hazırlanmış kişiselleştirilmiş bir doğum haritası yorumudur.*

**📞 Kişisel Danışmanlık:** Daha detaylı analiz için iletişime geçebilirsiniz.
"""

        slug = f"dogum-haritasi-{name.lower().replace(' ', '-')}-{sign_key}-{date_str}"

        return {
            "title": title,
            "content": content,
            "slug": slug,
            "type": "birth-chart",
            "name": name,
            "sign": sign_key
        }

    def create_compatibility_analysis(self, sign1_key: str, sign2_key: str) -> Dict[str, str]:
        """Burç uyumluluk analizi oluştur"""
        sign1_data = self.zodiac_data[sign1_key]
        sign2_data = self.zodiac_data[sign2_key]
        date_str = datetime.now().strftime("%Y-%m-%d")

        title = f"{sign1_data['name']} - {sign2_data['name']} Burç Uyumluluk Analizi"

        # Uyumluluk skorunu hesapla
        compatibility_score = self._calculate_compatibility(sign1_data, sign2_data)

        content = f"""---
title: "{title}"
description: "{sign1_data['name']} ve {sign2_data['name']} burçları arasında detaylı uyumluluk analizi."
pubDate: {date_str}
category: "astrology"
tags: ["uyumluluk", "{sign1_data['name'].lower()}", "{sign2_data['name'].lower()}", "ilişki", "astroloji"]
heroImage: "/images/compatibility.jpg"
type: "compatibility"
featured: true
compatibilityScore: {compatibility_score}
---

# {title}

## 💕 Genel Uyumluluk Skoru: {compatibility_score}%

{sign1_data['symbol']} **{sign1_data['name']}** + {sign2_data['symbol']} **{sign2_data['name']}**

---

## 🔍 Uyumluluk Analizi

### Element Uyumluluğu
**{sign1_data['name']} ({sign1_data['element']}) - {sign2_data['name']} ({sign2_data['element']})**

{self._get_element_compatibility(sign1_data, sign2_data)}

### Kalite Uyumluluğu
**{sign1_data['quality']} - {sign2_data['quality']}**

{self._get_quality_compatibility(sign1_data, sign2_data)}

### Gezegen Uyumluluğu
**{sign1_data['ruling_planet']} - {sign2_data['ruling_planet']}**

{self._get_planetary_compatibility(sign1_data, sign2_data)}

## 💖 İlişki Dinamikleri

### Aşk ve Romantizm
{self._get_love_compatibility(sign1_data, sign2_data)}

### İletişim Tarzı
{self._get_communication_style(sign1_data, sign2_data)}

### Çatışma Çözümü
{self._get_conflict_resolution(sign1_data, sign2_data)}

### Uzun Vadeli Uyum
{self._get_long_term_compatibility(sign1_data, sign2_data)}

## 🎯 İlişki Tavsiyeleri

### {sign1_data['name']} İçin Öneriler
{self._get_advice_for_sign(sign1_data, sign2_data)}

### {sign2_data['name']} İçin Öneriler
{self._get_advice_for_sign(sign2_data, sign1_data)}

### Ortak Aktivite Önerileri
{self._get_shared_activities(sign1_data, sign2_data)}

## 📊 Detaylı Uyumluluk Skorları

| Alan | Skor | Açıklama |
|------|------|----------|
| **Duygusal Bağ** | {random.randint(70, 95)}% | {self._get_emotional_score_desc()} |
| **İletişim** | {random.randint(65, 90)}% | {self._get_communication_score_desc()} |
| **Fiziksel Uyum** | {random.randint(75, 95)}% | {self._get_physical_score_desc()} |
| **Yaşam Tarzı** | {random.randint(60, 85)}% | {self._get_lifestyle_score_desc()} |
| **Değerler** | {random.randint(70, 90)}% | {self._get_values_score_desc()} |

## 🌟 Özel Tavsiyeler

### Güçlü Yönleriniz
{self._get_relationship_strengths(sign1_data, sign2_data)}

### Dikkat Edilmesi Gerekenler
{self._get_relationship_challenges(sign1_data, sign2_data)}

### İlişkiyi Güçlendirme Yolları
{self._get_relationship_enhancement(sign1_data, sign2_data)}

## 🔮 Sonuç

{sign1_data['name']} ve {sign2_data['name']} burçları arasındaki uyumluluk %{compatibility_score} olarak değerlendirilmektedir. Bu {self._get_compatibility_level(compatibility_score)} bir uyumluluk seviyesini göstermektedir.

**Önemli Hatırlatma:** Astroloji bir rehberdir, gerçek ilişki uyumunuz kişisel çabanıza, anlayışınıza ve sevginize bağlıdır.

---

*Bu analiz {sign1_data['name']} ve {sign2_data['name']} burçları için özel olarak hazırlanmıştır.*

**💕 İlişki Danışmanlığı:** Daha detaylı analiz için uzman desteği alabilirsiniz.
"""

        slug = f"uyumluluk-{sign1_key}-{sign2_key}-analizi-{date_str}"

        return {
            "title": title,
            "content": content,
            "slug": slug,
            "type": "compatibility",
            "sign1": sign1_key,
            "sign2": sign2_key,
            "score": compatibility_score
        }

    def _get_personality_traits(self, sign_data: Dict) -> str:
        """Kişilik özelliklerini getir"""
        traits = {
            "Ateş": "enerjik, girişken ve liderlik",
            "Toprak": "pratik, güvenilir ve kararlı",
            "Hava": "zeki, sosyal ve iletişimci",
            "Su": "duygusal, sezgisel ve empatik"
        }
        return traits.get(sign_data['element'], "güçlü")

    def _get_house_analysis(self, house_num: int, sign_data: Dict) -> str:
        """Ev analizlerini getir"""
        analyses = {
            1: f"{sign_data['ruling_planet']} etkisiyle güçlü bir kişiliğe sahipsiniz.",
            2: f"{sign_data['element']} elementi mali konularda size rehberlik eder.",
            7: f"İlişkilerde {sign_data['quality'].lower()} yaklaşımınız dikkat çeker.",
            10: f"Kariyerinizde {sign_data['ruling_planet']} enerjisi öne çıkar."
        }
        return analyses.get(house_num, "Pozitif enerji hakimdir.")

    def _get_moon_analysis(self, sign_data: Dict) -> str:
        """Ay analizi"""
        return f"Duygusal dünyanızda {sign_data['element'].lower()} elementi hakimdir. Bu size {random.choice(['içsel huzur', 'güçlü sezgiler', 'dengeli duygular'])} kazandırır."

    def _get_rising_sign_analysis(self, sign_data: Dict) -> str:
        """Yükselen burç analizi"""
        return f"Dış dünyadaki imajınız {sign_data['name']} enerjisiyle şekillenir. İlk izlenim olarak {random.choice(['güçlü', 'karizmatik', 'çekici', 'etkileyici'])} görünürsünüz."

    def _get_planetary_positions(self, sign_data: Dict) -> str:
        """Gezegen pozisyonları"""
        return f"**{sign_data['ruling_planet']}** ana yönetici gezegininiz olarak hayatınızda {random.choice(['güç', 'denge', 'yaratıcılık', 'ilham'])} sağlar."

    def _get_strengths_analysis(self, sign_data: Dict) -> str:
        """Güçlü yönler analizi"""
        strengths = [
            f"Doğal {sign_data['element'].lower()} elementi gücü",
            f"{sign_data['quality']} kalitesinden gelen kararlılık",
            f"{sign_data['ruling_planet']} enerjisinin desteği"
        ]
        return "• " + "\n• ".join(strengths)

    def _get_development_areas(self, sign_data: Dict) -> str:
        """Gelişim alanları"""
        areas = [
            f"{sign_data['element']} elementinin dengelenmesi",
            "Sabır ve empati geliştirme",
            "İletişim becerilerini güçlendirme"
        ]
        return "• " + "\n• ".join(areas)

    def _get_career_guidance(self, sign_data: Dict) -> str:
        """Kariyer rehberi"""
        guidance = {
            "Mars": "Liderlik gerektiren pozisyonlarda başarılısınız",
            "Venüs": "Sanat, güzellik ve diplomasi alanları size uygun",
            "Merkür": "İletişim, teknoloji ve eğitim alanlarında yeteneklisiniz",
            "Jüpiter": "Eğitim, hukuk ve uluslararası işler size uygun",
            "Satürn": "Yöneticilik, mühendislik ve yapısal işlerde başarılısınız",
            "Uranüs": "Teknoloji, yenilikçilik ve araştırma alanlarında başarılısınız",
            "Neptün": "Sanat, müzik ve spiritüel alanlarda yeteneklisiniz",
            "Plüton": "Dönüşüm, araştırma ve psikoloji alanlarında güçlüsünüz"
        }
        return guidance.get(sign_data['ruling_planet'], "Çok yönlü yetenekleriniz vardır")

    def _get_relationship_guidance(self, sign_data: Dict) -> str:
        """İlişki rehberi"""
        return f"{sign_data['element']} elementi size ilişkilerde {random.choice(['tutku', 'denge', 'anlayış', 'sadakat'])} getirir."

    def _get_yearly_predictions(self, sign_data: Dict) -> str:
        """Yıllık tahminler"""
        return f"2025 yılı {sign_data['name']} burcu için {random.choice(['büyüme', 'dönüşüm', 'başarı', 'yenilik'])} yılı olacak."

    def _get_important_dates(self, sign_data: Dict) -> str:
        """Önemli tarihler"""
        months = ["Mart", "Haziran", "Eylül", "Aralık"]
        return f"• {random.choice(months)} ayı: Önemli kararlar\n• {random.choice(months)} ayı: Yeni fırsatlar"

    def _calculate_compatibility(self, sign1: Dict, sign2: Dict) -> int:
        """Uyumluluk skoru hesapla"""
        base_score = 70

        # Element uyumluluğu
        if sign1['element'] == sign2['element']:
            base_score += 10
        elif self._elements_compatible(sign1['element'], sign2['element']):
            base_score += 5

        # Kalite uyumluluğu
        if sign1['quality'] != sign2['quality']:
            base_score += 5

        return min(95, base_score + random.randint(-5, 15))

    def _elements_compatible(self, elem1: str, elem2: str) -> bool:
        """Element uyumluluğu kontrol et"""
        compatible_pairs = [
            ("Ateş", "Hava"), ("Toprak", "Su"),
            ("Ateş", "Toprak"), ("Hava", "Su")
        ]
        return (elem1, elem2) in compatible_pairs or (elem2, elem1) in compatible_pairs

    def _get_element_compatibility(self, sign1: Dict, sign2: Dict) -> str:
        """Element uyumluluğu açıklaması"""
        if sign1['element'] == sign2['element']:
            return f"Aynı {sign1['element'].lower()} elementinden gelmeniz ortak anlayış yaratır."
        else:
            return f"{sign1['element']} ve {sign2['element']} elementleri tamamlayıcı enerji yaratır."

    def _get_quality_compatibility(self, sign1: Dict, sign2: Dict) -> str:
        """Kalite uyumluluğu"""
        return f"{sign1['quality']} ve {sign2['quality']} kaliteler dinamik bir denge oluşturur."

    def _get_planetary_compatibility(self, sign1: Dict, sign2: Dict) -> str:
        """Gezegen uyumluluğu"""
        return f"{sign1['ruling_planet']} ve {sign2['ruling_planet']} enerjileri güçlü bir kombinasyon yaratır."

    def _get_love_compatibility(self, sign1: Dict, sign2: Dict) -> str:
        """Aşk uyumluluğu"""
        return f"Romantik ilişkinizde {sign1['element'].lower()} ve {sign2['element'].lower()} enerjileri güzel bir uyum yaratır."

    def _get_communication_style(self, sign1: Dict, sign2: Dict) -> str:
        """İletişim tarzı"""
        return f"İletişimde {sign1['quality'].lower()} ve {sign2['quality'].lower()} yaklaşımlarınız dengeleyici etki yapar."

    def _get_conflict_resolution(self, sign1: Dict, sign2: Dict) -> str:
        """Çatışma çözümü"""
        return "Anlaşmazlıklarda empati ve sabırla hareket etmeniz çözüm getirir."

    def _get_long_term_compatibility(self, sign1: Dict, sign2: Dict) -> str:
        """Uzun vadeli uyum"""
        return "Uzun vadede birbirinizi tamamlayıcı enerjileriniz sayesinde güçlü bir bağ kurabilirsiniz."

    def _get_advice_for_sign(self, target_sign: Dict, partner_sign: Dict) -> str:
        """Burç için tavsiyeler"""
        return f"• Partnerinizin {partner_sign['element'].lower()} elementini anlayın\n• {target_sign['ruling_planet']} enerjinizi pozitif kullanın"

    def _get_shared_activities(self, sign1: Dict, sign2: Dict) -> str:
        """Ortak aktiviteler"""
        activities = ["Doğa yürüyüşleri", "Sanat etkinlikleri", "Seyahat planları", "Spor aktiviteleri"]
        return f"• {random.choice(activities)}\n• {random.choice(activities)}"

    def _get_emotional_score_desc(self) -> str:
        return random.choice(["Güçlü duygusal bağ", "Derin anlayış", "Empatik bağlantı"])

    def _get_communication_score_desc(self) -> str:
        return random.choice(["Açık iletişim", "Ortak dil", "Anlayışlı dialog"])

    def _get_physical_score_desc(self) -> str:
        return random.choice(["Güçlü çekim", "Uyumlu enerji", "Fiziksel uyum"])

    def _get_lifestyle_score_desc(self) -> str:
        return random.choice(["Benzer tercihler", "Tamamlayıcı yaşam tarzı", "Ortak hedefler"])

    def _get_values_score_desc(self) -> str:
        return random.choice(["Ortak değerler", "Benzer öncelikler", "Uyumlu idealler"])

    def _get_relationship_strengths(self, sign1: Dict, sign2: Dict) -> str:
        return f"• {sign1['element']} - {sign2['element']} elementi uyumu\n• Güçlü karşılıklı anlayış"

    def _get_relationship_challenges(self, sign1: Dict, sign2: Dict) -> str:
        return "• Farklılıklarınızı anlamaya çalışın\n• Sabırlı olun ve empati gösterin"

    def _get_relationship_enhancement(self, sign1: Dict, sign2: Dict) -> str:
        return "• Birlikte kaliteli zaman geçirin\n• Açık ve dürüst iletişim kurun"

    def _get_compatibility_level(self, score: int) -> str:
        if score >= 85:
            return "mükemmel"
        elif score >= 75:
            return "çok iyi"
        elif score >= 65:
            return "iyi"
        else:
            return "orta"

    def create_content_file(self, content_data: Dict[str, str]) -> str:
        """İçeriği dosyaya kaydet"""
        filename = f"{content_data['slug']}.md"
        filepath = os.path.join(self.content_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content_data['content'])

        return filepath

    def run_interactive_mode(self):
        """İnteraktif mod"""
        print("🌟 Premium Astroloji Araçları")
        print("=" * 50)

        while True:            print("\nPremium Özellikler:")
            print("1. Kişiselleştirilmiş Doğum Haritası")
            print("2. Burç Uyumluluk Analizi")
            print("3. Rastgele doğum haritası oluştur (demo)")
            print("4. Rastgele uyumluluk analizi oluştur (demo)")
            print("5. Premium içerik istatistikleri")
            print("6. Haftalık Astroloji Raporu")
            print("7. Yıllık Astroloji Tahmini")
            print("8. Çıkış")

            choice = input("\nSeçiminiz (1-8): ").strip()

            if choice == "1":
                name = input("İsim: ").strip()
                print("\nBurç seçimi:")
                for i, (key, data) in enumerate(self.zodiac_data.items(), 1):
                    print(f"{i:2d}. {data['name']}")

                try:
                    sign_choice = int(input("\nBurç numarası (1-12): ")) - 1
                    signs = list(self.zodiac_data.keys())
                    if 0 <= sign_choice < len(signs) and name:
                        sign_key = signs[sign_choice]
                        birth_details = {"demo": True}  # Demo için
                        content_data = self.create_birth_chart_content(name, sign_key, birth_details)
                        filepath = self.create_content_file(content_data)
                        print(f"✅ {name} için doğum haritası oluşturuldu: {filepath}")
                    else:
                        print("❌ Geçersiz bilgiler")
                except ValueError:
                    print("❌ Geçerli bir sayı girin")

            elif choice == "2":
                print("\nİlk burç seçimi:")
                for i, (key, data) in enumerate(self.zodiac_data.items(), 1):
                    print(f"{i:2d}. {data['name']}")

                try:
                    sign1_choice = int(input("\nİlk burç (1-12): ")) - 1
                    sign2_choice = int(input("İkinci burç (1-12): ")) - 1
                    signs = list(self.zodiac_data.keys())

                    if 0 <= sign1_choice < len(signs) and 0 <= sign2_choice < len(signs):
                        sign1_key = signs[sign1_choice]
                        sign2_key = signs[sign2_choice]
                        content_data = self.create_compatibility_analysis(sign1_key, sign2_key)
                        filepath = self.create_content_file(content_data)
                        print(f"✅ {self.zodiac_data[sign1_key]['name']} - {self.zodiac_data[sign2_key]['name']} uyumluluk analizi oluşturuldu")
                        print(f"📊 Uyumluluk skoru: %{content_data['score']}")
                    else:
                        print("❌ Geçersiz seçim")
                except ValueError:
                    print("❌ Geçerli sayılar girin")

            elif choice == "3":
                # Demo doğum haritası
                demo_names = ["Ahmet", "Ayşe", "Mehmet", "Fatma", "Ali", "Zeynep"]
                name = random.choice(demo_names)
                sign_key = random.choice(list(self.zodiac_data.keys()))
                birth_details = {"demo": True}
                content_data = self.create_birth_chart_content(name, sign_key, birth_details)
                filepath = self.create_content_file(content_data)
                print(f"✅ Demo doğum haritası oluşturuldu: {name} ({self.zodiac_data[sign_key]['name']})")

            elif choice == "4":
                # Demo uyumluluk analizi
                signs = list(self.zodiac_data.keys())
                sign1_key = random.choice(signs)
                sign2_key = random.choice(signs)
                content_data = self.create_compatibility_analysis(sign1_key, sign2_key)
                filepath = self.create_content_file(content_data)
                print(f"✅ Demo uyumluluk analizi: {self.zodiac_data[sign1_key]['name']} - {self.zodiac_data[sign2_key]['name']}")
                print(f"📊 Uyumluluk skoru: %{content_data['score']}")

            elif choice == "5":
                files = [f for f in os.listdir(self.content_dir) if f.endswith('.md')]
                birth_charts = [f for f in files if 'dogum-haritasi' in f]
                compatibility = [f for f in files if 'uyumluluk' in f]
                print(f"📊 Premium İçerik İstatistikleri:")
                print(f"🔮 Doğum Haritaları: {len(birth_charts)} adet")
                print(f"💕 Uyumluluk Analizleri: {len(compatibility)} adet")
                print(f"📄 Toplam Premium İçerik: {len(birth_charts) + len(compatibility)} adet")            elif choice == "6":
                # Premium Özellik 4: Haftalık Astroloji Raporu
                self.create_weekly_astrology_report()

            elif choice == "7":
                # Premium Özellik 5: Yıllık Astroloji Tahmini
                self.create_yearly_astrology_forecast()

            elif choice == "8":
                print("👋 Premium araçlar kapatılıyor...")
                break

            else:
                print("❌ Geçersiz seçim")

def main():
    """Ana fonksiyon"""
    tools = PremiumAstrologyTools()
    tools.run_interactive_mode()

if __name__ == "__main__":
    main()
