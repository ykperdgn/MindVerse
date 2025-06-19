#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quick Content Analysis and Gap Filling
"""

from astrology_content_manager import AstrologyContentManager

def quick_analysis_and_fill():
    """Quick content analysis and gap filling."""
    manager = AstrologyContentManager()

    print("🔍 Hızlı İçerik Analizi Başlıyor...")
    print("=" * 50)

    # Analiz raporu
    report = manager.generate_content_report()

    print(f"\n📊 MEVCUT DURUM:")
    print(f"📁 Toplam astroloji dosyası: {report['total_files']}")
    print(f"📈 Günlük kapsam: {report['coverage_percentage']['daily']:.1f}%")
    print(f"📈 Haftalık kapsam: {report['coverage_percentage']['weekly']:.1f}%")
    print(f"📈 Aylık kapsam: {report['coverage_percentage']['monthly']:.1f}%")

    print(f"\n💡 DURUM DEĞERLENDİRMESİ:")
    for rec in report['recommendations']:
        print(f"  {rec}")

    # Eksik içerikleri tamamla
    if len(report['content_gaps']['missing_daily']) > 0 or \
       len(report['content_gaps']['missing_weekly']) > 0 or \
       len(report['content_gaps']['missing_monthly']) > 0:

        print(f"\n🔧 Eksik içerikler tamamlanıyor...")
        created_files = manager.generate_missing_content(8)
        print(f"✅ {len(created_files)} eksik içerik oluşturuldu!")

        # Yeni analiz
        new_report = manager.generate_content_report()
        print(f"\n📊 GÜNCEL DURUM:")
        print(f"📁 Toplam astroloji dosyası: {new_report['total_files']}")
        print(f"📈 Günlük kapsam: {new_report['coverage_percentage']['daily']:.1f}%")
        print(f"📈 Haftalık kapsam: {new_report['coverage_percentage']['weekly']:.1f}%")
        print(f"📈 Aylık kapsam: {new_report['coverage_percentage']['monthly']:.1f}%")
    else:
        print(f"\n✅ Tüm temel içerikler mevcut!")

        # Özel içerik oluştur
        print(f"\n💫 Özel içerikler ekleniyor...")
        love_files = manager.create_specialized_content("love_special")
        career_files = manager.create_specialized_content("career_boost")

        total_special = len(love_files) + len(career_files)
        print(f"✅ {total_special} özel içerik oluşturuldu!")
        print(f"   💖 {len(love_files)} aşk temalı")
        print(f"   💼 {len(career_files)} kariyer temalı")

if __name__ == "__main__":
    quick_analysis_and_fill()
