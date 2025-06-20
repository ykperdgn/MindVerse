#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Astrology Content Manager - Fixed version
"""

import os
import json
import random
from datetime import datetime, timedelta
from typing import Dict, List

# Import with fallback
try:
    from enhanced_astrology_generator import EnhancedAstrologyGenerator
except ImportError:
    print("Enhanced generator not found, using basic...")
    from astrology_content_generator import AdvancedAstrologyGenerator as EnhancedAstrologyGenerator

class SimpleAstrologyManager:
    def __init__(self):
        self.generator = EnhancedAstrologyGenerator()
        self.content_dir = "src/content/astrology"

    def generate_missing_content(self, max_items: int = 10) -> List[str]:
        """Generate missing content for gaps"""
        created_files = []

        signs = list(self.generator.zodiac_signs.keys())
        content_types = ["daily", "weekly", "monthly"]

        for i in range(max_items):
            sign = random.choice(signs)
            content_type = random.choice(content_types)

            try:
                if content_type == "daily":
                    content_data = self.generator.generate_daily_content(sign)
                elif content_type == "weekly":
                    content_data = self.generator.generate_weekly_content(sign)
                else:
                    content_data = self.generator.generate_monthly_content(sign)

                filepath = self.generator.create_content_file(content_data)
                created_files.append(filepath)
                print(f"✅ {self.generator.zodiac_signs[sign]['name']} {content_type} content created")

            except Exception as e:
                print(f"❌ Error creating content for {sign}: {e}")
                continue

        return created_files

    def create_special_love_content(self) -> List[str]:
        """Create love-themed content"""
        created_files = []
        love_signs = ["boga", "yengec", "terazi", "balik"]

        for sign in love_signs:
            try:
                content_data = self.generator.generate_daily_content(sign)
                content_data["title"] = f"Aşk Enerjisi - {self.generator.zodiac_signs[sign]['name']} Burcu Özel Yorumu"

                filepath = self.generator.create_content_file(content_data)
                created_files.append(filepath)
                print(f"💖 {self.generator.zodiac_signs[sign]['name']} love content created")

            except Exception as e:
                print(f"❌ Error creating love content for {sign}: {e}")

        return created_files

    def create_career_content(self) -> List[str]:
        """Create career-themed content"""
        created_files = []
        career_signs = ["koc", "aslan", "basak", "oglak"]

        for sign in career_signs:
            try:
                content_data = self.generator.generate_weekly_content(sign)
                content_data["title"] = f"Kariyer Atılımı - {self.generator.zodiac_signs[sign]['name']} Burcu Özel Yorumu"

                filepath = self.generator.create_content_file(content_data)
                created_files.append(filepath)
                print(f"💼 {self.generator.zodiac_signs[sign]['name']} career content created")

            except Exception as e:
                print(f"❌ Error creating career content for {sign}: {e}")

        return created_files

    def run_interface(self):
        """Run simple interface"""
        print("🌟 Simple Astrology Manager")
        print("=" * 40)

        while True:
            print("\nOptions:")
            print("1. Generate 10 random content")
            print("2. Create love-themed content")
            print("3. Create career-themed content")
            print("4. Exit")

            choice = input("\nYour choice (1-4): ").strip()

            if choice == "1":
                files = self.generate_missing_content(10)
                print(f"✅ Created {len(files)} files")
            elif choice == "2":
                files = self.create_special_love_content()
                print(f"✅ Created {len(files)} love-themed files")
            elif choice == "3":
                files = self.create_career_content()
                print(f"✅ Created {len(files)} career-themed files")
            elif choice == "4":
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice!")

if __name__ == "__main__":
    manager = SimpleAstrologyManager()
    manager.run_interface()
