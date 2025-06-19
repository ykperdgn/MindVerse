#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MindVerse Daily - Gelişmiş Astroloji İçerik Üreticisi
Günlük, Haftalık, Aylık Burç Yorumları + Burç Özellikleri
"""

import os
import json
import random
import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Tuple

class AdvancedAstrologyGenerator:
    def __init__(self):
        self.base_path = "src/content/astrology"

        # Burç bilgileri - Tarihler, özellikler, gezegenler
        self.zodiac_signs = {
            "koc": {
                "name": "Koç",
                "english": "Aries",
                "dates": "21 Mart - 19 Nisan",
                "element": "Ateş",
                "quality": "Öncü",
                "ruling_planet": "Mars",
                "symbol": "🐏",
                "colors": ["Kırmızı", "Turuncu"],
                "lucky_numbers": [1, 8, 17],
                "keywords": ["Girişken", "Lider", "Cesur", "Enerjik", "Bağımsız"],
                "personality": "Doğal liderler olan Koçlar, hayata başkalarından önce atılmayı seven, cesur ve girişken kişilerdir.",
                "strengths": ["Liderlik", "Cesaret", "Girişkenlik", "Bağımsızlık", "Kararlılık"],
                "weaknesses": ["Sabırsızlık", "Öfke", "Düşüncesizlik", "Egoist davranış"],
                "compatible_signs": ["Aslan", "Yay", "İkizler", "Kova"],
                "career_fields": ["Yöneticilik", "Girişimcilik", "Spor", "Askerlik", "Satış"]
            },
            "boga": {
                "name": "Boğa",
                "english": "Taurus",
                "dates": "20 Nisan - 20 Mayıs",
                "element": "Toprak",
                "quality": "Sabit",
                "ruling_planet": "Venüs",
                "symbol": "🐂",
                "colors": ["Yeşil", "Pembe"],
                "lucky_numbers": [2, 6, 9, 12, 24],
                "keywords": ["Güvenilir", "Sabırlı", "Pratik", "Kararlı", "Sadık"],
                "personality": "Güvenilir ve sabırlı olan Boğalar, konforlarını seven, maddi güvenliğe önem veren kişilerdir.",
                "strengths": ["Güvenilirlik", "Sabır", "Kararlılık", "Sadakat", "Pratiklik"],
                "weaknesses": ["İnatçılık", "Materialism", "Değişime direnç", "Kıskançlık"],
                "compatible_signs": ["Başak", "Oğlak", "Yengeç", "Balık"],
                "career_fields": ["Bankacılık", "Emlak", "Sanat", "Aşçılık", "Tarım"]
            },
            "ikizler": {
                "name": "İkizler",
                "english": "Gemini",
                "dates": "21 Mayıs - 20 Haziran",
                "element": "Hava",
                "quality": "Değişken",
                "ruling_planet": "Merkür",
                "symbol": "👯",
                "colors": ["Sarı", "Açık Mavi"],
                "lucky_numbers": [5, 7, 14, 23],
                "keywords": ["İletişimci", "Zeki", "Meraklı", "Çok yönlü", "Sosyal"],
                "personality": "Zeki ve iletişim yeteneği güçlü olan İkizler, sürekli öğrenmeyi ve yeni deneyimleri seven kişilerdir.",
                "strengths": ["İletişim", "Zeka", "Adaptasyon", "Çok yönlülük", "Sosyallik"],
                "weaknesses": ["Kararsızlık", "Yüzeysellik", "Sabırsızlık", "Güvenilmezlik"],
                "compatible_signs": ["Terazi", "Kova", "Koç", "Aslan"],
                "career_fields": ["Gazetecilik", "Öğretmenlik", "Satış", "Yazarlık", "Teknoloji"]
            },
            "yengec": {
                "name": "Yengeç",
                "english": "Cancer",
                "dates": "21 Haziran - 22 Temmuz",
                "element": "Su",
                "quality": "Öncü",
                "ruling_planet": "Ay",
                "symbol": "🦀",
                "colors": ["Gümüş", "Beyaz", "Deniz Mavisi"],
                "lucky_numbers": [2, 7, 11, 16, 20, 25],
                "keywords": ["Duygusal", "Koruyucu", "Sezgisel", "Sadık", "Aileci"],
                "personality": "Duygusal ve koruyucu olan Yengeçler, aileye ve eve büyük değer veren, sezgileri güçlü kişilerdir.",
                "strengths": ["Empati", "Sadakat", "Sezgi", "Koruyuculuk", "Duygusal zeka"],
                "weaknesses": ["Aşırı duyarlılık", "Geçmişe takılma", "Değişken ruh hali", "Savunmacı tutum"],
                "compatible_signs": ["Akrep", "Balık", "Boğa", "Başak"],
                "career_fields": ["Hemşirelik", "Psikoloji", "Eğitim", "Emlak", "Beslenme"]
            },
            "aslan": {
                "name": "Aslan",
                "english": "Leo",
                "dates": "23 Temmuz - 22 Ağustos",
                "element": "Ateş",
                "quality": "Sabit",
                "ruling_planet": "Güneş",
                "symbol": "🦁",
                "colors": ["Altın", "Turuncu", "Kırmızı"],
                "lucky_numbers": [1, 3, 10, 19],
                "keywords": ["Yaratıcı", "Karizmatik", "Cömert", "Drama", "Gururlu"],
                "personality": "Karizmatik ve yaratıcı olan Aslanlar, dikkat çekmeyi seven, doğal performans yetisi olan kişilerdir.",
                "strengths": ["Karizma", "Yaratıcılık", "Cömertlik", "Liderlik", "Optimizm"],
                "weaknesses": ["Ego", "Drama", "Dikkat arayışı", "İnatçılık", "Kibir"],
                "compatible_signs": ["Koç", "Yay", "İkizler", "Terazi"],
                "career_fields": ["Oyunculuk", "Sanat", "Eğlence", "Yöneticilik", "Tasarım"]
            },
            "basak": {
                "name": "Başak",
                "english": "Virgo",
                "dates": "23 Ağustos - 22 Eylül",
                "element": "Toprak",
                "quality": "Değişken",
                "ruling_planet": "Merkür",
                "symbol": "👩‍🌾",
                "colors": ["Kahverengi", "Yeşil", "Lacivert"],
                "lucky_numbers": [6, 14, 18, 24, 26],
                "keywords": ["Mükemmeliyetçi", "Analitik", "Pratik", "Detaycı", "Yardımsever"],
                "personality": "Mükemmeliyetçi ve analitik olan Başaklar, detaylara dikkat eden, düzenli ve pratik kişilerdir.",
                "strengths": ["Analitik düşünce", "Detay odağı", "Güvenilirlik", "Yardımseverlik", "Pratiklik"],
                "weaknesses": ["Aşırı eleştiri", "Endişe", "Mükemmeliyetçilik", "Katılık"],
                "compatible_signs": ["Boğa", "Oğlak", "Yengeç", "Akrep"],
                "career_fields": ["Sağlık", "Muhasebe", "Araştırma", "Editörlük", "Hukuk"]
            },
            "terazi": {
                "name": "Terazi",
                "english": "Libra",
                "dates": "23 Eylül - 22 Ekim",
                "element": "Hava",
                "quality": "Öncü",
                "ruling_planet": "Venüs",
                "symbol": "⚖️",
                "colors": ["Pembe", "Açık Mavi", "Pastel Yeşil"],
                "lucky_numbers": [4, 6, 13, 15, 24],
                "keywords": ["Dengeli", "Diplomatlık", "Estetik", "Adalet", "Sosyal"],
                "personality": "Dengeli ve diplomatik olan Teraziler, adaleti ve güzelliği seven, sosyal becerileri gelişmiş kişilerdir.",
                "strengths": ["Diplomasi", "Adalet duygusu", "Estetik anlayışı", "Sosyallik", "İşbirliği"],
                "weaknesses": ["Kararsızlık", "Çelişki korkusu", "Bağımlılık", "Yüzeysellik"],
                "compatible_signs": ["İkizler", "Kova", "Aslan", "Yay"],
                "career_fields": ["Hukuk", "Diplomasi", "Sanat", "Moda", "İnsan kaynakları"]
            },
            "akrep": {
                "name": "Akrep",
                "english": "Scorpio",
                "dates": "23 Ekim - 21 Kasım",
                "element": "Su",
                "quality": "Sabit",
                "ruling_planet": "Plüton/Mars",
                "symbol": "🦂",
                "colors": ["Bordo", "Siyah", "Koyu Kırmızı"],
                "lucky_numbers": [8, 11, 18, 22],
                "keywords": ["Yoğun", "Gizemli", "Tutkulu", "Güçlü", "Dönüştürücü"],
                "personality": "Yoğun ve gizemli olan Akreplar, derin duygulara sahip, güçlü sezgileri olan kişilerdir.",
                "strengths": ["Güçlü irade", "Sezgi", "Sadakat", "Kararlılık", "Dönüşüm yetisi"],
                "weaknesses": ["Kıskançlık", "İntikamcılık", "Şüphecilik", "Saplantı"],
                "compatible_signs": ["Yengeç", "Balık", "Başak", "Oğlak"],
                "career_fields": ["Psikoloji", "Araştırma", "Tıp", "Dedektiflik", "Finans"]
            },
            "yay": {
                "name": "Yay",
                "english": "Sagittarius",
                "dates": "22 Kasım - 21 Aralık",
                "element": "Ateş",
                "quality": "Değişken",
                "ruling_planet": "Jüpiter",
                "symbol": "🏹",
                "colors": ["Mor", "Turkuaz", "Turuncu"],
                "lucky_numbers": [3, 9, 15, 21, 27],
                "keywords": ["Özgür", "Maceraperest", "Felsefi", "İyimser", "Gezgin"],
                "personality": "Özgür ruhlu ve maceraperest olan Yaylar, yeni kültürleri keşfetmeyi seven, felsefi düşünce yapısına sahip kişilerdir.",
                "strengths": ["İyimserlik", "Özgürlük sevgisi", "Felsefi düşünce", "Macera ruhu", "Dürüstlük"],
                "weaknesses": ["Sabırsızlık", "Düşüncesizlik", "Aşırı dürüstlük", "Sorumluluktan kaçış"],
                "compatible_signs": ["Koç", "Aslan", "Terazi", "Kova"],
                "career_fields": ["Turizm", "Eğitim", "Yayıncılık", "Spor", "Felsefe"]
            },
            "oglak": {
                "name": "Oğlak",
                "english": "Capricorn",
                "dates": "22 Aralık - 19 Ocak",
                "element": "Toprak",
                "quality": "Öncü",
                "ruling_planet": "Satürn",
                "symbol": "🐐",
                "colors": ["Siyah", "Kahverengi", "Koyu Yeşil"],
                "lucky_numbers": [6, 8, 10, 26],
                "keywords": ["Disiplinli", "Hırslı", "Sorumlu", "Pratik", "Kararlı"],
                "personality": "Disiplinli ve hırslı olan Oğlaklar, hedeflerine odaklanan, sorumluluklarını ciddiye alan kişilerdir.",
                "strengths": ["Disiplin", "Hırs", "Sorumluluk", "Kararlılık", "Pratiklik"],
                "weaknesses": ["Katılık", "Karamsar", "Aşırı ciddiyet", "Materialism"],
                "compatible_signs": ["Boğa", "Başak", "Akrep", "Balık"],
                "career_fields": ["Yöneticilik", "Mühendislik", "Bankacılık", "Siyaset", "İnşaat"]
            },
            "kova": {
                "name": "Kova",
                "english": "Aquarius",
                "dates": "20 Ocak - 18 Şubat",
                "element": "Hava",
                "quality": "Sabit",
                "ruling_planet": "Uranüs/Satürn",
                "symbol": "🏺",
                "colors": ["Elektrik Mavisi", "Gümüş", "Mor"],
                "lucky_numbers": [4, 7, 11, 22, 29],
                "keywords": ["Bağımsız", "Yenilikçi", "Özgün", "İnsancıl", "Vizyoner"],
                "personality": "Bağımsız ve yenilikçi olan Kovalar, gelecek odaklı düşünen, toplumsal değişime önem veren kişilerdir.",
                "strengths": ["Yenilikçilik", "Bağımsızlık", "İnsancıllık", "Vizyon", "Özgünlük"],
                "weaknesses": ["Duygusal mesafe", "İnatçılık", "Aşırı idealizm", "Soğukluk"],
                "compatible_signs": ["İkizler", "Terazi", "Koç", "Yay"],
                "career_fields": ["Teknoloji", "Bilim", "Sosyal hizmet", "Araştırma", "Aktivizm"]
            },
            "balik": {
                "name": "Balık",
                "english": "Pisces",
                "dates": "19 Şubat - 20 Mart",
                "element": "Su",
                "quality": "Değişken",
                "ruling_planet": "Neptün/Jüpiter",
                "symbol": "🐟",
                "colors": ["Deniz Yeşili", "Lavanta", "Gümüş"],
                "lucky_numbers": [3, 9, 12, 15, 18, 24],
                "keywords": ["Sezgisel", "Yaratıcı", "Duygusal", "Empatik", "Ruhsal"],
                "personality": "Sezgisel ve yaratıcı olan Balıklar, güçlü empati yetisine sahip, ruhsal dünyaları gelişmiş kişilerdir.",
                "strengths": ["Sezgi", "Empati", "Yaratıcılık", "Şefkat", "Ruhsal bağ"],
                "weaknesses": ["Aşırı duyarlılık", "Kaçış eğilimi", "Sınır eksikliği", "Hayalperestlik"],
                "compatible_signs": ["Yengeç", "Akrep", "Boğa", "Oğlak"],
                "career_fields": ["Sanat", "Müzik", "Psikoloji", "Sağlık", "Spiritüel hizmetler"]
            }
        }

        # İçerik şablonları
        self.content_templates = {
            "daily": {
                "title_formats": [
                    "{sign} Burcu Günlük Yorumu - {theme}",
                    "{sign} Burcu {date} Yorumu - {theme}",
                    "{sign} Burcu Günlük Astroloji Yorumu",
                    "Bugün {sign} Burcu İçin - {theme}"
                ],
                "themes": [
                    "Enerji Dolu Bir Gün", "Yeni Başlangıçlar", "İç Huzur", "Yaratıcılık Zamanı",
                    "Aşk Fısıltıları", "Kariyer Atılımı", "Ruhsal Gelişim", "Mali Şans"
                ]
            },
            "weekly": {
                "title_formats": [
                    "{sign} Burcu Haftalık Yorumu - {theme}",
                    "{sign} Burcu Bu Hafta - {theme}",
                    "{sign} Burcu Haftalık Astroloji Rehberi"
                ],
                "themes": [
                    "Dönüşüm Haftası", "Yaratıcılığın Zirvesi", "İlişkilerde Derinlik",
                    "Kariyer Fırsatları", "Ruhsal Yolculuk", "Maddi Bolluk"
                ]
            },
            "monthly": {
                "title_formats": [
                    "{sign} Burcu Aylık Yorumu - {theme}",
                    "{sign} Burcu {month} Ayı Yorumu",
                    "{sign} Burcu Aylık Astroloji Rehberi"
                ],
                "themes": [
                    "Büyük Dönüşümler", "Aşkın Gücü", "Kariyer Zirvesi",
                    "Ruhsal Uyanış", "Bolluk ve Bereket", "İç Yolculuk"
                ]
            }
        }

        # Astrolojik konular ve öneriler
        self.astrological_aspects = {
            "planets": {
                "Mars": ["enerji", "cesaret", "savaşçı ruh", "girişkenlik"],
                "Venüs": ["aşk", "güzellik", "sanat", "uyum"],
                "Merkür": ["iletişim", "zeka", "teknoloji", "ticaret"],
                "Jüpiter": ["şans", "genişleme", "felsefe", "yurtdışı"],
                "Satürn": ["disiplin", "sorumluluk", "test", "olgunluk"],
                "Uranüs": ["değişim", "özgürlük", "teknoloji", "devrim"],
                "Neptün": ["rüyalar", "sanat", "spiritüalite", "illüzyon"],
                "Plüton": ["dönüşüm", "güç", "gizem", "yeniden doğuş"]
            },
            "advice_categories": {
                "love": ["romantik", "ilişki", "aşk", "sevgi", "uyum"],
                "career": ["kariyer", "iş", "para", "başarı", "proje"],
                "health": ["sağlık", "enerji", "dinlenme", "spor", "beslenme"],
                "spiritual": ["ruhsal", "meditasyon", "spiritüel", "iç gelişim", "sezgi"]
            }
        }

    def get_random_sign(self) -> str:
        """Rastgele bir burç seç."""
        return random.choice(list(self.zodiac_signs.keys()))

    def generate_content_id(self, sign: str, period: str, theme: str) -> str:
        """Benzersiz içerik ID'si oluştur."""
        date_str = datetime.now().strftime("%Y-%m-%d")
        content_string = f"{sign}-{period}-{theme}-{date_str}"
        return hashlib.md5(content_string.encode()).hexdigest()[:8]

    def generate_daily_content(self, sign: str = None) -> Dict[str, str]:
        """Günlük burç yorumu oluştur."""
        if not sign:
            sign = self.get_random_sign()

        sign_data = self.zodiac_signs[sign]
        theme = random.choice(self.content_templates["daily"]["themes"])
        title_format = random.choice(self.content_templates["daily"]["title_formats"])

        date_str = datetime.now().strftime("%Y-%m-%d")
        title = title_format.format(
            sign=sign_data["name"],
            theme=theme,
            date=datetime.now().strftime("%d %B")
        )

        # İçerik oluştur
        content = self._generate_detailed_content(sign_data, "daily", theme)

        # Slug oluştur
        slug = f"{date_str}-{sign}-burcu-gunluk-yorum"

        return {
            "title": title,
            "content": content,
            "slug": slug,
            "sign": sign,
            "period": "daily"
        }

    def generate_weekly_content(self, sign: str = None) -> Dict[str, str]:
        """Haftalık burç yorumu oluştur."""
        if not sign:
            sign = self.get_random_sign()

        sign_data = self.zodiac_signs[sign]
        theme = random.choice(self.content_templates["weekly"]["themes"])
        title_format = random.choice(self.content_templates["weekly"]["title_formats"])

        date_str = datetime.now().strftime("%Y-%m-%d")
        title = title_format.format(
            sign=sign_data["name"],
            theme=theme
        )

        content = self._generate_detailed_content(sign_data, "weekly", theme)
        slug = f"{date_str}-{sign}-burcu-haftalik-yorum"

        return {
            "title": title,
            "content": content,
            "slug": slug,
            "sign": sign,
            "period": "weekly"
        }

    def generate_monthly_content(self, sign: str = None) -> Dict[str, str]:
        """Aylık burç yorumu oluştur."""
        if not sign:
            sign = self.get_random_sign()

        sign_data = self.zodiac_signs[sign]
        theme = random.choice(self.content_templates["monthly"]["themes"])
        title_format = random.choice(self.content_templates["monthly"]["title_formats"])

        date_str = datetime.now().strftime("%Y-%m-%d")
        month_name = datetime.now().strftime("%B")
        title = title_format.format(
            sign=sign_data["name"],
            theme=theme,
            month=month_name
        )

        content = self._generate_detailed_content(sign_data, "monthly", theme)
        slug = f"{date_str}-{sign}-burcu-aylik-yorum"

        return {
            "title": title,
            "content": content,
            "slug": slug,
            "sign": sign,
            "period": "monthly"
        }

    def _generate_detailed_content(self, sign_data: Dict, period: str, theme: str) -> str:
        """Detaylı içerik oluştur."""
        sign_name = sign_data["name"]

        # Gezegen etkisi seç
        planets = list(self.astrological_aspects["planets"].keys())
        active_planet = random.choice(planets)
        planet_effects = self.astrological_aspects["planets"][active_planet]

        # İçerik başlangıcı
        content = f"""---
title: "{theme} - {sign_name} Burcu {period.title()} Yorumu"
description: "{sign_name} burcu için detaylı astroloji yorumu. {theme.lower()} konusunda rehberlik."
pubDate: {datetime.now().strftime('%Y-%m-%d')}
category: "astrology"
tags: ["{sign_name.lower()} burcu", "{period} yorum", "astroloji", "burç yorumu"]
heroImage: "/social-media/og-image.jpg"
---

# {sign_name} Burcu {period.title()} Yorumu

{sign_data['symbol']} **{sign_name} Burcu** (**{sign_data['dates']}**)

{self._get_period_intro(period, sign_name, theme, active_planet)}

## 🌟 Burç Özellikleri

**Element:** {sign_data['element']} | **Kalite:** {sign_data['quality']} | **Yönetici Gezegen:** {sign_data['ruling_planet']}

**Güçlü Yanlar:** {', '.join(sign_data['strengths'])}

**Dikkat Edilmesi Gerekenler:** {', '.join(sign_data['weaknesses'])}

## 💫 {period.title()} Genel Durum

{active_planet} gezenenin etkisiyle bu {period} döneminde {sign_name} burcu için {random.choice(planet_effects)} enerjisi ön plana çıkacak.

{self._generate_general_forecast(sign_data, period)}

## 💕 Aşk ve İlişkiler

{self._generate_love_forecast(sign_data, period)}

## 💼 Kariyer ve Para

{self._generate_career_forecast(sign_data, period)}

## 🏃‍♀️ Sağlık ve Enerji

{self._generate_health_forecast(sign_data, period)}

## 🎯 {period.title()} Tavsiyeleri

{self._generate_advice(sign_data, period)}

## 🔮 Şanslı Elementler

**Şanslı Sayılar:** {', '.join(map(str, sign_data['lucky_numbers']))}

**Şanslı Renkler:** {', '.join(sign_data['colors'])}

**Uyumlu Burçlar:** {', '.join(sign_data['compatible_signs'])}

**Uygun Kariyer Alanları:** {', '.join(sign_data['career_fields'])}

## 💫 Sonuç

{self._generate_conclusion(sign_data, period, theme)}

---

*{sign_data['personality']}*
"""

        return content

    def _get_period_intro(self, period: str, sign_name: str, theme: str, planet: str) -> str:
        """Dönem bazlı giriş metni."""
        if period == "daily":
            return f"Bugün {sign_name} burcu için {planet} gezeninizin etkisiyle {theme.lower()} yaşayacağınız bir gün olacak."
        elif period == "weekly":
            return f"Bu hafta {sign_name} burcu için {planet} etkisiyle {theme.lower()} dönemine giriyorsunuz."
        else:  # monthly
            return f"Bu ay {sign_name} burcu için {planet} gezeninizin güçlü etkisiyle {theme.lower()} yaşayacağınız bereketli bir dönem başlıyor."

    def _generate_general_forecast(self, sign_data: Dict, period: str) -> str:
        """Genel durum tahmini."""
        element = sign_data['element']
        personality_traits = sign_data['keywords']

        forecasts = [
            f"{sign_data['name']} burcu olarak doğal {personality_traits[0].lower()} özelliğiniz bu dönemde avantajınız olacak.",
            f"{element} elementi size {period} boyunca güç verecek ve hedeflerinize odaklanmanızı sağlayacak.",
            f"Bu {period} {sign_data['ruling_planet']} gezereninizin etkisiyle {personality_traits[1].lower()} yanınız öne çıkacak."
        ]

        return random.choice(forecasts)

    def _generate_love_forecast(self, sign_data: Dict, period: str) -> str:
        """Aşk ve ilişki tahmini."""
        love_aspects = [
            f"💖 **Bekar {sign_data['name']}lar:** {random.choice(['Sosyal ortamlarda', 'İş yerinde', 'Hobilerle uğraşırken', 'Spor yaparken'])} ilginizi çekecek kişilerle tanışabilirsiniz.",
            f"💑 **İlişkisi Olanlar:** Partnerinizle {random.choice(['daha derin bağlar', 'romantik anlar', 'güzel sürprizler', 'özel aktiviteler'])} yaşayabilirsiniz.",
            f"🌹 {sign_data['colors'][0]} rengi bu {period} aşk hayatınızda şans getirebilir."
        ]

        return '\n\n'.join(love_aspects)

    def _generate_career_forecast(self, sign_data: Dict, period: str) -> str:
        """Kariyer ve para tahmini."""
        career_field = random.choice(sign_data['career_fields'])
        strength = random.choice(sign_data['strengths'])

        career_aspects = [
            f"🚀 **İş Hayatı:** {strength} özelliğiniz sayesinde {period} boyunca dikkat çekeceksiniz.",
            f"💰 **Mali Durum:** {career_field} alanında fırsatlar değerlendirilebilir.",
            f"📈 Bu {period} {random.choice(['yeni projeler', 'iş birliği', 'terfi fırsatları', 'ek gelir'])} için uygun zaman."
        ]

        return '\n\n'.join(career_aspects)

    def _generate_health_forecast(self, sign_data: Dict, period: str) -> str:
        """Sağlık ve enerji tahmini."""
        element = sign_data['element']

        health_aspects = {
            "Ateş": f"🔥 Enerji seviyeniz yüksek olacak. Aktif sporları tercih edin.",
            "Toprak": f"🌱 Vücudunuzla uyum içinde olacaksınız. Doğal beslenmeye önem verin.",
            "Hava": f"💨 Zihinsel aktifiteniz artacak. Nefes egzerzilerine zaman ayırın.",
            "Su": f"💧 Duygusal dengeniz önemli. Su sporları ve meditasyon faydalı olacak."
        }

        return health_aspects[element] + f"\n\n⚖️ Bu {period} genel sağlık durumunuz iyi olacak."

    def _generate_advice(self, sign_data: Dict, period: str) -> str:
        """Tavsiyeler oluştur."""
        strength = random.choice(sign_data['strengths'])
        weakness = random.choice(sign_data['weaknesses'])

        advice_list = [
            f"1. **{strength}** özelliğinizi bu {period} daha aktif kullanın",
            f"2. **{weakness}** konusunda dikkatli olun ve kendinizi geliştirin",
            f"3. **{sign_data['colors'][0]}** rengi bu {period} şansınızı artıracak",
            f"4. **{random.choice(sign_data['compatible_signs'])}** burcu ile işbirliği yapın",
            f"5. **{random.choice(sign_data['career_fields'])}** alanında fırsatları değerlendirin"
        ]

        return '\n'.join(advice_list)

    def _generate_conclusion(self, sign_data: Dict, period: str, theme: str) -> str:
        """Sonuç bölümü."""
        conclusions = [
            f"Bu {period} {sign_data['name']} burcu için {theme.lower()} yaşayacağınız, kişisel gelişiminizi destekleyecek bir dönem olacak.",
            f"{sign_data['name']} burcu olarak doğal yeteneklerinizi kullanarak bu {period} büyük adımlar atabilirsiniz.",
            f"Bu {period} sonunda kendinizi daha güçlü ve {random.choice(sign_data['keywords']).lower()} hissedeceksiniz."
        ]

        return random.choice(conclusions)

    def create_content_file(self, content_data: Dict[str, str]) -> str:
        """İçeriği dosyaya kaydet."""
        os.makedirs(self.base_path, exist_ok=True)

        filename = f"{content_data['slug']}.md"
        filepath = os.path.join(self.base_path, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content_data['content'])

        return filepath

    def generate_all_signs_daily(self) -> List[str]:
        """Tüm burçlar için günlük içerik oluştur."""
        created_files = []

        for sign_key in self.zodiac_signs.keys():
            content_data = self.generate_daily_content(sign_key)
            filepath = self.create_content_file(content_data)
            created_files.append(filepath)
            print(f"✅ {self.zodiac_signs[sign_key]['name']} burcu günlük yorumu oluşturuldu: {filepath}")

        return created_files

    def generate_all_signs_weekly(self) -> List[str]:
        """Tüm burçlar için haftalık içerik oluştur."""
        created_files = []

        for sign_key in self.zodiac_signs.keys():
            content_data = self.generate_weekly_content(sign_key)
            filepath = self.create_content_file(content_data)
            created_files.append(filepath)
            print(f"✅ {self.zodiac_signs[sign_key]['name']} burcu haftalık yorumu oluşturuldu: {filepath}")

        return created_files

    def generate_all_signs_monthly(self) -> List[str]:
        """Tüm burçlar için aylık içerik oluştur."""
        created_files = []

        for sign_key in self.zodiac_signs.keys():
            content_data = self.generate_monthly_content(sign_key)
            filepath = self.create_content_file(content_data)
            created_files.append(filepath)
            print(f"✅ {self.zodiac_signs[sign_key]['name']} burcu aylık yorumu oluşturuldu: {filepath}")

        return created_files

    def run_interactive_mode(self):
        """İnteraktif mod çalıştır."""
        print("🔮 Gelişmiş Astroloji İçerik Üreticisi")
        print("=" * 50)

        while True:
            print("\nSeçenekler:")
            print("1. Tek burç günlük yorum")
            print("2. Tek burç haftalık yorum")
            print("3. Tek burç aylık yorum")
            print("4. Tüm burçlar günlük yorumlar")
            print("5. Tüm burçlar haftalık yorumlar")
            print("6. Tüm burçlar aylık yorumlar")
            print("7. Burç özellikleri görüntüle")
            print("8. Çıkış")

            choice = input("\nSeçiminiz (1-8): ").strip()

            if choice == "1":
                sign = input("Burç adı (örn: koc, aslan) veya boş bırakın: ").strip().lower()
                sign = sign if sign in self.zodiac_signs else None
                content_data = self.generate_daily_content(sign)
                filepath = self.create_content_file(content_data)
                print(f"✅ Günlük yorum oluşturuldu: {filepath}")

            elif choice == "2":
                sign = input("Burç adı (örn: koc, aslan) veya boş bırakın: ").strip().lower()
                sign = sign if sign in self.zodiac_signs else None
                content_data = self.generate_weekly_content(sign)
                filepath = self.create_content_file(content_data)
                print(f"✅ Haftalık yorum oluşturuldu: {filepath}")

            elif choice == "3":
                sign = input("Burç adı (örn: koc, aslan) veya boş bırakın: ").strip().lower()
                sign = sign if sign in self.zodiac_signs else None
                content_data = self.generate_monthly_content(sign)
                filepath = self.create_content_file(content_data)
                print(f"✅ Aylık yorum oluşturuldu: {filepath}")

            elif choice == "4":
                print("🚀 Tüm burçlar için günlük yorumlar oluşturuluyor...")
                files = self.generate_all_signs_daily()
                print(f"✅ {len(files)} günlük yorum oluşturuldu!")

            elif choice == "5":
                print("🚀 Tüm burçlar için haftalık yorumlar oluşturuluyor...")
                files = self.generate_all_signs_weekly()
                print(f"✅ {len(files)} haftalık yorum oluşturuldu!")

            elif choice == "6":
                print("🚀 Tüm burçlar için aylık yorumlar oluşturuluyor...")
                files = self.generate_all_signs_monthly()
                print(f"✅ {len(files)} aylık yorum oluşturuldu!")

            elif choice == "7":
                self.display_zodiac_info()

            elif choice == "8":
                print("👋 Görüşürüz!")
                break

            else:
                print("❌ Geçersiz seçim. Lütfen 1-8 arası bir sayı girin.")

    def display_zodiac_info(self):
        """Burç bilgilerini görüntüle."""
        print("\n🌟 BURÇ BİLGİLERİ")
        print("=" * 60)

        for key, data in self.zodiac_signs.items():
            print(f"\n{data['symbol']} **{data['name']} Burcu** ({data['english']})")
            print(f"📅 Tarih: {data['dates']}")
            print(f"🌍 Element: {data['element']} | 🔄 Kalite: {data['quality']}")
            print(f"🪐 Yönetici Gezegen: {data['ruling_planet']}")
            print(f"🎨 Şanslı Renkler: {', '.join(data['colors'])}")
            print(f"🔢 Şanslı Sayılar: {', '.join(map(str, data['lucky_numbers']))}")
            print(f"💫 Anahtar Kelimeler: {', '.join(data['keywords'])}")
            print(f"💼 Uygun Kariyer: {', '.join(data['career_fields'][:3])}...")
            print("-" * 60)

if __name__ == "__main__":
    generator = AdvancedAstrologyGenerator()
    generator.run_interactive_mode()