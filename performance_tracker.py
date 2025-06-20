#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📊 MindVerse Blog - Gelişmiş Performans Tracker
Advanced Performance Tracking & Analytics
"""

import json
import time
import requests
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional
from collections import defaultdict
import subprocess

class PerformanceTracker:
    def __init__(self):
        self.site_url = "https://www.mindversedaily.com"
        self.data_dir = Path("performance_data")
        self.data_dir.mkdir(exist_ok=True)

        self.metrics_file = self.data_dir / "metrics.json"
        self.reports_dir = Path("reports")
        self.reports_dir.mkdir(exist_ok=True)

        # Performance thresholds
        self.thresholds = {
            "response_time": {"good": 2, "warning": 5, "critical": 10},
            "uptime": {"good": 99.9, "warning": 99.0, "critical": 95.0},
            "content_freshness": {"hours": 24},
            "error_rate": {"good": 0.1, "warning": 1.0, "critical": 5.0}
        }

        print("📊 Performance Tracker başlatıldı...")

    def collect_performance_metrics(self) -> Dict:
        """Performans metriklerini topla"""
        metrics = {
            "timestamp": datetime.now().isoformat(),
            "site_performance": self.measure_site_performance(),
            "content_metrics": self.analyze_content_performance(),
            "seo_metrics": self.collect_seo_metrics(),
            "user_experience": self.measure_user_experience(),
            "technical_metrics": self.collect_technical_metrics()
        }

        # Metrikleri kaydet
        self.save_metrics(metrics)
        return metrics

    def measure_site_performance(self) -> Dict:
        """Site performansı ölçümü"""
        performance = {
            "response_times": [],
            "status_codes": [],
            "ssl_info": {},
            "headers": {}
        }

        # Birden fazla istek yaparak ortalama al
        test_urls = [
            self.site_url,
            f"{self.site_url}/astrology/",
            f"{self.site_url}/astrology/haftalik-astroloji-raporu-2025-06-16"
        ]

        for url in test_urls:
            try:
                start_time = time.time()
                response = requests.get(url, timeout=15)
                end_time = time.time()

                response_time = end_time - start_time
                performance["response_times"].append({
                    "url": url,
                    "time": round(response_time, 3),
                    "status": response.status_code
                })

                performance["status_codes"].append(response.status_code)

                # İlk request için detay bilgiler
                if url == self.site_url:
                    performance["headers"] = dict(response.headers)
                    performance["ssl_info"] = {
                        "secure": response.url.startswith('https://'),
                        "cert_valid": True  # Basit check
                    }

            except Exception as e:
                performance["response_times"].append({
                    "url": url,
                    "error": str(e),
                    "time": -1
                })

        # Ortalama response time
        valid_times = [r["time"] for r in performance["response_times"] if r["time"] > 0]
        performance["avg_response_time"] = sum(valid_times) / len(valid_times) if valid_times else -1

        # Performance score
        performance["score"] = self.calculate_performance_score(performance)

        return performance

    def analyze_content_performance(self) -> Dict:
        """İçerik performansı analizi"""
        content_dir = Path("src/content")

        metrics = {
            "total_files": 0,
            "recent_files": 0,
            "file_sizes": [],
            "content_types": defaultdict(int),
            "content_quality": {}
        }

        cutoff_time = datetime.now() - timedelta(days=7)

        for content_file in content_dir.rglob("*.md"):
            metrics["total_files"] += 1

            # Dosya boyutu
            file_size = content_file.stat().st_size
            metrics["file_sizes"].append(file_size)

            # İçerik türü
            path_parts = content_file.parts
            if "astrology" in path_parts:
                metrics["content_types"]["astrology"] += 1
            elif "blog" in path_parts:
                metrics["content_types"]["blog"] += 1
            else:
                metrics["content_types"]["other"] += 1

            # Son dosyalar
            file_time = datetime.fromtimestamp(content_file.stat().st_mtime)
            if file_time > cutoff_time:
                metrics["recent_files"] += 1

        # İçerik kalitesi metrikleri
        metrics["content_quality"] = {
            "avg_file_size": sum(metrics["file_sizes"]) / len(metrics["file_sizes"]) if metrics["file_sizes"] else 0,
            "content_freshness": metrics["recent_files"] / max(metrics["total_files"], 1) * 100,
            "diversity_score": len(metrics["content_types"]) * 10
        }

        return metrics

    def collect_seo_metrics(self) -> Dict:
        """SEO metriklerini topla"""
        seo_metrics = {
            "meta_coverage": 0,
            "heading_structure": {},
            "image_optimization": {},
            "internal_linking": {},
            "page_speed": {}
        }

        try:
            # Ana sayfa SEO kontrolü
            response = requests.get(self.site_url, timeout=10)
            if response.status_code == 200:
                content = response.text

                # Meta tag kontrolü
                meta_checks = {
                    "title": "<title>" in content,
                    "description": 'name="description"' in content,
                    "og_title": 'property="og:title"' in content,
                    "og_description": 'property="og:description"' in content,
                    "canonical": 'rel="canonical"' in content
                }

                seo_metrics["meta_coverage"] = sum(meta_checks.values()) / len(meta_checks) * 100

                # Heading yapısı
                import re
                h1_count = len(re.findall(r'<h1[^>]*>', content))
                h2_count = len(re.findall(r'<h2[^>]*>', content))
                h3_count = len(re.findall(r'<h3[^>]*>', content))

                seo_metrics["heading_structure"] = {
                    "h1_count": h1_count,
                    "h2_count": h2_count,
                    "h3_count": h3_count,
                    "proper_structure": h1_count == 1 and h2_count > 0
                }

                # Image optimization check
                img_tags = re.findall(r'<img[^>]*>', content)
                imgs_with_alt = len(re.findall(r'<img[^>]*alt=["\'][^"\']*["\'][^>]*>', content))

                seo_metrics["image_optimization"] = {
                    "total_images": len(img_tags),
                    "images_with_alt": imgs_with_alt,
                    "alt_coverage": imgs_with_alt / max(len(img_tags), 1) * 100
                }

        except Exception as e:
            seo_metrics["error"] = str(e)

        return seo_metrics

    def measure_user_experience(self) -> Dict:
        """Kullanıcı deneyimi ölçümü"""
        ux_metrics = {
            "mobile_friendly": True,  # Varsayılan
            "accessibility_score": 0,
            "loading_experience": {},
            "interaction_readiness": {}
        }

        # Lighthouse-style metrikleri simüle et
        try:
            start_time = time.time()
            response = requests.get(self.site_url, timeout=15)
            load_time = time.time() - start_time

            ux_metrics["loading_experience"] = {
                "first_contentful_paint": round(load_time * 0.6, 2),
                "largest_contentful_paint": round(load_time * 0.8, 2),
                "cumulative_layout_shift": round(0.1, 3),  # Simulated
                "first_input_delay": round(100, 0)  # ms
            }

            # UX score hesapla
            lcp = ux_metrics["loading_experience"]["largest_contentful_paint"]
            if lcp < 2.5:
                ux_score = 90
            elif lcp < 4.0:
                ux_score = 70
            else:
                ux_score = 50

            ux_metrics["overall_score"] = ux_score

        except Exception as e:
            ux_metrics["error"] = str(e)

        return ux_metrics

    def collect_technical_metrics(self) -> Dict:
        """Teknik metrikler"""
        tech_metrics = {
            "build_performance": {},
            "deployment_status": {},
            "dependencies": {},
            "code_quality": {}
        }

        # Build performance
        try:
            start_time = time.time()
            result = subprocess.run(
                ["npm", "run", "build"],
                capture_output=True,
                text=True,
                timeout=180
            )
            build_time = time.time() - start_time

            tech_metrics["build_performance"] = {
                "build_time": round(build_time, 2),
                "success": result.returncode == 0,
                "output_size": len(result.stdout) + len(result.stderr)
            }

        except Exception as e:
            tech_metrics["build_performance"] = {"error": str(e)}

        # Package.json analizi
        try:
            with open("package.json", "r") as f:
                package_data = json.load(f)

            tech_metrics["dependencies"] = {
                "total_deps": len(package_data.get("dependencies", {})),
                "dev_deps": len(package_data.get("devDependencies", {})),
                "has_lockfile": Path("package-lock.json").exists()
            }

        except Exception as e:
            tech_metrics["dependencies"] = {"error": str(e)}

        return tech_metrics

    def calculate_performance_score(self, performance_data: Dict) -> int:
        """Performans skoru hesapla"""
        score = 100

        # Response time penalty
        avg_time = performance_data.get("avg_response_time", 0)
        if avg_time > self.thresholds["response_time"]["critical"]:
            score -= 40
        elif avg_time > self.thresholds["response_time"]["warning"]:
            score -= 20
        elif avg_time > self.thresholds["response_time"]["good"]:
            score -= 10

        # Status code penalty
        status_codes = performance_data.get("status_codes", [])
        error_count = sum(1 for code in status_codes if code >= 400)
        if error_count > 0:
            score -= error_count * 15

        # SSL bonus
        if performance_data.get("ssl_info", {}).get("secure"):
            score += 5

        return max(0, min(100, score))

    def save_metrics(self, metrics: Dict):
        """Metrikleri kaydet"""
        historical_data = []

        if self.metrics_file.exists():
            try:
                with open(self.metrics_file, 'r') as f:
                    historical_data = json.load(f)
            except:
                historical_data = []

        historical_data.append(metrics)

        # Son 1000 kayıt tut
        if len(historical_data) > 1000:
            historical_data = historical_data[-1000:]

        with open(self.metrics_file, 'w') as f:
            json.dump(historical_data, f, indent=2, ensure_ascii=False)

    def generate_performance_report(self, days: int = 7) -> str:
        """Performans raporu oluştur"""
        if not self.metrics_file.exists():
            return "Performans verisi bulunamadı"

        try:
            with open(self.metrics_file, 'r') as f:
                data = json.load(f)
        except:
            return "Veri okuma hatası"

        if not data:
            return "Veri boş"

        # Son N gün verilerini filtrele
        cutoff_time = datetime.now() - timedelta(days=days)
        recent_data = []

        for entry in data:
            try:
                entry_time = datetime.fromisoformat(entry['timestamp'].replace('Z', '+00:00'))
                if entry_time > cutoff_time:
                    recent_data.append(entry)
            except:
                continue

        if not recent_data:
            return f"Son {days} gün veri yok"

        # Analiz
        response_times = []
        performance_scores = []
        uptime_data = []

        for entry in recent_data:
            site_perf = entry.get('site_performance', {})

            if 'avg_response_time' in site_perf and site_perf['avg_response_time'] > 0:
                response_times.append(site_perf['avg_response_time'])

            if 'score' in site_perf:
                performance_scores.append(site_perf['score'])

            # Uptime calculation
            status_codes = site_perf.get('status_codes', [])
            if status_codes:
                successful_requests = sum(1 for code in status_codes if 200 <= code < 400)
                uptime_data.append(successful_requests / len(status_codes) * 100)

        # İstatistikler
        avg_response = sum(response_times) / len(response_times) if response_times else 0
        avg_performance = sum(performance_scores) / len(performance_scores) if performance_scores else 0
        avg_uptime = sum(uptime_data) / len(uptime_data) if uptime_data else 0

        # Trend analizi
        if len(performance_scores) >= 2:
            recent_avg = sum(performance_scores[-5:]) / min(5, len(performance_scores))
            older_avg = sum(performance_scores[:-5]) / max(1, len(performance_scores) - 5)
            trend = "📈 İyileşiyor" if recent_avg > older_avg else "📉 Kötüleşiyor" if recent_avg < older_avg else "➡️ Stabil"
        else:
            trend = "➡️ Yeterli veri yok"

        # Rapor oluştur
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_file = self.reports_dir / f"performance_report_{timestamp}.md"

        report_content = f"""# 📊 Performans Analiz Raporu
**Tarih:** {datetime.now().strftime("%d %B %Y, %H:%M")}
**Periode:** Son {days} gün
**Veri Noktası:** {len(recent_data)} ölçüm

---

## 🎯 Özet Metrikler

### Performans Skoru
- **Ortalama:** {avg_performance:.1f}/100
- **Trend:** {trend}
- **Durum:** {'🟢 İyi' if avg_performance >= 80 else '🟡 Orta' if avg_performance >= 60 else '🔴 Kötü'}

### Site Hızı
- **Ortalama Response Time:** {avg_response:.2f} saniye
- **Durum:** {'🟢 Hızlı' if avg_response < 2 else '🟡 Orta' if avg_response < 5 else '🔴 Yavaş'}

### Uptime
- **Ortalama Uptime:** %{avg_uptime:.2f}
- **Durum:** {'🟢 Mükemmel' if avg_uptime >= 99.9 else '🟡 İyi' if avg_uptime >= 99 else '🔴 Sorunlu'}

---

## 📈 Detaylı Analiz

### Response Time Dağılımı
"""

        if response_times:
            min_time = min(response_times)
            max_time = max(response_times)
            report_content += f"""
- **En Hızlı:** {min_time:.2f}s
- **En Yavaş:** {max_time:.2f}s
- **Medyan:** {sorted(response_times)[len(response_times)//2]:.2f}s
"""

        report_content += f"""

### Son 5 Ölçüm
"""

        # Son 5 ölçümü göster
        for i, entry in enumerate(recent_data[-5:], 1):
            timestamp = entry['timestamp'][:19]
            site_perf = entry.get('site_performance', {})
            score = site_perf.get('score', 0)
            response_time = site_perf.get('avg_response_time', 0)

            status_emoji = "🟢" if score >= 80 else "🟡" if score >= 60 else "🔴"
            report_content += f"**{i}.** {timestamp} - {status_emoji} Score: {score}/100, Time: {response_time:.2f}s\n"

        report_content += f"""

---

## 🔍 İçerik Performansı

### İçerik Metrikleri (Son Ölçüm)
"""

        if recent_data:
            content_metrics = recent_data[-1].get('content_metrics', {})
            quality = content_metrics.get('content_quality', {})

            report_content += f"""
- **Toplam Dosya:** {content_metrics.get('total_files', 0)}
- **Son Hafta Yeni:** {content_metrics.get('recent_files', 0)}
- **İçerik Tazelik:** %{quality.get('content_freshness', 0):.1f}
- **Çeşitlilik Skoru:** {quality.get('diversity_score', 0)}
"""

        report_content += f"""

---

## 🎯 SEO Performansı

### SEO Metrikleri (Son Ölçüm)
"""

        if recent_data:
            seo_metrics = recent_data[-1].get('seo_metrics', {})

            report_content += f"""
- **Meta Tag Kapsamı:** %{seo_metrics.get('meta_coverage', 0):.1f}
- **Görsel Alt Text:** %{seo_metrics.get('image_optimization', {}).get('alt_coverage', 0):.1f}
- **Heading Yapısı:** {'✅ Uygun' if seo_metrics.get('heading_structure', {}).get('proper_structure') else '❌ Düzeltilmeli'}
"""

        report_content += f"""

---

## 💡 Öneriler

### Performans İyileştirme
"""

        # Performansa göre öneriler
        if avg_response > 5:
            report_content += "- 🔴 **Kritik:** Response time çok yüksek - CDN ve caching optimizasyonu gerekli\n"
        elif avg_response > 2:
            report_content += "- 🟡 **Uyarı:** Response time iyileştirilebilir - Image optimization önerili\n"
        else:
            report_content += "- 🟢 **İyi:** Response time kabul edilebilir seviyede\n"

        if avg_uptime < 99:
            report_content += "- 🔴 **Kritik:** Uptime düşük - hosting ve monitoring kontrolü gerekli\n"
        elif avg_uptime < 99.9:
            report_content += "- 🟡 **Uyarı:** Uptime iyileştirilebilir - redundancy eklenebilir\n"
        else:
            report_content += "- 🟢 **Mükemmel:** Uptime hedef seviyede\n"

        report_content += f"""

### Sonraki Adımlar
1. **Performans İzleme:** Günlük otomatik kontroller
2. **Trend Analizi:** Haftalık performans değerlendirmesi
3. **Optimizasyon:** Belirlenen sorun alanlarında iyileştirme
4. **Monitoring Alerts:** Kritik threshold'lar için uyarı sistemi

---

**Rapor Oluşturma:** {datetime.now().strftime("%d %B %Y, %H:%M:%S")}
**Sonraki Rapor:** 1 hafta sonra önerilir

*Bu rapor Performance Tracker tarafından otomatik oluşturulmuştur.*
"""

        # Raporu kaydet
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report_content)

        print(f"📊 Performans raporu oluşturuldu: {report_file}")
        return str(report_file)

    def run_continuous_monitoring(self, interval_minutes: int = 30):
        """Sürekli izleme"""
        print(f"🔄 Sürekli performans izleme başlatıldı (her {interval_minutes} dakika)")
        print("CTRL+C ile durdurun")

        try:
            while True:
                print(f"\n📊 {datetime.now().strftime('%H:%M:%S')} - Performans ölçümü...")
                metrics = self.collect_performance_metrics()

                # Anlık sonuçları göster
                site_perf = metrics.get('site_performance', {})
                score = site_perf.get('score', 0)
                response_time = site_perf.get('avg_response_time', 0)

                status_emoji = "🟢" if score >= 80 else "🟡" if score >= 60 else "🔴"
                print(f"   {status_emoji} Score: {score}/100, Response: {response_time:.2f}s")

                # Kritik durumlar için uyarı
                if score < 50:
                    print("   🚨 KRITIK: Performans çok düşük!")
                elif response_time > 10:
                    print("   ⚠️ UYARI: Response time çok yüksek!")

                # Bekleme
                time.sleep(interval_minutes * 60)

        except KeyboardInterrupt:
            print("\n⏹️ Sürekli izleme durduruldu")

    def run_interactive_mode(self):
        """İnteraktif performans tracker"""
        print("\n📊 Performans Tracker")
        print("=" * 30)

        while True:
            print("\n🔧 Performans Seçenekleri:")
            print("1. 📊 Anlık Performans Ölçümü")
            print("2. 📈 Performans Raporu (7 gün)")
            print("3. 📈 Performans Raporu (30 gün)")
            print("4. 🔄 Sürekli İzleme Başlat")
            print("5. 📋 Geçmiş Veriler")
            print("6. 🎯 Performans Skoru Detayı")
            print("7. ⚙️ Threshold Ayarları")
            print("8. 📤 Rapor Dışa Aktar")
            print("9. Çıkış")

            choice = input("\nSeçiminiz (1-9): ").strip()

            if choice == "1":
                print("📊 Performans ölçümü yapılıyor...")
                metrics = self.collect_performance_metrics()

                site_perf = metrics.get('site_performance', {})
                content_perf = metrics.get('content_metrics', {})
                seo_perf = metrics.get('seo_metrics', {})

                print(f"\n🎯 Performans Sonuçları:")
                print(f"   Site Skoru: {site_perf.get('score', 0)}/100")
                print(f"   Response Time: {site_perf.get('avg_response_time', 0):.2f}s")
                print(f"   İçerik Dosyası: {content_perf.get('total_files', 0)}")
                print(f"   SEO Kapsamı: %{seo_perf.get('meta_coverage', 0):.1f}")

            elif choice == "2":
                report_file = self.generate_performance_report(7)
                print(f"📈 7 günlük rapor oluşturuldu: {report_file}")

            elif choice == "3":
                report_file = self.generate_performance_report(30)
                print(f"📈 30 günlük rapor oluşturuldu: {report_file}")

            elif choice == "4":
                interval = input("İzleme aralığı (dakika, varsayılan 30): ").strip()
                interval = int(interval) if interval.isdigit() else 30
                self.run_continuous_monitoring(interval)

            elif choice == "5":
                if self.metrics_file.exists():
                    with open(self.metrics_file, 'r') as f:
                        data = json.load(f)
                    print(f"📋 Toplam veri noktası: {len(data)}")
                    if data:
                        print(f"   İlk kayıt: {data[0]['timestamp'][:19]}")
                        print(f"   Son kayıt: {data[-1]['timestamp'][:19]}")
                else:
                    print("📋 Henüz veri kaydı yok")

            elif choice == "6":
                print("🎯 Performans Skoru Kriterleri:")
                print("   100-80: 🟢 Mükemmel")
                print("   79-60:  🟡 İyi")
                print("   59-40:  🟠 Orta")
                print("   39-0:   🔴 Kötü")
                print("\n   Faktörler:")
                print("   • Response Time (en önemli)")
                print("   • HTTP Status Codes")
                print("   • SSL Security")
                print("   • Error Rate")

            elif choice == "7":
                print("⚙️ Mevcut Threshold'lar:")
                for metric, values in self.thresholds.items():
                    print(f"   {metric}: {values}")

            elif choice == "8":
                print("📤 Rapor dışa aktarma özellikleri:")
                print("   • Markdown raporları reports/ klasöründe")
                print("   • JSON verileri performance_data/ klasöründe")
                print("   • Geçmiş tüm veriler metrics.json'da")

            elif choice == "9":
                print("👋 Performance Tracker kapatılıyor...")
                break

            else:
                print("❌ Geçersiz seçim (1-9 arası)")

def main():
    """Ana fonksiyon"""
    tracker = PerformanceTracker()
    tracker.run_interactive_mode()

if __name__ == "__main__":
    main()
