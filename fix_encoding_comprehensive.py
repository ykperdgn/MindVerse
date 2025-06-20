#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive Turkish Encoding Fixer for MindVerse
Fixes UTF-8 encoding issues in all Astro files
"""

import os
import sys
import glob
import re
from pathlib import Path

def fix_encoding_in_file(file_path):
    """Fix encoding issues in a single file"""
    try:
        # Try to read with UTF-8
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Common Turkish character fixes
        replacements = {
            # Broken UTF-8 sequences to correct Turkish characters
            'Ã§': 'ç', 'Ã‡': 'Ç',
            'ÄŸ': 'ğ', 'Ğ': 'Ğ',
            'ı': 'ı', 'İ': 'İ', 'Ä±': 'ı',
            'ö': 'ö', 'Ö': 'Ö',
            'ş': 'ş', 'Ş': 'Ş',
            'ü': 'ü', 'Ü': 'Ü',
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
            'Ä±': 'ı'
        }

        # Apply replacements
        modified = False
        for broken, correct in replacements.items():
            if broken in content:
                content = content.replace(broken, correct)
                modified = True

        # If modifications were made, write back to file
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed encoding in: {file_path}")
            return True

        return False

    except Exception as e:
        print(f"❌ Error processing {file_path}: {e}")
        return False

def main():
    """Main function to fix encoding in all relevant files"""

    # Get the project root directory
    project_root = Path(__file__).parent

    # File patterns to check
    patterns = [
        'src/**/*.astro',
        'src/**/*.md',
        'src/**/*.ts',
        'src/**/*.js',
        'public/**/*.html',
        '*.md',
        '*.astro'
    ]

    files_processed = 0
    files_fixed = 0

    print("🔧 Starting comprehensive Turkish encoding fix...")
    print(f"📁 Project root: {project_root}")

    for pattern in patterns:
        file_paths = glob.glob(str(project_root / pattern), recursive=True)

        for file_path in file_paths:
            if os.path.isfile(file_path):
                files_processed += 1
                if fix_encoding_in_file(file_path):
                    files_fixed += 1

    print(f"\n📊 Encoding Fix Summary:")
    print(f"   📁 Files processed: {files_processed}")
    print(f"   ✅ Files fixed: {files_fixed}")
    print(f"   ✨ Encoding issues resolved!")

    if files_fixed > 0:
        print(f"\n🚀 Rebuild and redeploy required to see changes in production.")

if __name__ == "__main__":
    main()
