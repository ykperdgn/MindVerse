#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced Turkish Encoding Fixer for MindVerse
Handles complex encoding issues including binary corrupted files
"""

import os
import sys
import glob
import re
from pathlib import Path

def handle_corrupted_file(file_path):
    """Handle files with corrupted encoding by trying multiple encodings"""
    encodings_to_try = ['utf-8', 'latin-1', 'cp1254', 'iso-8859-9', 'windows-1254']

    for encoding in encodings_to_try:
        try:
            with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
                content = f.read()

            # Apply Turkish character fixes
            replacements = {
                # More comprehensive Turkish character mappings
                'Ã§': 'ç', 'Ã‡': 'Ç',
                'ÄŸ': 'ğ', 'Ğ': 'Ğ',
                'ı': 'ı', 'İ': 'İ', 'Ä±': 'ı', 'Ä°': 'İ',
                'ö': 'ö', 'Ö': 'Ö', 'Ã¶': 'ö', 'Ã–': 'Ö',
                'ş': 'ş', 'Ş': 'Ş', 'Å\x9f': 'ş', 'Å\x9e': 'Ş',
                'ü': 'ü', 'Ü': 'Ü', 'Ã¼': 'ü', 'Ãœ': 'Ü',
                'GÃ¼nlÃ¼k': 'Günlük',
                'BurÃ§': 'Burç',
                'YorumlarÄ±': 'Yorumları',
                'YÄ±ldÄ±zlarÄ±n': 'Yıldızların',
                'rehberliÄŸinde': 'rehberliğinde',
                'hayatÄ±nÄ±zÄ±': 'hayatınızı',
                'keÅŸfedin': 'keşfedin',
                'haftalÄ±k': 'haftalık',
                'aylÄ±k': 'aylık',
                'analizleri': 'analizleri',
                'kiÅŸisel': 'kişisel',
                'GeliÅŸmiÅŸ': 'Gelişmiş',
                'Ã–zellikler': 'Özellikler',
                'Ã–zel': 'Özel',
                'Ã¼': 'ü',
                'Ã¶': 'ö',
                'Ã§': 'ç',
                'ÄŸ': 'ğ',
                'Å': 'ş',
                'Å\x9f': 'ş',
                'Ä°': 'İ',
                'Ä±': 'ı',
                # Additional corrupted patterns
                '\xfd': 'ı',
                '\xfc': 'ü',
                '\xf6': 'ö',
                '\xe7': 'ç',
                '\xf0': 'ğ',
                '\xfe': 'ş'
            }

            # Apply replacements
            modified = False
            for broken, correct in replacements.items():
                if broken in content:
                    content = content.replace(broken, correct)
                    modified = True

            # Additional regex-based fixes for complex patterns
            regex_fixes = [
                (r'Ä±([a-zA-Z])', r'ı\1'),
                (r'Ä°([a-zA-Z])', r'İ\1'),
                (r'Ã¼([a-zA-Z])', r'ü\1'),
                (r'Ã¶([a-zA-Z])', r'ö\1'),
                (r'Ã§([a-zA-Z])', r'ç\1'),
                (r'ÄŸ([a-zA-Z])', r'ğ\1'),
                (r'Å\x9f([a-zA-Z])', r'ş\1'),
            ]

            for pattern, replacement in regex_fixes:
                new_content = re.sub(pattern, replacement, content)
                if new_content != content:
                    content = new_content
                    modified = True

            if modified:
                # Write back with UTF-8
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Fixed corrupted encoding in: {file_path}")
                return True

            return False

        except Exception as e:
            continue

    print(f"❌ Could not fix: {file_path}")
    return False

def main():
    """Fix remaining encoding issues"""

    project_root = Path(__file__).parent

    # Focus on remaining problematic files
    patterns = [
        'src/content/astrology/*aylik*.md',
        'src/content/astrology/*gunluk*.md',
        'src/content/astrology/*haftalik*.md',
        'src/**/*.astro',
        'src/**/*.md'
    ]

    files_processed = 0
    files_fixed = 0

    print("🔧 Advanced Turkish encoding fix...")

    for pattern in patterns:
        file_paths = glob.glob(str(project_root / pattern), recursive=True)

        for file_path in file_paths:
            if os.path.isfile(file_path):
                files_processed += 1
                if handle_corrupted_file(file_path):
                    files_fixed += 1

    print(f"\n📊 Advanced Fix Summary:")
    print(f"   📁 Files processed: {files_processed}")
    print(f"   ✅ Files fixed: {files_fixed}")
    print(f"   ✨ Advanced encoding issues resolved!")

if __name__ == "__main__":
    main()
