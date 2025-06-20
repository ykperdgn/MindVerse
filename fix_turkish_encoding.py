#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import codecs

def fix_turkish_characters():
    """Astroloji dosyalarındaki Türkçe karakter sorunlarını düzelt"""

    # Karakter düzeltme eşlemeleri - daha kapsamlı
    char_fixes = {
        'G�nl�k': 'Günlük',
        'g�nl�k': 'günlük',
        'Haftal�k': 'Haftalık',
        'haftal�k': 'haftalık',
        'Ayl�k': 'Aylık',
        'ayl�k': 'aylık',
        '�zel': 'Özel',
        '�nemli': 'Önemli',
        'kar��la��r': 'karşılaşır',
        'de�er': 'değer',
        'g�n': 'gün',
        'b�y�k': 'büyük',
        'd�nem': 'dönem',
        '��kan': 'çıkan',
        'k���k': 'küçük',
        'ad�m': 'adım',
        'g��l�': 'güçlü',
        'ba�ar�': 'başarı',
        'ge�i�': 'geçiş',
        'ili�ki': 'ilişki',
        '�ok': 'çok',
        'y�ksek': 'yüksek',
        '��k��': 'çıkış',
        'g�r��': 'görüş',
        'd���nce': 'düşünce',
        'y�r�t': 'yürüt',
        '�al��ma': 'çalışma',
        'ki�i': 'kişi',
        'ya�am': 'yaşam',
        'b�t�n': 'bütün',
        'do�al': 'doğal',
        'i�in': 'için',
        'ge�en': 'geçen',
        'y�l': 'yıl',
        'a�k': 'aşk',
        'evlilik': 'evlilik',
        'a�': 'aş',
        's�re�': 'süreç',
        '��z�m': 'çözüm',
        # Unicode replacement characters
        '\ufffd': '',  # Remove replacement characters
        'Gï¿½nlï¿½k': 'Günlük',
        'gï¿½nlï¿½k': 'günlük',    }

    astrology_dir = "src/content/astrology"

    if not os.path.exists(astrology_dir):
        print(f"Directory {astrology_dir} not found!")
        return

    files = glob.glob(os.path.join(astrology_dir, "*.md"))
    fixed_count = 0

    for file_path in files:
        try:
            # Farklı encoding'lerle deneyelim
            content = None
            for encoding in ['utf-8', 'cp1254', 'iso-8859-9', 'latin1']:
                try:
                    with open(file_path, 'r', encoding=encoding) as f:
                        content = f.read()
                    break
                except UnicodeDecodeError:
                    continue

            if content is None:
                print(f"Could not read {file_path} with any encoding")
                continue

            original_content = content

            print(f"Processing: {os.path.basename(file_path)}")

            # Karakter düzeltmelerini uygula
            changes_made = False
            for wrong, correct in char_fixes.items():
                if wrong in content:
                    content = content.replace(wrong, correct)
                    changes_made = True
                    print(f"  Replaced '{wrong}' with '{correct}'")

            # Eğer değişiklik varsa dosyayı UTF-8 olarak kaydet
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✓ Fixed: {os.path.basename(file_path)}")
                fixed_count += 1
            else:
                print(f"  No changes needed")

        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    print(f"\nTotal files fixed: {fixed_count}")

if __name__ == "__main__":
    fix_turkish_characters()
