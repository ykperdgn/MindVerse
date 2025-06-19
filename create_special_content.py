#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Content Creator - Fixed version without syntax errors
"""

from enhanced_astrology_generator import EnhancedAstrologyGenerator
import random

def create_special_content():
    """Create special themed astrology content."""
    generator = EnhancedAstrologyGenerator()

    print("🌟 Özel İçerik Üretimi Başlıyor...")
    print("=" * 50)

    created_files = []

    # Aşk temalı özel içerikler
    print("\n💖 Aşk Temalı İçerikler Oluşturuluyor...")
    love_signs = ["boga", "yengec", "terazi", "balik"]
    love_themes = [
        "Aşkta Büyük Dönüşüm", "Kalp Fısıltıları",
        "Romantik Rüyalar", "Sonsuz Aşk Enerjisi"
    ]

    for sign in love_signs:
        theme = random.choice(love_themes)
        content_data = generator.generate_daily_content(sign)
        content_data["title"] = f"{theme} - {generator.zodiac_signs[sign]['name']} Burcu Özel Yorumu"

        # Dosya adını özelleştir
        date_str = content_data["slug"].split("-")[0:3]
        custom_slug = "-".join(date_str) + f"-{sign}-burcu-ask-özel-yorum"
        content_data["slug"] = custom_slug

        filepath = generator.create_content_file(content_data)
        created_files.append(filepath)
        print(f"✅ {generator.zodiac_signs[sign]['name']} aşk özel yorumu oluşturuldu")

    # Kariyer temalı özel içerikler
    print("\n💼 Kariyer Temalı İçerikler Oluşturuluyor...")
    career_signs = ["koc", "aslan", "basak", "oglak"]
    career_themes = [
        "Kariyer Zirvesi", "İş Hayatında Başarı",
        "Liderlik Enerjisi", "Mali Bolluk Dönemi"
    ]

    for sign in career_signs:
        theme = random.choice(career_themes)
        content_data = generator.generate_weekly_content(sign)
        content_data["title"] = f"{theme} - {generator.zodiac_signs[sign]['name']} Burcu Kariyer Rehberi"

        # Dosya adını özelleştir
        date_str = content_data["slug"].split("-")[0:3]
        custom_slug = "-".join(date_str) + f"-{sign}-burcu-kariyer-özel-yorum"
        content_data["slug"] = custom_slug

        filepath = generator.create_content_file(content_data)
        created_files.append(filepath)
        print(f"✅ {generator.zodiac_signs[sign]['name']} kariyer özel yorumu oluşturuldu")

    # Ruhsal gelişim temalı özel içerikler
    print("\n🧘 Ruhsal Gelişim Temalı İçerikler Oluşturuluyor...")
    spiritual_signs = ["yengec", "akrep", "balik", "yay"]
    spiritual_themes = [
        "Ruhsal Uyanış", "İç Huzur Yolculuğu",
        "Kozmik Enerji Akışı", "Sezgisel Güçlenme"
    ]

    for sign in spiritual_signs:
        theme = random.choice(spiritual_themes)
        content_data = generator.generate_monthly_content(sign)
        content_data["title"] = f"{theme} - {generator.zodiac_signs[sign]['name']} Burcu Ruhsal Rehberi"

        # Dosya adını özelleştir
        date_str = content_data["slug"].split("-")[0:3]
        custom_slug = "-".join(date_str) + f"-{sign}-burcu-ruhsal-özel-yorum"
        content_data["slug"] = custom_slug

        filepath = generator.create_content_file(content_data)
        created_files.append(filepath)
        print(f"✅ {generator.zodiac_signs[sign]['name']} ruhsal özel yorumu oluşturuldu")

    print(f"\n🎉 Toplam {len(created_files)} özel içerik oluşturuldu!")
    print(f"   💖 {len(love_signs)} aşk temalı")
    print(f"   💼 {len(career_signs)} kariyer temalı")
    print(f"   🧘 {len(spiritual_signs)} ruhsal temalı")

    return created_files

if __name__ == "__main__":
    create_special_content()
