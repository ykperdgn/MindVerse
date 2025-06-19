#!/usr/bin/env python3
"""
Comprehensive Bilingual Content Generator for MindVerse Blog
Generates historical and daily horoscope content for both Turkish and English versions
"""

import os
import json
import random
from datetime import datetime, timedelta
from pathlib import Path
import re

class BilingualHoroscopeGenerator:
    def __init__(self):
        self.zodiac_signs = {
            'aries': {'tr': 'koç', 'en': 'aries', 'symbol': '♈', 'element': 'Fire', 'planet': 'Mars', 'dates': 'Mar 21 - Apr 19'},
            'taurus': {'tr': 'boğa', 'en': 'taurus', 'symbol': '♉', 'element': 'Earth', 'planet': 'Venus', 'dates': 'Apr 20 - May 20'},
            'gemini': {'tr': 'ikizler', 'en': 'gemini', 'symbol': '♊', 'element': 'Air', 'planet': 'Mercury', 'dates': 'May 21 - Jun 20'},
            'cancer': {'tr': 'yengeç', 'en': 'cancer', 'symbol': '♋', 'element': 'Water', 'planet': 'Moon', 'dates': 'Jun 21 - Jul 22'},
            'leo': {'tr': 'aslan', 'en': 'leo', 'symbol': '♌', 'element': 'Fire', 'planet': 'Sun', 'dates': 'Jul 23 - Aug 22'},
            'virgo': {'tr': 'başak', 'en': 'virgo', 'symbol': '♍', 'element': 'Earth', 'planet': 'Mercury', 'dates': 'Aug 23 - Sep 22'},
            'libra': {'tr': 'terazi', 'en': 'libra', 'symbol': '♎', 'element': 'Air', 'planet': 'Venus', 'dates': 'Sep 23 - Oct 22'},
            'scorpio': {'tr': 'akrep', 'en': 'scorpio', 'symbol': '♏', 'element': 'Water', 'planet': 'Pluto', 'dates': 'Oct 23 - Nov 21'},
            'sagittarius': {'tr': 'yay', 'en': 'sagittarius', 'symbol': '♐', 'element': 'Fire', 'planet': 'Jupiter', 'dates': 'Nov 22 - Dec 21'},
            'capricorn': {'tr': 'oğlak', 'en': 'capricorn', 'symbol': '♑', 'element': 'Earth', 'planet': 'Saturn', 'dates': 'Dec 22 - Jan 19'},
            'aquarius': {'tr': 'kova', 'en': 'aquarius', 'symbol': '♒', 'element': 'Air', 'planet': 'Uranus', 'dates': 'Jan 20 - Feb 18'},
            'pisces': {'tr': 'balık', 'en': 'pisces', 'symbol': '♓', 'element': 'Water', 'planet': 'Neptune', 'dates': 'Feb 19 - Mar 20'}
        }

        self.content_templates = {
            'tr': {
                'general_intros': [
                    "Bugün {sign} burcu için oldukça hareketli bir gün olacak.",
                    "{sign} burcu için bugün yeni fırsatların kapısı aralanıyor.",
                    "Bugün {sign} burcu için enerjiniz yüksek ve motivasyonunuz güçlü.",
                    "{sign} burcu için bugün önemli gelişmelerin yaşanacağı bir gün.",
                    "Bugün {sign} burcu için hem zorluklar hem de fırsatlar bir arada."
                ],
                'love_phrases': [
                    "Aşk hayatınızda pozitif gelişmeler yaşanabilir.",
                    "İlişkinizde iletişim önemli olacak.",
                    "Duygusal açıdan dengeli bir gün geçirebilirsiniz.",
                    "Sevgilinizle güzel anlar paylaşabilirsiniz.",
                    "Yeni tanışıklıklar için uygun bir zaman.",
                    "İlişkinizdeki sorunları çözme zamanı gelmiş olabilir."
                ],
                'career_phrases': [
                    "Kariyerinizde yeni fırsatlar ortaya çıkabilir.",
                    "İş yerindeki projelerinizde ilerleme kaydedebilirsiniz.",
                    "Mesleki hedeflerinize odaklanmanız gereken bir gün.",
                    "İş hayatında dikkatli adımlar atmanız önemli.",
                    "Yaratıcılığınızı iş hayatında kullanabilirsiniz.",
                    "İş birliği yapacağınız kişilerle verimli çalışabilirsiniz."
                ],
                'health_phrases': [
                    "Sağlığınıza özen gösterin ve düzenli beslenmeye dikkat edin.",
                    "Fiziksel aktivitelerinizi artırmanız faydalı olacak.",
                    "Stres yönetimine odaklanarak zihinsel sağlığınızı koruyun.",
                    "Uyku düzeninize dikkat etmeniz gereken bir dönem.",
                    "Doğal beslenme ve su tüketimine özen gösterin.",
                    "Meditasyon ve nefes egzersizleri size iyi gelecek."
                ]
            },
            'en': {
                'general_intros': [
                    "Today will be quite an active day for {sign}.",
                    "The door to new opportunities is opening for {sign} today.",
                    "Today your energy is high and your motivation is strong for {sign}.",
                    "Today will be a day of important developments for {sign}.",
                    "Today brings both challenges and opportunities for {sign}."
                ],
                'love_phrases': [
                    "Positive developments may occur in your love life.",
                    "Communication will be important in your relationship.",
                    "You can have an emotionally balanced day.",
                    "You may share beautiful moments with your partner.",
                    "It's a good time for new encounters.",
                    "It might be time to solve problems in your relationship."
                ],
                'career_phrases': [
                    "New opportunities may emerge in your career.",
                    "You can make progress on your workplace projects.",
                    "It's a day to focus on your professional goals.",
                    "It's important to take careful steps in your work life.",
                    "You can use your creativity in your professional life.",
                    "You can work efficiently with people you'll collaborate with."
                ],
                'health_phrases': [
                    "Take care of your health and pay attention to regular nutrition.",
                    "Increasing your physical activities will be beneficial.",
                    "Focus on stress management to protect your mental health.",
                    "It's a period when you need to pay attention to your sleep pattern.",
                    "Pay attention to natural nutrition and water consumption.",
                    "Meditation and breathing exercises will be good for you."
                ]
            }
        }

    def generate_daily_horoscope(self, sign_key, language='tr', date=None):
        """Generate a daily horoscope for a specific sign and language"""
        if date is None:
            date = datetime.now()

        sign_data = self.zodiac_signs[sign_key]
        templates = self.content_templates[language]

        sign_name = sign_data['tr'].title() if language == 'tr' else sign_data['en'].title()

        # Generate content
        general = random.choice(templates['general_intros']).format(sign=sign_name)
        love = random.choice(templates['love_phrases'])
        career = random.choice(templates['career_phrases'])
        health = random.choice(templates['health_phrases'])

        # Lucky elements
        lucky_numbers = random.sample(range(1, 50), 3)
        colors = {
            'tr': ['Kırmızı', 'Mavi', 'Yeşil', 'Sarı', 'Mor', 'Turuncu', 'Pembe', 'Beyaz'],
            'en': ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Orange', 'Pink', 'White']
        }
        times = {
            'tr': ['Sabah', 'Öğlen', 'Akşam', 'Gece'],
            'en': ['Morning', 'Noon', 'Evening', 'Night']
        }

        lucky_color = random.choice(colors[language])
        lucky_time = random.choice(times[language])

        return {
            'general': general,
            'love': love,
            'career': career,
            'health': health,
            'lucky_numbers': lucky_numbers,
            'lucky_color': lucky_color,
            'lucky_time': lucky_time,
            'element': sign_data['element'],
            'planet': sign_data['planet'],
            'symbol': sign_data['symbol'],
            'dates': sign_data['dates']
        }

    def create_turkish_horoscope_content(self, sign_key, date):
        """Create Turkish horoscope markdown content"""
        sign_data = self.zodiac_signs[sign_key]
        horoscope = self.generate_daily_horoscope(sign_key, 'tr', date)

        content = f"""---
title: "{sign_data['tr'].title()} Burcu Günlük Yorum - {date.strftime('%d %B %Y')}"
description: "{sign_data['tr'].title()} burcu için {date.strftime('%d %B %Y')} günlük burç yorumu. Aşk, kariyer, sağlık ve şanslı sayılar."
pubDate: {date.strftime('%Y-%m-%d')}
category: "astrology"
tags: ["{sign_data['tr']}", "günlük", "burç", "yorum", "astroloji"]
heroImage: "/images/zodiac/{sign_key}.jpg"
---

# {sign_data['tr'].title()} Burcu Günlük Yorum - {date.strftime('%d %B %Y')}

{horoscope['symbol']} **{sign_data['tr'].title()} Burcu** ({sign_data['dates']})

## Genel Durum

{horoscope['general']} {sign_data['element']} elementi size bugün güçlü bir enerji kazandıracak. {sign_data['planet']} gezegeninin etkisi altında olan {sign_data['tr']} burcu için bugün özellikle dikkat edilmesi gereken noktalar var.

## Aşk ve İlişkiler ❤️

{horoscope['love']} Venüs'ün konumu bugün duygusal hayatınızda önemli etkiler yaratabilir. Bekar {sign_data['tr']} burçları için yeni tanışma fırsatları ortaya çıkabilir.

### İlişki Önerileri:
- Partnerinizle açık iletişim kurun
- Duygularınızı samimi şekilde paylaşın
- Küçük jestlerle sevginizi gösterin
- Geçmiş tartışmaları geride bırakın

## Kariyer ve İş Hayatı 💼

{horoscope['career']} Mars'ın pozisyonu iş hayatınızda yeni atılımlar yapmanız için size destek olacak. Yaratıcı projelerinizi hayata geçirmek için uygun bir zaman.

### Kariyer Tavsiyeleri:
- Yeni projelere açık olun
- İş arkadaşlarınızla iş birliği yapın
- Detaylara dikkat edin
- Uzun vadeli planlar yapın

## Sağlık ve Zindelik 🏥

{horoscope['health']} Ay'ın etkisi altında vücut direncinde artış gözlemlenebilir. Ancak aşırı yorgunluktan kaçınmak önemli.

### Sağlık Önerileri:
- Düzenli egzersiz yapın
- Bol su için
- Stresle başa çıkma yolları bulun
- Yeterli uyku alın

## Bugünün Şanslı Unsurları 🍀

- **Şanslı Sayılar:** {', '.join(map(str, horoscope['lucky_numbers']))}
- **Şanslı Renk:** {horoscope['lucky_color']}
- **Şanslı Zaman:** {horoscope['lucky_time']}
- **Element:** {horoscope['element']}
- **Yönetici Gezegen:** {horoscope['planet']}

## Genel Değerlendirme

{sign_data['tr'].title()} burcu için bugün genel olarak pozitif enerjilerin hakim olacağı bir gün. Özellikle {horoscope['lucky_time'].lower()} saatlerinde alacağınız kararlar size fayda sağlayabilir. {horoscope['lucky_color'].lower()} rengi bugün size şans getirebilir.

### Önemli Notlar:
- Aceleci davranmaktan kaçının
- Sezgilerinize güvenin
- Çevrenizdekilere karşı anlayışlı olun
- Yeni deneyimlere açık olun

Unutmayın ki astroloji bir rehberdir, kendi içsel gücünüz ve seçimleriniz her zaman en önemli faktördür.

---

*Bu yorum {date.strftime('%d %B %Y')} tarihi için hazırlanmıştır. Her gün güncel burç yorumları için sitemizi takip etmeyi unutmayın.*
"""
        return content

    def create_english_horoscope_content(self, sign_key, date):
        """Create English horoscope markdown content"""
        sign_data = self.zodiac_signs[sign_key]
        horoscope = self.generate_daily_horoscope(sign_key, 'en', date)

        content = f"""---
title: "{sign_data['en'].title()} Daily Horoscope - {date.strftime('%B %d, %Y')}"
description: "Daily horoscope for {sign_data['en'].title()} on {date.strftime('%B %d, %Y')}. Love, career, health insights and lucky elements."
pubDate: {date.strftime('%Y-%m-%d')}
category: "astrology"
tags: ["{sign_data['en']}", "daily", "horoscope", "astrology", "zodiac"]
heroImage: "/images/zodiac/{sign_key}.jpg"
---

# {sign_data['en'].title()} Daily Horoscope - {date.strftime('%B %d, %Y')}

{horoscope['symbol']} **{sign_data['en'].title()}** ({sign_data['dates']})

## General Overview

{horoscope['general']} The {horoscope['element']} element will bring you strong energy today. As a {sign_data['en'].title()} ruled by {horoscope['planet']}, there are specific points to pay attention to today.

## Love & Relationships ❤️

{horoscope['love']} Venus's position today can create significant effects in your emotional life. Single {sign_data['en'].title()} signs may encounter new meeting opportunities.

### Relationship Advice:
- Communicate openly with your partner
- Share your feelings sincerely
- Show your love with small gestures
- Leave past arguments behind

## Career & Work Life 💼

{horoscope['career']} Mars's position will support you in making new breakthroughs in your professional life. It's a suitable time to implement your creative projects.

### Career Tips:
- Be open to new projects
- Collaborate with colleagues
- Pay attention to details
- Make long-term plans

## Health & Wellness 🏥

{horoscope['health']} Under the Moon's influence, an increase in body resistance may be observed. However, it's important to avoid excessive fatigue.

### Health Recommendations:
- Exercise regularly
- Drink plenty of water
- Find ways to cope with stress
- Get adequate sleep

## Today's Lucky Elements 🍀

- **Lucky Numbers:** {', '.join(map(str, horoscope['lucky_numbers']))}
- **Lucky Color:** {horoscope['lucky_color']}
- **Lucky Time:** {horoscope['lucky_time']}
- **Element:** {horoscope['element']}
- **Ruling Planet:** {horoscope['planet']}

## Overall Assessment

Today will generally be a day dominated by positive energies for {sign_data['en'].title()}. Especially decisions made during {horoscope['lucky_time'].lower()} hours can benefit you. The color {horoscope['lucky_color'].lower()} may bring you luck today.

### Important Notes:
- Avoid hasty behavior
- Trust your intuition
- Be understanding towards those around you
- Be open to new experiences

Remember that astrology is a guide; your inner strength and choices are always the most important factors.

---

*This horoscope was prepared for {date.strftime('%B %d, %Y')}. Don't forget to follow our site for daily updated horoscope readings.*
"""
        return content

    def generate_historical_content(self, days_back=30):
        """Generate historical horoscope content for the past X days"""
        print(f"🔄 Generating historical content for the past {days_back} days...")

        # Create content directories if they don't exist
        tr_dir = Path('src/content/astrology')
        tr_dir.mkdir(parents=True, exist_ok=True)

        generated_count = 0

        for days_ago in range(days_back, 0, -1):
            date = datetime.now() - timedelta(days=days_ago)

            for sign_key in self.zodiac_signs:
                # Turkish content
                tr_filename = f"{date.strftime('%Y-%m-%d')}-{self.zodiac_signs[sign_key]['tr']}-gunluk-yorum.md"
                tr_filepath = tr_dir / tr_filename

                if not tr_filepath.exists():
                    tr_content = self.create_turkish_horoscope_content(sign_key, date)

                    with open(tr_filepath, 'w', encoding='utf-8') as f:
                        f.write(tr_content)

                    generated_count += 1

        print(f"✅ Generated {generated_count} historical horoscope files")
        return generated_count

    def generate_today_content(self):
        """Generate today's horoscope content for both languages"""
        print("📅 Generating today's horoscope content...")

        today = datetime.now()
        tr_dir = Path('src/content/astrology')
        tr_dir.mkdir(parents=True, exist_ok=True)

        generated_count = 0

        for sign_key in self.zodiac_signs:
            # Turkish content
            tr_filename = f"{today.strftime('%Y-%m-%d')}-{self.zodiac_signs[sign_key]['tr']}-gunluk-yorum.md"
            tr_filepath = tr_dir / tr_filename

            if not tr_filepath.exists():
                tr_content = self.create_turkish_horoscope_content(sign_key, today)

                with open(tr_filepath, 'w', encoding='utf-8') as f:
                    f.write(tr_content)

                generated_count += 1

        print(f"✅ Generated {generated_count} today's horoscope files")
        return generated_count

class ContentManager:
    def __init__(self):
        self.generator = BilingualHoroscopeGenerator()

    def run_daily_update(self):
        """Run the daily content update process"""
        print("🚀 Starting daily content update process...")
        print("=" * 50)

        # Generate today's content
        today_count = self.generator.generate_today_content()

        # Update SEO files
        print("🔄 Updating SEO files...")
        os.system('python generate_enhanced_seo.py')

        print("=" * 50)
        print("✅ Daily update process completed!")
        print(f"📝 New content files: {today_count}")
        print("📄 SEO files updated")

        return True

    def bootstrap_historical_content(self, days=30):
        """Bootstrap the site with historical content"""
        print("🎯 Bootstrapping site with historical content...")
        print("=" * 50)

        # Generate historical content
        historical_count = self.generator.generate_historical_content(days)

        # Generate today's content
        today_count = self.generator.generate_today_content()

        # Update SEO files
        print("🔄 Updating SEO files...")
        os.system('python generate_enhanced_seo.py')

        print("=" * 50)
        print("✅ Historical content bootstrap completed!")
        print(f"📊 Historical files: {historical_count}")
        print(f"📅 Today's files: {today_count}")
        print(f"📄 Total content: {historical_count + today_count}")
        print("🗺️ SEO files updated")

        return True

def main():
    """Main function"""
    import sys

    manager = ContentManager()

    if len(sys.argv) > 1:
        if sys.argv[1] == "daily":
            manager.run_daily_update()
        elif sys.argv[1] == "bootstrap":
            days = int(sys.argv[2]) if len(sys.argv) > 2 else 30
            manager.bootstrap_historical_content(days)
        else:
            print("Usage: python bilingual_content_generator.py [daily|bootstrap] [days]")
    else:
        # Default: run daily update
        manager.run_daily_update()

if __name__ == "__main__":
    main()
