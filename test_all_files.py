#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Script for Astrology System
Tests all components and reports issues
"""

import os
import sys
import importlib.util

def test_file_syntax(filename):
    """Test if a Python file has valid syntax"""
    try:
        spec = importlib.util.spec_from_file_location("module", filename)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return True, "OK"
    except SyntaxError as e:
        return False, f"Syntax Error: {e}"
    except ImportError as e:
        return False, f"Import Error: {e}"
    except Exception as e:
        return False, f"Other Error: {e}"

def main():
    """Main test function"""
    print("🔍 Testing Python Files for Syntax Issues")
    print("=" * 50)

    python_files = [
        "astrology_content_generator.py",
        "enhanced_astrology_generator.py",
        "batch_astrology_generator.py",
        "astrology_content_manager.py",
        "simple_astrology_manager.py",
        "auto_social_poster.py",
        "automated_deployment.py",
        "content_enhancer.py",
        "fix_turkish_encoding.py"
    ]

    results = {}

    for filename in python_files:
        if os.path.exists(filename):
            success, message = test_file_syntax(filename)
            results[filename] = (success, message)

            if success:
                print(f"✅ {filename}: {message}")
            else:
                print(f"❌ {filename}: {message}")
        else:
            results[filename] = (False, "File not found")
            print(f"⚠️  {filename}: File not found")

    print("\n" + "=" * 50)
    print("📊 SUMMARY")
    print("=" * 50)

    working_files = [f for f, (success, _) in results.items() if success]
    broken_files = [f for f, (success, _) in results.items() if not success]

    print(f"✅ Working files: {len(working_files)}")
    print(f"❌ Broken files: {len(broken_files)}")

    if broken_files:
        print(f"\n🔧 Files needing fixes:")
        for filename in broken_files:
            print(f"   - {filename}: {results[filename][1]}")

    # Test basic astrology functionality
    print(f"\n🧪 Testing Basic Functionality")
    print("-" * 30)

    try:
        # Try to create a simple astrology content
        print("Testing astrology content creation...")

        # Import working modules
        if "simple_astrology_manager.py" in working_files:
            from simple_astrology_manager import SimpleAstrologyManager
            manager = SimpleAstrologyManager()
            print("✅ Simple astrology manager loaded successfully")
        else:
            print("❌ No working astrology manager found")

    except Exception as e:
        print(f"❌ Functionality test failed: {e}")

if __name__ == "__main__":
    main()
