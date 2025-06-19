#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔧 Astrology Schema Fixer
Adds missing required fields to astrology content files
"""

import os
import re
from pathlib import Path

class AstrologySchemaFixer:
    def __init__(self):
        self.astrology_dir = Path("src/content/astrology")
        self.fixed_count = 0
        self.error_count = 0

    def fix_astrology_frontmatter(self, content):
        """Add missing required fields to astrology frontmatter"""
        lines = content.split('\n')
        in_frontmatter = False
        frontmatter_lines = []
        content_lines = []

        for i, line in enumerate(lines):
            if line.strip() == '---':
                if not in_frontmatter:
                    in_frontmatter = True
                    frontmatter_lines.append(line)
                else:
                    # End of frontmatter
                    in_frontmatter = False
                    frontmatter_lines.append(line)
                    content_lines = lines[i+1:]
                    break
                continue

            if in_frontmatter:
                frontmatter_lines.append(line)

        # Parse existing frontmatter
        has_description = any(line.strip().startswith('description:') for line in frontmatter_lines)
        has_pubDate = any(line.strip().startswith('pubDate:') for line in frontmatter_lines)
        has_category = any(line.strip().startswith('category:') for line in frontmatter_lines)

        # Add missing fields
        new_frontmatter = []
        for line in frontmatter_lines:
            if line.strip() == '---' and line == frontmatter_lines[0]:
                new_frontmatter.append(line)
                continue
            elif line.strip() == '---' and line == frontmatter_lines[-1]:
                # Add missing fields before closing ---
                if not has_description:
                    # Extract title for description
                    title_line = next((l for l in frontmatter_lines if l.strip().startswith('title:')), '')
                    if title_line:
                        title = title_line.split(':', 1)[1].strip().strip('"\'')
                        new_frontmatter.append(f'description: "{title}"')

                if not has_pubDate:
                    # Use date field if available
                    date_line = next((l for l in frontmatter_lines if l.strip().startswith('date:')), '')
                    if date_line:
                        date_value = date_line.split(':', 1)[1].strip()
                        new_frontmatter.append(f'pubDate: {date_value}')

                if not has_category:
                    new_frontmatter.append('category: "daily-horoscope"')

                new_frontmatter.append(line)
            else:
                new_frontmatter.append(line)

        # Reconstruct content
        return '\n'.join(new_frontmatter + content_lines)

    def fix_file(self, file_path):
        """Fix a single astrology file"""
        try:
            # Try different encodings
            for encoding in ['utf-8', 'latin-1', 'cp1252']:
                try:
                    with open(file_path, 'r', encoding=encoding) as f:
                        content = f.read()
                    break
                except UnicodeDecodeError:
                    continue
            else:
                print(f"  ⚠️ Could not decode: {file_path.name}")
                return False

            # Check if file needs the required fields
            if 'description:' not in content or 'pubDate:' not in content or 'category:' not in content:
                fixed_content = self.fix_astrology_frontmatter(content)

                # Write back the fixed content
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)

                self.fixed_count += 1
                print(f"  ✅ Fixed: {file_path.name}")
                return True

            return False

        except Exception as e:
            print(f"  ❌ Error fixing {file_path.name}: {e}")
            self.error_count += 1
            return False

    def fix_all_files(self):
        """Fix all astrology files"""
        print("🔧 Starting Astrology Schema Fix...")

        md_files = list(self.astrology_dir.glob("*.md"))
        if not md_files:
            print("  No markdown files found in astrology directory")
            return

        print(f"📁 Processing {len(md_files)} astrology files...")

        for md_file in md_files:
            if md_file.name.startswith('2025-06-20'):  # Only recent files
                self.fix_file(md_file)

        print(f"\n🎉 Astrology Schema Fix Completed!")
        print(f"📊 Results:")
        print(f"  ✅ Fixed files: {self.fixed_count}")
        print(f"  ❌ Errors: {self.error_count}")

        return self.fixed_count

if __name__ == "__main__":
    fixer = AstrologySchemaFixer()
    fixer.fix_all_files()
