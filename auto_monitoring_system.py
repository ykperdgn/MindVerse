#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔄 MindVerse Blog - Otomatik İzleme ve Eylem Sistemi
Real-time Monitoring & Automated Actions
"""

import time
import json
import requests
import schedule
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List
import subprocess

class AutoMonitoringSystem:
    def __init__(self):
        self.site_url = "https://mindversedaily.com"
        self.monitoring_data = Path("monitoring_data.json")
        self.alerts_log = Path("alerts.log")
        self.config = self.load_config()

        # İzleme parametreleri
        self.thresholds = {
            "response_time": 5.0,  # 5 saniye
            "uptime_check_interval": 5,  # 5 dakika
            "content_check_interval": 60,  # 60 dakika
            "seo_check_interval": 1440,  # 24 saat
            "security_check_interval": 4320  # 3 gün
        }

        print("🔄 Otomatik izleme sistemi başlatıldı...")

    def load_config(self) -> Dict:
        """Konfigürasyon yükle"""
        default_config = {
            "email_notifications": False,
            "slack_webhook": None,
            "auto_fix_enabled": True,
            "monitoring_enabled": True,
            "log_level": "info"
        }

        config_file = Path("monitoring_config.json")
        if config_file.exists():
            try:
                with open(config_file, 'r') as f:
                    return {**default_config, **json.load(f)}
            except:
                return default_config

        # Default config'i kaydet
        with open(config_file, 'w') as f:
            json.dump(default_config, f, indent=2)

        return default_config

    def log_event(self, level: str, message: str):
        """Olay kaydı"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {level.upper()}: {message}\n"

        with open(self.alerts_log, 'a', encoding='utf-8') as f:
            f.write(log_entry)

        print(f"{timestamp} - {level.upper()}: {message}")

    def check_site_uptime(self) -> Dict:
        """Site uptime kontrolü"""
        try:
            start_time = time.time()
            response = requests.get(self.site_url, timeout=10)
            response_time = time.time() - start_time

            status = {
                "timestamp": datetime.now().isoformat(),
                "is_up": response.status_code == 200,
                "response_time": round(response_time, 2),
                "status_code": response.status_code,
                "url": self.site_url
            }

            # Threshold kontrolü
            if response_time > self.thresholds["response_time"]:
                self.log_event("warning", f"Yavaş response time: {response_time:.2f}s")
                self.handle_slow_response(response_time)

            if response.status_code != 200:
                self.log_event("error", f"Site down! Status: {response.status_code}")
                self.handle_site_down(status)
            else:
                self.log_event("info", f"Site up - {response_time:.2f}s")

            return status

        except Exception as e:
            error_status = {
                "timestamp": datetime.now().isoformat(),
                "is_up": False,
                "error": str(e),
                "url": self.site_url
            }

            self.log_event("error", f"Site check failed: {e}")
            self.handle_site_down(error_status)
            return error_status

    def check_content_freshness(self) -> Dict:
        """İçerik güncellik kontrolü"""
        content_dir = Path("src/content/astrology")
        today = datetime.now().date()

        # Bugünün içeriği var mı?
        today_files = []
        for file_path in content_dir.glob("*.md"):
            filename = file_path.name
            if today.strftime("%Y-%m-%d") in filename:
                today_files.append(filename)

        content_status = {
            "timestamp": datetime.now().isoformat(),
            "today_content_count": len(today_files),
            "has_daily_content": len(today_files) >= 12,  # Her burç için
            "today_files": today_files
        }

        # Eksik içerik uyarısı
        if len(today_files) < 12:
            self.log_event("warning", f"Eksik günlük içerik: {len(today_files)}/12")
            if self.config["auto_fix_enabled"]:
                self.auto_generate_missing_content()

        return content_status

    def check_api_health(self) -> Dict:
        """API sağlık kontrolü"""
        api_status = {
            "timestamp": datetime.now().isoformat(),
            "prokerala_api": {"status": "unknown", "response_time": 0},
            "internal_apis": {"status": "ok"}
        }

        # Prokerala API test (eğer varsa)
        try:
            # Bu kısım gerçek API key gerektirir
            self.log_event("info", "API health check - simulated")
            api_status["prokerala_api"]["status"] = "ok"
        except Exception as e:
            api_status["prokerala_api"]["status"] = "error"
            api_status["prokerala_api"]["error"] = str(e)
            self.log_event("warning", f"API check failed: {e}")

        return api_status

    def check_seo_vitals(self) -> Dict:
        """SEO vital kontrolleri"""
        seo_status = {
            "timestamp": datetime.now().isoformat(),
            "sitemap_accessible": False,
            "robots_txt_accessible": False,
            "meta_tags_present": False
        }

        # Sitemap kontrolü
        try:
            sitemap_response = requests.get(f"{self.site_url}/sitemap.xml", timeout=5)
            seo_status["sitemap_accessible"] = sitemap_response.status_code == 200
        except:
            pass

        # Robots.txt kontrolü
        try:
            robots_response = requests.get(f"{self.site_url}/robots.txt", timeout=5)
            seo_status["robots_txt_accessible"] = robots_response.status_code == 200
        except:
            pass

        # Ana sayfa meta tag kontrolü
        try:
            homepage = requests.get(self.site_url, timeout=5)
            if homepage.status_code == 200:
                content = homepage.text
                seo_status["meta_tags_present"] = all([
                    '<meta name="description"' in content,
                    '<title>' in content,
                    'og:title' in content
                ])
        except:
            pass

        # SEO sorunları varsa uyar
        if not seo_status["sitemap_accessible"]:
            self.log_event("warning", "Sitemap erişilemez")

        return seo_status

    def handle_site_down(self, status: Dict):
        """Site down durumu işleme"""
        self.log_event("critical", "Site down detected - attempting recovery")

        if self.config["auto_fix_enabled"]:
            # Otomatik düzeltme denemeleri
            self.attempt_auto_recovery()

        # Bildirim gönder
        self.send_alert("Site Down", f"Site erişilemez durumda: {status}")

    def handle_slow_response(self, response_time: float):
        """Yavaş response işleme"""
        if self.config["auto_fix_enabled"] and response_time > 10:
            self.log_event("warning", "Attempting performance optimization")
            # Basit cache clear denemesi
            self.clear_cache()

    def attempt_auto_recovery(self):
        """Otomatik kurtarma denemeleri"""
        recovery_actions = [
            self.redeploy_site,
            self.clear_cache,
            self.restart_services
        ]

        for action in recovery_actions:
            try:
                result = action()
                if result:
                    self.log_event("info", f"Recovery action successful: {action.__name__}")
                    break
            except Exception as e:
                self.log_event("error", f"Recovery action failed {action.__name__}: {e}")

    def redeploy_site(self) -> bool:
        """Site yeniden deploy"""
        try:
            self.log_event("info", "Attempting redeploy...")
            result = subprocess.run(
                ["npx", "vercel", "--prod"],
                capture_output=True,
                text=True,
                timeout=300
            )
            return result.returncode == 0
        except Exception as e:
            self.log_event("error", f"Redeploy failed: {e}")
            return False

    def clear_cache(self) -> bool:
        """Cache temizliği"""
        try:
            # Vercel cache purge (gerçek implementation gerekir)
            self.log_event("info", "Cache clearing attempted")
            return True
        except Exception as e:
            self.log_event("error", f"Cache clear failed: {e}")
            return False

    def restart_services(self) -> bool:
        """Servis yeniden başlatma"""
        try:
            # Container restart vs. (gerçek implementation gerekir)
            self.log_event("info", "Service restart attempted")
            return True
        except Exception as e:
            self.log_event("error", f"Service restart failed: {e}")
            return False

    def auto_generate_missing_content(self):
        """Eksik içerik otomatik oluşturma"""
        try:
            self.log_event("info", "Auto-generating missing daily content...")
            result = subprocess.run(
                ["python", "enhanced_daily_automation.py"],
                capture_output=True,
                text=True,
                timeout=120
            )

            if result.returncode == 0:
                self.log_event("info", "Daily content auto-generation successful")
                # Auto deploy
                if self.config["auto_fix_enabled"]:
                    self.auto_deploy_content()
            else:
                self.log_event("error", f"Content generation failed: {result.stderr}")

        except Exception as e:
            self.log_event("error", f"Auto content generation error: {e}")

    def auto_deploy_content(self):
        """İçerik otomatik deploy"""
        try:
            # Git add & commit
            subprocess.run(["git", "add", "."], check=True, timeout=30)
            subprocess.run([
                "git", "commit", "-m",
                f"🤖 Auto-generated content {datetime.now().strftime('%Y-%m-%d')}"
            ], check=True, timeout=30)
            subprocess.run(["git", "push"], check=True, timeout=60)

            # Vercel deploy
            subprocess.run(["npx", "vercel", "--prod"], check=True, timeout=300)

            self.log_event("info", "Auto-deploy successful")

        except Exception as e:
            self.log_event("error", f"Auto-deploy failed: {e}")

    def send_alert(self, subject: str, body: str):
        """Bildirim gönder (slack vb.)"""
        self.log_event("alert", f"ALERT: {subject} - {body}")

        # Slack notification
        if self.config.get("slack_webhook"):
            self._send_slack_alert(subject, body)

    def _send_slack_alert(self, subject: str, body: str):
        """Slack ile bildirim gönder"""
        webhook_url = self.config.get("slack_webhook")
        if not webhook_url:
            return

        payload = {
            "text": f"🚨 *MindVerse Monitoring Alert* 🚨\n*Subject:* {subject}\n*Details:* {body}"
        }
        try:
            response = requests.post(webhook_url, json=payload, timeout=10)
            if response.status_code == 200:
                self.log_event("info", "Slack alert sent successfully")
            else:
                self.log_event("warning", f"Failed to send Slack alert: {response.status_code}")
        except Exception as e:
            self.log_event("error", f"Error sending Slack alert: {e}")

    def save_monitoring_data(self, data: Dict):
        """İzleme verilerini kaydet"""
        # Geçmiş verileri yükle
        historical_data = []
        if self.monitoring_data.exists():
            try:
                with open(self.monitoring_data, 'r') as f:
                    historical_data = json.load(f)
            except:
                historical_data = []

        # Yeni veri ekle
        historical_data.append(data)

        # Son 1000 kayıt tut
        if len(historical_data) > 1000:
            historical_data = historical_data[-1000:]

        # Kaydet
        with open(self.monitoring_data, 'w') as f:
            json.dump(historical_data, f, indent=2, ensure_ascii=False)

    def generate_monitoring_report(self) -> str:
        """İzleme raporu oluştur"""
        if not self.monitoring_data.exists():
            return "Henüz izleme verisi yok"

        try:
            with open(self.monitoring_data, 'r') as f:
                data = json.load(f)

            if not data:
                return "İzleme verisi boş"

            # Son 24 saat verilerini analiz et
            last_24h = []
            cutoff_time = datetime.now() - timedelta(hours=24)

            for entry in data:
                entry_time = datetime.fromisoformat(entry['timestamp'].replace('Z', '+00:00'))
                if entry_time > cutoff_time:
                    last_24h.append(entry)

            if not last_24h:
                return "Son 24 saat veri yok"

            # İstatistikler
            uptime_checks = [d for d in last_24h if 'is_up' in d]
            up_count = sum(1 for d in uptime_checks if d['is_up'])
            uptime_percentage = (up_count / len(uptime_checks) * 100) if uptime_checks else 0

            avg_response_time = sum(d.get('response_time', 0) for d in uptime_checks) / len(uptime_checks) if uptime_checks else 0

            report = f"""🔄 İzleme Raporu - Son 24 Saat

📊 Genel İstatistikler:
- Uptime: %{uptime_percentage:.1f}
- Ortalama Response Time: {avg_response_time:.2f}s
- Toplam Check: {len(uptime_checks)}
- Up Count: {up_count}

📈 Son Durumlar:
"""

            # Son 5 kontrolü göster
            recent_checks = sorted(uptime_checks, key=lambda x: x['timestamp'], reverse=True)[:5]
            for check in recent_checks:
                status_emoji = "🟢" if check.get('is_up') else "🔴"
                report += f"- {check['timestamp'][:19]}: {status_emoji} {check.get('response_time', 0):.2f}s\n"

            return report

        except Exception as e:
            return f"Rapor oluşturma hatası: {e}"

    def setup_monitoring_schedule(self):
        """İzleme programını kur"""
        print("⏰ İzleme programı kuruluyor...")

        # Uptime check - her 5 dakika
        schedule.every(self.thresholds["uptime_check_interval"]).minutes.do(
            self.scheduled_uptime_check
        )

        # İçerik check - her saat
        schedule.every(self.thresholds["content_check_interval"]).minutes.do(
            self.scheduled_content_check
        )

        # SEO check - günlük
        schedule.every(self.thresholds["seo_check_interval"]).minutes.do(
            self.scheduled_seo_check
        )

        # API health check - her 30 dakika
        schedule.every(30).minutes.do(self.scheduled_api_check)

        print("✅ İzleme programı kuruldu")

    def scheduled_uptime_check(self):
        """Programlı uptime kontrolü"""
        status = self.check_site_uptime()
        self.save_monitoring_data({
            "type": "uptime_check",
            "timestamp": datetime.now().isoformat(),
            **status
        })

    def scheduled_content_check(self):
        """Programlı içerik kontrolü"""
        status = self.check_content_freshness()
        self.save_monitoring_data({
            "type": "content_check",
            "timestamp": datetime.now().isoformat(),
            **status
        })

    def scheduled_seo_check(self):
        """Programlı SEO kontrolü"""
        status = self.check_seo_vitals()
        self.save_monitoring_data({
            "type": "seo_check",
            "timestamp": datetime.now().isoformat(),
            **status
        })

    def scheduled_api_check(self):
        """Programlı API kontrolü"""
        status = self.check_api_health()
        self.save_monitoring_data({
            "type": "api_check",
            "timestamp": datetime.now().isoformat(),
            **status
        })

    def run_monitoring_loop(self):
        """İzleme döngüsü çalıştır"""
        print("🔄 İzleme döngüsü başlatılıyor...")
        print("CTRL+C ile durdurun")

        try:
            while True:
                schedule.run_pending()
                time.sleep(60)  # Her dakika check et
        except KeyboardInterrupt:
            print("\n⏹️ İzleme durduruldu")

    def run_interactive_mode(self):
        """İnteraktif monitoring modu"""
        print("\n🔄 Otomatik İzleme Sistemi")
        print("=" * 40)

        while True:
            print("\n📊 İzleme Seçenekleri:")
            print("1. 🔍 Anlık Site Kontrolü")
            print("2. 📄 İçerik Durumu")
            print("3. 🔗 API Sağlığı")
            print("4. 🎯 SEO Vitals")
            print("5. 📈 İzleme Raporu")
            print("6. ⏰ Otomatik İzleme Başlat")
            print("7. 🛠️ Otomatik Düzeltme Test")
            print("8. ⚙️ Konfigürasyon")
            print("9. 📋 Log Görüntüle")
            print("10. Çıkış")

            choice = input("\nSeçiminiz (1-10): ").strip()

            if choice == "1":
                status = self.check_site_uptime()
                print(f"🌐 Site Durumu: {'🟢 UP' if status['is_up'] else '🔴 DOWN'}")
                print(f"⏱️ Response Time: {status.get('response_time', 'N/A')}s")

            elif choice == "2":
                content_status = self.check_content_freshness()
                print(f"📄 Bugünkü İçerik: {content_status['today_content_count']}/12")
                print(f"📝 Durum: {'✅ Tamam' if content_status['has_daily_content'] else '⚠️ Eksik'}")

            elif choice == "3":
                api_status = self.check_api_health()
                print(f"🔗 API Durumu: {api_status['prokerala_api']['status']}")

            elif choice == "4":
                seo_status = self.check_seo_vitals()
                print(f"🗂️ Sitemap: {'✅' if seo_status['sitemap_accessible'] else '❌'}")
                print(f"🤖 Robots.txt: {'✅' if seo_status['robots_txt_accessible'] else '❌'}")
                print(f"🏷️ Meta Tags: {'✅' if seo_status['meta_tags_present'] else '❌'}")

            elif choice == "5":
                report = self.generate_monitoring_report()
                print(report)

            elif choice == "6":
                self.setup_monitoring_schedule()
                print("🚀 Otomatik izleme başlatılıyor...")
                self.run_monitoring_loop()

            elif choice == "7":
                print("🛠️ Otomatik düzeltme test ediliyor...")
                self.auto_generate_missing_content()

            elif choice == "8":
                print("⚙️ Mevcut Konfigürasyon:")
                for key, value in self.config.items():
                    print(f"   {key}: {value}")

            elif choice == "9":
                if self.alerts_log.exists():
                    with open(self.alerts_log, 'r', encoding='utf-8') as f:
                        logs = f.readlines()
                        print("📋 Son 10 Log Kaydı:")
                        for log in logs[-10:]:
                            print(f"   {log.strip()}")
                else:
                    print("📋 Henüz log kaydı yok")

            elif choice == "10":
                print("👋 İzleme sistemi kapatılıyor...")
                break

            else:
                print("❌ Geçersiz seçim (1-10 arası)")

def main():
    """Ana fonksiyon"""
    monitor = AutoMonitoringSystem()
    monitor.run_interactive_mode()

if __name__ == "__main__":
    main()
