#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MindVerse Blog - Akıllı Site Optimizer ve Hata Giderici
Tüm site yapısını analiz eder ve otomatik olarak hataları giderir
"""

import os
import json
import re
import sys
import logging
from pathlib import Path
from datetime import datetime
import requests
from urllib.parse import urljoin, urlparse
import time

class IntelligentSiteOptimizer:
    def __init__(self, base_path=None):
        self.base_path = Path(base_path) if base_path else Path.cwd()
        self.errors_found = []
        self.fixes_applied = []
        self.warnings = []

        # Logging setup
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('site_optimization.log', encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def log_issue(self, issue_type, description, file_path=None, fix_applied=None):
        """Issue logging"""
        issue = {
            'timestamp': datetime.now().isoformat(),
            'type': issue_type,
            'description': description,
            'file': str(file_path) if file_path else None,
            'fix_applied': fix_applied
        }

        if issue_type == 'ERROR':
            self.errors_found.append(issue)
        elif issue_type == 'WARNING':
            self.warnings.append(issue)
        elif issue_type == 'FIX':
            self.fixes_applied.append(issue)

        self.logger.info(f"{issue_type}: {description}")

    def check_file_structure(self):
        """Dosya yapısını kontrol et"""
        self.logger.info("🔍 Dosya yapısı analizi başlıyor...")

        essential_files = [
            'package.json',
            'astro.config.mjs',
            'vercel.json',
            'src/layouts/Layout.astro',
            'src/pages/index.astro'
        ]

        for file_path in essential_files:
            full_path = self.base_path / file_path
            if not full_path.exists():
                self.log_issue('ERROR', f'Kritik dosya eksik: {file_path}', full_path)
            else:
                self.logger.info(f"✅ {file_path} mevcut")

    def check_content_structure(self):
        """Content yapısını kontrol et"""
        self.logger.info("📄 İçerik yapısı analizi başlıyor...")

        content_dir = self.base_path / 'src' / 'content'
        if not content_dir.exists():
            self.log_issue('ERROR', 'Content dizini bulunamadı', content_dir)
            return

        # Content kategorilerini kontrol et
        categories = ['astrology', 'technology', 'space', 'health', 'psychology', 'love', 'history', 'quotes']

        for category in categories:
            cat_dir = content_dir / category
            if cat_dir.exists():
                # Boş dosyaları kontrol et
                md_files = list(cat_dir.glob('*.md'))
                empty_files = [f for f in md_files if f.stat().st_size == 0]

                if empty_files:
                    for empty_file in empty_files:
                        self.log_issue('ERROR', f'Boş içerik dosyası: {empty_file}', empty_file)
                        # Boş dosyayı sil
                        try:
                            empty_file.unlink()
                            self.log_issue('FIX', f'Boş dosya silindi: {empty_file}', empty_file, True)
                        except Exception as e:
                            self.log_issue('ERROR', f'Dosya silinemedi: {e}', empty_file)

                self.logger.info(f"📁 {category}: {len(md_files)} dosya")
            else:
                self.log_issue('WARNING', f'Kategori dizini eksik: {category}', cat_dir)

    def check_astro_pages(self):
        """Astro sayfalarını kontrol et"""
        self.logger.info("🚀 Astro sayfa yapısı analizi başlıyor...")

        pages_dir = self.base_path / 'src' / 'pages'
        if not pages_dir.exists():
            self.log_issue('ERROR', 'Pages dizini bulunamadı', pages_dir)
            return

        # Tüm .astro dosyalarını bul
        astro_files = list(pages_dir.rglob('*.astro'))

        for astro_file in astro_files:
            try:
                content = astro_file.read_text(encoding='utf-8')

                # Syntax hatalarını kontrol et
                if '---' not in content:
                    self.log_issue('WARNING', f'Frontmatter eksik: {astro_file}', astro_file)

                # Dinamik sayfalar için getStaticPaths kontrolü
                if '[' in astro_file.name and ']' in astro_file.name:
                    if 'getStaticPaths' not in content and 'export const prerender = true' not in content:
                        self.log_issue('WARNING', f'Dinamik sayfa için getStaticPaths veya prerender eksik: {astro_file}', astro_file)

            except Exception as e:
                self.log_issue('ERROR', f'Dosya okuma hatası: {e}', astro_file)

    def check_configuration_files(self):
        """Konfigürasyon dosyalarını kontrol et"""
        self.logger.info("⚙️ Konfigürasyon dosyası analizi başlıyor...")

        # astro.config.mjs kontrolü
        astro_config = self.base_path / 'astro.config.mjs'
        if astro_config.exists():
            try:
                content = astro_config.read_text(encoding='utf-8')

                # Syntax kontrolü
                if 'export default defineConfig' not in content:
                    self.log_issue('ERROR', 'astro.config.mjs syntax hatası', astro_config)

                # Vercel adapter kontrolü
                if '@astrojs/vercel' not in content:
                    self.log_issue('WARNING', 'Vercel adapter eksik', astro_config)

                self.logger.info("✅ astro.config.mjs kontrol edildi")
            except Exception as e:
                self.log_issue('ERROR', f'astro.config.mjs okuma hatası: {e}', astro_config)

        # vercel.json kontrolü
        vercel_config = self.base_path / 'vercel.json'
        if vercel_config.exists():
            try:
                with open(vercel_config, 'r', encoding='utf-8') as f:
                    config = json.load(f)

                if 'framework' not in config:
                    self.log_issue('WARNING', 'Framework belirtilmemiş', vercel_config)

                self.logger.info("✅ vercel.json kontrol edildi")
            except json.JSONDecodeError as e:
                self.log_issue('ERROR', f'vercel.json JSON hatası: {e}', vercel_config)
            except Exception as e:
                self.log_issue('ERROR', f'vercel.json okuma hatası: {e}', vercel_config)

    def check_routes_and_links(self):
        """Route'ları ve linkleri kontrol et"""
        self.logger.info("🔗 Route ve link analizi başlıyor...")

        # Route çakışmalarını kontrol et
        pages_dir = self.base_path / 'src' / 'pages'
        if pages_dir.exists():
            routes = []

            for astro_file in pages_dir.rglob('*.astro'):
                # Route path'ini hesapla
                relative_path = astro_file.relative_to(pages_dir)
                route_path = str(relative_path).replace('\\', '/').replace('.astro', '')

                # index.astro dosyaları için özel durum
                if route_path.endswith('/index'):
                    route_path = route_path[:-6] or '/'

                routes.append((route_path, astro_file))

            # Çakışmaları kontrol et
            route_counts = {}
            for route, file_path in routes:
                if route not in route_counts:
                    route_counts[route] = []
                route_counts[route].append(file_path)

            for route, files in route_counts.items():
                if len(files) > 1:
                    self.log_issue('ERROR', f'Route çakışması: {route} -> {files}')

    def fix_dynamic_pages(self):
        """Dinamik sayfaları düzelt"""
        self.logger.info("🔧 Dinamik sayfa optimizasyonu başlıyor...")

        pages_dir = self.base_path / 'src' / 'pages'
        if not pages_dir.exists():
            return

        dynamic_pages = []
        for astro_file in pages_dir.rglob('*.astro'):
            if '[' in astro_file.name and ']' in astro_file.name:
                dynamic_pages.append(astro_file)

        for page_file in dynamic_pages:
            try:
                content = page_file.read_text(encoding='utf-8')

                # Eğer getStaticPaths yoksa ve prerender da yoksa ekle
                if 'getStaticPaths' not in content and 'export const prerender = true' not in content:
                    # Frontmatter bölümünü bul
                    if content.startswith('---'):
                        parts = content.split('---', 2)
                        if len(parts) >= 3:
                            frontmatter = parts[1]
                            rest_content = parts[2]

                            # prerender ekle
                            new_frontmatter = frontmatter.strip() + '\\nexport const prerender = true;\\n'
                            new_content = f'---\\n{new_frontmatter}---{rest_content}'

                            page_file.write_text(new_content, encoding='utf-8')
                            self.log_issue('FIX', f'Dinamik sayfa için prerender eklendi: {page_file}', page_file, True)

            except Exception as e:
                self.log_issue('ERROR', f'Dinamik sayfa düzeltme hatası: {e}', page_file)

    def optimize_content_files(self):
        """Content dosyalarını optimize et"""
        self.logger.info("📝 İçerik dosyası optimizasyonu başlıyor...")

        content_dir = self.base_path / 'src' / 'content'
        if not content_dir.exists():
            return

        for md_file in content_dir.rglob('*.md'):
            try:
                content = md_file.read_text(encoding='utf-8')

                # Frontmatter kontrolü
                if not content.startswith('---'):
                    self.log_issue('WARNING', f'Frontmatter eksik: {md_file}', md_file)
                    continue

                # Minimum alan kontrolü
                frontmatter_match = re.match(r'^---\\n(.*?)\\n---', content, re.DOTALL)
                if frontmatter_match:
                    frontmatter = frontmatter_match.group(1)
                    required_fields = ['title', 'date', 'summary', 'tags']

                    for field in required_fields:
                        if f'{field}:' not in frontmatter:
                            self.log_issue('WARNING', f'Gerekli alan eksik ({field}): {md_file}', md_file)

            except Exception as e:
                self.log_issue('ERROR', f'İçerik dosyası okuma hatası: {e}', md_file)

    def check_build_performance(self):
        """Build performansını kontrol et"""
        self.logger.info("⚡ Build performans analizi başlıyor...")

        # Bundle analizi için dist klasörünü kontrol et
        dist_dir = self.base_path / 'dist'
        if dist_dir.exists():
            # Büyük dosyaları bul
            large_files = []
            for file_path in dist_dir.rglob('*'):
                if file_path.is_file():
                    size_mb = file_path.stat().st_size / (1024 * 1024)
                    if size_mb > 1:  # 1MB'den büyük dosyalar
                        large_files.append((file_path, size_mb))

            if large_files:
                for file_path, size in sorted(large_files, key=lambda x: x[1], reverse=True):
                    self.log_issue('WARNING', f'Büyük dosya tespit edildi: {file_path} ({size:.2f}MB)')

    def generate_optimization_report(self):
        """Optimizasyon raporu oluştur"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'errors_found': len(self.errors_found),
                'warnings': len(self.warnings),
                'fixes_applied': len(self.fixes_applied)
            },
            'errors': self.errors_found,
            'warnings': self.warnings,
            'fixes': self.fixes_applied
        }

        report_file = self.base_path / 'SITE_OPTIMIZATION_REPORT.json'
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        # Markdown raporu da oluştur
        md_report = self.generate_markdown_report()
        md_file = self.base_path / 'SITE_OPTIMIZATION_REPORT.md'
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(md_report)

        self.logger.info(f"📊 Optimizasyon raporu oluşturuldu: {report_file}")
        return report

    def generate_markdown_report(self):
        """Markdown format rapor oluştur"""
        report = f"""# 🔧 MindVerse Blog - Site Optimizasyon Raporu
**Tarih:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 📊 Özet
- **Bulunan Hatalar:** {len(self.errors_found)}
- **Uyarılar:** {len(self.warnings)}
- **Uygulanan Düzeltmeler:** {len(self.fixes_applied)}

## 🚨 Kritik Hatalar
"""

        if self.errors_found:
            for i, error in enumerate(self.errors_found, 1):
                report += f"### {i}. {error['description']}\\n"
                if error['file']:
                    report += f"**Dosya:** `{error['file']}`\\n"
                report += f"**Zaman:** {error['timestamp']}\\n\\n"
        else:
            report += "✅ Kritik hata bulunamadı!\\n\\n"

        report += "## ⚠️ Uyarılar\\n"

        if self.warnings:
            for i, warning in enumerate(self.warnings, 1):
                report += f"### {i}. {warning['description']}\\n"
                if warning['file']:
                    report += f"**Dosya:** `{warning['file']}`\\n"
                report += f"**Zaman:** {warning['timestamp']}\\n\\n"
        else:
            report += "✅ Uyarı bulunamadı!\\n\\n"

        report += "## ✅ Uygulanan Düzeltmeler\\n"

        if self.fixes_applied:
            for i, fix in enumerate(self.fixes_applied, 1):
                report += f"### {i}. {fix['description']}\\n"
                if fix['file']:
                    report += f"**Dosya:** `{fix['file']}`\\n"
                report += f"**Zaman:** {fix['timestamp']}\\n\\n"
        else:
            report += "ℹ️ Otomatik düzeltme uygulanmadı.\\n\\n"

        report += f"""
## 🎯 Öneriler

### Performans Optimizasyonu
- Büyük dosyaları sıkıştırın
- Görsel optimizasyonu yapın
- CSS/JS minification kullanın

### SEO Optimizasyonu
- Meta etiketlerini kontrol edin
- Sitemap güncelleyin
- Robot.txt dosyasını gözden geçirin

### Güvenlik
- HTTPS kullanın
- Güvenlik başlıklarını ekleyin
- Dependency'leri güncelleyin

---
*Rapor oluşturma zamanı: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""

        return report

    def run_full_optimization(self):
        """Tam optimizasyon süreci"""
        self.logger.info("🚀 MindVerse Blog - Kapsamlı Site Optimizasyonu Başlıyor")
        self.logger.info("=" * 60)

        try:
            # 1. Dosya yapısı kontrolü
            self.check_file_structure()

            # 2. İçerik yapısı kontrolü
            self.check_content_structure()

            # 3. Astro sayfaları kontrolü
            self.check_astro_pages()

            # 4. Konfigürasyon kontrolü
            self.check_configuration_files()

            # 5. Route ve link kontrolü
            self.check_routes_and_links()

            # 6. Dinamik sayfa düzeltmeleri
            self.fix_dynamic_pages()

            # 7. İçerik optimizasyonu
            self.optimize_content_files()

            # 8. Build performans kontrolü
            self.check_build_performance()

            # 9. Rapor oluştur
            report = self.generate_optimization_report()

            self.logger.info("=" * 60)
            self.logger.info("✅ Site optimizasyonu tamamlandı!")
            self.logger.info(f"📊 Toplam hata: {len(self.errors_found)}")
            self.logger.info(f"⚠️ Toplam uyarı: {len(self.warnings)}")
            self.logger.info(f"🔧 Uygulanan düzeltme: {len(self.fixes_applied)}")

            return report

        except Exception as e:
            self.logger.error(f"Optimizasyon sırasında hata: {e}")
            return None

def main():
    """Ana fonksiyon"""
    print("🔧 MindVerse Blog - Akıllı Site Optimizer")
    print("=" * 50)

    optimizer = IntelligentSiteOptimizer()
    report = optimizer.run_full_optimization()

    if report:
        print("\\n🎉 Optimizasyon başarıyla tamamlandı!")
        print(f"📊 Detaylı rapor: SITE_OPTIMIZATION_REPORT.md")
    else:
        print("❌ Optimizasyon sırasında hata oluştu!")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
