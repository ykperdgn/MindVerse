#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import re
from collections import defaultdict

class MindVerseContentCleaner:
    def __init__(self):
        self.content_dir = "src/content"
        self.stats = {
            'total_files': 0,
            'duplicates_deleted': 0,
            'short_files_deleted': 0,
            'astrology_kept': 0,
            'space_saved': 0
        }

    def count_words_in_content(self, filepath):
        """Count words in markdown content, excluding frontmatter"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Remove frontmatter (everything between first and second ---)
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    content = parts[2].strip()

            # Remove markdown formatting
            content = re.sub(r'#{1,6}\s+', '', content)  # Headers
            content = re.sub(r'\*\*([^*]+)\*\*', r'\1', content)  # Bold
            content = re.sub(r'\*([^*]+)\*', r'\1', content)  # Italic
            content = re.sub(r'`([^`]+)`', r'\1', content)  # Code
            content = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', content)  # Links

            # Count words
            words = len([word for word in content.split() if word.strip()])
            return words

        except Exception as e:
            print(f"Error reading {filepath}: {e}")
            return 0

    def is_astrology_file(self, filepath):
        """Check if file is an astrology/horoscope file"""
        astrology_patterns = [
            'astrology',
            'burcu',
            'gunluk',
            'haftalik',
            'aylik',
            'daily',
            'weekly',
            'monthly',
            'horoscope'
        ]

        filename = os.path.basename(filepath).lower()
        return any(pattern in filename for pattern in astrology_patterns)

    def get_file_hash(self, filepath):
        """Get content hash for duplicate detection"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Remove frontmatter and normalize
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    content = parts[2].strip()

            # Normalize whitespace
            normalized = ' '.join(content.split())
            return hash(normalized)
        except:
            return None

    def find_duplicates(self):
        """Find files with identical content"""
        file_hashes = defaultdict(list)

        for filepath in glob.glob(f"{self.content_dir}/**/*.md", recursive=True):
            if not self.is_astrology_file(filepath):  # Skip astrology files
                file_hash = self.get_file_hash(filepath)
                if file_hash:
                    file_hashes[file_hash].append(filepath)

        duplicates = []
        for hash_val, files in file_hashes.items():
            if len(files) > 1:
                duplicates.append(files)

        return duplicates

    def find_short_files(self, min_words=500):
        """Find files with less than min_words (excluding astrology)"""
        short_files = []

        for filepath in glob.glob(f"{self.content_dir}/**/*.md", recursive=True):
            if not self.is_astrology_file(filepath):  # Skip astrology files
                word_count = self.count_words_in_content(filepath)
                if word_count < min_words:
                    short_files.append((filepath, word_count))

        return sorted(short_files, key=lambda x: x[1])

    def delete_duplicates(self, dry_run=True):
        """Delete duplicate files, keeping the newest/largest"""
        duplicates = self.find_duplicates()

        print(f"\n🔄 Processing {len(duplicates)} duplicate sets...")

        for files in duplicates:
            # Sort by modification time (newest first) and size (largest first)
            files_with_stats = []
            for filepath in files:
                stat = os.stat(filepath)
                files_with_stats.append((filepath, stat.st_mtime, stat.st_size))

            files_with_stats.sort(key=lambda x: (-x[1], -x[2]))

            # Keep first, delete rest
            keep_file = files_with_stats[0][0]
            delete_files = [f[0] for f in files_with_stats[1:]]

            print(f"Keeping: {os.path.basename(keep_file)}")

            for delete_file in delete_files:
                size = os.path.getsize(delete_file)
                print(f"  Deleting: {os.path.basename(delete_file)} ({size} bytes)")

                if not dry_run:
                    try:
                        os.remove(delete_file)
                        self.stats['duplicates_deleted'] += 1
                        self.stats['space_saved'] += size
                        print(f"    ✅ Deleted")
                    except Exception as e:
                        print(f"    ❌ Error: {e}")

    def delete_short_files(self, min_words=500, dry_run=True):
        """Delete files with less than min_words"""
        short_files = self.find_short_files(min_words)

        print(f"\n📏 Processing {len(short_files)} short files (< {min_words} words)...")

        for filepath, word_count in short_files:
            size = os.path.getsize(filepath)
            category = filepath.split(os.sep)[-2] if os.sep in filepath else "unknown"
            filename = os.path.basename(filepath)

            print(f"Deleting: [{category}] {filename} ({word_count} words, {size} bytes)")

            if not dry_run:
                try:
                    os.remove(filepath)
                    self.stats['short_files_deleted'] += 1
                    self.stats['space_saved'] += size
                    print(f"  ✅ Deleted")
                except Exception as e:
                    print(f"  ❌ Error: {e}")

    def count_astrology_files(self):
        """Count astrology files that will be kept"""
        count = 0
        for filepath in glob.glob(f"{self.content_dir}/**/*.md", recursive=True):
            if self.is_astrology_file(filepath):
                count += 1

        self.stats['astrology_kept'] = count
        return count

    def analyze_content(self):
        """Analyze all content and show statistics"""
        print("🔍 CONTENT ANALYSIS")
        print("=" * 50)

        all_files = list(glob.glob(f"{self.content_dir}/**/*.md", recursive=True))
        self.stats['total_files'] = len(all_files)

        duplicates = self.find_duplicates()
        short_files = self.find_short_files()
        astrology_count = self.count_astrology_files()

        print(f"Total files: {len(all_files)}")
        print(f"Astrology files (will be kept): {astrology_count}")
        print(f"Duplicate sets: {len(duplicates)}")
        print(f"Short files (< 500 words): {len(short_files)}")

        # Show breakdown by category
        categories = defaultdict(int)
        for filepath in all_files:
            if os.sep in filepath:
                category = filepath.split(os.sep)[-2]
                categories[category] += 1

        print(f"\nFiles by category:")
        for category, count in sorted(categories.items()):
            print(f"  {category}: {count} files")

        return duplicates, short_files

    def clean_content(self, dry_run=True):
        """Main cleanup function"""
        print("🧹 MINDVERSE CONTENT CLEANER")
        print("=" * 50)
        print(f"Mode: {'DRY RUN' if dry_run else 'EXECUTE'}")
        print("Keeping all astrology files for future content generation")
        print()

        # Analyze first
        duplicates, short_files = self.analyze_content()

        if not duplicates and not short_files:
            print("✅ No cleanup needed!")
            return

        # Clean duplicates
        if duplicates:
            self.delete_duplicates(dry_run)

        # Clean short files
        if short_files:
            self.delete_short_files(dry_run=dry_run)

        # Summary
        print(f"\n📊 CLEANUP SUMMARY:")
        print("=" * 30)
        print(f"Total files: {self.stats['total_files']}")
        print(f"Astrology files kept: {self.stats['astrology_kept']}")
        print(f"Duplicates deleted: {self.stats['duplicates_deleted']}")
        print(f"Short files deleted: {self.stats['short_files_deleted']}")
        print(f"Space saved: {self.stats['space_saved']:,} bytes")

        remaining = (self.stats['total_files'] -
                    self.stats['duplicates_deleted'] -
                    self.stats['short_files_deleted'])
        print(f"Remaining files: {remaining}")

def main():
    import sys

    cleaner = MindVerseContentCleaner()

    if len(sys.argv) > 1 and sys.argv[1] == '--execute':
        print("⚠️  EXECUTE MODE: Files will be permanently deleted!")
        response = input("Are you sure? Type 'yes' to continue: ")
        if response.lower() == 'yes':
            cleaner.clean_content(dry_run=False)
        else:
            print("Operation cancelled.")
    else:
        cleaner.clean_content(dry_run=True)
        print(f"\n💡 This was a dry run. Use '--execute' to actually delete files.")

if __name__ == '__main__':
    main()
