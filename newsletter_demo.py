#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from advanced_daily_automation import NewsletterSystem

def demo_newsletter():
    print("📧 Newsletter Demo")
    newsletter = NewsletterSystem()

    # Add test subscriber
    success, message = newsletter.add_subscriber("test@example.com", "tr")
    print(f"Add subscriber: {success}, {message}")

    # Get subscriber count
    subscribers = newsletter.get_subscribers()
    print(f"Total subscribers: {len(subscribers)}")

    print("✅ Newsletter demo completed!")

if __name__ == "__main__":
    demo_newsletter()
