#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Otomatik Premium İçerik Oluşturucu
"""

from premium_astrology_tools import PremiumAstrologyTools
import random

def create_premium_demos():
    """Otomatik demo içerikler oluştur"""
    tools = PremiumAstrologyTools()

    print("🌟 Otomatik Premium İçerik Oluşturuluyor...")
    print("=" * 50)

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

        content_data = tools.create_birth_chart_content(name, sign_key, birth_details)
        filepath = tools.create_content_file(content_data)
        created_files.append(filepath)
        print(f"✅ {name} ({tools.zodiac_data[sign_key]['name']}) doğum haritası oluşturuldu")

    # 5 uyumluluk analizi oluştur
    print("\n💕 Uyumluluk Analizleri Oluşturuluyor...")
    for i in range(5):
        sign1_key = random.choice(signs)
        sign2_key = random.choice(signs)

        content_data = tools.create_compatibility_analysis(sign1_key, sign2_key)
        filepath = tools.create_content_file(content_data)
        created_files.append(filepath)
        print(f"✅ {tools.zodiac_data[sign1_key]['name']} - {tools.zodiac_data[sign2_key]['name']} uyumluluk analizi (%{content_data['score']})")

    print(f"\n🎉 Toplam {len(created_files)} premium içerik oluşturuldu!")

    return created_files

if __name__ == "__main__":
    create_premium_demos()
