#!/usr/bin/env python3
"""
Fix language issues in astrology content files
Replace English terms (Daily, Weekly, Monthly) with Turkish equivalents
"""

import os
import re
import glob

def fix_language_issues():
    """Fix language issues in all astrology content files"""
    
    # Define replacements
    replacements = {
        # Title and content replacements
        'Weekly Yorumu': 'Haftalık Yorumu',
        'Daily Yorumu': 'Günlük Yorumu',
        'Monthly Yorumu': 'Aylık Yorumu',
        
        # Header replacements
        '# Akrep Burcu Weekly Yorumu': '# Akrep Burcu Haftalık Yorumu',
        '# Akrep Burcu Daily Yorumu': '# Akrep Burcu Günlük Yorumu',
        '# Akrep Burcu Monthly Yorumu': '# Akrep Burcu Aylık Yorumu',
        
        # Section headers
        '## 💫 Weekly Genel Durum': '## 💫 Haftalık Genel Durum',
        '## 💫 Daily Genel Durum': '## 💫 Günlük Genel Durum',
        '## 💫 Monthly Genel Durum': '## 💫 Aylık Genel Durum',
        
        # Content text replacements
        'weekly döneminde': 'haftalık döneminde',
        'daily döneminde': 'günlük döneminde',
        'monthly döneminde': 'aylık döneminde',
        
        'weekly boyunca': 'haftalık boyunca',
        'daily boyunca': 'günlük boyunca',
        'monthly boyunca': 'aylık boyunca',
        
        'Bu weekly': 'Bu haftalık',
        'Bu daily': 'Bu günlük',
        'Bu monthly': 'Bu aylık',
        
        # Tags
        '"weekly yorum"': '"haftalık yorum"',
        '"daily yorum"': '"günlük yorum"',
        '"monthly yorum"': '"aylık yorum"',
        
        # Advice sections
        '## 🎯 Weekly Tavsiyeleri': '## 🎯 Haftalık Tavsiyeleri',
        '## 🎯 Daily Tavsiyeleri': '## 🎯 Günlük Tavsiyeleri',
        '## 🎯 Monthly Tavsiyeleri': '## 🎯 Aylık Tavsiyeleri',
        
        # Health sections
        '⚖️ Bu weekly genel': '⚖️ Bu haftalık genel',
        '⚖️ Bu daily genel': '⚖️ Bu günlük genel',
        '⚖️ Bu monthly genel': '⚖️ Bu aylık genel',
        
        # General pattern replacements
        'Weekly': 'Haftalık',
        'Daily': 'Günlük', 
        'Monthly': 'Aylık',
        'weekly': 'haftalık',
        'daily': 'günlük',
        'monthly': 'aylık'
    }
    
    # Get all astrology markdown files
    astrology_path = 'src/content/astrology/*.md'
    files = glob.glob(astrology_path)
    
    fixed_files = []
    
    for file_path in files:
        try:
            # Read file content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Apply replacements
            for old_text, new_text in replacements.items():
                content = content.replace(old_text, new_text)
            
            # Only write if changes were made
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixed_files.append(os.path.basename(file_path))
                print(f"✅ Fixed: {os.path.basename(file_path)}")
            
        except Exception as e:
            print(f"❌ Error processing {file_path}: {e}")
    
    print(f"\n🎉 Language fix complete!")
    print(f"📝 Fixed {len(fixed_files)} files")
    if fixed_files:
        print(f"📋 Fixed files: {', '.join(fixed_files)}")

if __name__ == "__main__":
    fix_language_issues()
