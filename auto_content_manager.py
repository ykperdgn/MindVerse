#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated Content Management System for MindVerse
- Daily horoscope generation
- Content scheduling and publishing
- SEO optimization
- Historical content generation
"""

import os
import sys
import json
import datetime
import subprocess
from pathlib import Path
from daily_horoscope_generator import DailyHoroscopeGenerator

class AutoContentManager:
    def __init__(self):
        self.base_path = Path(__file__).parent
        self.today = datetime.date.today()
        self.horoscope_generator = DailyHoroscopeGenerator()
        
    def generate_daily_content(self):
        """Generate all daily content for today"""
        print(f"🗓️ Generating content for {self.today.strftime('%B %d, %Y')}")
        
        try:
            # Generate Turkish horoscopes
            print("📝 Creating Turkish horoscopes...")
            turkish_files = self.horoscope_generator.generate_all_daily_horoscopes('turkish')
            
            # Generate English horoscopes
            print("📝 Creating English horoscopes...")
            english_files = self.horoscope_generator.generate_all_daily_horoscopes('english')
            
            # Generate weekly summaries (if it's Monday)
            if self.today.weekday() == 0:  # Monday
                print("📊 Creating weekly summaries...")
                self.horoscope_generator.generate_weekly_summary('turkish')
                self.horoscope_generator.generate_weekly_summary('english')
            
            total_files = len(turkish_files) + len(english_files)
            print(f"✅ Generated {total_files} content files")
            
            return True
            
        except Exception as e:
            print(f"❌ Error generating daily content: {e}")
            return False
    
    def generate_historical_content(self, days_back=30):
        """Generate historical content for the past N days"""
        print(f"📚 Generating historical content for past {days_back} days...")
        
        generated_count = 0
        for i in range(1, days_back + 1):
            target_date = self.today - datetime.timedelta(days=i)
            
            # Temporarily set the generator's date
            original_date = self.horoscope_generator.today
            self.horoscope_generator.today = target_date
            
            try:
                # Generate content for this date
                turkish_files = self.horoscope_generator.generate_all_daily_horoscopes('turkish')
                english_files = self.horoscope_generator.generate_all_daily_horoscopes('english')
                
                generated_count += len(turkish_files) + len(english_files)
                
                if i % 7 == 0:  # Progress update every week
                    print(f"  ✓ Completed {i} days ({generated_count} files so far)")
                    
            except Exception as e:
                print(f"  ❌ Error for {target_date}: {e}")
            
            # Restore original date
            self.horoscope_generator.today = original_date
        
        print(f"✅ Historical generation complete: {generated_count} files")
        return generated_count

    def update_sitemap(self):
        """Update sitemap with new content"""
        try:
            print("🗺️ Updating sitemap...")
            result = subprocess.run([
                sys.executable, "generate_seo_files.py"
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ Sitemap updated successfully")
                return True
            else:
                print(f"❌ Sitemap update failed: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"❌ Error updating sitemap: {e}")
            return False

    def build_site(self):
        """Build the Astro site"""
        try:
            print("🏗️ Building site...")
            result = subprocess.run([
                "npm", "run", "build"
            ], capture_output=True, text=True, cwd=self.base_path)
            
            if result.returncode == 0:
                print("✅ Site built successfully")
                return True
            else:
                print(f"❌ Build failed: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"❌ Error building site: {e}")
            return False

    def git_commit_and_push(self):
        """Commit new content to git and push"""
        try:
            print("📤 Committing and pushing to git...")
            
            # Add all new files
            subprocess.run(["git", "add", "."], cwd=self.base_path)
            
            # Commit with date
            commit_message = f"Auto-update: Daily content for {self.today.strftime('%Y-%m-%d')}"
            subprocess.run([
                "git", "commit", "-m", commit_message
            ], cwd=self.base_path)
            
            # Push to remote
            subprocess.run(["git", "push"], cwd=self.base_path)
            
            print("✅ Git commit and push completed")
            return True
            
        except Exception as e:
            print(f"❌ Git operation failed: {e}")
            return False

    def cleanup_old_content(self, days_to_keep=90):
        """Remove content older than specified days"""
        try:
            print(f"🧹 Cleaning up content older than {days_to_keep} days...")
            
            cutoff_date = self.today - datetime.timedelta(days=days_to_keep)
            content_dir = self.base_path / "src" / "content" / "astrology"
            
            removed_count = 0
            for file_path in content_dir.glob("*.md"):
                # Extract date from filename
                try:
                    if "-gunluk-" in file_path.name or "-daily-" in file_path.name:
                        date_part = file_path.name.split("-")[-1].replace(".md", "")
                        file_date = datetime.datetime.strptime(date_part, "%Y-%m-%d").date()
                        
                        if file_date < cutoff_date:
                            file_path.unlink()
                            removed_count += 1
                            
                except (ValueError, IndexError):
                    continue  # Skip files that don't match expected pattern
            
            print(f"✅ Cleaned up {removed_count} old files")
            return removed_count
            
        except Exception as e:
            print(f"❌ Cleanup failed: {e}")
            return 0

    def run_daily_workflow(self):
        """Run the complete daily content workflow"""
        print("🚀 Starting daily content workflow")
        print("=" * 50)
        
        success_steps = 0
        total_steps = 5
        
        # Step 1: Generate daily content
        if self.generate_daily_content():
            success_steps += 1
        
        # Step 2: Update sitemap
        if self.update_sitemap():
            success_steps += 1
        
        # Step 3: Build site
        if self.build_site():
            success_steps += 1
        
        # Step 4: Git operations
        if self.git_commit_and_push():
            success_steps += 1
        
        # Step 5: Cleanup old content
        if self.cleanup_old_content() >= 0:  # Even 0 removed files is success
            success_steps += 1
        
        print("=" * 50)
        print(f"📊 Workflow completed: {success_steps}/{total_steps} steps successful")
        
        if success_steps == total_steps:
            print("🎉 All steps completed successfully!")
            return True
        else:
            print("⚠️ Some steps failed. Check the logs above.")
            return False

    def run_historical_setup(self, days=30):
        """Set up historical content for new deployment"""
        print("🏛️ Running historical content setup")
        print("=" * 50)
        
        # Generate historical content
        file_count = self.generate_historical_content(days)
        
        if file_count > 0:
            # Update sitemap
            self.update_sitemap()
            
            # Build site
            self.build_site()
            
            print(f"🎉 Historical setup complete: {file_count} files generated")
            return True
        else:
            print("❌ Historical setup failed")
            return False

def main():
    """Main function with command line interface"""
    manager = AutoContentManager()
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "daily":
            # Run daily workflow
            manager.run_daily_workflow()
            
        elif command == "historical":
            # Generate historical content
            days = int(sys.argv[2]) if len(sys.argv) > 2 else 30
            manager.run_historical_setup(days)
            
        elif command == "content":
            # Just generate content
            manager.generate_daily_content()
            
        elif command == "cleanup":
            # Just cleanup old content
            days = int(sys.argv[2]) if len(sys.argv) > 2 else 90
            manager.cleanup_old_content(days)
            
        else:
            print("❌ Unknown command. Use: daily, historical, content, or cleanup")
            
    else:
        # Default: run daily workflow
        print("ℹ️ No command specified, running daily workflow")
        print("Available commands:")
        print("  daily      - Run complete daily workflow")
        print("  historical - Generate historical content")
        print("  content    - Generate today's content only")
        print("  cleanup    - Clean up old content")
        print()
        
        manager.run_daily_workflow()

if __name__ == "__main__":
    main()
