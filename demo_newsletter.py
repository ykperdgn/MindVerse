#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📧 Newsletter System Demo
Test newsletter subscription and sending functionality
"""

import sys
from pathlib import Path

# Add the current directory to Python path
sys.path.append(str(Path(__file__).parent))

from advanced_daily_automation import NewsletterSystem

def demo_newsletter_system():
    """Demo newsletter system functionality"""
    print("📧 Newsletter System Demo")
    print("=" * 50)
    
    newsletter = NewsletterSystem()
    
    # Add some test subscribers
    test_subscribers = [
        ("john@example.com", "en"),
        ("ahmet@example.com", "tr"),
        ("mary@example.com", "en"),
        ("zeynep@example.com", "tr"),
        ("carlos@example.com", "en")
    ]
    
    print("👥 Adding test subscribers...")
    for email, language in test_subscribers:
        success, message = newsletter.add_subscriber(email, language)
        status = "✅" if success else "❌"
        print(f"  {status} {email} ({language}): {message}")
    
    # Show subscriber statistics
    subscribers = newsletter.get_subscribers()
    tr_count = len([s for s in subscribers if s['language'] == 'tr'])
    en_count = len([s for s in subscribers if s['language'] == 'en'])
    
    print(f"\n📊 Subscriber Statistics:")
    print(f"  Total: {len(subscribers)}")
    print(f"  Turkish: {tr_count}")
    print(f"  English: {en_count}")
    
    # Demo newsletter sending (without actual email)
    print(f"\n📬 Demo Newsletter Sending...")
    
    # Create dummy article and horoscope data
    recent_articles = [
        "src/content/health/mental-saglik-ve-stres-yonetimi.md",
        "src/content/love/marriage-and-partnership-tips_en.md",
        "src/content/space/future-of-space-travel_en.md"
    ]
    
    recent_horoscopes = [
        "src/content/astrology/koc-gunluk-2025-06-20.md",
        "src/content/astrology/koc-daily-2025-06-20_en.md"
    ]
    
    newsletter.send_weekly_newsletter(recent_articles, recent_horoscopes)
    
    print("\n✅ Newsletter demo completed!")
    print("💡 In production, this would send actual emails via SendGrid/Mailgun")

if __name__ == "__main__":
    demo_newsletter_system()
