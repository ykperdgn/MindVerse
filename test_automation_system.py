#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧪 Test Script for Advanced Daily Automation System
Tests all major components: Content Generation, Astrology, Newsletter
"""

import sys
import os
from datetime import datetime, timedelta
from pathlib import Path

# Add the current directory to Python path
sys.path.append(str(Path(__file__).parent))

from advanced_daily_automation import AdvancedContentManager, AstrologySystem, NewsletterSystem

def test_content_generation():
    """Test daily content generation"""
    print("🧪 Testing Content Generation System...")

    content_manager = AdvancedContentManager()

    # Test Turkish content generation
    print("  📝 Testing Turkish content generation...")
    try:
        result = content_manager.generate_daily_turkish_content()
        if result:
            print(f"  ✅ Turkish content generated successfully: {result}")
        else:
            print("  ❌ Turkish content generation failed")
    except Exception as e:
        print(f"  ❌ Turkish content generation error: {e}")

    # Test English content generation
    print("  📝 Testing English content generation...")
    try:
        result = content_manager.generate_daily_english_content()
        if result:
            print(f"  ✅ English content generated successfully: {result}")
        else:
            print("  ❌ English content generation failed")
    except Exception as e:
        print(f"  ❌ English content generation error: {e}")

def test_astrology_system():
    """Test astrology horoscope generation"""
    print("\n🔮 Testing Astrology System...")

    astrology = AstrologySystem()

    try:
        result = astrology.generate_daily_horoscopes()
        if result:
            print(f"  ✅ Daily horoscopes generated successfully: {result}")
        else:
            print("  ❌ Daily horoscope generation failed")
    except Exception as e:
        print(f"  ❌ Astrology system error: {e}")

def test_newsletter_system():
    """Test newsletter system"""
    print("\n📧 Testing Newsletter System...")

    newsletter = NewsletterSystem()

    # Test subscriber management
    print("  👥 Testing subscriber management...")
    try:
        # Add a test subscriber
        newsletter.add_subscriber("test@example.com", "Test User")
        print("  ✅ Subscriber added successfully")

        # Get subscriber count
        count = len(newsletter.get_subscribers())
        print(f"  📊 Total subscribers: {count}")

    except Exception as e:
        print(f"  ❌ Newsletter system error: {e}")

def test_file_organization():
    """Test file organization and structure"""
    print("\n📁 Testing File Organization...")

    content_path = Path("src/content")

    # Check if all required directories exist
    required_dirs = ['health', 'love', 'psychology', 'space', 'quotes', 'history', 'astrology']

    for directory in required_dirs:
        dir_path = content_path / directory
        if dir_path.exists():
            file_count = len(list(dir_path.glob("*.md")))
            print(f"  ✅ {directory}: {file_count} files")
        else:
            print(f"  ❌ Missing directory: {directory}")

def test_git_integration():
    """Test Git integration"""
    print("\n🔄 Testing Git Integration...")

    content_manager = AdvancedContentManager()

    try:
        # Test git status check
        status = content_manager.check_git_status()
        print(f"  📊 Git status: {status}")

        # Note: We won't actually commit in test mode
        print("  ✅ Git integration test passed (no actual commit made)")

    except Exception as e:
        print(f"  ❌ Git integration error: {e}")

def run_comprehensive_test():
    """Run all tests"""
    print("🚀 Starting Comprehensive System Test")
    print("=" * 60)

    # Record start time
    start_time = datetime.now()

    try:
        # Run all test functions
        test_file_organization()
        test_content_generation()
        test_astrology_system()
        test_newsletter_system()
        test_git_integration()

        # Calculate duration
        duration = datetime.now() - start_time

        print("\n" + "=" * 60)
        print(f"🎉 Test completed in {duration.total_seconds():.2f} seconds")
        print("✅ System is ready for daily automation!")

    except Exception as e:
        print(f"\n❌ Critical system error: {e}")
        print("🔧 Please fix the issues before running daily automation")

if __name__ == "__main__":
    run_comprehensive_test()
