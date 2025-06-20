#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Otomatik Premium İçerik Oluşturucu v3.0
Tüm premium özellikler dahil
"""

from premium_astrology_tools_v2 import PremiumAstrologyToolsV2
import random

def create_premium_demos():
    """Otomatik demo içerikler oluştur"""
    tools = PremiumAstrologyToolsV2()

    print("🌟 Otomatik Premium İçerik Oluşturucu v3.0")
    print("=" * 60)

    # Demo isimleri
    demo_names = ["Ahmet", "Ayşe", "Mehmet", "Fatma", "Ali", "Zeynep", "Can", "Elif", "Murat", "Selin"]
    signs = list(tools.zodiac_data.keys())

    created_files = []

    # 5 doğum haritası oluştur
    print("\n🔮 Doğum Haritaları Oluşturuluyor...")
    for i in range(5):
        name = random.choice(demo_names)
        sign_key = random.choice(signs)
        birth_details = {"demo": True}

        # Demo doğum haritası için basit create fonksiyonu
        content_data = {
            'content': f"""---
title: "{name} İçin Detaylı Doğum Haritası Analizi"
description: "{name} için kişiselleştirilmiş doğum haritası analizi."
pubDate: 2025-06-20
category: "astrology"
tags: ["doğum haritası", "{tools.zodiac_data[sign_key]['name'].lower()}", "demo"]
heroImage: "/images/birth-chart.jpg"
type: "birth-chart"
featured: true
---

# 🔮 {name} İçin Detaylı Doğum Haritası Analizi

Bu analiz {tools.zodiac_data[sign_key]['name']} burcu için hazırlanmıştır.

## Temel Burç Bilgileri
- **Burç:** {tools.zodiac_data[sign_key]['name']} {tools.zodiac_data[sign_key]['symbol']}
- **Element:** {tools.zodiac_data[sign_key]['element']}
- **Kalite:** {tools.zodiac_data[sign_key]['quality']}
- **Yönetici Gezegen:** {tools.zodiac_data[sign_key]['ruling_planet']}

Demo içerik oluşturuldu.
""",
            'slug': f"dogum-haritasi-{name.lower()}-{sign_key}-demo-{i+1}"
        }

        filepath = tools.create_content_file(content_data)
        created_files.append(filepath)
        print(f"  ✅ {name} ({tools.zodiac_data[sign_key]['name']}) doğum haritası oluşturuldu")

    # 3 uyumluluk analizi oluştur
    print("\n💕 Uyumluluk Analizleri Oluşturuluyor...")
    for i in range(3):
        sign1_key = random.choice(signs)
        sign2_key = random.choice(signs)

        score = random.randint(60, 95)
        content_data = {
            'content': f"""---
title: "{tools.zodiac_data[sign1_key]['name']} - {tools.zodiac_data[sign2_key]['name']} Uyumluluk Analizi"
description: "{tools.zodiac_data[sign1_key]['name']} ve {tools.zodiac_data[sign2_key]['name']} burçları arasındaki uyumluluk analizi."
pubDate: 2025-06-20
category: "astrology"
tags: ["uyumluluk", "{tools.zodiac_data[sign1_key]['name'].lower()}", "{tools.zodiac_data[sign2_key]['name'].lower()}"]
heroImage: "/images/compatibility.jpg"
type: "compatibility"
featured: true
---

# 💕 {tools.zodiac_data[sign1_key]['name']} - {tools.zodiac_data[sign2_key]['name']} Uyumluluk Analizi

## Genel Uyumluluk Skoru: %{score}

Bu analiz {tools.zodiac_data[sign1_key]['name']} ve {tools.zodiac_data[sign2_key]['name']} burçları arasındaki uyumluluğu incelemektedir.

## Burç Özellikleri

### {tools.zodiac_data[sign1_key]['symbol']} {tools.zodiac_data[sign1_key]['name']}
- Element: {tools.zodiac_data[sign1_key]['element']}
- Kalite: {tools.zodiac_data[sign1_key]['quality']}
- Yönetici: {tools.zodiac_data[sign1_key]['ruling_planet']}

### {tools.zodiac_data[sign2_key]['symbol']} {tools.zodiac_data[sign2_key]['name']}
- Element: {tools.zodiac_data[sign2_key]['element']}
- Kalite: {tools.zodiac_data[sign2_key]['quality']}
- Yönetici: {tools.zodiac_data[sign2_key]['ruling_planet']}

Demo uyumluluk analizi oluşturuldu.
""",
            'slug': f"uyumluluk-{sign1_key}-{sign2_key}-demo-{i+1}"
        }

        filepath = tools.create_content_file(content_data)
        created_files.append(filepath)
        print(f"  ✅ {tools.zodiac_data[sign1_key]['name']} - {tools.zodiac_data[sign2_key]['name']} (%{score})")

    # 2 haftalık rapor oluştur
    print("\n📅 Haftalık Raporlar Oluşturuluyor...")
    for i in range(2):
        filepath = tools.create_weekly_astrology_report()
        created_files.append(filepath)
        print(f"  ✅ Haftalık rapor #{i+1} oluşturuldu")

    # 1 yıllık tahmin oluştur
    print("\n🎯 Yıllık Tahmin Oluşturuluyor...")
    filepath = tools.create_yearly_astrology_forecast()
    created_files.append(filepath)
    print(f"  ✅ 2026 yılı tahmini oluşturuldu")

    print(f"\n🎉 Toplam {len(created_files)} premium içerik oluşturuldu!")
    print("\nOluşturulan içerikler:")
    for file in created_files:
        print(f"  📄 {file}")

    return created_files

if __name__ == "__main__":
    create_premium_demos()
