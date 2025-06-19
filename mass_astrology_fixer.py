#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 Mass Astrology Schema Fixer
Fixes all new astrology files to match required schema
"""

import os
import re
from pathlib import Path

def fix_astrology_file(file_path):
    """Fix a single astrology file frontmatter"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split into frontmatter and content
        parts = content.split('---', 2)
        if len(parts) < 3:
            return False

        frontmatter = parts[1].strip()
        main_content = parts[2]

        # Parse frontmatter lines
        fm_lines = frontmatter.split('\n')
        new_fm_lines = []

        has_description = False
        has_pubDate = False
        has_category = False
        title_value = ""
        date_value = ""

        # Process existing lines
        for line in fm_lines:
            if line.strip().startswith('title:'):
                title_value = line.split(':', 1)[1].strip().strip('"\'')
                new_fm_lines.append(line)
            elif line.strip().startswith('description:'):
                has_description = True
                new_fm_lines.append(line)
            elif line.strip().startswith('pubDate:'):
                has_pubDate = True
                new_fm_lines.append(line)
            elif line.strip().startswith('category:'):
                has_category = True
                new_fm_lines.append(line)
            elif line.strip().startswith('date:'):
                date_value = line.split(':', 1)[1].strip()
                new_fm_lines.append(line)
            else:
                new_fm_lines.append(line)

        # Add missing required fields
        if not has_description and title_value:
            new_fm_lines.insert(1, f'description: "{title_value}"')

        if not has_pubDate and date_value:
            new_fm_lines.insert(2, f'pubDate: {date_value}')

        if not has_category:
            new_fm_lines.insert(3, 'category: "daily-horoscope"')

        # Reconstruct content
        new_content = '---\n' + '\n'.join(new_fm_lines) + '\n---' + main_content

        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True

    except Exception as e:
        print(f"Error fixing {file_path.name}: {e}")
        return False

# Fix all 2025-06-20 astrology files
astrology_dir = Path("src/content/astrology")
files_to_fix = list(astrology_dir.glob("*-2025-06-20*.md"))

print(f"🔧 Fixing {len(files_to_fix)} astrology files...")

fixed_count = 0
for file_path in files_to_fix:
    if fix_astrology_file(file_path):
        fixed_count += 1
        print(f"  ✅ Fixed: {file_path.name}")

print(f"\n🎉 Fixed {fixed_count} astrology files!")
