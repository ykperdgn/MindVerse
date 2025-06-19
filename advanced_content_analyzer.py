#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔍 Advanced Content Analyzer & Optimizer
- Duplicate title detection and removal
- Content length analysis
- Category balancing
- Pagination preparation
"""

import os
import re
import hashlib
from collections import defaultdict, Counter
from pathlib import Path
import glob

class AdvancedContentAnalyzer:
    def __init__(self):
        self.content_dir = Path("src/content")
        self.min_word_count = 600
        self.target_articles_per_category = 20

        self.categories = [
            'health', 'love', 'psychology', 'history',
            'space', 'quotes', 'astrology'
        ]

        self.analysis_results = {
            'duplicates': defaultdict(list),
            'short_content': [],
            'category_stats': defaultdict(dict),
            'title_conflicts': defaultdict(list),
            'actions_needed': []
        }

    def extract_title_from_file(self, filepath):
        """Extract title from frontmatter"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract title from frontmatter
            if content.startswith('---'):
                frontmatter_end = content.find('---', 3)
                if frontmatter_end != -1:
                    frontmatter = content[3:frontmatter_end]
                    title_match = re.search(r"title:\s*['\"]([^'\"]+)['\"]", frontmatter)
                    if title_match:
                        return title_match.group(1).strip()

            return None
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
            return None

    def count_words_in_content(self, filepath):
        """Count words excluding frontmatter"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Remove frontmatter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    content = parts[2].strip()

            # Clean markdown and count words
            content = re.sub(r'#{1,6}\s+', '', content)
            content = re.sub(r'\*\*([^*]+)\*\*', r'\1', content)
            content = re.sub(r'\*([^*]+)\*', r'\1', content)
            content = re.sub(r'`([^`]+)`', r'\1', content)
            content = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', content)

            words = len([word for word in content.split() if word.strip()])
            return words

        except Exception as e:
            print(f"Error reading {filepath}: {e}")
            return 0

    def analyze_duplicate_titles(self):
        """Find articles with same titles but different lengths"""
        print("🔍 Analyzing duplicate titles...")

        title_to_files = defaultdict(list)

        for category in self.categories:
            category_path = self.content_dir / category
            if not category_path.exists():
                continue

            for md_file in category_path.glob("*.md"):
                title = self.extract_title_from_file(md_file)
                if title:
                    word_count = self.count_words_in_content(md_file)
                    title_to_files[title.lower()].append({
                        'file': str(md_file),
                        'title': title,
                        'words': word_count,
                        'category': category
                    })

        # Find duplicates
        duplicates_found = 0
        for title, files in title_to_files.items():
            if len(files) > 1:
                # Sort by word count (descending)
                files.sort(key=lambda x: x['words'], reverse=True)

                print(f"\n📄 Duplicate title found: '{files[0]['title']}'")
                for i, file_info in enumerate(files):
                    status = "✅ KEEP (longest)" if i == 0 else "❌ DELETE"
                    print(f"  {status} {file_info['words']} words - {Path(file_info['file']).name}")

                # Mark shorter ones for deletion
                for file_info in files[1:]:
                    self.analysis_results['duplicates'][title].append(file_info)
                    duplicates_found += 1

        print(f"\n📊 Found {duplicates_found} duplicate files to remove")
        return duplicates_found

    def analyze_short_content(self):
        """Find articles shorter than minimum word count"""
        print(f"\n🔍 Analyzing content shorter than {self.min_word_count} words...")

        short_files = []

        for category in self.categories:
            category_path = self.content_dir / category
            if not category_path.exists():
                continue

            for md_file in category_path.glob("*.md"):
                word_count = self.count_words_in_content(md_file)
                title = self.extract_title_from_file(md_file)

                if word_count < self.min_word_count:
                    short_files.append({
                        'file': str(md_file),
                        'title': title or 'No title',
                        'words': word_count,
                        'category': category
                    })

        # Sort by word count
        short_files.sort(key=lambda x: x['words'])

        print(f"\n📄 Found {len(short_files)} articles shorter than {self.min_word_count} words:")
        for file_info in short_files:
            print(f"  ❌ {file_info['words']} words - {Path(file_info['file']).name}")

        self.analysis_results['short_content'] = short_files
        return len(short_files)

    def analyze_category_balance(self):
        """Analyze content distribution per category"""
        print(f"\n📊 Analyzing category balance (target: {self.target_articles_per_category} per category)...")

        for category in self.categories:
            category_path = self.content_dir / category

            if not category_path.exists():
                print(f"  ❌ Category '{category}' directory missing")
                self.analysis_results['category_stats'][category] = {
                    'current': 0, 'target': self.target_articles_per_category,
                    'needed': self.target_articles_per_category
                }
                continue

            # Count existing files
            md_files = list(category_path.glob("*.md"))

            # Count by language
            turkish_files = [f for f in md_files if not f.name.endswith('_en.md')]
            english_files = [f for f in md_files if f.name.endswith('_en.md')]

            total_files = len(md_files)
            needed = max(0, self.target_articles_per_category - total_files)

            print(f"  📁 {category}: {total_files} articles ({len(turkish_files)} TR + {len(english_files)} EN)")
            if needed > 0:
                print(f"    🎯 Need {needed} more articles to reach target of {self.target_articles_per_category}")
            else:
                print(f"    ✅ Target reached!")

            self.analysis_results['category_stats'][category] = {
                'current': total_files,
                'turkish': len(turkish_files),
                'english': len(english_files),
                'target': self.target_articles_per_category,
                'needed': needed
            }

    def remove_duplicate_and_short_content(self):
        """Remove duplicate and short content files"""
        if not self.analysis_results['duplicates'] and not self.analysis_results['short_content']:
            print("📄 No files to remove.")
            return 0

        removed_count = 0
        total_space_saved = 0

        print("\n🗑️ Removing duplicate and short content...")

        # Remove duplicates
        for title, duplicate_files in self.analysis_results['duplicates'].items():
            for file_info in duplicate_files:
                try:
                    file_path = Path(file_info['file'])
                    file_size = file_path.stat().st_size
                    file_path.unlink()
                    print(f"  ✅ Removed duplicate: {file_path.name} ({file_info['words']} words)")
                    removed_count += 1
                    total_space_saved += file_size
                except Exception as e:
                    print(f"  ❌ Error removing {file_path.name}: {e}")

        # Remove short content (but preserve astrology files)
        for file_info in self.analysis_results['short_content']:
            if file_info['category'] == 'astrology':
                continue  # Skip astrology files

            try:
                file_path = Path(file_info['file'])
                file_size = file_path.stat().st_size
                file_path.unlink()
                print(f"  ✅ Removed short content: {file_path.name} ({file_info['words']} words)")
                removed_count += 1
                total_space_saved += file_size
            except Exception as e:
                print(f"  ❌ Error removing {file_path.name}: {e}")

        print(f"\n📊 Cleanup Summary:")
        print(f"  🗑️ Files removed: {removed_count}")
        print(f"  💾 Space saved: {total_space_saved:,} bytes")

        return removed_count

    def generate_cleanup_report(self):
        """Generate detailed cleanup report"""
        print("\n" + "="*80)
        print("📋 ADVANCED CONTENT ANALYSIS REPORT")
        print("="*80)

        print(f"\n🎯 TARGET: {self.target_articles_per_category} articles per category (min {self.min_word_count} words)")

        # Duplicate analysis
        duplicate_count = sum(len(files) for files in self.analysis_results['duplicates'].values())
        print(f"\n📄 DUPLICATE TITLES: {len(self.analysis_results['duplicates'])} titles with {duplicate_count} duplicate files")

        # Short content analysis
        short_count = len(self.analysis_results['short_content'])
        print(f"📏 SHORT CONTENT: {short_count} files under {self.min_word_count} words")

        # Category balance
        print(f"\n📊 CATEGORY ANALYSIS:")
        total_needed = 0
        for category, stats in self.analysis_results['category_stats'].items():
            status = "✅" if stats['needed'] == 0 else "🎯"
            print(f"  {status} {category.capitalize()}: {stats['current']}/{stats['target']} articles")
            if stats['needed'] > 0:
                print(f"    📝 Need {stats['needed']} more articles")
                total_needed += stats['needed']

        print(f"\n🎯 TOTAL ARTICLES NEEDED: {total_needed}")

        # Action plan
        print(f"\n📋 RECOMMENDED ACTIONS:")
        print(f"  1. Remove {duplicate_count} duplicate files")
        print(f"  2. Remove {short_count} short content files")
        print(f"  3. Generate {total_needed} new articles to balance categories")
        print(f"  4. Implement pagination system for category pages")
        print(f"  5. Add search functionality")

    def run_full_analysis(self):
        """Run complete content analysis"""
        print("🚀 Starting Advanced Content Analysis...")

        # Run all analyses
        self.analyze_duplicate_titles()
        self.analyze_short_content()
        self.analyze_category_balance()

        # Generate report
        self.generate_cleanup_report()

        # Ask for confirmation
        print(f"\n❓ Do you want to proceed with cleanup? (y/n): ", end="")
        response = input().lower().strip()

        if response == 'y':
            removed = self.remove_duplicate_and_short_content()
            print(f"\n✅ Cleanup completed! Removed {removed} files.")

            # Re-analyze after cleanup
            print(f"\n🔄 Re-analyzing after cleanup...")
            self.analysis_results = {
                'duplicates': defaultdict(list),
                'short_content': [],
                'category_stats': defaultdict(dict),
                'title_conflicts': defaultdict(list),
                'actions_needed': []
            }
            self.analyze_category_balance()

        else:
            print(f"\n⏸️ Cleanup cancelled. Analysis results saved for review.")

        return self.analysis_results

if __name__ == "__main__":
    analyzer = AdvancedContentAnalyzer()
    results = analyzer.run_full_analysis()
