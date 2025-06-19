#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔧 YAML Frontmatter Fixer
Fixes YAML formatting issues in markdown files
"""

import os
import re
from pathlib import Path

class YAMLFrontmatterFixer:
    def __init__(self):
        self.content_dir = Path("src/content")
        self.fixed_count = 0
        self.error_count = 0

    def fix_yaml_quotes(self, content):
        """Fix YAML frontmatter quote issues"""
        lines = content.split('\n')
        in_frontmatter = False
        fixed_lines = []

        for line in lines:
            if line.strip() == '---':
                in_frontmatter = not in_frontmatter
                fixed_lines.append(line)
                continue

            if in_frontmatter:
                # Fix title field with single quotes containing apostrophes
                if line.strip().startswith("title: '") and line.strip().endswith("'"):
                    # Extract the title content
                    title_content = line.strip()[8:-1]  # Remove "title: '" and final "'"
                    # Replace with double quotes
                    fixed_line = f'title: "{title_content}"'
                    fixed_lines.append(fixed_line)
                    continue

                # Fix summary field
                elif line.strip().startswith("summary: '") and line.strip().endswith("'"):
                    summary_content = line.strip()[10:-1]  # Remove "summary: '" and final "'"
                    fixed_line = f'summary: "{summary_content}"'
                    fixed_lines.append(fixed_line)
                    continue

                # Fix author field
                elif line.strip().startswith("author: '") and line.strip().endswith("'"):
                    author_content = line.strip()[9:-1]  # Remove "author: '" and final "'"
                    fixed_line = f'author: "{author_content}"'
                    fixed_lines.append(fixed_line)
                    continue

                # Fix keywords field
                elif line.strip().startswith("keywords: '") and line.strip().endswith("'"):
                    keywords_content = line.strip()[11:-1]  # Remove "keywords: '" and final "'"
                    fixed_line = f'keywords: "{keywords_content}"'
                    fixed_lines.append(fixed_line)
                    continue

                # Fix tags field with single quotes
                elif line.strip().startswith("tags: [") and "'" in line:
                    # Replace single quotes with double quotes in array
                    fixed_line = line.replace("'", '"')
                    fixed_lines.append(fixed_line)
                    continue

            fixed_lines.append(line)

        return '\n'.join(fixed_lines)

    def fix_file(self, file_path):
        """Fix a single markdown file"""
        try:
            # Try different encodings
            encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252']
            content = None

            for encoding in encodings:
                try:
                    with open(file_path, 'r', encoding=encoding) as f:
                        content = f.read()
                    break
                except UnicodeDecodeError:
                    continue

            if content is None:
                print(f"  ⚠️ Skipping {file_path.name}: Unable to decode file")
                return False

            # Check if file needs fixing
            if "title: '" in content or "summary: '" in content or "author: '" in content or "keywords: '" in content:
                fixed_content = self.fix_yaml_quotes(content)

                # Write back the fixed content
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)

                self.fixed_count += 1
                print(f"  ✅ Fixed: {file_path.name}")
                return True
            else:
                print(f"  ✓ Skipping {file_path.name}: No issues found")

            return False

        except Exception as e:
            print(f"  ❌ Error fixing {file_path.name}: {e}")
            self.error_count += 1
            return False

    def fix_all_files(self):
        """Fix all markdown files in content directory"""
        print("🔧 Starting YAML Frontmatter Fix...")        # Focus on categories we know have issues
        target_categories = ['health', 'history', 'love', 'psychology', 'quotes', 'space', 'cinema', 'art', 'technology']

        for category_name in target_categories:
            category_dir = self.content_dir / category_name
            if category_dir.exists() and category_dir.is_dir():
                print(f"\n📁 Processing {category_name}...")

                md_files = list(category_dir.glob("*.md"))
                if not md_files:
                    print("  No markdown files found")
                    continue

                for md_file in md_files:
                    self.fix_file(md_file)

        print(f"\n🎉 YAML Fix Completed!")
        print(f"📊 Results:")
        print(f"  ✅ Fixed files: {self.fixed_count}")
        print(f"  ❌ Errors: {self.error_count}")

        return self.fixed_count

if __name__ == "__main__":
    fixer = YAMLFrontmatterFixer()
    fixer.fix_all_files()
