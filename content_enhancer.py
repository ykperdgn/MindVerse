#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import glob

def enhance_astrology_content():
    """Astroloji içeriklerini SEO için optimize et"""

    print("🚀 Astroloji İçerik Optimizasyonu Başlatılıyor...\n")

    # Burç keywords map
    sign_keywords = {
        'koc': 'koç burcu, koç günlük, koç astroloji, koç yorumu, aries',
        'boga': 'boğa burcu, boğa günlük, boğa astroloji, boğa yorumu, taurus',
        'ikizler': 'ikizler burcu, ikizler günlük, ikizler astroloji, gemini',
        'yengec': 'yengeç burcu, yengeç günlük, yengeç astroloji, cancer',
        'aslan': 'aslan burcu, aslan günlük, aslan astroloji, aslan yorumu, leo',
        'basak': 'başak burcu, başak günlük, başak astroloji, virgo',
        'terazi': 'terazi burcu, terazi günlük, terazi astroloji, libra',
        'akrep': 'akrep burcu, akrep günlük, akrep astroloji, scorpio',
        'yay': 'yay burcu, yay günlük, yay astroloji, sagittarius',
        'oglak': 'oğlak burcu, oğlak günlük, oğlak astroloji, capricorn',
        'kova': 'kova burcu, kova günlük, kova astroloji, aquarius',
        'balik': 'balık burcu, balık günlük, balık astroloji, pisces'
    }

    # Astroloji içerik uzantıları
    content_extensions = {
        'gunluk': {
            'title_suffix': 'Günlük Yorumu',
            'content': [
                "\n## 🌅 Sabah Enerjisi\n\nBugün sabah saatlerinde kendinizi daha enerjik hissedeceksiniz. Güneş'in olumlu etkisiyle yeni başlangıçlar için ideal bir zaman.\n",
                "\n## 🌙 Akşam Değerlendirmesi\n\nGünün sonunda yaşadıklarınızı değerlendirme zamanı. Bu deneyimler gelecekteki kararlarınız için değerli ipuçları verecek.\n",
                "\n## 💎 Öneriler\n\n- Sabah meditasyonu yapın\n- Pozitif düşüncelere odaklanın\n- Sevdiklerinizle vakit geçirin\n- Yeni projeler için plan yapın\n"
            ]
        },
        'haftalik': {
            'title_suffix': 'Haftalık Yorumu',
            'content': [
                "\n## 📅 Haftalık Genel Bakış\n\nBu hafta sizin için dönüşüm ve yeniliklerin haftası olacak. Gezegen hareketleri lehinizdeki gelişmeleri destekliyor.\n",
                "\n## 🎯 Odaklanılacak Alanlar\n\n- **Pazartesi-Çarşamba**: İletişim ve sosyal aktiviteler\n- **Perşembe-Cuma**: Kariyer ve iş hayatı\n- **Hafta Sonu**: Dinlenme ve yenilenme\n",
                "\n## ⚠️ Dikkat Edilecekler\n\nBu hafta aceleci kararlar almaktan kaçının. Özellikle finansal konularda temkinli olun.\n"
            ]
        },
        'aylik': {
            'title_suffix': 'Aylık Yorumu',
            'content': [
                "\n## 🌙 Aylık Enerji Akışı\n\nBu ay sizin için büyüme ve gelişimin ayı. Uzun vadeli hedeflerinize odaklanmak için mükemmel bir zaman.\n",
                "\n## 📈 Fırsat Dönemleri\n\n- **İlk hafta**: Yeni başlangıçlar ve projeler\n- **İkinci hafta**: İlişkiler ve sosyal bağlantılar\n- **Üçüncü hafta**: Kariyer ve başarı\n- **Son hafta**: Değerlendirme ve planlama\n",
                "\n## 🔮 Astrolojik Destek\n\nBu ay boyunca gezegen hareketleri sizden yana. Özellikle yaratıcı projelerinizde büyük ilerlemeler kaydedebilirsiniz.\n"
            ]
        }    }

    astrology_dir = "src/content/astrology"

    if not os.path.exists(astrology_dir):
        print(f"❌ {astrology_dir} bulunamadı!")
        return

    files = glob.glob(os.path.join(astrology_dir, "*.md"))
    enhanced_count = 0

    for file_path in files:
        filename = os.path.basename(file_path)
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
                print(f"⚠️ Could not read {filename} with any encoding")
                continue

            # Burç ismini çıkar
            sign_match = None
            for sign in sign_keywords.keys():
                if sign in filename:
                    sign_match = sign
                    break

            if not sign_match:
                continue

            # İçerik tipini belirle
            content_type = None
            for ctype in content_extensions.keys():
                if ctype in filename:
                    content_type = ctype
                    break

            if not content_type:
                continue

            original_content = content

            # Keywords ekle
            if 'keywords:' not in content:
                keywords = sign_keywords[sign_match]
                if content_type == 'gunluk':
                    keywords += ', günlük burç, burç yorumu, astroloji rehberi'
                elif content_type == 'haftalik':
                    keywords += ', haftalık burç, burç analizi, astroloji danışmanlık'
                elif content_type == 'aylik':
                    keywords += ', aylık burç, burç tahmini, astroloji merkezi'

                # Keywords'i description'dan sonra ekle
                content = re.sub(
                    r'(description: [^\n]+\n)',
                    f'\\1keywords: "{keywords}"\n',
                    content
                )

            # İçerik uzatma
            word_count = len(re.sub(r'---.*?---', '', content, flags=re.DOTALL).split())
            if word_count < 350:
                additional_content = ''.join(content_extensions[content_type]['content'])

                # İçeriği sonuna ekle (closing tags'den önce)
                if content.endswith('```'):
                    content = content[:-3] + additional_content + '\n```'
                else:
                    content += additional_content

            # Tarih ve gezegen bilgileri ekle
            if "## 🌟 Günün Gezegeni" not in content:
                planet_info = f"\n## 🌟 Günün Gezegeni\n\n**Bugünün Ana Etkisi**: Mars'ın {sign_match.title()} burcundaki konumu size ekstra enerji veriyor. Bu etkiyi doğru yönlendirin.\n"
                content += planet_info

            # Eğer değişiklik varsa kaydet
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                enhanced_count += 1
                print(f"✅ Enhanced: {filename}")

        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")

    print(f"\n🎉 Toplam {enhanced_count} dosya optimize edildi!")

    # Index sayfasının title'ını düzelt
    index_path = "src/pages/index.astro"
    if os.path.exists(index_path):
        try:
            with open(index_path, 'r', encoding='utf-8') as f:
                content = f.read()

            if 'title: "Sağlık"' in content:
                content = content.replace('title: "Sağlık"', 'title: "MindVerse - Çoklu Niş Bilgi Portalı"')

                with open(index_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print("✅ Index title fixed!")

        except Exception as e:
            print(f"❌ Error fixing index: {e}")

if __name__ == "__main__":
    enhance_astrology_content()
