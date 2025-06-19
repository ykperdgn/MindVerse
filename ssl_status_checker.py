#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SSL Certificate Status Checker for mindversedaily.com
"""

import requests
import time
import ssl
import socket
from datetime import datetime

def check_ssl_status(domain):
    """Check SSL certificate status for a domain."""
    try:
        # Try HTTPS connection
        response = requests.get(f"https://{domain}", timeout=10)
        if response.status_code == 200:
            print(f"✅ HTTPS working for {domain}")
            return True
    except requests.exceptions.SSLError:
        print(f"❌ SSL Certificate not ready for {domain}")
        return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection error for {domain}: {e}")
        return False

def check_http_status(domain):
    """Check HTTP status to ensure site is accessible."""
    try:
        response = requests.get(f"http://{domain}", timeout=10)
        if response.status_code == 200:
            print(f"✅ HTTP working for {domain}")
            return True
    except requests.exceptions.RequestException as e:
        print(f"❌ HTTP error for {domain}: {e}")
        return False

def check_ssl_certificate_details(domain):
    """Get SSL certificate details if available."""
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                print(f"📋 SSL Certificate found for {domain}")
                print(f"   Issuer: {cert.get('issuer', 'Unknown')}")
                print(f"   Subject: {cert.get('subject', 'Unknown')}")
                return True
    except Exception as e:
        print(f"🔍 No SSL certificate yet for {domain}: {e}")
        return False

def monitor_ssl_status():
    """Monitor SSL status for mindversedaily.com domains."""
    domains = ["www.mindversedaily.com", "mindversedaily.com"]

    print(f"🔍 SSL Certificate Status Check - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    for domain in domains:
        print(f"\n🌐 Checking {domain}:")

        # Check HTTP first
        http_status = check_http_status(domain)

        # Check HTTPS
        https_status = check_ssl_status(domain)

        # Get certificate details if available
        if https_status:
            check_ssl_certificate_details(domain)

        print(f"   Status: HTTP {'✅' if http_status else '❌'} | HTTPS {'✅' if https_status else '❌'}")

    print("\n" + "=" * 60)
    if any(check_ssl_status(d) for d in domains):
        print("🎉 SSL is working! You can now enable 'Enforce HTTPS' in GitHub Pages settings.")
    else:
        print("⏳ SSL certificates are still being generated. Please wait 5-10 more minutes.")
        print("💡 Manual check: https://github.com/ykperdgn/MindVerse/settings/pages")

if __name__ == "__main__":
    monitor_ssl_status()
