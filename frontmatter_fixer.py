#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MindVerse Blog - Frontmatter Fixer
Eksik frontmatter'lı Astro dosyalarını otomatik olarak düzeltir
"""

import os
import sys
from pathlib import Path
import logging

class FrontmatterFixer:
    def __init__(self, base_path=None):
        self.base_path = Path(base_path) if base_path else Path.cwd()
        self.fixed_files = []

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def get_frontmatter_template(self, file_path):
        """Dosya tipine göre uygun frontmatter template döndürür"""

        file_name = file_path.name.lower()

        templates = {
            'contact.astro': {
                'title': 'İletişim - MindVerse Daily',
                'description': 'MindVerse Daily ile iletişime geçin. Sorularınız, önerileriniz için bize ulaşın.',
                'layout': '../layouts/Layout.astro'
            },
            'privacy-policy.astro': {
                'title': 'Gizlilik Politikası - MindVerse Daily',
                'description': 'MindVerse Daily gizlilik politikası ve kişisel veri kullanım koşulları.',
                'layout': '../layouts/Layout.astro'
            },
            'terms.astro': {
                'title': 'Kullanım Koşulları - MindVerse Daily',
                'description': 'MindVerse Daily kullanım koşulları ve hizmet şartları.',
                'layout': '../layouts/Layout.astro'
            },
            'astrology-test.astro': {
                'title': 'Astroloji Test - MindVerse Daily',
                'description': 'Astroloji bilginizi test edin, kişilik özelliklerinizi keşfedin.',
                'layout': '../layouts/Layout.astro'
            },
            'index_new.astro': {
                'title': 'Ana Sayfa (Test) - MindVerse Daily',
                'description': 'MindVerse Daily test ana sayfası.',
                'layout': '../layouts/Layout.astro'
            }
        }

        # Admin sayfaları için
        if 'admin' in str(file_path):
            admin_name = file_path.name.replace('.astro', '')
            return {
                'title': f'Admin {admin_name.title()} - MindVerse Daily',
                'description': f'MindVerse Daily admin paneli - {admin_name}',
                'layout': '../../layouts/Layout.astro'
            }

        # Dinamik sayfalar için
        if '[' in file_name and ']' in file_name:
            if 'category' in file_name and 'slug' in file_name:
                return {
                    'title': 'Makale - MindVerse Daily',
                    'description': 'MindVerse Daily makale sayfası',
                    'layout': '../../layouts/Layout.astro',
                    'prerender': True
                }
            elif 'category' in file_name:
                return {
                    'title': 'Kategori - MindVerse Daily',
                    'description': 'MindVerse Daily kategori sayfası',
                    'layout': '../../layouts/Layout.astro',
                    'prerender': True
                }

        # Varsayılan template
        return templates.get(file_name, {
            'title': 'MindVerse Daily',
            'description': 'MindVerse Daily - Astroloji, teknoloji ve yaşam',
            'layout': '../layouts/Layout.astro'
        })

    def create_frontmatter(self, template_data):
        """Template'den frontmatter string oluşturur"""
        frontmatter = "---\n"

        for key, value in template_data.items():
            if isinstance(value, bool):
                frontmatter += f"export const {key} = {str(value).lower()};\n"
            elif isinstance(value, str):
                frontmatter += f'{key}: "{value}"\n'
            else:
                frontmatter += f'{key}: {value}\n'

        frontmatter += "---\n\n"
        return frontmatter

    def get_basic_content(self, file_path):
        """Dosya tipine göre temel içerik döndürür"""

        file_name = file_path.name.lower()

        if file_name == 'contact.astro':
            return '''<Layout title="İletişim - MindVerse Daily" description="MindVerse Daily ile iletişime geçin.">
    <main class="container mx-auto px-4 py-8">
        <h1 class="text-4xl font-bold mb-8 text-center">İletişim</h1>
        <div class="max-w-2xl mx-auto">
            <p class="text-lg mb-6 text-center">
                Sorularınız, önerileriniz veya işbirliği teklifleriniz için bizimle iletişime geçebilirsiniz.
            </p>

            <div class="bg-blue-50 dark:bg-blue-900/20 p-6 rounded-lg">
                <h2 class="text-2xl font-semibold mb-4">İletişim Bilgileri</h2>
                <div class="space-y-3">
                    <p><strong>E-posta:</strong> info@mindversedaily.com</p>
                    <p><strong>Website:</strong> www.mindversedaily.com</p>
                </div>
            </div>
        </div>
    </main>
</Layout>'''

        elif file_name == 'privacy-policy.astro':
            return '''<Layout title="Gizlilik Politikası - MindVerse Daily" description="MindVerse Daily gizlilik politikası.">
    <main class="container mx-auto px-4 py-8">
        <h1 class="text-4xl font-bold mb-8 text-center">Gizlilik Politikası</h1>
        <div class="max-w-4xl mx-auto prose dark:prose-invert">
            <h2>Kişisel Verilerin Korunması</h2>
            <p>MindVerse Daily olarak, kullanıcılarımızın gizliliğini korumayı öncelik olarak görüyoruz.</p>

            <h2>Toplanan Veriler</h2>
            <p>Sitemizi ziyaret ettiğinizde, aşağıdaki veriler toplanabilir:</p>
            <ul>
                <li>IP adresi</li>
                <li>Tarayıcı bilgileri</li>
                <li>Ziyaret edilen sayfalar</li>
                <li>Ziyaret zamanı</li>
            </ul>

            <h2>Verilerin Kullanımı</h2>
            <p>Toplanan veriler sadece site performansını iyileştirmek ve kullanıcı deneyimini geliştirmek için kullanılır.</p>
        </div>
    </main>
</Layout>'''

        elif file_name == 'terms.astro':
            return '''<Layout title="Kullanım Koşulları - MindVerse Daily" description="MindVerse Daily kullanım koşulları.">
    <main class="container mx-auto px-4 py-8">
        <h1 class="text-4xl font-bold mb-8 text-center">Kullanım Koşulları</h1>
        <div class="max-w-4xl mx-auto prose dark:prose-invert">
            <h2>Hizmet Koşulları</h2>
            <p>MindVerse Daily web sitesini kullanarak aşağıdaki koşulları kabul etmiş sayılırsınız.</p>

            <h2>İçerik Kullanımı</h2>
            <p>Sitemizdeki içerikler telif hakları ile korunmaktadır. İzinsiz kullanım yasaktır.</p>

            <h2>Sorumluluk Reddi</h2>
            <p>Astroloji içerikleri eğlence amaçlıdır. Hayati kararlar için profesyonel danışmanlık alınması önerilir.</p>
        </div>
    </main>
</Layout>'''

        elif 'admin' in str(file_path):
            admin_name = file_path.name.replace('.astro', '')
            return f'''<Layout title="Admin {admin_name.title()} - MindVerse Daily" description="Admin paneli">
    <main class="container mx-auto px-4 py-8">
        <h1 class="text-3xl font-bold mb-8">Admin - {admin_name.title()}</h1>
        <div class="bg-yellow-50 dark:bg-yellow-900/20 p-4 rounded-lg">
            <p>Bu sayfa geliştirilme aşamasındadır.</p>
        </div>
    </main>
</Layout>'''

        else:
            return '''<Layout title="MindVerse Daily" description="Astroloji, teknoloji ve yaşam">
    <main class="container mx-auto px-4 py-8">
        <h1 class="text-3xl font-bold mb-8">MindVerse Daily</h1>
        <p>Bu sayfa geliştirilme aşamasındadır.</p>
    </main>
</Layout>'''

    def fix_file(self, file_path):
        """Tek dosyayı düzeltir"""
        try:
            # Dosya içeriğini oku
            if file_path.stat().st_size == 0:
                # Boş dosya - tamamen yeniden oluştur
                template_data = self.get_frontmatter_template(file_path)
                frontmatter = self.create_frontmatter(template_data)
                content = self.get_basic_content(file_path)

                new_content = frontmatter + content

            else:
                # İçerik var ama frontmatter eksik
                content = file_path.read_text(encoding='utf-8')

                if not content.startswith('---'):
                    template_data = self.get_frontmatter_template(file_path)
                    frontmatter = self.create_frontmatter(template_data)

                    new_content = frontmatter + content
                else:
                    # Zaten frontmatter var
                    return False

            # Dosyayı yaz
            file_path.write_text(new_content, encoding='utf-8')
            self.fixed_files.append(str(file_path))
            self.logger.info(f"✅ Düzeltildi: {file_path}")
            return True

        except Exception as e:
            self.logger.error(f"❌ Hata ({file_path}): {e}")
            return False

    def fix_all_files(self):
        """Tüm problematic dosyaları düzeltir"""
        self.logger.info("🔧 Frontmatter düzeltme işlemi başlıyor...")

        pages_dir = self.base_path / 'src' / 'pages'
        if not pages_dir.exists():
            self.logger.error("Pages dizini bulunamadı!")
            return

        # Tüm .astro dosyalarını bul
        astro_files = list(pages_dir.rglob('*.astro'))

        for astro_file in astro_files:
            try:
                # Dosya boyutunu kontrol et veya frontmatter var mı bak
                if astro_file.stat().st_size == 0:
                    self.fix_file(astro_file)
                else:
                    content = astro_file.read_text(encoding='utf-8')
                    if not content.startswith('---'):
                        self.fix_file(astro_file)

            except Exception as e:
                self.logger.error(f"Dosya kontrol hatası ({astro_file}): {e}")

        self.logger.info(f"🎉 Toplam {len(self.fixed_files)} dosya düzeltildi!")
        return self.fixed_files

def main():
    """Ana fonksiyon"""
    print("🔧 MindVerse Blog - Frontmatter Fixer")
    print("=" * 40)

    fixer = FrontmatterFixer()
    fixed_files = fixer.fix_all_files()

    if fixed_files:
        print(f"\\n✅ Başarıyla düzeltilen dosyalar:")
        for file_path in fixed_files:
            print(f"  - {file_path}")
    else:
        print("\\n✅ Tüm dosyalar zaten düzgün!")

    return 0

if __name__ == "__main__":
    sys.exit(main())
