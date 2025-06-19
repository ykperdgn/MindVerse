#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import hashlib
from collections import defaultdict
import argparse

class ContentCleanup:
    def __init__(self, content_dir="src/content"):
        self.content_dir = content_dir
        self.duplicates = defaultdict(list)
        self.short_files = []
        self.stats = {
            'total_files': 0,
            'duplicates_found': 0,
            'short_files_found': 0,
            'files_deleted': 0,
            'size_saved': 0
        }

    def get_file_hash(self, filepath):
        """Calculate MD5 hash of file content (excluding frontmatter)"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Remove frontmatter (everything between first --- and second ---)
            parts = content.split('---')
            if len(parts) >= 3:
                content_only = '---'.join(parts[2:])
            else:
                content_only = content

            # Normalize whitespace and calculate hash
            normalized = ' '.join(content_only.split())
            return hashlib.md5(normalized.encode()).hexdigest()
        except:
            return None

    def get_content_length(self, filepath):
        """Get word count of content (excluding frontmatter)"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Remove frontmatter
            parts = content.split('---')
            if len(parts) >= 3:
                content_only = '---'.join(parts[2:])
            else:
                content_only = content

            # Count words
            words = len(content_only.split())
            return words
        except:
            return 0

    def find_duplicates(self):
        """Find duplicate content files"""
        print("🔍 Scanning for duplicate content...")

        file_hashes = defaultdict(list)

        for filepath in glob.glob(f"{self.content_dir}/**/*.md", recursive=True):
            self.stats['total_files'] += 1

            file_hash = self.get_file_hash(filepath)
            if file_hash:
                file_hashes[file_hash].append(filepath)

        # Identify duplicates
        for hash_value, files in file_hashes.items():
            if len(files) > 1:
                self.duplicates[hash_value] = files
                self.stats['duplicates_found'] += len(files) - 1  # All but one are duplicates

        print(f"   Found {len(self.duplicates)} sets of duplicates")
        print(f"   Total duplicate files: {self.stats['duplicates_found']}")

    def find_short_content(self, min_words=500):
        """Find files with content shorter than min_words"""
        print(f"📏 Scanning for content shorter than {min_words} words...")

        for filepath in glob.glob(f"{self.content_dir}/**/*.md", recursive=True):
            word_count = self.get_content_length(filepath)
            if word_count < min_words:
                self.short_files.append((filepath, word_count))

        self.short_files.sort(key=lambda x: x[1])  # Sort by word count
        self.stats['short_files_found'] = len(self.short_files)

        print(f"   Found {len(self.short_files)} short files")

    def show_duplicates(self):
        """Display duplicate files"""
        if not self.duplicates:
            print("✅ No duplicates found!")
            return

        print(f"\n📋 DUPLICATE CONTENT REPORT:")
        print("=" * 60)

        for i, (hash_value, files) in enumerate(self.duplicates.items(), 1):
            print(f"\n{i}. Duplicate Set ({len(files)} files):")
            for j, filepath in enumerate(files):
                size = os.path.getsize(filepath)
                print(f"   {j+1}) {filepath} ({size} bytes)")

                # Show first few lines of content
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        for line in lines[:5]:
                            if line.strip() and not line.startswith('---'):
                                print(f"      >> {line.strip()[:50]}...")
                                break
                except:
                    pass

    def show_short_files(self):
        """Display short files"""
        if not self.short_files:
            print("✅ No short files found!")
            return

        print(f"\n📏 SHORT CONTENT REPORT:")
        print("=" * 60)

        for i, (filepath, word_count) in enumerate(self.short_files[:20], 1):
            size = os.path.getsize(filepath)
            print(f"{i:2d}. {filepath}")
            print(f"    Words: {word_count}, Size: {size} bytes")

    def remove_duplicates(self, dry_run=True):
        """Remove duplicate files (keep the largest/newest)"""
        if not self.duplicates:
            print("No duplicates to remove.")
            return

        print(f"\n🗑️  REMOVING DUPLICATES (dry_run={dry_run}):")
        print("=" * 60)

        for hash_value, files in self.duplicates.items():
            # Sort by size (largest first), then by modification time (newest first)
            files_with_stats = []
            for filepath in files:
                stat = os.stat(filepath)
                files_with_stats.append((filepath, stat.st_size, stat.st_mtime))

            files_with_stats.sort(key=lambda x: (-x[1], -x[2]))

            # Keep the first (largest/newest), remove the rest
            keep_file = files_with_stats[0][0]
            remove_files = [f[0] for f in files_with_stats[1:]]

            print(f"\nKeeping: {keep_file}")
            for remove_file in remove_files:
                size = os.path.getsize(remove_file)
                print(f"Removing: {remove_file} ({size} bytes)")

                if not dry_run:
                    try:
                        os.remove(remove_file)
                        self.stats['files_deleted'] += 1
                        self.stats['size_saved'] += size
                        print(f"   ✅ Deleted")
                    except Exception as e:
                        print(f"   ❌ Error: {e}")

    def remove_short_files(self, min_words=500, dry_run=True):
        """Remove files with content shorter than min_words"""
        if not self.short_files:
            print("No short files to remove.")
            return

        print(f"\n🗑️  REMOVING SHORT FILES (dry_run={dry_run}):")
        print("=" * 60)

        for filepath, word_count in self.short_files:
            size = os.path.getsize(filepath)
            print(f"Removing: {filepath} ({word_count} words, {size} bytes)")

            if not dry_run:
                try:
                    os.remove(filepath)
                    self.stats['files_deleted'] += 1
                    self.stats['size_saved'] += size
                    print(f"   ✅ Deleted")
                except Exception as e:
                    print(f"   ❌ Error: {e}")

    def print_summary(self):
        """Print cleanup summary"""
        print(f"\n📊 CLEANUP SUMMARY:")
        print("=" * 40)
        print(f"Total files scanned: {self.stats['total_files']}")
        print(f"Duplicate files found: {self.stats['duplicates_found']}")
        print(f"Short files found: {self.stats['short_files_found']}")
        print(f"Files deleted: {self.stats['files_deleted']}")
        print(f"Space saved: {self.stats['size_saved']:,} bytes")

def main():
    parser = argparse.ArgumentParser(description='Clean up duplicate and short content files')
    parser.add_argument('--dry-run', action='store_true', default=True,
                        help='Show what would be deleted without actually deleting')
    parser.add_argument('--execute', action='store_true',
                        help='Actually delete files (overrides --dry-run)')
    parser.add_argument('--min-words', type=int, default=500,
                        help='Minimum word count for content (default: 500)')
    parser.add_argument('--content-dir', default='src/content',
                        help='Content directory to scan (default: src/content)')

    args = parser.parse_args()

    # If --execute is specified, override dry_run
    dry_run = not args.execute

    print("🧹 MINDVERSE CONTENT CLEANUP TOOL")
    print("=" * 50)
    print(f"Content directory: {args.content_dir}")
    print(f"Minimum words: {args.min_words}")
    print(f"Mode: {'DRY RUN' if dry_run else 'EXECUTE'}")
    print()

    cleanup = ContentCleanup(args.content_dir)

    # Find issues
    cleanup.find_duplicates()
    cleanup.find_short_content(args.min_words)

    # Show reports
    cleanup.show_duplicates()
    cleanup.show_short_files()

    # Cleanup (if requested)
    if not dry_run:
        response = input("\n⚠️  Are you sure you want to delete these files? (yes/no): ")
        if response.lower() in ['yes', 'y']:
            cleanup.remove_duplicates(dry_run=False)
            cleanup.remove_short_files(args.min_words, dry_run=False)
        else:
            print("Operation cancelled.")
    else:
        print(f"\n💡 This was a dry run. Use --execute to actually delete files.")

    cleanup.print_summary()

if __name__ == '__main__':
    main()
