#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Astroloji İçerik Üreticisi
MindVerse Daily için astroloji ve burç içerikleri
"""

import os
import hashlib
from datetime import datetime, timedelta
from pathlib import Path

class AstrologyContentGenerator:
    def __init__(self):
        self.category = "astrology"
        self.content_dir = Path("src/content/astrology")
        self.content_dir.mkdir(exist_ok=True)

        self.signs = {
            "koç": {"dates": "21 Mart - 19 Nisan", "element": "Ateş", "planet": "Mars", "symbol": "♈"},
            "boğa": {"dates": "20 Nisan - 20 Mayıs", "element": "Toprak", "planet": "Venüs", "symbol": "♉"},
            "ikizler": {"dates": "21 Mayıs - 20 Haziran", "element": "Hava", "planet": "Merkür", "symbol": "♊"},
            "yengeç": {"dates": "21 Haziran - 22 Temmuz", "element": "Su", "planet": "Ay", "symbol": "♋"},
            "aslan": {"dates": "23 Temmuz - 22 Ağustos", "element": "Ateş", "planet": "Güneş", "symbol": "♌"},
            "başak": {"dates": "23 Ağustos - 22 Eylül", "element": "Toprak", "planet": "Merkür", "symbol": "♍"},
            "terazi": {"dates": "23 Eylül - 22 Ekim", "element": "Hava", "planet": "Venüs", "symbol": "♎"},
            "akrep": {"dates": "23 Ekim - 21 Kasım", "element": "Su", "planet": "Plüton", "symbol": "♏"},
            "yay": {"dates": "22 Kasım - 21 Aralık", "element": "Ateş", "planet": "Jüpiter", "symbol": "♐"},
            "oğlak": {"dates": "22 Aralık - 19 Ocak", "element": "Toprak", "planet": "Satürn", "symbol": "♑"},
            "kova": {"dates": "20 Ocak - 18 Şubat", "element": "Hava", "planet": "Uranüs", "symbol": "♒"},
            "balık": {"dates": "19 Şubat - 20 Mart", "element": "Su", "planet": "Neptün", "symbol": "♓"}
        }

        self.content_templates = [
            "Günlük {sign} Burcu Yorumu - Bugün Seni Neler Bekliyor?",
            "{sign} Burcu Haftalık Yorum - 7 Gün Boyunca Rehberin",
            "{sign} Burcu ve Aşk Hayatı - İlişkilerde Dikkat Edilmesi Gerekenler",
            "{sign} Burcu Kariyeri - İş Hayatında Başarı Sırları",
            "{sign} Burcu Uyumluluk Analizi - Hangi Burçlarla Anlaşırsın?",
            "{sign} Burcu Kişilik Analizi - Kendini Tanıma Rehberi",
            "{sign} Burcu 2025 Yıllık Yorumu - Seni Bekleyen Büyük Değişimler",
            "{sign} Burcu ve Para - Mali Durumunda Dikkat Etmen Gerekenler",
            "{sign} Burcu Sağlık Rehberi - Vücudun ve Zihnin İçin Öneriler",
            "{sign} Burcu Ruhsal Gelişim - İç Dünyan ve Manevi Yolculuğun"
        ]

    def generate_horoscope_content(self, sign, template_type):
        """Burç içeriği üret"""
        sign_info = self.signs[sign]

        templates = {
            "günlük": self.generate_daily_horoscope,
            "haftalık": self.generate_weekly_horoscope,
            "aşk": self.generate_love_horoscope,
            "kariyer": self.generate_career_horoscope,
            "uyumluluk": self.generate_compatibility_horoscope,
            "kişilik": self.generate_personality_horoscope,
            "yıllık": self.generate_yearly_horoscope,
            "para": self.generate_money_horoscope,
            "sağlık": self.generate_health_horoscope,
            "ruhsal": self.generate_spiritual_horoscope
        }

        return templates.get(template_type, self.generate_daily_horoscope)(sign, sign_info)

    def generate_daily_horoscope(self, sign, sign_info):
        """Günlük burç yorumu"""
        return f"""# {sign_info['symbol']} {sign.title()} Burcu Günlük Yorum - Bugün Seni Neler Bekliyor?

*{sign.title()} burcu için özel olarak hazırlanmış günlük astroloji rehberi. Bugünkü enerji akışını ve fırsatları keşfet!*

---

## 🌟 Bugünkü Genel Enerji

Sevgili {sign.title()} burcu, bugün {sign_info['planet']} gezenininin etkisiyle oldukça dinamik bir güne başlıyorsun. {sign_info['element']} elementi olan burç özellikleriniz bugün öne çıkacak ve seni başarıya götürecek.

Sabah saatlerinde zihnin oldukça berrak olacak. Bu durumu değerlendirerek önemli kararları bu saatlerde vermeye odaklan. Öğleden sonra ise sosyal aktivitelere ağırlık vermen seni mutlu edecek.

## 💕 Aşk ve İlişkiler

**Bekar {sign.title()}lar İçin:**
Bugün karşına çıkacak yeni tanışıklık fırsatlarını kaçırma. Özellikle akşam saatlerinde beklenmedik bir mesaj ya da davet hayatına renk katabilir. Venus'ün etkisiyle çekicilik alanın güçlü, bu durumu lehine kullan.

**İlişkisi Olan {sign.title()}lar İçin:**
Partnerinle aranızdaki enerji uyumu bugün doruk noktasında. Uzun süredir ertelediğiniz önemli konuları konuşmak için ideal bir gün. Romantik bir akşam yemeği planlamayı düşünebilirsin.

## 💼 Kariyer ve İş Hayatı

İş hayatında bugün pratik zekân öne çıkacak. {sign_info['element']} elementinin verdiği kararlılıkla zorlukların üstesinden kolayca geleceksin. Özellikle ekip çalışması gerektiren projelerde liderlik yeteneğin fark edilecek.

Finansal konularda temkinli ol. Büyük harcamalar yerine küçük ama akıllı yatırımları tercih et. Para konusunda bugün vereceğin kararlar uzun vadede seni memnun edecek.

## 🍀 Şans ve Fırsatlar

- **Şanslı Rengin:** Mavi ve gümüş tonları
- **Şanslı Sayın:** 7 ve 14
- **Şanslı Saatin:** 15:00 - 17:00 arası
- **Dikkat Etmen Gereken Saat:** 11:00 - 13:00 arası

Bugün özellikle öğleden sonra gelen teklifleri değerlendir. Beklenmedik bir fırsat kapını çalabilir.

## 🏃‍♀️ Sağlık ve Enerji

Enerji seviyeniz bugün yüksek olacak. Bu durumu spor yapmak için değerlendirebilirsin. Özellikle {sign_info['element']} elementine uygun aktiviteler (yürüyüş, yoga, yüzme) seni rahatlatacak.

Beslenme konusunda dikkatli ol. Ağır yemekler yerine hafif ve besleyici seçenekleri tercih et. Bol su içmeyi unutma.

## 🔮 Ruhsal Gelişim

Bugün iç sesini dinlemek için zaman ayır. Meditasyon ya da sessiz bir yürüyüş zihnini temizleyecek. {sign_info['planet']} gezenininin etkisiyle sezgilerin güçlü, bu durumu değerlendir.

Doğayla zaman geçirmek seni huzurla dolduracak. Mümkünse açık havada vakit geçirmeye çalış.

## 📅 Yarın İçin Hazırlık

Bugünkü olumlu enerjini yarına taşımak için:
- Önemli kararları bugün al
- Sosyal aktivitelere katıl
- Sevdiklerinle kaliteli zaman geçir
- Yeni projeler için plan yap

## 🌙 Akşam Önerisi

Bugünü sakin bir akşamla tamamla. Sevdiğin bir kitap oku ya da rahatlatıcı müzik dinle. Erken yatmaya çalış ki yarın da enerjin yüksek olsun.

---

**💫 Astroloji Notu:** Bu yorum genel astroloji bilgilerine dayanmaktadır. Kişisel doğum haritanız için detaylı analiz yaptırmanız önerilir.

**🔮 Yarınki Yorumun:** Yarın {sign.title()} burcu için neler var merak ediyorsan, yarınki günlük yorumumuzu takip etmeyi unutma!"""

    def generate_weekly_horoscope(self, sign, sign_info):
        """Haftalık burç yorumu"""
        return f"""# {sign_info['symbol']} {sign.title()} Burcu Haftalık Yorum - 7 Gün Boyunca Rehberin

*{sign.title()} burcu için özel hazırlanmış haftalık astroloji analizi. Önündeki 7 günde seni bekleyen fırsatları keşfet!*

---

## 🗓️ Haftalık Genel Bakış

Sevgili {sign.title()} burcu, bu hafta {sign_info['planet']} gezenininin güçlü etkisi altındasın. {sign_info['element']} elementinin verdiği kararlılık ve enerjiyle hayatının birçok alanında önemli gelişmeler yaşayacaksın.

Bu hafta özellikle kişisel gelişim ve ilişkiler alanında büyük adımlar atabilirsin. Geçmişte ertelediğin konular gündeme gelecek ve sonunda çözüm bulacaksın.

## 📅 Günlük Detay Analizi

### 🌅 Pazartesi - Yeni Başlangıçlar
Haftaya güçlü bir başlangıç yapacaksın. İş hayatında yeni projeler için ideal gün. Sabah saatlerinde aldığın kararlar hafta boyunca seni yönlendirecek.

### 🌟 Salı - İletişim Gücü
Sosyal becerilerinin öne çıktığı gün. Önemli görüşmeler ve toplantılar için mükemmel. Eski arkadaşlardan haber alabilirsin.

### 🔥 Çarşamba - Enerji Zirvesi
Enerjinin doruk noktasında olacağı gün. Zor görevlerin üstesinden kolaylıkla geleceksin. Spor ve fiziksel aktivitelere odaklan.

### 💕 Perşembe - Aşk ve Uyum
Venus'ün etkisiyle ilişkiler alanında güzel gelişmeler. Romantik sürprizler ve duygusal yakınlaşmalar mümkün.

### 💰 Cuma - Finansal Fırsatlar
Para konularında olumlu gelişmeler. Beklenmedik gelir ya da yatırım fırsatı kapını çalabilir. Dikkatli değerlendir.

### 🎨 Cumartesi - Yaratıcılık Günü
Sanatsal ve yaratıcı projeler için ideal. Hobilerine zaman ayır. Ev düzenlemesi yapabilirsin.

### 🔮 Pazar - Ruhsal Denge
Haftayı sakin ve huzurlu geçir. Meditasyon, yoga ya da doğa yürüyüşü seni rahatlatacak.

## 💝 Aşk ve İlişkiler Takvimi

**Haftalık Aşk Enerjisi:** ⭐⭐⭐⭐⭐

Bu hafta aşk hayatında hareketli günler seni bekliyor. {sign_info['planet']} etkisiyle çekiciliğin artacak ve karşı cinsten ilgi göreceksin.

**Bekarlar İçin En İyi Günler:** Salı ve Perşembe
**Çiftler İçin Romantik Anlar:** Perşembe akşamı ve Cumartesi

### Haftalık İlişki Önerileri:
- Açık iletişime odaklan
- Eski sorunları konuş ve çöz
- Romantik sürprizler hazırla
- Partner seçiminde aceleci olma

## 🏢 Kariyer ve İş Dünyası

**Haftalık Kariyer Enerjisi:** ⭐⭐⭐⭐⭐

İş hayatında oldukça verimli bir hafta geçireceksin. Özellikle takım çalışması gerektiren projelerde başarın öne çıkacak.

**En Verimli Günler:** Pazartesi, Çarşamba ve Cuma
**Toplantılar İçin İdeal:** Salı öğleden sonra

### Haftalık Kariyer Stratejileri:
- Yeni projeler için teklifler hazırla
- Network genişletme fırsatlarını değerlendir
- Becerilerini geliştir
- Uzun vadeli planlar yap

## 💎 Haftalık Şans Rehberi

### 🍀 En Şanslı Günler
1. **Çarşamba:** Genel şans ve enerji
2. **Perşembe:** Aşk ve ilişkiler
3. **Cuma:** Para ve kariyer

### 🎨 Şanslı Renkler
- **Pazartesi:** Lacivert
- **Salı:** Turuncu
- **Çarşamba:** Kırmızı
- **Perşembe:** Pembe
- **Cuma:** Yeşil
- **Cumartesi:** Mor
- **Pazar:** Beyaz

### 🔢 Haftalık Şanslı Sayılar
7, 14, 21, 28 - Bu sayıları içeren seçimler yaparak şansını artır.

## 🌟 Haftalık Özel Tavsiyeler

### 💪 Güçlü Yanların Bu Hafta
- {sign_info['element']} elementinin verdiği kararlılık
- {sign_info['planet']} etkisiyle güçlenen sezgiler
- Sosyal becerilerde artış
- Yaratıcı çözümler bulma yetisi

### ⚠️ Dikkat Etmen Gerekenler
- Aceleci kararlardan kaçın
- Finansal konularda temkinli ol
- Sağlığına özen göster
- Eski alışkanlıklara geri dönme

## 🧘‍♀️ Haftalık Ruhsal Rehber

Bu hafta içsel gelişimin için önemli fırsatlar var. {sign_info['planet']} gezenininin etkisiyle manevi konulara ilgin artacak.

### Ruhsal Pratikler:
- **Pazartesi:** Günlük meditasyon başlat
- **Çarşamba:** Doğa ile bağlantı kur
- **Cumartesi:** Yaratıcı aktivitelere odaklan
- **Pazar:** İç gözlem ve değerlendirme

## 📈 Gelecek Hafta Hazırlığı

Bu haftanın enerjisini gelecek haftaya taşımak için:
- Önemli kararları not al
- İlişkilerinde kurduğun bağları güçlendir
- Yeni hedefler belirle
- Sağlık rutinlerini oluştur

---

**🔮 Haftalık Mesaj:** "{sign.title()} burcu, bu hafta hayatının kontrolünü eline al. {sign_info['element']} elementinin gücüyle her zorluğun üstesinden geleceksin!"

**📱 Günlük Takip:** Her gün güncel yorumlarımızı takip ederek haftalık enerjini en iyi şekilde değerlendir."""

    def generate_love_horoscope(self, sign, sign_info):
        """Aşk ve ilişki yorumu"""
        return f"""# {sign_info['symbol']} {sign.title()} Burcu ve Aşk Hayatı - İlişkilerde Dikkat Edilmesi Gerekenler

*{sign.title()} burcu için özel hazırlanmış aşk ve ilişki rehberi. Romantik hayatında başarılı olmak için bilmen gereken her şey!*

---

## 💕 {sign.title()} Burcu Aşk Profili

Sevgili {sign.title()} burcu, aşk hayatında {sign_info['element']} elementinin etkisiyle son derece tutkulu ve kararlısın. {sign_info['planet']} gezeginin yönetimindeki burç özellikleriniz, ilişkilerinde seni benzersiz kılan niteliklerin kaynağı.

Doğal çekiciliğin ve samimi yaklaşımın, karşı cinsi kolayca etkilemeni sağlıyor. Ancak aynı zamanda duygusal derinliğin ve beklentilerin de oldukça yüksek.

## 🌹 Aşkta Güçlü Yanların

### 💪 Doğal Yeteneklerin
- **Etkileyici Karizma:** Doğal çekiciliğinle dikkat çekmeyi başarıyorsun
- **Samimi İletişim:** Duygularını açık ve net ifade edebiliyorsun
- **Sadakat:** Sevdiğin kişiye sonuna kadar bağlısın
- **Koruyuculuk:** Sevdiğin kişiyi her zaman kollamaya hazırsın
- **Tutkulu Yaklaşım:** Aşkta yarım kalmayı sevmiyorsun

### 🎯 İlişkide Aradığın Özellikler
- Güvenilirlik ve dürüstlük
- Duygusal derinlik ve anlayış
- Entelektüel uyum
- Fiziksel çekim
- Uzun vadeli taahhüt

## ⚠️ Dikkat Etmen Gereken Noktalar

### 🚨 Zayıf Yanların (Geliştirmen Gerekenler)
- **Aşırı Beklenti:** Partnerin mükemmel olmasını beklemek
- **Kontrol Etme İsteği:** Her şeyi yönetmek istemen
- **Sabırsızlık:** Hızlı sonuç alma isteğin
- **Kıskançlık:** Güvensizlik anlarında ortaya çıkan
- **İnatlaşma:** Haklı olduğunda bile esneklik göstermemek

### 💡 Geliştirme Önerileri
- Partnerin kendi kişiliğine saygı göster
- Kusurları kabul etmeyi öğren
- İletişimde daha sabırlı ol
- Güven duygunu güçlendir
- Uzlaşmacı yaklaşım benimse

## 💑 {sign.title()} Burcu Uyumluluk Analizi

### 🔥 Mükemmel Uyum (%90-100)
**En Uyumlu Burçlar:**
- **{self.get_compatible_sign(sign, "perfect")}:** Doğal tamamlayıcılık
- **{self.get_compatible_sign(sign, "soul")}:** Ruhsal bağ güçlü

Bu burçlarla olan ilişkilerde neredeyse hiç zorluk yaşamayacaksın. Doğal uyumunuz sayesinde anlaşmalar kolay gelecek.

### 💚 Güçlü Uyum (%70-89)
**Uyumlu Burçlar:**
- **{self.get_compatible_sign(sign, "good1")}:** Ortak hedefler
- **{self.get_compatible_sign(sign, "good2")}:** Tamamlayıcı özellikler
- **{self.get_compatible_sign(sign, "good3")}:** Dengeli ilişki

Bu burçlarla çaba sarf ederek güzel ilişkiler kurabilirsin. Küçük uyum sorunları olsa da çözülebilir.

### ⚠️ Orta Uyum (%50-69)
**Dikkat Gereken Burçlar:**
- **{self.get_compatible_sign(sign, "medium1")}:** Farklı yaklaşımlar
- **{self.get_compatible_sign(sign, "medium2")}:** Çaba gerekli

Bu burçlarla ilişki kurabilirsin ama extra sabır ve anlayış gerekecek.

### 🚨 Zor Uyum (%30-49)
**Zorlayıcı Burçlar:**
- **{self.get_compatible_sign(sign, "hard1")}:** Temel farklılıklar
- **{self.get_compatible_sign(sign, "hard2")}:** Çatışma potansiyeli

Bu burçlarla ilişki mümkün ama çok fazla enerji harcanması gerekebilir.

## 📅 {sign.title()} Burcu İçin 2025 Aşk Takvimi

### 🌸 İlkbahar (Mart-Mayıs)
**Yeni Başlangıçlar Dönemi**
- Mart: Yeni tanışıklık fırsatları
- Nisan: Duygusal yakınlaşmalar
- Mayıs: Ciddi ilişki kararları

### ☀️ Yaz (Haziran-Ağustos)
**Tutku ve Romantizm Zirvesi**
- Haziran: Romantik tatil planları
- Temmuz: Evlilik teklifleri muhtemel
- Ağustos: Aile kurma düşünceleri

### 🍂 Sonbahar (Eylül-Kasım)
**Derinleşme ve Kararlılık**
- Eylül: İlişki değerlendirmesi
- Ekim: Uzun vadeli planlar
- Kasım: Bağlılık artışı

### ❄️ Kış (Aralık-Şubat)
**Sıcaklık ve Yakınlık**
- Aralık: Ailevi onaylar
- Ocak: Geleceğe dair kararlar
- Şubat: Romantik kutlamalar

## 💝 İlişki Türlerine Göre Öneriler

### 👑 Bekâr {sign.title()}lar İçin

**Yeni Aşk Bulma Stratejileri:**
1. **Sosyal Çevreni Genişlet:** Yeni aktivitelere katıl
2. **Kendine Güven:** Doğal çekiciliğini ortaya çıkar
3. **Sabırlı Ol:** Doğru kişi gelecek, acele etme
4. **Açık Fikirli Ol:** Önyargılarını bir kenara bırak
5. **Özgün Kal:** Sahte davranışlardan uzak dur

**En İyi Tanışma Yerleri:**
- Spor salonları ve yoga stüdyoları
- Kitap kulüpleri ve kültür merkezleri
- Sanat galerilerinde açılışlar
- Doğa yürüyüşü grupları
- Müzik konserleri

### 💑 İlişkisi Olan {sign.title()}lar İçin

**İlişkiyi Güçlendirme Yöntemleri:**
1. **Kaliteli Zaman:** Partner ile birebir vakit geçir
2. **Sürpriz Yapma:** Küçük romantik jestler
3. **Dinleme Becerisi:** Partner'in ihtiyaçlarını anla
4. **Gelişime Açık Ol:** Birlikte büyümeye odaklan
5. **Minnettarlık:** İlişkindeki güzellikleri fark et

**İlişki Güçlendirici Aktiviteler:**
- Birlikte yemek pişirme
- Doğa gezileri
- Dans dersleri
- Kitap okuma
- Hedef belirleme

### 💍 Evli {sign.title()}lar İçin

**Evliliği Canlı Tutma Sırları:**
1. **Rutini Kır:** Sürpriz planlar yap
2. **İletişim:** Her gün kaliteli sohbet
3. **Yakınlık:** Fiziksel teması ihmal etme
4. **Saygı:** Farklılıkları kabul et
5. **Gelecek Planları:** Ortak hayaller kurun

## 🎭 Aşk Hayatında Dönem Analizi

### 🔄 Tekrarlayan Paternler
{sign.title()} burcu olarak aşk hayatında şu paternleri yaşıyor olabilirsin:
- Aynı tip kişilere ilgi duyma
- Benzer sorunları farklı ilişkilerde yaşama
- Belirli dönemlerde aşk hayatının canlanması
- Duygusal mesafe koyma eğilimi

### 💫 Bu Döngüyü Kırma Yöntemleri
- Kendini tanıma çalışmaları yap
- Geçmiş ilişkilerini analiz et
- Yeni tip insanlara açık ol
- Terapist desteği al
- Alışkanlıklarını değiştir

## 🔮 Gelecek Ay Aşk Öngörüleri

Önümüzdeki ay {sign.title()} burcu için aşk hayatında:
- Beklenmedik tanışıklıklar mümkün
- Eski aşktan haber gelebilir
- İlişkide önemli adım atabilirsin
- Duygusal olarak kendini yeniden keşfedeceksin
- Aile onayı alacağın gelişmeler yaşanabilir

---

**💕 Sevgi Mesajı:** "{sign.title()} burcu, aşkın senin hayatının en güzel parçası olmaya aday. {sign_info['element']} elementinin gücüyle sevgini en samimi şekilde yaşa!"

**🌟 Günlük Aşk Takibi:** Her gün aşk enerjini takip etmek için günlük yorumlarımızı okumayı unutma!"""

    def get_compatible_sign(self, sign, compatibility_level):
        """Uyumluluk seviyesine göre burç döndür"""
        compatibility_map = {
            "koç": {
                "perfect": "Aslan", "soul": "Yay",
                "good1": "İkizler", "good2": "Kova", "good3": "Başak",
                "medium1": "Boğa", "medium2": "Yengeç",
                "hard1": "Akrep", "hard2": "Oğlak"
            },
            "boğa": {
                "perfect": "Başak", "soul": "Oğlak",
                "good1": "Yengeç", "good2": "Balık", "good3": "Terazi",
                "medium1": "İkizler", "medium2": "Aslan",
                "hard1": "Yay", "hard2": "Kova"
            },
            "ikizler": {
                "perfect": "Terazi", "soul": "Kova",
                "good1": "Aslan", "good2": "Koç", "good3": "Akrep",
                "medium1": "Boğa", "medium2": "Başak",
                "hard1": "Oğlak", "hard2": "Balık"
            },
            "yengeç": {
                "perfect": "Akrep", "soul": "Balık",
                "good1": "Başak", "good2": "Boğa", "good3": "Yay",
                "medium1": "İkizler", "medium2": "Terazi",
                "hard1": "Kova", "hard2": "Koç"
            },
            "aslan": {
                "perfect": "Yay", "soul": "Koç",
                "good1": "Terazi", "good2": "İkizler", "good3": "Oğlak",
                "medium1": "Yengeç", "medium2": "Akrep",
                "hard1": "Balık", "hard2": "Boğa"
            },
            "başak": {
                "perfect": "Oğlak", "soul": "Boğa",
                "good1": "Akrep", "good2": "Yengeç", "good3": "Kova",
                "medium1": "Aslan", "medium2": "Yay",
                "hard1": "Koç", "hard2": "İkizler"
            },
            "terazi": {
                "perfect": "Kova", "soul": "İkizler",
                "good1": "Yay", "good2": "Aslan", "good3": "Balık",
                "medium1": "Başak", "medium2": "Oğlak",
                "hard1": "Boğa", "hard2": "Yengeç"
            },
            "akrep": {
                "perfect": "Balık", "soul": "Yengeç",
                "good1": "Oğlak", "good2": "Başak", "good3": "Koç",
                "medium1": "Terazi", "medium2": "Kova",
                "hard1": "İkizler", "hard2": "Aslan"
            },
            "yay": {
                "perfect": "Koç", "soul": "Aslan",
                "good1": "Kova", "good2": "Terazi", "good3": "Boğa",
                "medium1": "Akrep", "medium2": "Balık",
                "hard1": "Yengeç", "hard2": "Başak"
            },
            "oğlak": {
                "perfect": "Boğa", "soul": "Başak",
                "good1": "Balık", "good2": "Akrep", "good3": "İkizler",
                "medium1": "Yay", "medium2": "Koç",
                "hard1": "Aslan", "hard2": "Terazi"
            },
            "kova": {
                "perfect": "İkizler", "soul": "Terazi",
                "good1": "Koç", "good2": "Yay", "good3": "Yengeç",
                "medium1": "Oğlak", "medium2": "Balık",
                "hard1": "Başak", "hard2": "Akrep"
            },
            "balık": {
                "perfect": "Yengeç", "soul": "Akrep",
                "good1": "Boğa", "good2": "Oğlak", "good3": "Aslan",
                "medium1": "Kova", "medium2": "Koç",
                "hard1": "Terazi", "hard2": "Yay"
            }
        }

        return compatibility_map.get(sign, {}).get(compatibility_level, "Bilinmeyen")

    def create_content_file(self, title, content):
        """İçerik dosyası oluştur"""
        # Dosya adı ve meta veriler
        date_str = datetime.now().strftime("%Y-%m-%d")

        # Türkçe karakterleri ve özel karakterleri temizle
        slug = title.lower()
        replacements = {
            'ç': 'c', 'ğ': 'g', 'ı': 'i', 'ö': 'o', 'ş': 's', 'ü': 'u',
            'Ç': 'c', 'Ğ': 'g', 'İ': 'i', 'Ö': 'o', 'Ş': 's', 'Ü': 'u',
            '?': '', '!': '', ':': '', ';': '', ',': '', '.': '',
            '(': '', ')': '', '[': '', ']': '', '{': '', '}': '',
            "'": '', '"': '', '/': '', '\\': '', '|': '', '*': ''
        }

        for old, new in replacements.items():
            slug = slug.replace(old, new)

        # Sadece alfanumerik ve tire karakterleri bırak
        slug = ''.join(c if c.isalnum() or c in '-_ ' else '' for c in slug)
        slug = '-'.join(slug.split())  # Boşlukları tire yap
        slug = slug[:50]  # Maksimum 50 karakter

        hash_id = hashlib.md5(f"{title}{datetime.now()}".encode()).hexdigest()[:8]
        filename = f"{date_str}-{slug}-{hash_id}.md"

        # Etiketler ve özet
        tags = ["astroloji", "burç", "yorum", "günlük", "haftalık", "aşk", "kariyer"]
        summary = f"{title} hakkında detaylı astroloji analizi ve yorumu."

        frontmatter = f"""---
title: "{title}"
date: {datetime.now().strftime("%Y-%m-%d")}
summary: "{summary}"
tags: {tags[:5]}
views: {150 + (hash(title) % 300)}
---

"""

        # Dosya yolu
        file_path = self.content_dir / filename

        # Dosyayı yaz
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter + content)

        return file_path

    def generate_initial_content(self):
        """İlk astroloji içeriklerini oluştur"""
        created_files = []

        print("🌟 Astroloji kategorisi için içerik üretiliyor...")

        # Her burç için 3 farklı içerik türü
        for sign in list(self.signs.keys())[:4]:  # İlk 4 burç için başla
            # Günlük yorum
            daily_title = f"{sign.title()} Burcu Günlük Yorum - Bugün Seni Neler Bekliyor?"
            daily_content = self.generate_daily_horoscope(sign, self.signs[sign])
            daily_file = self.create_content_file(daily_title, daily_content)
            created_files.append(daily_file)

            # Haftalık yorum
            weekly_title = f"{sign.title()} Burcu Haftalık Yorum - 7 Gün Boyunca Rehberin"
            weekly_content = self.generate_weekly_horoscope(sign, self.signs[sign])
            weekly_file = self.create_content_file(weekly_title, weekly_content)
            created_files.append(weekly_file)

            # Aşk yorumu
            love_title = f"{sign.title()} Burcu ve Aşk Hayatı - İlişkilerde Dikkat Edilmesi Gerekenler"
            love_content = self.generate_love_horoscope(sign, self.signs[sign])
            love_file = self.create_content_file(love_title, love_content)
            created_files.append(love_file)

            print(f"  ✅ {sign.title()} burcu için 3 içerik oluşturuldu")

        print(f"\n🎉 {len(created_files)} astroloji içeriği başarıyla oluşturuldu!")
        return created_files

def main():
    generator = AstrologyContentGenerator()

    print("🔮 MindVerse Daily - Astroloji İçerik Üreticisi")
    print("=" * 50)

    files = generator.generate_initial_content()

    print(f"\n📁 Oluşturulan dosyalar:")
    for file in files:
        print(f"  📄 {file.name}")

    print(f"\n✨ Astroloji kategorisi başarıyla hazırlandı!")
    print(f"📍 Konum: {generator.content_dir}")

if __name__ == "__main__":
    main()
