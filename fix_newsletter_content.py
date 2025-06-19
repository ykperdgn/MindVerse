#!/usr/bin/env python3
"""
Remove newsletter references from content files
"""

import os
import re
import glob

def fix_content_files():
    """Remove newsletter sections from markdown files"""

    # Pattern to match newsletter sections
    newsletter_pattern = r'## 📬 Günlük İçerikler İçin Bültenimize Katılın\s*\n\s*Bu tür kaliteli içerikleri kaçırmamak için e-posta bültenimize abone olabilirsiniz\. Haftalık özetler ve özel araştırmalar doğrudan e-postanızda!\s*\n'

    # Find all markdown files in content directories
    content_dirs = ['src/content/health', 'src/content/love', 'src/content/history',
                   'src/content/psychology', 'src/content/space', 'src/content/quotes',
                   'src/content/astrology']

    fixed_files = []

    for content_dir in content_dirs:
        if os.path.exists(content_dir):
            for md_file in glob.glob(f'{content_dir}/*.md'):
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Remove newsletter section
                    new_content = re.sub(newsletter_pattern, '', content, flags=re.MULTILINE)

                    # Only write if content changed
                    if new_content != content:
                        with open(md_file, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        fixed_files.append(md_file)
                        print(f"Fixed: {md_file}")

                except Exception as e:
                    print(f"Error processing {md_file}: {e}")

    return fixed_files

if __name__ == "__main__":
    print("🔧 Removing newsletter references from content files...")
    fixed = fix_content_files()
    print(f"\n✅ Fixed {len(fixed)} files")
    if fixed:
        print("\nFixed files:")
        for file in fixed:
            print(f"  - {file}")
