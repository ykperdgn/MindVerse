#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎛️ MindVerse Blog - Merkezi Kontrol Paneli
Central Control Dashboard for Site Management
"""

import os
import sys
import json
import time
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List
import requests

# Import our custom modules
MODULES_LOADED = False
try:
    from site_management_agent import MindVerseSiteAgent
    from auto_monitoring_system import AutoMonitoringSystem
    from performance_tracker import PerformanceTracker
    MODULES_LOADED = True
except ImportError as e:
    print(f"⚠️ Module import hatası: {e}")
    print("Lütfen tüm gerekli dosyaların mevcut olduğundan emin olun. Bazı özellikler devre dışı kalacak.")


class MindVerseControlCenter:
    def __init__(self):
        self.site_url = "https://mindversedaily.com"
        self.project_dir = Path(".")

        # Alt sistemleri başlat
        self.site_agent = None
        self.monitoring_system = None
        self.performance_tracker = None

        if MODULES_LOADED:
            try:
                self.site_agent = MindVerseSiteAgent()
                self.monitoring_system = AutoMonitoringSystem()
                self.performance_tracker = PerformanceTracker()
            except Exception as e:
                print(f"⚠️ Alt sistem başlatma hatası: {e}")

        # Dashboard durumu
        self.dashboard_data = {
            "last_update": datetime.now().isoformat(),
            "system_status": "online",
            "active_modules": [name for name, mod in [("SiteAgent", self.site_agent), ("Monitoring", self.monitoring_system), ("Performance", self.performance_tracker)] if mod]
        }

        print("🎛️ MindVerse Kontrol Merkezi başlatıldı...")
        if not MODULES_LOADED:
            print("🔥 UYARI: Gerekli modüller yüklenemedi. İşlevsellik sınırlı olacak.")

    def get_system_overview(self) -> Dict:
        """Sistem genel durumu"""
        overview = {
            "timestamp": datetime.now().isoformat(),
            "site_status": self.check_site_status(),
            "content_status": self.check_content_status(),
            "performance_status": self.check_performance_status(),
            "security_status": self.check_security_status(),
            "deployment_status": self.check_deployment_status()
        }

        return overview

    def check_site_status(self) -> Dict:
        """Site durum kontrolü"""
        try:
            start_time = time.time()
            response = requests.get(self.site_url, timeout=10)
            response_time = time.time() - start_time

            return {
                "status": "online" if response.status_code == 200 else "offline",
                "response_time": round(response_time, 2),
                "status_code": response.status_code,
                "ssl_active": response.url.startswith('https://'),
                "last_check": datetime.now().isoformat()
            }
        except Exception as e:
            return {
                "status": "offline",
                "error": str(e),
                "last_check": datetime.now().isoformat()
            }

    def check_content_status(self) -> Dict:
        """İçerik durum kontrolü"""
        content_dir = Path("src/content")

        if not content_dir.exists():
            return {"status": "error", "message": "Content directory not found"}

        today = datetime.now().date()
        today_str = today.strftime("%Y-%m-%d")

        # Bugünkü içerik sayısı
        today_files = list(content_dir.rglob(f"*{today_str}*.md"))
        total_files = list(content_dir.rglob("*.md"))

        return {
            "status": "good" if len(today_files) >= 12 else "warning",
            "today_content": len(today_files),
            "total_content": len(total_files),
            "last_update": datetime.now().isoformat()
        }

    def check_performance_status(self) -> Dict:
        """Performans durum kontrolü"""
        try:
            if self.performance_tracker:
                # Son performans verisini al
                metrics_file = Path("performance_data/metrics.json")
                if metrics_file.exists():
                    with open(metrics_file, 'r') as f:
                        data = json.load(f)

                    if data:
                        latest = data[-1]
                        site_perf = latest.get('site_performance', {})
                        score = site_perf.get('score', 0)

                        return {
                            "status": "good" if score >= 80 else "warning" if score >= 60 else "critical",
                            "score": score,
                            "response_time": site_perf.get('avg_response_time', 0),
                            "last_check": latest.get('timestamp', '')
                        }

            return {"status": "unknown", "message": "No performance data available"}

        except Exception as e:
            return {"status": "error", "error": str(e)}

    def check_security_status(self) -> Dict:
        """Güvenlik durum kontrolü"""
        security_checks = {
            "https_enabled": False,
            "env_protected": False,
            "dependencies_safe": True
        }

        # HTTPS kontrolü
        try:
            response = requests.get(self.site_url, timeout=5)
            security_checks["https_enabled"] = response.url.startswith('https://')
        except:
            pass

        # .env koruması kontrolü
        gitignore_path = Path(".gitignore")
        if gitignore_path.exists():
            try:
                with open(gitignore_path, 'r') as f:
                    content = f.read()
                    security_checks["env_protected"] = ".env" in content
            except:
                pass

        # Güvenlik skoru hesapla
        score = sum(security_checks.values()) / len(security_checks) * 100

        return {
            "status": "good" if score >= 80 else "warning" if score >= 60 else "critical",
            "score": round(score, 1),
            "checks": security_checks,
            "last_check": datetime.now().isoformat()
        }

    def check_deployment_status(self) -> Dict:
        """Deployment durum kontrolü"""
        try:
            # Git status
            git_result = subprocess.run(
                ["git", "status", "--porcelain"],
                capture_output=True,
                text=True,
                timeout=10
            )

            has_changes = bool(git_result.stdout.strip())

            # Vercel status (basit check)
            vercel_result = subprocess.run(
                ["npx", "vercel", "ls"],
                capture_output=True,
                text=True,
                timeout=30
            )

            vercel_connected = vercel_result.returncode == 0

            return {
                "status": "synced" if not has_changes else "pending",
                "git_changes": has_changes,
                "vercel_connected": vercel_connected,
                "last_check": datetime.now().isoformat()
            }

        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "last_check": datetime.now().isoformat()
            }

    def run_quick_health_check(self) -> Dict:
        """Hızlı sağlık kontrolü"""
        print("🔍 Hızlı sağlık kontrolü yapılıyor...")

        health_data = {
            "timestamp": datetime.now().isoformat(),
            "overall_status": "healthy",
            "issues": [],
            "checks": {}
        }

        # Site erişilebilirlik
        site_status = self.check_site_status()
        health_data["checks"]["site"] = site_status
        if site_status["status"] != "online":
            health_data["issues"].append("Site offline")
            health_data["overall_status"] = "critical"

        # İçerik güncelliği
        content_status = self.check_content_status()
        health_data["checks"]["content"] = content_status
        if content_status["status"] == "warning":
            health_data["issues"].append("Eksik günlük içerik")
            if health_data["overall_status"] == "healthy":
                health_data["overall_status"] = "warning"

        # Deployment durumu
        deployment_status = self.check_deployment_status()
        health_data["checks"]["deployment"] = deployment_status
        if deployment_status["status"] == "pending":
            health_data["issues"].append("Pending git changes")

        return health_data

    def execute_automated_tasks(self) -> Dict:
        """Otomatik görevleri çalıştır"""
        print("🤖 Otomatik görevler çalıştırılıyor...")

        results = {
            "timestamp": datetime.now().isoformat(),
            "tasks_run": [],
            "successes": 0,
            "failures": 0
        }

        # Görev listesi
        tasks = [
            ("Content Generation", self.generate_daily_content),
            ("Performance Check", self.run_performance_check),
            ("SEO Optimization", self.run_seo_optimization),
            ("Security Scan", self.run_security_scan),
            ("Auto Deploy", self.auto_deploy_if_needed)
        ]

        for task_name, task_func in tasks:
            try:
                print(f"   ⏳ {task_name}...")
                result = task_func()
                results["tasks_run"].append({
                    "name": task_name,
                    "status": "success",
                    "result": result
                })
                results["successes"] += 1
                print(f"   ✅ {task_name} tamamlandı")
            except Exception as e:
                results["tasks_run"].append({
                    "name": task_name,
                    "status": "failed",
                    "error": str(e)
                })
                results["failures"] += 1
                print(f"   ❌ {task_name} başarısız: {e}")

        return results

    def generate_daily_content(self) -> str:
        """Günlük içerik oluşturma"""
        try:
            result = subprocess.run(
                ["python", "enhanced_daily_automation.py"],
                capture_output=True,
                text=True,
                timeout=120
            )
            return "Content generation completed" if result.returncode == 0 else f"Failed: {result.stderr}"
        except Exception as e:
            return f"Error: {e}"

    def run_performance_check(self) -> str:
        """Performans kontrolü"""
        if self.performance_tracker:
            try:
                metrics = self.performance_tracker.collect_performance_metrics()
                score = metrics.get('site_performance', {}).get('score', 0)
                return f"Performance score: {score}/100"
            except Exception as e:
                return f"Error: {e}"
        return "Performance tracker not available"

    def run_seo_optimization(self) -> str:
        """SEO optimizasyonu"""
        try:
            # SEO script varsa çalıştır
            if Path("generate_enhanced_seo.py").exists():
                result = subprocess.run(
                    ["python", "generate_enhanced_seo.py"],
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                return "SEO optimization completed" if result.returncode == 0 else "SEO optimization failed"
            return "SEO script not found"
        except Exception as e:
            return f"Error: {e}"

    def run_security_scan(self) -> str:
        """Güvenlik taraması"""
        security_status = self.check_security_status()
        score = security_status.get('score', 0)
        return f"Security score: {score}/100"

    def auto_deploy_if_needed(self) -> str:
        """Gerekirse otomatik deploy"""
        deployment_status = self.check_deployment_status()

        if deployment_status.get("git_changes"):
            try:
                # Auto commit ve deploy
                subprocess.run(["git", "add", "."], check=True, timeout=30)
                subprocess.run([
                    "git", "commit", "-m",
                    f"🤖 Auto-update {datetime.now().strftime('%Y-%m-%d %H:%M')}"
                ], check=True, timeout=30)
                subprocess.run(["git", "push"], check=True, timeout=60)
                subprocess.run(["npx", "vercel", "--prod"], check=True, timeout=300)
                return "Auto-deployed successfully"
            except Exception as e:
                return f"Auto-deploy failed: {e}"

        return "No deployment needed"

    def generate_dashboard_report(self) -> str:
        """Dashboard raporu oluştur"""
        overview = self.get_system_overview()
        health = self.run_quick_health_check()

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_file = Path(f"reports/dashboard_report_{timestamp}.md")
        report_file.parent.mkdir(exist_ok=True)

        site_status = overview.get('site_status', {})
        content_status = overview.get('content_status', {})
        performance_status = overview.get('performance_status', {})
        security_status = overview.get('security_status', {})
        deployment_status = overview.get('deployment_status', {})

        report_content = f"""# 🎛️ MindVerse Kontrol Paneli Raporu
**Tarih:** {datetime.now().strftime("%d %B %Y, %H:%M")}
**Genel Durum:** {health.get('overall_status', 'unknown').upper()}

---

## 🎯 Sistem Durumu Özeti

### Site Durumu
- **Status:** {'🟢 Online' if site_status.get('status') == 'online' else '🔴 Offline'}
- **Response Time:** {site_status.get('response_time', 'N/A')}s
- **SSL:** {'✅ Aktif' if site_status.get('ssl_active') else '❌ Pasif'}

### İçerik Durumu
- **Status:** {'🟢 İyi' if content_status.get('status') == 'good' else '🟡 Uyarı'}
- **Bugünkü İçerik:** {content_status.get('today_content', 'N/A')}/12
- **Toplam İçerik:** {content_status.get('total_content', 'N/A')}

### Performans Durumu
- **Status:** {performance_status.get('status', 'N/A')}
- **Skor:** {performance_status.get('score', 'N/A')}/100
- **Response Time:** {performance_status.get('response_time', 'N/A')}s

### Güvenlik Durumu
- **Status:** {security_status.get('status', 'N/A')}
- **Skor:** {security_status.get('score', 'N/A')}/100
- **HTTPS:** {'✅' if security_status.get('checks', {}).get('https_enabled') else '❌'}

### Deployment Durumu
- **Status:** {deployment_status.get('status', 'N/A')}
- **Git Changes:** {'✅ Var' if deployment_status.get('git_changes') else '❌ Yok'}
- **Vercel:** {'✅ Bağlı' if deployment_status.get('vercel_connected') else '❌ Sorun'}

---

## ⚠️ Tespit Edilen Sorunlar

"""

        if health.get('issues'):
            for i, issue in enumerate(health['issues'], 1):
                report_content += f"{i}. {issue}\n"
        else:
            report_content += "🟢 Herhangi bir sorun tespit edilmedi\n"

        report_content += f"""

---

## 📊 Detaylı Metrikler

### Site Performansı
- Response Time: {site_status.get('response_time', 'N/A')}s
- Status Code: {site_status.get('status_code', 'N/A')}
- SSL Security: {'Aktif' if site_status.get('ssl_active') else 'Pasif'}

### İçerik Analizi
- Günlük İçerik Oranı: {content_status.get('today_content', 0)}/12 (%{content_status.get('today_content', 0)/12*100:.1f} if isinstance(content_status.get('today_content'), int) else 'N/A')
- Toplam İçerik Hacmi: {content_status.get('total_content', 'N/A')} dosya

### Güvenlik Kontrolleri
- HTTPS: {'✅' if security_status.get('checks', {}).get('https_enabled') else '❌'}
- Env Protection: {'✅' if security_status.get('checks', {}).get('env_protected') else '❌'}
- Dependencies: {'✅' if security_status.get('checks', {}).get('dependencies_safe') else '❌'}

---

## 🎯 Önerilen Eylemler

"""

        # Duruma göre öneriler
        if health.get('overall_status') == 'critical':
            report_content += "🚨 **KRİTİK:** Acil müdahale gerekli\n"
            report_content += "1. Site erişilebilirlik kontrolü\n"
            report_content += "2. Server logları inceleme\n"
            report_content += "3. Hosting provider kontrol\n"
        elif health.get('overall_status') == 'warning':
            report_content += "⚠️ **UYARI:** İyileştirme gerekli\n"
            report_content += "1. Eksik içerik tamamlama\n"
            report_content += "2. Performans optimizasyonu\n"
            report_content += "3. Günlük izleme aktivasyonu\n"
        else:
            report_content += "✅ **İYİ:** Rutin bakım yeterli\n"
            report_content += "1. Günlük otomatik kontrole devam\n"
            report_content += "2. İçerik planlaması\n"
            report_content += "3. Performans izleme\n"

        report_content += f"""

---

**Rapor Oluşturma:** {datetime.now().strftime("%d %B %Y, %H:%M:%S")}
**Sonraki Kontrol:** 4 saat sonra önerilir

*Bu rapor MindVerse Kontrol Merkezi tarafından otomatik oluşturulmuştur.*
"""

        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report_content)

        return str(report_file)

    def run_interactive_dashboard(self):
        """İnteraktif kontrol paneli"""
        print("\n🎛️ MindVerse Merkezi Kontrol Paneli")
        print("=" * 50)

        while True:
            # Dashboard header
            overview = self.get_system_overview()
            site_status = "🟢" if overview['site_status']['status'] == 'online' else "🔴"
            content_status = "🟢" if overview['content_status']['status'] == 'good' else "🟡"

            print(f"\n📊 Sistem Durumu: {site_status} Site | {content_status} İçerik | {datetime.now().strftime('%H:%M:%S')}")
            print("-" * 50)

            print("\n🎛️ Kontrol Seçenekleri:")
            print("1. 🔍 Hızlı Sistem Kontrolü")
            print("2. 📊 Detaylı Sistem Analizi")
            print("3. 🤖 Otomatik Görevleri Çalıştır")
            print("4. 📈 Performans İzleme")
            print("5. 🔄 Site İzleme Sistemi")
            print("6. 📄 Dashboard Raporu Oluştur")
            print("7. ⚙️ Site Yönetimi Ajanı")
            print("8. 🛠️ Manuel İşlemler")
            print("9. 📋 Log ve Raporlar")
            print("10. Çıkış")

            choice = input("\nSeçiminiz (1-10): ").strip()

            if choice == "1":
                health = self.run_quick_health_check()
                print(f"\n🎯 Genel Durum: {health['overall_status'].upper()}")
                if health['issues']:
                    print("⚠️ Tespit edilen sorunlar:")
                    for issue in health['issues']:
                        print(f"   • {issue}")
                else:
                    print("✅ Sistem sağlıklı çalışıyor")

            elif choice == "2":
                if self.site_agent:
                    report_file = self.site_agent.run_comprehensive_analysis()
                    print(f"📊 Detaylı analiz tamamlandı: {report_file}")
                else:
                    print("❌ Site ajanı mevcut değil")

            elif choice == "3":
                results = self.execute_automated_tasks()
                print(f"🤖 Otomatik görevler tamamlandı:")
                print(f"   ✅ Başarılı: {results['successes']}")
                print(f"   ❌ Başarısız: {results['failures']}")

            elif choice == "4":
                if self.performance_tracker:
                    self.performance_tracker.run_interactive_mode()
                else:
                    print("❌ Performance tracker mevcut değil")

            elif choice == "5":
                if self.monitoring_system:
                    self.monitoring_system.run_interactive_mode()
                else:
                    print("❌ Monitoring sistemi mevcut değil")

            elif choice == "6":
                report_file = self.generate_dashboard_report()
                print(f"📄 Dashboard raporu oluşturuldu: {report_file}")

            elif choice == "7":
                if self.site_agent:
                    self.site_agent.run_interactive_mode()
                else:
                    print("❌ Site yönetimi ajanı mevcut değil")

            elif choice == "8":
                self.run_manual_operations()

            elif choice == "9":
                self.show_logs_and_reports()

            elif choice == "10":
                print("👋 Merkezi kontrol paneli kapatılıyor...")
                break

            else:
                print("❌ Geçersiz seçim (1-10 arası)")

    def run_manual_operations(self):
        """Manuel işlemler menüsü"""
        print("\n🛠️ Manuel İşlemler")
        print("1. Git Commit & Push")
        print("2. Vercel Deploy")
        print("3. Content Generation")
        print("4. Build Test")
        print("5. Cache Clear")
        print("6. Geri")

        choice = input("\nSeçiminiz (1-6): ").strip()

        if choice == "1":
            try:
                message = input("Commit mesajı: ").strip() or f"Manual update {datetime.now().strftime('%Y-%m-%d %H:%M')}"
                subprocess.run(["git", "add", "."], check=True)
                subprocess.run(["git", "commit", "-m", message], check=True)
                subprocess.run(["git", "push"], check=True)
                print("✅ Git işlemleri tamamlandı")
            except Exception as e:
                print(f"❌ Git hatası: {e}")

        elif choice == "2":
            try:
                subprocess.run(["npx", "vercel", "--prod"], check=True, timeout=300)
                print("✅ Vercel deploy tamamlandı")
            except Exception as e:
                print(f"❌ Deploy hatası: {e}")

        elif choice == "3":
            try:
                subprocess.run(["python", "enhanced_daily_automation.py"], check=True, timeout=120)
                print("✅ İçerik oluşturma tamamlandı")
            except Exception as e:
                print(f"❌ İçerik oluşturma hatası: {e}")

        elif choice == "4":
            try:
                result = subprocess.run(["npm", "run", "build"], capture_output=True, text=True, timeout=180)
                if result.returncode == 0:
                    print("✅ Build başarılı")
                else:
                    print(f"❌ Build hatası: {result.stderr}")
            except Exception as e:
                print(f"❌ Build test hatası: {e}")

        elif choice == "5":
            print("🔄 Cache temizleme simülasyonu (gerçek implementation gerekir)")

        elif choice == "6":
            return

    def show_logs_and_reports(self):
        """Log ve raporlar görüntüleme"""
        print("\n📋 Log ve Raporlar")

        # Reports klasörünü listele
        reports_dir = Path("reports")
        if reports_dir.exists():
            reports = list(reports_dir.glob("*.md"))
            print(f"📄 Mevcut raporlar ({len(reports)} adet):")
            for i, report in enumerate(sorted(reports, reverse=True)[:10], 1):
                print(f"   {i}. {report.name}")
        else:
            print("📄 Henüz rapor bulunmuyor")

        # Log dosyalarını kontrol et
        log_files = ["alerts.log", "automation.log", "deployment.log"]
        print(f"\n📝 Log dosyaları:")
        for log_file in log_files:
            if Path(log_file).exists():
                size = Path(log_file).stat().st_size
                print(f"   ✅ {log_file} ({size} bytes)")
            else:
                print(f"   ❌ {log_file} (bulunamadı)")

def main():
    """Ana fonksiyon"""
    try:
        control_center = MindVerseControlCenter()
        if not MODULES_LOADED:
            print("\n🔥 Bazı modüller yüklenemediği için kontrol merkezi sınırlı modda çalışacak.")
            print("Lütfen hataları giderip yeniden başlatın.")
        control_center.run_interactive_dashboard()
    except KeyboardInterrupt:
        print("\n👋 Kontrol merkezi kapatılıyor...")
    except Exception as e:
        print(f"❌ Kritik hata: {e}")
        print("Lütfen tüm bağımlılıkların yüklü olduğundan emin olun")

if __name__ == "__main__":
    main()
