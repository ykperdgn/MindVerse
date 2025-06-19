#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Daily Horoscope Content Generator for MindVerse
Generates daily, weekly, and monthly horoscope content automatically
Supports both Turkish and English content generation
"""

import os
import datetime
import json
import random
from pathlib import Path

class DailyHoroscopeGenerator:
    def __init__(self):
        self.base_path = Path(__file__).parent
        self.content_path = self.base_path / "src" / "content" / "astrology"
        self.today = datetime.date.today()
        
        # Zodiac signs with their information
        self.zodiac_signs = {
            'koc': {
                'name': 'Koç',
                'en_name': 'Aries',
                'symbol': '♈',
                'dates': '21 Mart - 19 Nisan',
                'en_dates': 'Mar 21 - Apr 19',
                'element': 'Ateş',
                'en_element': 'Fire',
                'planet': 'Mars',
                'colors': ['Kırmızı', 'Turuncu'],
                'en_colors': ['Red', 'Orange'],
                'traits': ['cesur', 'lider', 'dinamik', 'enerjik', 'atılgan'],
                'en_traits': ['brave', 'leader', 'dynamic', 'energetic', 'assertive']
            },
            'boga': {
                'name': 'Boğa',
                'en_name': 'Taurus',
                'symbol': '♉',
                'dates': '20 Nisan - 20 Mayıs',
                'en_dates': 'Apr 20 - May 20',
                'element': 'Toprak',
                'en_element': 'Earth',
                'planet': 'Venüs',
                'colors': ['Yeşil', 'Pembe'],
                'en_colors': ['Green', 'Pink'],
                'traits': ['sabırlı', 'güvenilir', 'pratik', 'kararlı', 'sensuel'],
                'en_traits': ['patient', 'reliable', 'practical', 'determined', 'sensual']
            },
            'ikizler': {
                'name': 'İkizler',
                'en_name': 'Gemini',
                'symbol': '♊',
                'dates': '21 Mayıs - 20 Haziran',
                'en_dates': 'May 21 - Jun 20',
                'element': 'Hava',
                'en_element': 'Air',
                'planet': 'Merkür',
                'colors': ['Sarı', 'Mavi'],
                'en_colors': ['Yellow', 'Blue'],
                'traits': ['meraklı', 'konuşkan', 'çok yönlü', 'zeki', 'uyumlu'],
                'en_traits': ['curious', 'talkative', 'versatile', 'intelligent', 'adaptable']
            },
            'yengec': {
                'name': 'Yengeç',
                'en_name': 'Cancer',
                'symbol': '♋',
                'dates': '21 Haziran - 22 Temmuz',
                'en_dates': 'Jun 21 - Jul 22',
                'element': 'Su',
                'en_element': 'Water',
                'planet': 'Ay',
                'colors': ['Gümüş', 'Beyaz'],
                'en_colors': ['Silver', 'White'],
                'traits': ['duygusal', 'koruyucu', 'sezgisel', 'sevecen', 'empatik'],
                'en_traits': ['emotional', 'protective', 'intuitive', 'loving', 'empathetic']
            },
            'aslan': {
                'name': 'Aslan',
                'en_name': 'Leo',
                'symbol': '♌',
                'dates': '23 Temmuz - 22 Ağustos',
                'en_dates': 'Jul 23 - Aug 22',
                'element': 'Ateş',
                'en_element': 'Fire',
                'planet': 'Güneş',
                'colors': ['Altın', 'Turuncu'],
                'en_colors': ['Gold', 'Orange'],
                'traits': ['karizmatik', 'yaratıcı', 'gururlu', 'cömert', 'dramatik'],
                'en_traits': ['charismatic', 'creative', 'proud', 'generous', 'dramatic']
            },
            'basak': {
                'name': 'Başak',
                'en_name': 'Virgo',
                'symbol': '♍',
                'dates': '23 Ağustos - 22 Eylül',
                'en_dates': 'Aug 23 - Sep 22',
                'element': 'Toprak',
                'en_element': 'Earth',
                'planet': 'Merkür',
                'colors': ['Lacivert', 'Gri'],
                'en_colors': ['Navy Blue', 'Gray'],
                'traits': ['mükemmeliyetçi', 'analitik', 'düzenli', 'titiz', 'yardımsever'],
                'en_traits': ['perfectionist', 'analytical', 'organized', 'meticulous', 'helpful']
            },
            'terazi': {
                'name': 'Terazi',
                'en_name': 'Libra',
                'symbol': '♎',
                'dates': '23 Eylül - 22 Ekim',
                'en_dates': 'Sep 23 - Oct 22',
                'element': 'Hava',
                'en_element': 'Air',
                'planet': 'Venüs',
                'colors': ['Pembe', 'Açık Mavi'],
                'en_colors': ['Pink', 'Light Blue'],
                'traits': ['diplomatik', 'adil', 'sosyal', 'estetik', 'barışçıl'],
                'en_traits': ['diplomatic', 'fair', 'social', 'aesthetic', 'peaceful']
            },
            'akrep': {
                'name': 'Akrep',
                'en_name': 'Scorpio',
                'symbol': '♏',
                'dates': '23 Ekim - 21 Kasım',
                'en_dates': 'Oct 23 - Nov 21',
                'element': 'Su',
                'en_element': 'Water',
                'planet': 'Plüton',
                'colors': ['Bordo', 'Siyah'],
                'en_colors': ['Burgundy', 'Black'],
                'traits': ['yoğun', 'tutkulu', 'gizemli', 'kararlı', 'dönüştürücü'],
                'en_traits': ['intense', 'passionate', 'mysterious', 'determined', 'transformative']
            },
            'yay': {
                'name': 'Yay',
                'en_name': 'Sagittarius',
                'symbol': '♐',
                'dates': '22 Kasım - 21 Aralık',
                'en_dates': 'Nov 22 - Dec 21',
                'element': 'Ateş',
                'en_element': 'Fire',
                'planet': 'Jüpiter',
                'colors': ['Mor', 'Turuncusu'],
                'en_colors': ['Purple', 'Orange'],
                'traits': ['özgürlükçü', 'maceraperest', 'iyimser', 'felsefi', 'dürüst'],
                'en_traits': ['freedom-loving', 'adventurous', 'optimistic', 'philosophical', 'honest']
            },
            'oglak': {
                'name': 'Oğlak',
                'en_name': 'Capricorn',
                'symbol': '♑',
                'dates': '22 Aralık - 19 Ocak',
                'en_dates': 'Dec 22 - Jan 19',
                'element': 'Toprak',
                'en_element': 'Earth',
                'planet': 'Satürn',
                'colors': ['Kahverengi', 'Siyah'],
                'en_colors': ['Brown', 'Black'],
                'traits': ['disiplinli', 'hırslı', 'pratik', 'sorumlu', 'geleneksel'],
                'en_traits': ['disciplined', 'ambitious', 'practical', 'responsible', 'traditional']
            },
            'kova': {
                'name': 'Kova',
                'en_name': 'Aquarius',
                'symbol': '♒',
                'dates': '20 Ocak - 18 Şubat',
                'en_dates': 'Jan 20 - Feb 18',
                'element': 'Hava',
                'en_element': 'Air',
                'planet': 'Uranüs',
                'colors': ['Elektrik Mavisi', 'Gümüş'],
                'en_colors': ['Electric Blue', 'Silver'],
                'traits': ['bağımsız', 'yenilikçi', 'insancıl', 'orijinal', 'vizyoner'],
                'en_traits': ['independent', 'innovative', 'humanitarian', 'original', 'visionary']
            },
            'balik': {
                'name': 'Balık',
                'en_name': 'Pisces',
                'symbol': '♓',
                'dates': '19 Şubat - 20 Mart',
                'en_dates': 'Feb 19 - Mar 20',
                'element': 'Su',
                'en_element': 'Water',
                'planet': 'Neptün',
                'colors': ['Deniz Yeşili', 'Lavanta'],
                'en_colors': ['Sea Green', 'Lavender'],
                'traits': ['sezgisel', 'yaratıcı', 'şefkatli', 'rüyacı', 'mistik'],
                'en_traits': ['intuitive', 'creative', 'compassionate', 'dreamy', 'mystical']
            }
        }
        
        # Content templates for different aspects
        self.templates = {
            'turkish': {
                'general': [
                    "Bugün {sign} burcu için oldukça dinamik bir gün olacak. {element} elementi size güç veriyor.",
                    "{planet} gezeninizin etkisi altında, yeni fırsatlar kapınızı çalabilir.",
                    "Bugün kendinizi {traits} hissedeceksiniz. Bu size avantaj sağlayacak.",
                    "Doğal {element} enerjiniz bugün doruk noktasında. Bunu değerlendirin.",
                    "Bugün {color} rengini tercih etmek size şans getirebilir."
                ],
                'love': [
                    "Aşk hayatınızda romantik sürprizler sizi bekliyor. Partnernizle daha derin bağlar kurabilirsiniz.",
                    "Bekar {sign}'lar için yeni tanışıklıklar mümkün. Sosyal ortamlarda dikkat çekersiniz.",
                    "İlişkinizdeki iletişim bugün öne çıkıyor. Duygularınızı açık bir şekilde ifade edin.",
                    "Venüs'ün etkisiyle romantik anlar yaşayabilirsiniz. Sevdiklerinize zaman ayırın.",
                    "Duygusal bağlarınız güçleniyor. Aile ve sevdiklerinizle kaliteli vakit geçirin."
                ],
                'career': [
                    "İş hayatınızda yeni projeler ve fırsatlar gündeme gelebilir. Yaratıcılığınızı kullanın.",
                    "Kariyerinizde ileriye dönük adımlar atma zamanı. Amirleriniz size güveniyor.",
                    "Ekip çalışması bugün öne çıkıyor. İş arkadaşlarınızla uyum içinde çalışın.",
                    "Mali konularda dikkatli olun. Yatırım fırsatları değerlendirilebilir.",
                    "Liderlik özellikleriniz bugün ön plana çıkıyor. İnisiyatif almaktan çekinmeyin."
                ],
                'health': [
                    "Sağlığınıza özen göstermeniz gereken bir dönem. Beslenmenize dikkat edin.",
                    "Fiziksel aktivite yapmanız ruh halinizi olumlu etkileyecek. Spor yapmayı ihmal etmeyin.",
                    "Stres seviyenizi kontrol altında tutun. Meditasyon ve nefes egzersizleri faydalı olacak.",
                    "Vücudunuzun ihtiyaçlarını dinleyin. Yeterli uyku ve dinlenme önemli.",
                    "Doğal beslenme tercihleriniz sağlığınızı destekleyecek. Su tüketiminizi artırın."
                ]
            },
            'english': [
                {
                    'general': [
                        "Today brings dynamic energy for {sign}. Your {element} element gives you strength.",
                        "Under the influence of {planet}, new opportunities may knock on your door.",
                        "You'll feel {traits} today. This will give you an advantage.",
                        "Your natural {element} energy is at its peak today. Take advantage of this.",
                        "Choosing {color} color today might bring you luck."
                    ],
                    'love': [
                        "Romantic surprises await you in your love life. You can form deeper bonds with your partner.",
                        "Single {sign}s may meet new people. You'll attract attention in social settings.",
                        "Communication in your relationship is highlighted today. Express your feelings openly.",
                        "With Venus's influence, you may experience romantic moments. Spend time with loved ones.",
                        "Your emotional bonds are strengthening. Spend quality time with family and loved ones."
                    ],
                    'career': [
                        "New projects and opportunities may arise in your work life. Use your creativity.",
                        "It's time to take forward-looking steps in your career. Your superiors trust you.",
                        "Teamwork is highlighted today. Work in harmony with your colleagues.",
                        "Be careful with financial matters. Investment opportunities can be evaluated.",
                        "Your leadership qualities come to the fore today. Don't hesitate to take initiative."
                    ],
                    'health': [
                        "A period when you need to take care of your health. Pay attention to your nutrition.",
                        "Physical activity will positively affect your mood. Don't neglect exercise.",
                        "Keep your stress level under control. Meditation and breathing exercises will be beneficial.",
                        "Listen to your body's needs. Adequate sleep and rest are important.",
                        "Natural nutrition choices will support your health. Increase your water consumption."
                    ]
                }
            ]
        }

    def generate_lucky_numbers(self):
        """Generate 3 random lucky numbers"""
        return sorted(random.sample(range(1, 42), 3))

    def generate_daily_horoscope(self, sign_key, language='turkish'):
        """Generate a complete daily horoscope for a zodiac sign"""
        sign = self.zodiac_signs[sign_key]
        
        if language == 'turkish':
            general = random.choice(self.templates['turkish']['general']).format(
                sign=sign['name'],
                element=sign['element'],
                planet=sign['planet'],
                traits=random.choice(sign['traits']),
                color=random.choice(sign['colors'])
            )
            
            love = random.choice(self.templates['turkish']['love']).format(
                sign=sign['name']
            )
            
            career = random.choice(self.templates['turkish']['career'])
            health = random.choice(self.templates['turkish']['health'])
            
            lucky_color = random.choice(sign['colors'])
            lucky_time = random.choice(['Sabah', 'Öğlen', 'Akşam', 'Gece'])
            
        else:  # English
            templates = self.templates['english'][0]
            general = random.choice(templates['general']).format(
                sign=sign['en_name'],
                element=sign['en_element'],
                planet=sign['planet'],
                traits=random.choice(sign['en_traits']),
                color=random.choice(sign['en_colors'])
            )
            
            love = random.choice(templates['love']).format(
                sign=sign['en_name']
            )
            
            career = random.choice(templates['career'])
            health = random.choice(templates['health'])
            
            lucky_color = random.choice(sign['en_colors'])
            lucky_time = random.choice(['Morning', 'Midday', 'Evening', 'Night'])

        return {
            'general': general,
            'love': love,
            'career': career,
            'health': health,
            'lucky': {
                'numbers': self.generate_lucky_numbers(),
                'color': lucky_color,
                'time': lucky_time
            }
        }

    def create_daily_content_file(self, sign_key, language='turkish'):
        """Create a daily horoscope content file"""
        sign = self.zodiac_signs[sign_key]
        horoscope = self.generate_daily_horoscope(sign_key, language)
        
        date_str = self.today.strftime('%Y-%m-%d')
        
        if language == 'turkish':
            filename = f"{sign_key}-gunluk-{date_str}.md"
            title = f"{sign['name']} Günlük Yorumu - {self.today.strftime('%d.%m.%Y')}"
            description = f"{sign['name']} burcu için günlük astroloji yorumu. Aşk, kariyer, sağlık ve genel rehberlik."
            keywords = f"{sign['name'].lower()}, günlük yorum, {sign['element'].lower()}, astroloji, burç"
        else:
            filename = f"{sign_key}-daily-{date_str}.md"
            title = f"{sign['en_name']} Daily Horoscope - {self.today.strftime('%B %d, %Y')}"
            description = f"Daily astrology reading for {sign['en_name']}. Love, career, health and general guidance."
            keywords = f"{sign['en_name'].lower()}, daily horoscope, {sign['en_element'].lower()}, astrology, zodiac"

        content = f"""---
title: "{title}"
description: "{description}"
keywords: "{keywords}"
date: {self.today.isoformat()}
category: "astrology"
tags: ["astrology", "{sign_key}", "daily", "{sign['element'].lower() if language == 'turkish' else sign['en_element'].lower()}"]
author: "MindVerse Astroloji"
summary: "{'Günlük astroloji yorumu ve rehberlik' if language == 'turkish' else 'Daily astrology reading and guidance'}"
views: 0
---

## {'Genel Durum' if language == 'turkish' else 'General Situation'}

{horoscope['general']}

## {'Aşk ve İlişkiler' if language == 'turkish' else 'Love and Relationships'}

{horoscope['love']}

## {'Kariyer ve İş' if language == 'turkish' else 'Career and Work'}

{horoscope['career']}

## {'Sağlık ve Zindelik' if language == 'turkish' else 'Health and Wellness'}

{horoscope['health']}

## {'Şanslı Elementler' if language == 'turkish' else 'Lucky Elements'}

- **{'Şanslı Sayılar' if language == 'turkish' else 'Lucky Numbers'}:** {', '.join(map(str, horoscope['lucky']['numbers']))}
- **{'Şanslı Renk' if language == 'turkish' else 'Lucky Color'}:** {horoscope['lucky']['color']}
- **{'En İyi Zaman' if language == 'turkish' else 'Best Time'}:** {horoscope['lucky']['time']}

---

*{'Bu yorum sadece eğlence amaçlıdır ve kesin gerçekleri yansıtmaz.' if language == 'turkish' else 'This reading is for entertainment purposes only and does not reflect absolute truths.'}*
"""

        # Create directory if it doesn't exist
        content_dir = self.content_path
        content_dir.mkdir(parents=True, exist_ok=True)
        
        # Write file
        file_path = content_dir / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return file_path

    def generate_all_daily_horoscopes(self, language='turkish'):
        """Generate daily horoscopes for all zodiac signs"""
        created_files = []
        
        for sign_key in self.zodiac_signs.keys():
            try:
                file_path = self.create_daily_content_file(sign_key, language)
                created_files.append(file_path)
                print(f"✅ Created: {file_path}")
            except Exception as e:
                print(f"❌ Error creating horoscope for {sign_key}: {e}")
        
        return created_files

    def generate_weekly_summary(self, language='turkish'):
        """Generate a weekly astrology summary"""
        date_str = self.today.strftime('%Y-%m-%d')
        week_num = self.today.isocalendar()[1]
        
        if language == 'turkish':
            filename = f"haftalik-ozet-{date_str}.md"
            title = f"Haftalık Astroloji Özeti - {week_num}. Hafta {self.today.year}"
            description = "Tüm burçlar için haftalık astroloji özeti ve genel kozmik enerji analizi."
        else:
            filename = f"weekly-summary-{date_str}.md"
            title = f"Weekly Astrology Summary - Week {week_num}, {self.today.year}"
            description = "Weekly astrology summary for all zodiac signs and general cosmic energy analysis."

        cosmic_themes = {
            'turkish': [
                "Bu hafta Merkür'ün etkisi güçlü hissediliyor",
                "Venüs'ün harmonik enerjisi ilişkileri destekliyor",
                "Mars'ın dinamik etkisi motivasyonu artırıyor",
                "Ay'ın dönüşümsel gücü değişimleri getiriyor"
            ],
            'english': [
                "Mercury's influence is strongly felt this week",
                "Venus's harmonic energy supports relationships",
                "Mars's dynamic influence increases motivation",
                "The Moon's transformational power brings changes"
            ]
        }
        
        theme = random.choice(cosmic_themes[language])
        
        content = f"""---
title: "{title}"
description: "{description}"
keywords: "{'haftalık astroloji, burç yorumu, kozmik enerji' if language == 'turkish' else 'weekly astrology, horoscope, cosmic energy'}"
date: {self.today.isoformat()}
category: "astrology"
tags: ["astrology", "weekly", "summary", "cosmic"]
author: "MindVerse Astroloji"
summary: "{description}"
views: 0
---

## {'Genel Kozmik Enerji' if language == 'turkish' else 'General Cosmic Energy'}

{theme}. {'Bu hafta tüm burçlar için önemli gelişmeler yaşanacak.' if language == 'turkish' else 'Important developments will occur for all zodiac signs this week.'}

## {'Haftalık Öne Çıkanlar' if language == 'turkish' else 'Weekly Highlights'}

{'### Ateş Burçları (Koç, Aslan, Yay)' if language == 'turkish' else '### Fire Signs (Aries, Leo, Sagittarius)'}
{'Enerjiniz yüksek, yeni projelere başlamak için ideal zaman.' if language == 'turkish' else 'Your energy is high, ideal time to start new projects.'}

{'### Toprak Burçları (Boğa, Başak, Oğlak)' if language == 'turkish' else '### Earth Signs (Taurus, Virgo, Capricorn)'}
{'Pratik yaklaşımınız size avantaj sağlayacak.' if language == 'turkish' else 'Your practical approach will give you an advantage.'}

{'### Hava Burçları (İkizler, Terazi, Kova)' if language == 'turkish' else '### Air Signs (Gemini, Libra, Aquarius)'}
{'İletişim ve sosyal bağlantılar ön planda.' if language == 'turkish' else 'Communication and social connections are prominent.'}

{'### Su Burçları (Yengeç, Akrep, Balık)' if language == 'turkish' else '### Water Signs (Cancer, Scorpio, Pisces)'}
{'Sezgisel kararlarınız doğru yönde olacak.' if language == 'turkish' else 'Your intuitive decisions will be in the right direction.'}

---

*{'Detaylı günlük yorumlar için ilgili burç sayfalarını ziyaret edin.' if language == 'turkish' else 'Visit respective zodiac pages for detailed daily readings.'}*
"""

        # Write file
        content_dir = self.content_path
        file_path = content_dir / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return file_path

def main():
    """Main function to generate horoscope content"""
    generator = DailyHoroscopeGenerator()
    
    print("🔮 MindVerse Daily Horoscope Generator")
    print("=====================================")
    
    # Generate Turkish content
    print("\n📝 Generating Turkish daily horoscopes...")
    turkish_files = generator.generate_all_daily_horoscopes('turkish')
    
    # Generate English content  
    print("\n📝 Generating English daily horoscopes...")
    english_files = generator.generate_all_daily_horoscopes('english')
    
    # Generate weekly summaries
    print("\n📊 Generating weekly summaries...")
    turkish_weekly = generator.generate_weekly_summary('turkish')
    english_weekly = generator.generate_weekly_summary('english')
    
    print(f"\n✅ Successfully generated {len(turkish_files)} Turkish files")
    print(f"✅ Successfully generated {len(english_files)} English files")
    print(f"✅ Created weekly summaries")
    print(f"\n📁 Total files created: {len(turkish_files) + len(english_files) + 2}")
    
    return True

if __name__ == "__main__":
    main()
