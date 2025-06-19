#!/usr/bin/env python3
"""
Automated Daily Deployment Script for MindVerse Blog
Handles daily content generation, builds, and deployment
"""

import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
import json

class AutomatedDeployment:
    def __init__(self):
        self.project_root = Path.cwd()
        self.log_file = self.project_root / 'deployment.log'

    def log(self, message, level="INFO"):
        """Log messages with timestamp"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] [{level}] {message}"
        print(log_entry)

        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry + '\n')

    def run_command(self, command, description=""):
        """Run a shell command and log the result"""
        try:
            self.log(f"Running: {command}")
            result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=self.project_root)

            if result.returncode == 0:
                self.log(f"✅ {description} completed successfully")
                if result.stdout:
                    self.log(f"Output: {result.stdout.strip()}")
                return True
            else:
                self.log(f"❌ {description} failed: {result.stderr}", "ERROR")
                return False

        except Exception as e:
            self.log(f"❌ Error running {command}: {str(e)}", "ERROR")
            return False

    def generate_daily_content(self):
        """Generate today's horoscope content"""
        self.log("🔄 Generating daily horoscope content...")

        success = self.run_command(
            "python bilingual_content_generator.py daily",
            "Daily content generation"
        )

        if success:
            self.log("✅ Daily content generation completed")
        else:
            self.log("❌ Daily content generation failed", "ERROR")

        return success

    def build_site(self):
        """Build the Astro site"""
        self.log("🏗️ Building Astro site...")

        success = self.run_command(
            "npm run build",
            "Site build"
        )

        if success:
            self.log("✅ Site build completed")
        else:
            self.log("❌ Site build failed", "ERROR")

        return success

    def check_build_stats(self):
        """Check and log build statistics"""
        try:
            dist_path = self.project_root / 'dist'
            if dist_path.exists():
                # Count HTML files
                html_files = list(dist_path.rglob('*.html'))
                self.log(f"📊 Build statistics: {len(html_files)} HTML pages generated")

                # Log some key pages
                key_pages = [
                    'index.html',
                    'en/index.html',
                    'astrology/index.html',
                    'en/astrology/index.html'
                ]

                for page in key_pages:
                    page_path = dist_path / page
                    if page_path.exists():
                        self.log(f"✅ Key page exists: /{page}")
                    else:
                        self.log(f"⚠️ Key page missing: /{page}", "WARNING")

                return True
            else:
                self.log("❌ Dist directory not found", "ERROR")
                return False

        except Exception as e:
            self.log(f"❌ Error checking build stats: {str(e)}", "ERROR")
            return False

    def deploy_to_vercel(self):
        """Deploy to Vercel (if configured)"""
        self.log("🚀 Checking Vercel deployment...")

        # Check if vercel.json exists
        if (self.project_root / 'vercel.json').exists():
            success = self.run_command(
                "vercel --prod",
                "Vercel deployment"
            )

            if success:
                self.log("✅ Vercel deployment completed")
            else:
                self.log("❌ Vercel deployment failed", "ERROR")

            return success
        else:
            self.log("ℹ️ Vercel not configured, skipping deployment")
            return True

    def deploy_to_github_pages(self):
        """Deploy to GitHub Pages (if configured)"""
        self.log("🚀 Checking GitHub Pages deployment...")

        # Check if .github/workflows exists
        github_workflows = self.project_root / '.github' / 'workflows'
        if github_workflows.exists():
            # Commit and push changes
            commands = [
                "git add .",
                f'git commit -m "Daily content update - {datetime.now().strftime(\"%Y-%m-%d\")}"',
                "git push origin main"
            ]

            all_success = True
            for cmd in commands:
                success = self.run_command(cmd, f"Git operation: {cmd}")
                if not success:
                    all_success = False
                    break

            if all_success:
                self.log("✅ GitHub Pages deployment initiated")
            else:
                self.log("❌ GitHub Pages deployment failed", "ERROR")

            return all_success
        else:
            self.log("ℹ️ GitHub Pages not configured, skipping deployment")
            return True

    def cleanup_old_content(self, days_to_keep=90):
        """Clean up content older than specified days"""
        self.log(f"🧹 Cleaning up content older than {days_to_keep} days...")

        try:
            cutoff_date = datetime.now() - timedelta(days=days_to_keep)
            content_dir = self.project_root / 'src' / 'content' / 'astrology'

            if not content_dir.exists():
                self.log("ℹ️ No content directory found, skipping cleanup")
                return True

            deleted_count = 0
            for md_file in content_dir.glob('*.md'):
                # Extract date from filename (format: YYYY-MM-DD-...)
                filename = md_file.name
                if len(filename) >= 10:
                    try:
                        file_date_str = filename[:10]
                        file_date = datetime.strptime(file_date_str, '%Y-%m-%d')

                        if file_date < cutoff_date:
                            md_file.unlink()
                            deleted_count += 1

                    except ValueError:
                        # Skip files that don't match the date pattern
                        continue

            self.log(f"✅ Cleanup completed: {deleted_count} old files removed")
            return True

        except Exception as e:
            self.log(f"❌ Cleanup failed: {str(e)}", "ERROR")
            return False

    def generate_deployment_report(self):
        """Generate a deployment report"""
        self.log("📊 Generating deployment report...")

        try:
            report = {
                'timestamp': datetime.now().isoformat(),
                'date': datetime.now().strftime('%Y-%m-%d'),
                'deployment_status': 'completed',
                'site_stats': {}
            }

            # Count content files
            content_dir = self.project_root / 'src' / 'content' / 'astrology'
            if content_dir.exists():
                md_files = list(content_dir.glob('*.md'))
                report['site_stats']['total_horoscope_files'] = len(md_files)

            # Check dist directory
            dist_path = self.project_root / 'dist'
            if dist_path.exists():
                html_files = list(dist_path.rglob('*.html'))
                report['site_stats']['total_html_pages'] = len(html_files)

            # Save report
            report_file = self.project_root / 'deployment_report.json'
            with open(report_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)

            self.log(f"✅ Deployment report saved: {report_file}")
            self.log(f"📈 Total horoscope files: {report['site_stats'].get('total_horoscope_files', 0)}")
            self.log(f"📄 Total HTML pages: {report['site_stats'].get('total_html_pages', 0)}")

            return True

        except Exception as e:
            self.log(f"❌ Failed to generate report: {str(e)}", "ERROR")
            return False

    def run_full_deployment(self):
        """Run the complete daily deployment process"""
        self.log("🚀 Starting automated daily deployment...")
        self.log("=" * 60)

        start_time = datetime.now()
        success_steps = 0
        total_steps = 7

        steps = [
            ("Generate daily content", self.generate_daily_content),
            ("Build site", self.build_site),
            ("Check build stats", self.check_build_stats),
            ("Deploy to Vercel", self.deploy_to_vercel),
            ("Deploy to GitHub Pages", self.deploy_to_github_pages),
            ("Cleanup old content", self.cleanup_old_content),
            ("Generate report", self.generate_deployment_report)
        ]

        for step_name, step_function in steps:
            self.log(f"🔄 Step: {step_name}")
            if step_function():
                success_steps += 1
                self.log(f"✅ {step_name} completed")
            else:
                self.log(f"❌ {step_name} failed", "ERROR")

        end_time = datetime.now()
        duration = end_time - start_time

        self.log("=" * 60)
        self.log(f"🎯 Deployment completed: {success_steps}/{total_steps} steps successful")
        self.log(f"⏱️ Total duration: {duration}")

        if success_steps == total_steps:
            self.log("✅ All deployment steps completed successfully!")
            return True
        else:
            self.log(f"⚠️ Deployment completed with {total_steps - success_steps} failures", "WARNING")
            return False

def main():
    """Main function"""
    deployment = AutomatedDeployment()

    if len(sys.argv) > 1:
        command = sys.argv[1].lower()

        if command == "daily":
            deployment.run_full_deployment()
        elif command == "content":
            deployment.generate_daily_content()
        elif command == "build":
            deployment.build_site()
        elif command == "deploy":
            success = deployment.deploy_to_vercel() and deployment.deploy_to_github_pages()
            if success:
                print("✅ Deployment completed successfully")
            else:
                print("❌ Deployment failed")
        elif command == "cleanup":
            deployment.cleanup_old_content()
        elif command == "report":
            deployment.generate_deployment_report()
        else:
            print("Usage: python automated_deployment.py [daily|content|build|deploy|cleanup|report]")
    else:
        # Default: run full deployment
        deployment.run_full_deployment()

if __name__ == "__main__":
    main()
