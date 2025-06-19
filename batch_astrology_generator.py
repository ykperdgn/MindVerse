#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Batch Astrology Content Generator - Automated bulk content creation
"""

from enhanced_astrology_generator import EnhancedAstrologyGenerator
import random

def generate_bulk_astrology_content():
    """Generate bulk astrology content automatically."""
    generator = EnhancedAstrologyGenerator()

    print("🔮 Otomatik Astroloji İçerik Üretimi Başlıyor...")
    print("=" * 50)

    # Generate 5 random articles
    created_files = []
    periods = ["günlük", "haftalık", "aylık"]

    for i in range(5):
        sign = generator.get_random_sign()
        period = random.choice(periods)

        print(f"\n📝 {i+1}/5 - {generator.zodiac_signs[sign]['name']} burcu {period} yorumu oluşturuluyor...")

        if period == "günlük":
            content_data = generator.generate_daily_content(sign)
        elif period == "haftalık":
            content_data = generator.generate_weekly_content(sign)
        else:
            content_data = generator.generate_monthly_content(sign)

        filepath = generator.create_content_file(content_data)
        created_files.append(filepath)
        print(f"✅ {content_data['title']} oluşturuldu")

    print(f"\n🎉 Toplam {len(created_files)} astroloji içeriği başarıyla oluşturuldu!")

    # Show created files
    print("\n📋 Oluşturulan Dosyalar:")
    for i, filepath in enumerate(created_files, 1):
        filename = filepath.split('\\')[-1]
        print(f"{i}. {filename}")

    return created_files

if __name__ == "__main__":
    generate_bulk_astrology_content()
