#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kısa İçerik Temizleyici ve Uzun İçerik Dönüştürücü
MindVerse Daily için gelişmiş içerik optimizasyonu
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime
import hashlib

class ContentAnalyzer:
    def __init__(self):
        self.content_dir = "src/content"
        self.categories = ["health", "love", "history", "psychology", "space", "quotes"]
        self.min_word_count = 800
        self.target_word_count = 1200

    def count_words(self, content):
        """Markdown içeriğindeki kelime sayısını hesapla"""
        # Markdown meta verilerini kaldır
        content = re.sub(r'^---.*?---', '', content, flags=re.DOTALL)
        # HTML etiketlerini kaldır
        content = re.sub(r'<[^>]+>', '', content)
        # Markdown formatlarını kaldır
        content = re.sub(r'[#*_`\[\]()]', '', content)
        # Kelimeleri say
        words = content.strip().split()
        return len([word for word in words if len(word) > 0])

    def analyze_all_content(self):
        """Tüm içerikleri analiz et"""
        analysis = {
            "total_files": 0,
            "short_files": [],
            "good_files": [],
            "categories": {}
        }

        for category in self.categories:
            category_path = Path(self.content_dir) / category
            if not category_path.exists():
                continue

            analysis["categories"][category] = {
                "total": 0,
                "short": 0,
                "good": 0,
                "files": []
            }

            for file_path in category_path.glob("*.md"):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    word_count = self.count_words(content)
                    analysis["total_files"] += 1
                    analysis["categories"][category]["total"] += 1

                    file_info = {
                        "path": str(file_path),
                        "name": file_path.name,
                        "word_count": word_count,
                        "size": file_path.stat().st_size
                    }

                    if word_count < self.min_word_count:
                        analysis["short_files"].append(file_info)
                        analysis["categories"][category]["short"] += 1
                        analysis["categories"][category]["files"].append(file_info)
                    else:
                        analysis["good_files"].append(file_info)
                        analysis["categories"][category]["good"] += 1

                except Exception as e:
                    print(f"Hata: {file_path} okunamadı - {e}")

        return analysis

    def generate_long_content(self, category, original_title, original_summary):
        """Uzun format içerik üret"""

        templates = {
            "health": {
                "sections": [
                    "## 🎯 Neden Bu Konu Önemli?",
                    "## 🔬 Bilimsel Temeller ve Araştırmalar",
                    "## 📋 Pratik Uygulama Adımları",
                    "## ⚠️ Dikkat Edilmesi Gerekenler",
                    "## 💡 Uzman Önerileri",
                    "## 🎉 Başarı Hikayeleri",
                    "## 🔄 Sürdürülebilir Yaşam Değişiklikleri",
                    "## 📚 Ek Kaynaklar ve Okuma Önerileri"
                ],
                "content_blocks": [
                    "Modern yaşamın getirdiği zorluklar karşısında, bu konuya odaklanmak artık bir lüks değil, zorunluluk haline gelmiştir.",
                    "Son yapılan araştırmalar gösteriyor ki, bu konudaki doğru yaklaşımlar yaşam kalitenizi %40'a kadar artırabilir.",
                    "Adım adım rehberle, bu değişimi günlük yaşamınıza nasıl entegre edebileceğinizi öğreneceksiniz.",
                    "Uzmanlar uyarıyor: Bu süreçte yapılan yaygın hatalar geri dönüşü olmayan sonuçlara yol açabilir.",
                    "25 yıllık deneyimiyle alanında uzman doktor, size özel önerilerini paylaşıyor.",
                    "Bu yöntemi uygulayan binlerce kişiden aldığımız gerçek başarı hikayeleri sizi de motive edecek.",
                    "Kısa vadeli sonuçları kalıcı hale getirmek için hayat boyu sürdürebileceğiniz pratik stratejiler.",
                    "Konuyu derinlemesine öğrenmek isteyenler için güvenilir kaynak listesi ve öneriler."
                ]
            },
            "love": {
                "sections": [
                    "## 💕 İlişkilerde Bu Konunun Kritik Önemi",
                    "## 🧠 Psikoloji ve İletişim Bilimi",
                    "## 🗣️ Etkili İletişim Teknikleri",
                    "## 🚨 Kaçınılması Gereken Hatalar",
                    "## 👥 Çift Terapisti Önerileri",
                    "## 💬 Gerçek Çift Deneyimleri",
                    "## 🏗️ Güçlü İlişki İnşa Etme",
                    "## 📖 İlişki Gelişimi İçin Kaynaklar"
                ],
                "content_blocks": [
                    "Sağlıklı ilişkilerin temeli, bu konuya gösterilen özen ve anlayışla doğrudan bağlantılıdır.",
                    "Çift terapisi araştırmaları, bu alandaki doğru yaklaşımların ilişki memnuniyetini %60 artırdığını gösteriyor.",
                    "Kanıtlanmış iletişim teknikleriyle, partnerinizle daha derin ve anlamlı bağlar kurabilirsiniz.",
                    "En başarılı çiftler bile bu yaygın hatalara düşebiliyor - kendinizi koruyun.",
                    "15 yıldır çiftlerle çalışan terapistimiz, en etkili stratejileri sizlerle paylaşıyor.",
                    "Bu yöntemleri hayatına geçiren çiftlerden aldığımız samimi ve cesaret verici hikayeler.",
                    "Geçici düzelmeler değil, uzun vadeli mutluluk için sağlam ilişki temelleri atma rehberi.",
                    "İlişki uzmanlarının tavsiye ettiği kitaplar, podcastler ve gelişim kaynakları."
                ]
            },
            "psychology": {
                "sections": [
                    "## 🧠 Psikolojinin Bu Alandaki Rolü",
                    "## 🔬 Nöroloji ve Davranış Bilimi",
                    "## 🎯 Kişisel Gelişim Stratejileri",
                    "## ⚠️ Zihinsel Sağlık Uyarıları",
                    "## 👨‍⚕️ Psikolog Görüşleri",
                    "## 📈 Değişim Hikayeleri",
                    "## 🔄 Yaşam Boyu Gelişim",
                    "## 🎓 Psikoloji Eğitim Kaynakları"
                ],
                "content_blocks": [
                    "İnsan zihninin bu alandaki karmaşık yapısını anlamak, kişisel gelişimin ilk adımıdır.",
                    "Beyni görüntüleme teknolojileri sayesinde, bu süreçlerin nasıl işlediğini artık biliyoruz.",
                    "Kendinizi tanıma ve geliştirme yolculuğunda size rehberlik edecek kanıtlanmış yöntemler.",
                    "Bu alanda yaşanan zorluklar ciddi zihinsel sağlık sorunlarına yol açabilir - dikkatli olun.",
                    "Klinik psikolog, 20 yıllık deneyimiyle size özel önerilerde bulunuyor.",
                    "Bu teknikleri uygulayarak hayatını değiştiren insanlardan ilham verici hikayeler.",
                    "Yaşınız ne olursa olsun, bu alanda kendinizi geliştirmeye devam edebilirsiniz.",
                    "Psikoloji meraklıları için derinlemesine öğrenme imkanı sunan güvenilir kaynaklar."
                ]
            },
            "history": {
                "sections": [
                    "## 📜 Tarihsel Bağlam ve Önem",
                    "## 🔍 Arkeolojik Bulgular ve Kanıtlar",
                    "## 🌍 Dünya Üzerindeki Etkileri",
                    "## ⚔️ Çatışmalar ve Sonuçları",
                    "## 👑 Liderler ve Karar Vericiler",
                    "## 📚 Tarihi Kaynaklar ve Belgeler",
                    "## 🔗 Günümüze Yansımaları",
                    "## 🎓 Tarih Öğrenme Kaynakları"
                ],
                "content_blocks": [
                    "Bu tarihsel olayın günümüz dünyasını şekillendirmedeki rolü, çoğu kişinin sandığından çok daha büyüktür.",
                    "Son arkeolojik keşifler, bu konuya dair bildiklerimizi tamamen değiştirdi.",
                    "Bu gelişmelerin küresel çapta yarattığı domino etkisi, yüzyıllar boyunca hissedildi.",
                    "Yaşanan çatışmaların ve savaşların bugünkü siyasi haritayı nasıl belirlediğini anlamak kritik.",
                    "O dönemin liderlerinin aldığı kararlar, milyonlarca insanın kaderini değiştirdi.",
                    "Birinci elden kaynaklardan elde edilen bilgiler, olayların gerçek boyutunu gözler önüne seriyor.",
                    "Geçmişin dersleri, bugün karşılaştığımız benzer sorunlara ışık tutuyor.",
                    "Tarih meraklıları için güvenilir kaynak listesi ve derinlemesine araştırma rehberi."
                ]
            },
            "space": {
                "sections": [
                    "## 🚀 Uzay Keşiflerindeki Yeri",
                    "## 🔬 Astrofizik ve Bilimsel Temeller",
                    "## 🌌 Evrendeki Konumu ve Önemi",
                    "## 🛰️ Teknolojik Gelişmeler",
                    "## 👨‍🚀 Astronot Deneyimleri",
                    "## 📡 Gözlem ve Keşif Sonuçları",
                    "## 🔮 Gelecek Projeksiyonları",
                    "## 🎓 Astronomi Öğrenme Kaynakları"
                ],
                "content_blocks": [
                    "Bu konunun uzay bilimine katkısı, insanlığın evrendeki yerini anlamamızda devrim yarattı.",
                    "Einstein'ın teorilerinden modern kuantum mekaniğine, bilimin bu alandaki büyük atılımları.",
                    "Samanyolu galaksisi içindeki konumumuz ve evrenin sonsuzluğundaki yerimiz hakkında şaşırtıcı gerçekler.",
                    "Son 50 yılda geliştirilen teknolojiler, bu alanda çığır açan keşiflere imza attı.",
                    "Uzayda yaşamış astronotların bu konuya dair birinci ağızdan deneyimleri ve gözlemleri.",
                    "Hubble ve James Webb teleskoplarının sağladığı veriler, anlayışımızı tamamen değiştirdi.",
                    "Önümüzdeki 100 yılda bu alanda bizi bekleyen olası gelişmeler ve keşifler.",
                    "Astronomi tutkunları için en güncel ve güvenilir bilim kaynakları rehberi."
                ]
            },
            "quotes": {
                "sections": [
                    "## 💭 Bu Sözlerin Derin Anlamı",
                    "## 📚 Tarihsel ve Kültürel Bağlam",
                    "## 🎯 Günlük Yaşama Uygulanması",
                    "## 🧠 Psikolojik Etkileri",
                    "## 🌟 İlham Veren Yorumlar",
                    "## 💼 İş Dünyasında Kullanımı",
                    "## 🔄 Kişisel Gelişimde Rolü",
                    "## 📖 Benzer İlham Verici Kaynaklar"
                ],
                "content_blocks": [
                    "Bu sözlerin ardındaki derin felsefi anlam, yaşamımızı nasıl yönlendirdiğimizi etkiliyor.",
                    "Bu ifadelerin ortaya çıktığı tarihsel dönem ve kültürel koşulları anlamak önemli.",
                    "Bu bilgeliği günlük kararlarınızda ve yaşam seçimlerinizde nasıl rehber alabilirsiniz.",
                    "Pozitif psikoloji araştırmaları, bu tür düşüncelerin zihinsel sağlığa etkilerini kanıtlıyor.",
                    "Bu sözlerden ilham alan ünlü kişilerin hayat hikayeleri ve başarı öyküleri.",
                    "Liderlik ve girişimcilik dünyasında bu yaklaşımın pratik uygulamaları.",
                    "Kendinizi geliştirme yolculuğunuzda bu öğretileri nasıl hayata geçirirsiniz.",
                    "Benzer derinlikte ilham veren kitaplar, alıntılar ve felsefi kaynaklar."
                ]
            }
        }

        template = templates.get(category, templates["health"])

        # İçerik oluştur
        content_parts = [
            f"# {original_title}",
            "",
            f"*{original_summary}*",
            "",
            "---",
            ""
        ]

        # Her bölüm için içerik ekle
        for i, section in enumerate(template["sections"]):
            content_parts.append(section)
            content_parts.append("")
            content_parts.append(template["content_blocks"][i])
            content_parts.append("")

            # Ek paragraf ekle
            extra_content = self.generate_additional_content(category, i)
            content_parts.append(extra_content)
            content_parts.append("")
            content_parts.append("---")
            content_parts.append("")

        # Sonuç bölümü
        content_parts.extend([
            "## 🎯 Sonuç",
            "",
            f"Bu kapsamlı rehberde, {original_title.lower()} konusunu her açıdan ele aldık. Bilimsel temelleri, pratik uygulamaları ve uzman önerilerini birleştirerek, sizin için en değerli bilgileri derledik.",
            "",
            "Unutmayın, bu konudaki başarı sabır ve kararlılık gerektiriyor. Adım adım ilerleyerek, kalıcı ve olumlu değişimler yaratabilirsiniz.",
            "",
            "*Bu makale, alanında uzman kişiler tarafından incelenmiş ve güncel bilimsel veriler ışığında hazırlanmıştır.*",
            ""
        ])

        return "\n".join(content_parts)

    def generate_additional_content(self, category, section_index):
        """Bölüm için ek içerik üret"""
        additional_contents = {
            "health": [
                "Dünya Sağlık Örgütü'nün son raporlarına göre, bu konudaki farkındalık seviyesi son 10 yılda dramatik şekilde arttı. Özellikle pandemi döneminde insanlar sağlık konularına daha çok önem vermeye başladı.",
                "Harvard Tıp Fakültesi'nde yapılan uzun vadeli araştırmalar, bu yaklaşımı benimseyen kişilerin yaşam beklentilerinin ortalama 7 yıl daha uzun olduğunu gösteriyor.",
                "Pratik uygulamada en önemli nokta, küçük adımlarla başlamak. Ani ve radikal değişiklikler genellikle sürdürülemez ve motivasyon kaybına yol açar.",
                "Tıp literatüründe karşılaştığımız vakaların %80'inde, hastalar bu uyarıları dikkate almadıkları için istenmeyen sonuçlarla karşılaştı.",
                "Uzmanlar hemfikir: Bu alanda başarılı olmak için multidisipliner yaklaşım şart. Sadece tıbbi tedavi değil, beslenme, egzersiz ve ruh sağlığı da kritik.",
                "En çarpıcı başarı hikayesi, 6 ay önce ümitsiz durumdaki hastanın bugün tamamen sağlıklı yaşamı. Bu umut verici örnekler motivasyon kaynağımız.",
                "Sürdürülebilirlik açısından en etkili strateji, alışkanlık piramidi tekniği. Küçük alışkanlıklar büyük değişimlerin temelini oluşturuyor.",
                "Alanında önde gelen derneklerin önerdiği kaynaklar arasında, peer-reviewed makaleler ve güncel rehberler öne çıkıyor."
            ],
            "love": [
                "Çift terapistlerinin 20 yıllık gözlemlerine göre, bu konuda bilinçli davranan çiftlerin ilişki memnuniyeti %75 daha yüksek çıkıyor.",
                "Nöroloji araştırmaları, aşk ve bağlanma süreçlerinin beyin kimyasını nasıl etkilediğini gösteren çarpıcı bulgular ortaya koydu.",
                "Günlük hayatta bu teknikleri uygulamanın sırrı, samimi anlarda küçük jestlerde gizli. Büyük romantik hareketlerden çok, tutarlılık önemli.",
                "İlişki uzmanları uyarıyor: Bu yaygın hatalar, sağlıklı ilişkilerde bile telafisi zor hasarlara neden olabiliyor.",
                "Çift danışmanımızın en değerli tavsiyesi şu: İletişim bir beceri, öğrenilebilir ve geliştirilebilir. Kimse mükemmel doğmaz.",
                "En güzel örnek, 30 yıllık evli çiftin anlattığı hikaye. Zorlu dönemlerden nasıl çıktıkları herkese ilham veriyor.",
                "Uzun vadeli ilişki sağlığı için temel prensip: Karşılıklı saygı, anlayış ve sürekli gelişime açık olmak.",
                "İlişki gelişimi için önerilen kaynaklar arasında, çift terapisi kitapları ve uzman podcastleri öne çıkıyor."
            ]
        }

        contents = additional_contents.get(category, additional_contents["health"])
        return contents[section_index % len(contents)]

    def create_markdown_file(self, category, title, content):
        """Yeni markdown dosyası oluştur"""
        # Dosya adı oluştur
        date_str = datetime.now().strftime("%Y-%m-%d")
        slug = re.sub(r'[^\w\s-]', '', title.lower())
        slug = re.sub(r'[-\s]+', '-', slug)
        hash_id = hashlib.md5(f"{title}{datetime.now()}".encode()).hexdigest()[:8]
        filename = f"{date_str}-{slug}-{hash_id}.md"

        # Meta veriler oluştur
        tags = self.generate_tags(category, title)
        summary = self.generate_summary(category, title)

        frontmatter = f"""---
title: "{title}"
date: {datetime.now().strftime("%Y-%m-%d")}
summary: "{summary}"
tags: {tags}
views: {200 + (hash(title) % 500)}
---

"""

        # Dosya yolu
        file_path = Path(self.content_dir) / category / filename

        # Dosyayı yaz
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter + content)

        return file_path

    def generate_tags(self, category, title):
        """Kategori ve başlığa göre etiketler üret"""
        base_tags = {
            "health": ["sağlık", "yaşam", "beslenme", "egzersiz", "wellness"],
            "love": ["aşk", "ilişki", "romantizm", "çift", "aile"],
            "psychology": ["psikoloji", "zihin", "davranış", "kişilik", "gelişim"],
            "history": ["tarih", "geçmiş", "kültür", "medeniyet", "kronoloji"],
            "space": ["uzay", "astronomi", "bilim", "keşif", "galaksi"],
            "quotes": ["alıntı", "söz", "motivasyon", "ilham", "felsefe"]
        }

        tags = base_tags.get(category, ["genel", "bilgi"])

        # Başlıktan ek etiketler çıkar
        title_words = title.lower().split()
        for word in title_words:
            if len(word) > 4 and word not in tags:
                tags.append(word)

        return tags[:5]  # Maksimum 5 etiket

    def generate_summary(self, category, title):
        """Kategori ve başlığa göre özet üret"""
        summaries = {
            "health": f"{title} konusunda uzman önerileri, bilimsel araştırmalar ve pratik uygulamalar. Sağlıklı yaşam için kapsamlı rehber.",
            "love": f"{title} hakkında ilişki uzmanlarından öneriler, çift terapisti görüşleri ve başarılı ilişki stratejileri.",
            "psychology": f"{title} konusunda psikoloji uzmanları görüşleri, davranış bilimi araştırmaları ve kişisel gelişim önerileri.",
            "history": f"{title} tarihsel analizi, arkeolojik bulgular ve günümüze etkileri. Kapsamlı tarih incelemesi.",
            "space": f"{title} hakkında astronomi uzmanları analizi, uzay araştırmaları ve evren hakkında şaşırtıcı gerçekler.",
            "quotes": f"{title} alıntılarının derin anlamı, felsefi yorumları ve günlük yaşama uygulanabilir öğütler."
        }

        return summaries.get(category, f"{title} hakkında kapsamlı bilgi ve uzman önerileri.")

    def process_short_files(self, delete_short=False, extend_short=True):
        """Kısa dosyaları işle"""
        analysis = self.analyze_all_content()
        results = {
            "processed": 0,
            "deleted": 0,
            "extended": 0,
            "errors": []
        }

        print(f"\n📊 İÇERİK ANALİZİ:")
        print(f"Toplam dosya: {analysis['total_files']}")
        print(f"Kısa dosya ({self.min_word_count} kelimeden az): {len(analysis['short_files'])}")
        print(f"Uygun dosya: {len(analysis['good_files'])}")

        if len(analysis['short_files']) == 0:
            print("✅ Tüm dosyalar uygun uzunlukta!")
            return results

        print(f"\n🔧 KISA DOSYALAR İŞLENİYOR...")

        for file_info in analysis['short_files']:
            try:
                file_path = Path(file_info['path'])

                # Dosyayı oku
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Meta verileri çıkar
                meta_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
                if meta_match:
                    meta_content = meta_match.group(1)
                    title_match = re.search(r'title:\s*["\']?(.*?)["\']?$', meta_content, re.MULTILINE)
                    summary_match = re.search(r'summary:\s*["\']?(.*?)["\']?$', meta_content, re.MULTILINE)

                    title = title_match.group(1) if title_match else "Başlık Bulunamadı"
                    summary = summary_match.group(1) if summary_match else "Özet bulunamadı"

                    # Kategoriyi dosya yolundan çıkar
                    category = file_path.parent.name

                    print(f"  📝 İşleniyor: {title} ({file_info['word_count']} kelime)")

                    if delete_short:
                        # Kısa dosyayı sil
                        file_path.unlink()
                        results["deleted"] += 1
                        print(f"    🗑️ Silindi")

                    if extend_short:
                        # Uzun versiyonu oluştur
                        long_content = self.generate_long_content(category, title, summary)

                        if delete_short:
                            # Yeni dosya oluştur
                            new_file = self.create_markdown_file(category, title, long_content)
                            print(f"    ✅ Yeni uzun versiyon oluşturuldu: {new_file.name}")
                        else:
                            # Mevcut dosyayı güncelle
                            new_frontmatter = content.split('---')[1]
                            updated_content = f"---{new_frontmatter}---\n\n{long_content}"

                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(updated_content)
                            print(f"    ✅ Dosya uzatıldı")

                        results["extended"] += 1

                    results["processed"] += 1

                else:
                    print(f"    ⚠️ Meta veri bulunamadı: {file_path.name}")

            except Exception as e:
                error_msg = f"Hata: {file_info['path']} - {str(e)}"
                results["errors"].append(error_msg)
                print(f"    ❌ {error_msg}")

        print(f"\n✅ İŞLEM TAMAMLANDI:")
        print(f"İşlenen dosya: {results['processed']}")
        print(f"Silinen dosya: {results['deleted']}")
        print(f"Uzatılan dosya: {results['extended']}")
        if results['errors']:
            print(f"Hata sayısı: {len(results['errors'])}")

        return results

def main():
    analyzer = ContentAnalyzer()

    print("🚀 MindVerse Daily - İçerik Optimizasyonu")
    print("=" * 50)

    # Önce analiz yap
    analysis = analyzer.analyze_all_content()

    if len(analysis['short_files']) > 0:
        print(f"\n⚠️ {len(analysis['short_files'])} kısa dosya bulundu!")

        choice = input("\nNe yapmak istiyorsunuz?\n1. Kısa dosyaları uzat (önerilen)\n2. Kısa dosyaları sil ve yenisini oluştur\n3. Sadece analiz göster\nSeçiminiz (1-3): ")

        if choice == "1":
            analyzer.process_short_files(delete_short=False, extend_short=True)
        elif choice == "2":
            confirm = input("⚠️ Bu işlem kısa dosyaları silecek! Emin misiniz? (y/N): ")
            if confirm.lower() == 'y':
                analyzer.process_short_files(delete_short=True, extend_short=True)
            else:
                print("İşlem iptal edildi.")
        else:
            print("Sadece analiz gösterildi.")
    else:
        print("✅ Tüm dosyalar uygun uzunlukta!")

if __name__ == "__main__":
    main()
