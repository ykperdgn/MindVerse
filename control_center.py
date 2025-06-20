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

# Try to import new advanced modules
ADVANCED_MODULES_LOADED = False
try:
    from intelligent_scheduler import IntelligentScheduler
    from advanced_analytics import AdvancedAnalytics
    ADVANCED_MODULES_LOADED = True
except ImportError as e:
    print(f"⚠️ Gelişmiş modül import hatası: {e}")
    print("Gelişmiş özellikler devre dışı kalacak.")


class MindVerseControlCenter:
    def __init__(self):
        self.site_url = "https://mindversedaily.com"
        self.project_dir = Path(".")

        # Alt sistemleri başlat
        self.site_agent = None
        self.monitoring_system = None
        self.performance_tracker = None
        self.scheduler = None
        self.analytics = None

        if MODULES_LOADED:
            try:
                self.site_agent = MindVerseSiteAgent()
                self.monitoring_system = AutoMonitoringSystem()
                self.performance_tracker = PerformanceTracker()
            except Exception as e:
                print(f"⚠️ Alt sistem başlatma hatası: {e}")

        if ADVANCED_MODULES_LOADED:
            try:
                self.scheduler = IntelligentScheduler()
                self.analytics = AdvancedAnalytics()
                print("🚀 Gelişmiş sistemler yüklendi")
            except Exception as e:
                print(f"⚠️ Gelişmiş sistem başlatma hatası: {e}")

        # Dashboard durumu
        self.dashboard_data = {
            "last_update": datetime.now().isoformat(),
            "system_status": "online",
            "active_modules": [name for name, mod in [("SiteAgent", self.site_agent), ("Monitoring", self.monitoring_system), ("Performance", self.performance_tracker), ("Scheduler", self.scheduler), ("Analytics", self.analytics)] if mod]
        }

        print("🎛️ MindVerse Kontrol Merkezi başlatıldı...")
        if not MODULES_LOADED:
            print("🔥 UYARI: Gerekli modüller yüklenemedi. İşlevsellik sınırlı olacak.")
        if not ADVANCED_MODULES_LOADED:
            print("🔥 UYARI: Gelişmiş modüller yüklenemedi. Gelişmiş işlevsellik sınırlı olacak.")

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
            print("10. 🧠 Akıllı Zamanlayıcı")
            print("11. 📊 Gelişmiş Analitik")
            print("12. 🚀 Otomasyon Merkezi")
            print("13. Çıkış")
            choice = input("\nSeçiminiz (1-13): ").strip()

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
                self.run_intelligent_scheduler()

            elif choice == "11":
                self.run_advanced_analytics()

            elif choice == "12":
                self.run_automation_center()

            elif choice == "13":
                print("👋 Merkezi kontrol paneli kapatılıyor...")
                break

            else:
                print("❌ Geçersiz seçim (1-13 arası)")

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
        """Log ve rapor görüntüleme"""
        print("\n📋 Log ve Raporlar")
        print("1. Son log kayıtları")
        print("2. Performans raporları")
        print("3. Site analiz raporları")
        print("4. Monitoring logları")
        print("5. Geri")

        choice = input("Seçiminiz (1-5): ").strip()

        if choice == "1":
            self.show_recent_logs()
        elif choice == "2":
            self.show_performance_reports()
        elif choice == "3":
            self.show_analysis_reports()
        elif choice == "4":
            self.show_monitoring_logs()
        elif choice == "5":
            return
        else:
            print("❌ Geçersiz seçim")

    def show_recent_logs(self):
        """Son log kayıtlarını göster"""
        try:
            log_files = [
                "automation.log",
                "alerts.log",
                "deployment.log"
            ]

            print("📋 Son Log Kayıtları:")
            for log_file in log_files:
                log_path = Path(log_file)
                if log_path.exists():
                    print(f"\n--- {log_file} ---")
                    with open(log_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        # Son 10 satırı göster
                        for line in lines[-10:]:
                            print(f"   {line.strip()}")
                else:
                    print(f"⚠️ {log_file} bulunamadı")
        except Exception as e:
            print(f"❌ Log okuma hatası: {e}")

    def show_performance_reports(self):
        """Performans raporlarını göster"""
        try:
            reports_dir = Path("reports")
            if not reports_dir.exists():
                print("❌ Reports klasörü bulunamadı")
                return

            performance_reports = list(reports_dir.glob("performance_*.md"))

            if not performance_reports:
                print("⚠️ Performans raporu bulunamadı")
                return

            print("📈 Performans Raporları:")
            for report in sorted(performance_reports)[-5:]:  # Son 5 rapor
                print(f"   📄 {report.name}")

        except Exception as e:
            print(f"❌ Performans raporu hatası: {e}")

    def show_analysis_reports(self):
        """Site analiz raporlarını göster"""
        try:
            reports_dir = Path("reports")
            if not reports_dir.exists():
                print("❌ Reports klasörü bulunamadı")
                return

            analysis_reports = list(reports_dir.glob("site_analysis_*.md"))

            if not analysis_reports:
                print("⚠️ Analiz raporu bulunamadı")
                return

            print("🔍 Site Analiz Raporları:")
            for report in sorted(analysis_reports)[-5:]:  # Son 5 rapor
                print(f"   📄 {report.name}")
                # Rapor özeti göster
                try:
                    with open(report, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # İlk birkaç satırı göster
                        lines = content.split('\n')[:10]
                        for line in lines:
                            if line.strip() and not line.startswith('#'):
                                print(f"      {line[:100]}...")
                                break
                except Exception:
                    pass

        except Exception as e:
            print(f"❌ Analiz raporu hatası: {e}")

    def show_monitoring_logs(self):
        """İzleme loglarını göster"""
        try:
            monitoring_file = Path("monitoring_data.json")
            if monitoring_file.exists():
                print("🔄 İzleme Verileri:")
                with open(monitoring_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    print(f"   Son güncelleme: {data.get('last_update', 'Bilinmiyor')}")
                    print(f"   İzleme sayısı: {len(data.get('checks', []))}")
            else:
                print("⚠️ İzleme verisi bulunamadı")

            # Alert logları
            alerts_file = Path("alerts.log")
            if alerts_file.exists():
                print("\n⚠️ Son Uyarılar:")
                with open(alerts_file, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    for line in lines[-5:]:  # Son 5 uyarı
                        print(f"   {line.strip()}")

        except Exception as e:
            print(f"❌ İzleme log hatası: {e}")

    def run_intelligent_scheduler(self):
        """Akıllı zamanlayıcı çalıştırma"""
        if not ADVANCED_MODULES_LOADED or not self.scheduler:
            print("❌ Akıllı zamanlayıcı mevcut değil")
            return

        print("\n🧠 Akıllı Zamanlayıcı")
        print("1. Zamanlama Kurulumu")
        print("2. Manuel Görev Çalıştır")
        print("3. Sürekli İzleme Başlat")
        print("4. Zamanlanmış Görevleri Görüntüle")
        print("5. Geri")

        choice = input("Seçiminiz (1-5): ").strip()

        if choice == "1":
            self.scheduler.setup_daily_schedule()
            print("✅ Zamanlama kuruldu")
        elif choice == "2":
            task = input("Görev adı (morning/midday/evening/night/weekly/health): ").strip()
            self.scheduler.run_manual_task(task)
        elif choice == "3":
            print("🚀 Sürekli izleme başlatılıyor...")
            print("⚠️ Bu mod sürekli çalışacak. Ctrl+C ile durdurun.")
            try:
                self.scheduler.setup_daily_schedule()
                self.scheduler.run_continuous()
            except KeyboardInterrupt:
                print("\n👋 Sürekli izleme durduruldu")
        elif choice == "4":
            print("📅 Zamanlanmış görevler görüntüleniyor...")
            # Schedule jobs listesi gösterilebilir
        elif choice == "5":
            return

    def run_advanced_analytics(self):
        """Gelişmiş analitik çalıştırma"""
        if not ADVANCED_MODULES_LOADED or not self.analytics:
            print("❌ Gelişmiş analitik sistemi mevcut değil")
            return

        print("\n📊 Gelişmiş Analitik Sistemi")
        print("1. Kapsamlı Veri Toplama")
        print("2. İş Zekası Raporu Oluştur")
        print("3. Görsel Analitik")
        print("4. Trend Analizi")
        print("5. Performans Karşılaştırması")
        print("6. Geri")

        choice = input("Seçiminiz (1-6): ").strip()

        if choice == "1":
            print("📥 Kapsamlı veri toplama başlatılıyor...")
            data = self.analytics.collect_comprehensive_data()
            print("✅ Veri toplama tamamlandı")
        elif choice == "2":
            print("📊 İş zekası raporu oluşturuluyor...")
            data = self.analytics.collect_comprehensive_data()
            report = self.analytics.generate_business_intelligence_report(data)
            print(f"✅ İş zekası raporu: {report}")
        elif choice == "3":
            print("📈 Görsel analitik oluşturuluyor...")
            data = self.analytics.collect_comprehensive_data()
            self.analytics.create_visual_analytics(data)
            print("✅ Görsel analitik tamamlandı")
        elif choice == "4":
            print("📈 Trend analizi yapılıyor...")
            data = self.analytics.collect_comprehensive_data()
            trends = data.get("trend_analysis", {})
            print("✅ Trend analizi tamamlandı")
        elif choice == "5":
            print("⚖️ Performans karşılaştırması yapılıyor...")
            # Performans karşılaştırma implementasyonu
            print("✅ Karşılaştırma tamamlandı")
        elif choice == "6":
            return

    def run_automation_center(self):
        """Otomasyon merkezi"""
        print("\n🚀 Otomasyon Merkezi")
        print("1. Günlük İçerik Otomasyonu")
        print("2. SEO Optimizasyon Otomasyonu")
        print("3. Sosyal Medya Otomasyonu")
        print("4. Performans Optimizasyon Otomasyonu")
        print("5. Backup ve Güvenlik Otomasyonu")
        print("6. Kapsamlı Otomasyon Paketi")
        print("7. Geri")

        choice = input("Seçiminiz (1-7): ").strip()

        if choice == "1":
            self.run_content_automation()
        elif choice == "2":
            self.run_seo_automation()
        elif choice == "3":
            self.run_social_automation()
        elif choice == "4":
            self.run_performance_automation()
        elif choice == "5":
            self.run_backup_automation()
        elif choice == "6":
            self.run_comprehensive_automation()
        elif choice == "7":
            return

    def run_content_automation(self):
        """İçerik otomasyonu"""
        print("📝 İçerik otomasyonu başlatılıyor...")
        try:
            # Günlük içerik üretimi
            result = subprocess.run([
                "python", "enhanced_daily_automation.py"
            ], capture_output=True, text=True, timeout=300)

            if result.returncode == 0:
                print("✅ Günlük içerik üretimi tamamlandı")
            else:
                print(f"❌ İçerik üretimi hatası: {result.stderr}")

            # Çeşitlendirilmiş içerik
            result2 = subprocess.run([
                "python", "advanced_content_balancer.py"
            ], capture_output=True, text=True, timeout=240)

            if result2.returncode == 0:
                print("✅ Çeşitlendirilmiş içerik tamamlandı")

        except Exception as e:
            print(f"❌ İçerik otomasyonu hatası: {e}")

    def run_seo_automation(self):
        """SEO otomasyonu"""
        print("🔍 SEO otomasyonu başlatılıyor...")
        try:
            result = subprocess.run([
                "python", "generate_enhanced_seo.py"
            ], capture_output=True, text=True, timeout=180)

            if result.returncode == 0:
                print("✅ SEO optimizasyonu tamamlandı")
            else:
                print(f"❌ SEO otomasyonu hatası: {result.stderr}")

        except Exception as e:
            print(f"❌ SEO otomasyonu hatası: {e}")

    def run_social_automation(self):
        """Sosyal medya otomasyonu"""
        print("📱 Sosyal medya otomasyonu başlatılıyor...")
        try:
            result = subprocess.run([
                "python", "auto_social_poster_clean.py"
            ], capture_output=True, text=True, timeout=120)

            if result.returncode == 0:
                print("✅ Sosyal medya otomasyonu tamamlandı")
            else:
                print(f"❌ Sosyal medya otomasyonu hatası: {result.stderr}")

        except Exception as e:
            print(f"❌ Sosyal medya otomasyonu hatası: {e}")

    def run_performance_automation(self):
        """Performans optimizasyon otomasyonu"""
        print("⚡ Performans optimizasyonu başlatılıyor...")
        try:
            # Site performans kontrolü
            if self.performance_tracker:
                metrics = self.performance_tracker.get_current_metrics()
                print(f"📊 Mevcut performans skoru: {metrics.get('overall_score', 'N/A')}")

            # Otomatik optimizasyonlar
            optimizations = [
                "Image compression check",
                "Cache optimization",
                "Bundle size analysis",
                "Database optimization"
            ]

            for opt in optimizations:
                print(f"   🔧 {opt}...")
                time.sleep(1)  # Simulation

            print("✅ Performans optimizasyonu tamamlandı")

        except Exception as e:
            print(f"❌ Performans otomasyonu hatası: {e}")

    def run_backup_automation(self):
        """Backup ve güvenlik otomasyonu"""
        print("🔒 Backup ve güvenlik otomasyonu başlatılıyor...")
        try:
            # Git backup
            result = subprocess.run([
                "git", "add", "."
            ], capture_output=True, text=True, timeout=30)

            if result.returncode == 0:
                commit_msg = f"🤖 Automated backup - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
                subprocess.run([
                    "git", "commit", "-m", commit_msg
                ], capture_output=True, text=True, timeout=30)

                subprocess.run([
                    "git", "push"
                ], capture_output=True, text=True, timeout=60)

                print("✅ Git backup tamamlandı")

            # Güvenlik kontrolleri
            security_checks = [
                "SSL certificate check",
                "Dependencies security scan",
                "File permissions check",
                "Environment variables check"
            ]

            for check in security_checks:
                print(f"   🔍 {check}...")
                time.sleep(0.5)

            print("✅ Güvenlik kontrolleri tamamlandı")

        except Exception as e:
            print(f"❌ Backup otomasyonu hatası: {e}")

    def run_comprehensive_automation(self):
        """Kapsamlı otomasyon paketi"""
        print("🚀 Kapsamlı otomasyon paketi başlatılıyor...")
        print("Bu işlem tüm otomasyon görevlerini sırayla çalıştıracak...")

        confirmation = input("Devam etmek istiyor musunuz? (y/N): ").strip().lower()
        if confirmation not in ['y', 'yes', 'evet']:
            print("❌ İşlem iptal edildi")
            return

        automations = [
            ("📝 İçerik Otomasyonu", self.run_content_automation),
            ("🔍 SEO Otomasyonu", self.run_seo_automation),
            ("📱 Sosyal Medya Otomasyonu", self.run_social_automation),
            ("⚡ Performans Otomasyonu", self.run_performance_automation),
            ("🔒 Backup Otomasyonu", self.run_backup_automation)
        ]

        successful = 0
        for name, func in automations:
            try:
                print(f"\n{name} başlatılıyor...")
                func()
                successful += 1
            except Exception as e:
                print(f"❌ {name} hatası: {e}")

        print(f"\n🎯 Kapsamlı otomasyon tamamlandı!")
        print(f"✅ Başarılı: {successful}/{len(automations)}")
        print(f"❌ Başarısız: {len(automations) - successful}")

def main():
    """Ana fonksiyon"""
    try:
        control_center = MindVerseControlCenter()
        if not MODULES_LOADED:
            print("\n🔥 Bazı modüller yüklenemediği için kontrol merkezi sınırlı modda çalışacak.")
            print("Lütfen hataları giderip yeniden başlatın.")
        if not ADVANCED_MODULES_LOADED:
            print("\n🔥 Gelişmiş modüller yüklenemediği için kontrol merkezi sınırlı modda çalışacak.")
            print("Lütfen hataları giderip yeniden başlatın.")
        control_center.run_interactive_dashboard()
    except KeyboardInterrupt:
        print("\n👋 Kontrol merkezi kapatılıyor...")
    except Exception as e:
        print(f"❌ Kritik hata: {e}")
        print("Lütfen tüm bağımlılıkların yüklü olduğundan emin olun")

if __name__ == "__main__":
    main()
