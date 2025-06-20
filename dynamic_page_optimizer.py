#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MindVerse Blog - Dinamik Sayfa Optimizer
Tüm dinamik sayfaları prerender için düzeltir
"""

import os
import sys
from pathlib import Path
import logging
import re

class DynamicPageOptimizer:
    def __init__(self, base_path=None):
        self.base_path = Path(base_path) if base_path else Path.cwd()
        self.fixed_files = []

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def has_prerender_or_getstaticpaths(self, content):
        """Dosyada prerender veya getStaticPaths var mı kontrol et"""
        return ('export const prerender = true' in content or
                'getStaticPaths' in content)

    def fix_dynamic_page(self, file_path):
        """Dinamik sayfayı düzelt"""
        try:
            content = file_path.read_text(encoding='utf-8')

            # Zaten düzgünse atla
            if self.has_prerender_or_getstaticpaths(content):
                return False

            # Frontmatter'ı bul
            if not content.startswith('---'):
                self.logger.warning(f"Frontmatter bulunamadı: {file_path}")
                return False

            parts = content.split('---', 2)
            if len(parts) < 3:
                self.logger.warning(f"Geçersiz frontmatter: {file_path}")
                return False

            frontmatter = parts[1]
            rest_content = parts[2]

            # Import Layout ekle
            if 'import Layout' not in frontmatter:
                # Layout import'unu belirle
                depth = str(file_path.relative_to(self.base_path / 'src' / 'pages')).count(os.sep)
                layout_path = '../' * (depth + 1) + 'layouts/Layout.astro'

                frontmatter = f'import Layout from "{layout_path}";\\n' + frontmatter

            # prerender ekle
            if 'export const prerender = true' not in frontmatter:
                frontmatter += '\\nexport const prerender = true;\\n'

            # getStaticPaths ekle
            if 'getStaticPaths' not in frontmatter:
                # Dosya adına göre getStaticPaths oluştur
                file_name = file_path.name

                if '[category]' in file_name and '[slug]' in file_name:
                    # Category ve slug var
                    getstaticpaths = '''
export async function getStaticPaths() {
  const categories = ['astrology', 'technology', 'space', 'health', 'psychology', 'love', 'history', 'quotes'];
  return categories.flatMap(category => [
    { params: { category, slug: `${category}-sample-article` } }
  ]);
}

const { category, slug } = Astro.params;'''

                elif '[category]' in file_name:
                    # Sadece category var
                    getstaticpaths = '''
export async function getStaticPaths() {
  return [
    { params: { category: 'astrology' } },
    { params: { category: 'technology' } },
    { params: { category: 'space' } },
    { params: { category: 'health' } },
    { params: { category: 'psychology' } },
    { params: { category: 'love' } },
    { params: { category: 'history' } },
    { params: { category: 'quotes' } }
  ];
}

const { category } = Astro.params;'''

                elif '[slug]' in file_name:
                    # Sadece slug var
                    if 'astrology' in str(file_path):
                        getstaticpaths = '''
export async function getStaticPaths() {
  return [
    { params: { slug: 'koc-burcu-gunluk' } },
    { params: { slug: 'boga-burcu-gunluk' } },
    { params: { slug: 'ikizler-burcu-gunluk' } },
    { params: { slug: 'yengec-burcu-gunluk' } }
  ];
}

const { slug } = Astro.params;'''
                    elif 'daily-horoscopes' in str(file_path):
                        getstaticpaths = '''
export async function getStaticPaths() {
  return [
    { params: { slug: 'aries-daily' } },
    { params: { slug: 'taurus-daily' } },
    { params: { slug: 'gemini-daily' } },
    { params: { slug: 'cancer-daily' } }
  ];
}

const { slug } = Astro.params;'''
                    else:
                        getstaticpaths = '''
export async function getStaticPaths() {
  return [
    { params: { slug: 'sample-article' } }
  ];
}

const { slug } = Astro.params;'''

                frontmatter += getstaticpaths

            # Yeni içeriği oluştur
            new_content = f'---\\n{frontmatter}\\n---{rest_content}'

            # Dosyayı kaydet
            file_path.write_text(new_content, encoding='utf-8')
            self.fixed_files.append(str(file_path))
            self.logger.info(f"✅ Düzeltildi: {file_path}")
            return True

        except Exception as e:
            self.logger.error(f"❌ Hata ({file_path}): {e}")
            return False

    def fix_all_dynamic_pages(self):
        """Tüm dinamik sayfaları düzelt"""
        self.logger.info("🔧 Dinamik sayfa optimizasyonu başlıyor...")

        pages_dir = self.base_path / 'src' / 'pages'
        if not pages_dir.exists():
            self.logger.error("Pages dizini bulunamadı!")
            return []

        # Dinamik sayfaları bul
        dynamic_pages = []
        for astro_file in pages_dir.rglob('*.astro'):
            if '[' in astro_file.name and ']' in astro_file.name:
                dynamic_pages.append(astro_file)

        self.logger.info(f"🔍 {len(dynamic_pages)} dinamik sayfa bulundu")

        for page_file in dynamic_pages:
            self.fix_dynamic_page(page_file)

        self.logger.info(f"🎉 Toplam {len(self.fixed_files)} dosya düzeltildi!")
        return self.fixed_files

def main():
    """Ana fonksiyon"""
    print("🔧 MindVerse Blog - Dinamik Sayfa Optimizer")
    print("=" * 50)

    optimizer = DynamicPageOptimizer()
    fixed_files = optimizer.fix_all_dynamic_pages()

    if fixed_files:
        print(f"\\n✅ Başarıyla düzeltilen dosyalar:")
        for file_path in fixed_files:
            print(f"  - {file_path}")
    else:
        print("\\n✅ Tüm dinamik sayfalar zaten düzgün!")

    return 0

if __name__ == "__main__":
    sys.exit(main())
