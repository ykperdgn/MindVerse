#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Otomatik Premium İçerik Oluşturucu v2.0
Premium Özellik 4 ve 5 dahil
"""

from premium_astrology_tools_v2 import PremiumAstrologyToolsV2
import random

def create_premium_demos():
    """Otomatik demo içerikler oluştur (v3 logic, compatible with PremiumAstrologyToolsV2)"""
    tools = PremiumAstrologyToolsV2()

    print("🌟 Otomatik Premium İçerik Oluşturucu v2.1 (Patched)")
    print("=" * 60)

    demo_names = ["Ahmet", "Ayşe", "Mehmet", "Fatma", "Ali", "Zeynep", "Can", "Elif", "Murat", "Selin"]
    signs = list(tools.zodiac_data.keys())
    created_files = []

    # 5 doğum haritası oluştur
    print("\n🔮 Doğum Haritaları Oluşturuluyor...")
    for i in range(5):
        name = random.choice(demo_names)
        sign_key = random.choice(signs)
        birth_details = {"demo": True}
        content_data = {
            'content': f"""---\ntitle: \"{name} İçin Detaylı Doğum Haritası Analizi\"\ndescription: \"{name} için kişiselleştirilmiş doğum haritası analizi.\"\npubDate: 2025-06-20\ncategory: \"astrology\"\ntags: [\"doğum haritası\", \"{tools.zodiac_data[sign_key]['name'].lower()}\", \"demo\"]\nheroImage: \"/images/birth-chart.jpg\"\ntype: \"birth-chart\"\nfeatured: true\n---\n\n# 🔮 {name} İçin Detaylı Doğum Haritası Analizi\n\nBu analiz {tools.zodiac_data[sign_key]['name']} burcu için hazırlanmıştır.\n\n## Temel Burç Bilgileri\n- **Burç:** {tools.zodiac_data[sign_key]['name']} {tools.zodiac_data[sign_key]['symbol']}\n- **Element:** {tools.zodiac_data[sign_key]['element']}\n- **Kalite:** {tools.zodiac_data[sign_key]['quality']}\n- **Yönetici Gezegen:** {tools.zodiac_data[sign_key]['ruling_planet']}\n\nDemo içerik oluşturuldu.\n""",
            'slug': f"dogum-haritasi-{name.lower()}-{sign_key}-demo-{i+1}"
        }
        filepath = tools.create_content_file(content_data)
        created_files.append(filepath)
        print(f"  ✅ {name} ({tools.zodiac_data[sign_key]['name']}) doğum haritası oluşturuldu")

    # 5 uyumluluk analizi oluştur
    print("\n💕 Uyumluluk Analizleri Oluşturuluyor...")
    for i in range(5):
        sign1_key = random.choice(signs)
        sign2_key = random.choice(signs)
        score = random.randint(60, 95)
        content_data = {
            'content': f"""---\ntitle: \"{tools.zodiac_data[sign1_key]['name']} - {tools.zodiac_data[sign2_key]['name']} Uyumluluk Analizi\"\ndescription: \"{tools.zodiac_data[sign1_key]['name']} ve {tools.zodiac_data[sign2_key]['name']} burçları arasındaki uyumluluk analizi.\"\npubDate: 2025-06-20\ncategory: \"astrology\"\ntags: [\"uyumluluk\", \"{tools.zodiac_data[sign1_key]['name'].lower()}\", \"{tools.zodiac_data[sign2_key]['name'].lower()}\"]\nheroImage: \"/images/compatibility.jpg\"\ntype: \"compatibility\"\nfeatured: true\n---\n\n# 💕 {tools.zodiac_data[sign1_key]['name']} - {tools.zodiac_data[sign2_key]['name']} Uyumluluk Analizi\n\n## Genel Uyumluluk Skoru: %{score}\n\nBu analiz {tools.zodiac_data[sign1_key]['name']} ve {tools.zodiac_data[sign2_key]['name']} burçları arasındaki uyumluluğu incelemektedir.\n\n## Burç Özellikleri\n\n### {tools.zodiac_data[sign1_key]['symbol']} {tools.zodiac_data[sign1_key]['name']}\n- Element: {tools.zodiac_data[sign1_key]['element']}\n- Kalite: {tools.zodiac_data[sign1_key]['quality']}\n- Yönetici: {tools.zodiac_data[sign1_key]['ruling_planet']}\n\n### {tools.zodiac_data[sign2_key]['symbol']} {tools.zodiac_data[sign2_key]['name']}\n- Element: {tools.zodiac_data[sign2_key]['element']}\n- Kalite: {tools.zodiac_data[sign2_key]['quality']}\n- Yönetici: {tools.zodiac_data[sign2_key]['ruling_planet']}\n\nDemo uyumluluk analizi oluşturuldu.\n""",
            'slug': f"uyumluluk-{sign1_key}-{sign2_key}-demo-{i+1}"
        }
        filepath = tools.create_content_file(content_data)
        created_files.append(filepath)
        print(f"  ✅ {tools.zodiac_data[sign1_key]['name']} - {tools.zodiac_data[sign2_key]['name']} (%{score})")

    # 3 haftalık rapor oluştur (v2.0 özelliği)
    print("\n📅 Haftalık Astroloji Raporları Oluşturuluyor...")
    for i in range(3):
        filepath = tools.create_weekly_astrology_report()
        created_files.append(filepath)
        print(f"  ✅ Haftalık astroloji raporu oluşturuldu")

    # 2 yıllık tahmin oluştur (v2.0 özelliği)
    print("\n🎯 Yıllık Astroloji Tahminleri Oluşturuluyor...")
    for year in [2026, 2027]:
        filepath = tools.create_yearly_astrology_forecast()
        created_files.append(filepath)
        print(f"  ✅ {year} yılı astroloji tahmini oluşturuldu")

    print(f"\n🎉 Toplam {len(created_files)} premium içerik oluşturuldu!")
    print("\n📊 İçerik Dağılımı:")
    print(f"🔮 Doğum Haritaları: 5 adet")
    print(f"💕 Uyumluluk Analizleri: 5 adet")
    print(f"📅 Haftalık Raporlar: 3 adet")
    print(f"🎯 Yıllık Tahminler: 2 adet")

    return created_files

if __name__ == "__main__":
    create_premium_demos()
