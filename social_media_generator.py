#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MindVerse Social Media Graphics Generator
Sosyal medya paylaşımları için otomatik grafik üretici
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_og_image(title="MindVerse", subtitle="Çoklu Niş Bilgi Portalı", category="general"):
    """Open Graph paylaşım görseli oluşturur"""

    # Görsel boyutları (Facebook/Twitter optimized)
    width, height = 1200, 630

    # Kategori renkleri
    category_colors = {
        'health': '#10B981',  # green
        'love': '#EF4444',    # red
        'history': '#F59E0B', # yellow
        'psychology': '#8B5CF6', # purple
        'space': '#3B82F6',   # blue
        'quotes': '#6B7280',  # gray
        'general': '#4F46E5'  # indigo
    }

    # Arka plan gradyanı
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)

    # Gradient arka plan oluştur
    primary_color = category_colors.get(category, category_colors['general'])

    # Basit gradient etkisi
    for y in range(height):
        # RGB değerlerini hesapla
        r = int(0x4F + (0xFF - 0x4F) * (y / height))
        g = int(0x46 + (0xFF - 0x46) * (y / height))
        b = int(0xE5 + (0xFF - 0xE5) * (y / height))

        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Logo/Brand alanı
    try:
        # Font boyutları
        title_font_size = 80
        subtitle_font_size = 40

        # Varsayılan font kullan (sistem fontu)
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()

        # Başlık
        title_bbox = draw.textbbox((0, 0), title, font=title_font)
        title_width = title_bbox[2] - title_bbox[0]
        title_height = title_bbox[3] - title_bbox[1]

        title_x = (width - title_width) // 2
        title_y = height // 2 - 100

        # Başlık gölgesi
        draw.text((title_x + 3, title_y + 3), title, font=title_font, fill='rgba(0,0,0,0.3)')
        draw.text((title_x, title_y), title, font=title_font, fill='white')

        # Alt başlık
        subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
        subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]

        subtitle_x = (width - subtitle_width) // 2
        subtitle_y = title_y + title_height + 20

        draw.text((subtitle_x + 2, subtitle_y + 2), subtitle, font=subtitle_font, fill='rgba(0,0,0,0.3)')
        draw.text((subtitle_x, subtitle_y), subtitle, font=subtitle_font, fill='white')

        # Kategori badge
        if category != 'general':
            badge_text = category.upper()
            badge_font = ImageFont.load_default()

            badge_bbox = draw.textbbox((0, 0), badge_text, font=badge_font)
            badge_width = badge_bbox[2] - badge_bbox[0] + 20
            badge_height = badge_bbox[3] - badge_bbox[1] + 10

            badge_x = 50
            badge_y = 50

            # Badge arka planı
            draw.rounded_rectangle(
                [badge_x, badge_y, badge_x + badge_width, badge_y + badge_height],
                radius=15,
                fill=primary_color
            )

            # Badge metni
            text_x = badge_x + 10
            text_y = badge_y + 5
            draw.text((text_x, text_y), badge_text, font=badge_font, fill='white')

        # URL
        url_text = "mindverse-orcin.vercel.app"
        url_font = ImageFont.load_default()

        url_bbox = draw.textbbox((0, 0), url_text, font=url_font)
        url_width = url_bbox[2] - url_bbox[0]

        url_x = width - url_width - 50
        url_y = height - 50

        draw.text((url_x, url_y), url_text, font=url_font, fill='rgba(255,255,255,0.8)')

    except Exception as e:
        print(f"Font hatası: {e}")
        # Basit fallback
        draw.text((width//2 - 100, height//2), title, fill='white')
        draw.text((width//2 - 150, height//2 + 50), subtitle, fill='white')

    return img

def generate_social_media_assets():
    """Sosyal medya varlıklarını oluşturur"""

    # Çıktı klasörü
    output_dir = "public/social-media"
    os.makedirs(output_dir, exist_ok=True)

    # Ana OG görseli
    main_og = create_og_image("MindVerse", "Çoklu Niş Bilgi Portalı", "general")
    main_og.save(f"{output_dir}/og-image.jpg", "JPEG", quality=90)

    # Kategori bazlı görseller
    categories = {
        'health': 'Sağlık Rehberi',
        'love': 'Aşk & İlişkiler',
        'history': 'Tarih Arşivi',
        'psychology': 'Psikoloji Dünyası',
        'space': 'Uzay Bilimleri',
        'quotes': 'İlham Alıntıları'
    }

    for category, subtitle in categories.items():
        category_og = create_og_image("MindVerse", subtitle, category)
        category_og.save(f"{output_dir}/og-{category}.jpg", "JPEG", quality=90)
        print(f"✅ {category} kategori görseli oluşturuldu")

    # Twitter profil görseli (1500x500)
    twitter_header = Image.new('RGB', (1500, 500), color='#4F46E5')
    draw = ImageDraw.Draw(twitter_header)

    # Twitter header için gradyan
    for y in range(500):
        intensity = int(255 * (1 - y / 500 * 0.3))
        draw.line([(0, y), (1500, y)], fill=(79, 70, 229, intensity))

    # Twitter header metni
    try:
        title_font = ImageFont.load_default()
        draw.text((750 - 100, 200), "MindVerse", font=title_font, fill='white', anchor="mm")
        draw.text((750 - 150, 250), "Çoklu Niş Bilgi Portalı", font=title_font, fill='rgba(255,255,255,0.9)', anchor="mm")
    except:
        draw.text((600, 200), "MindVerse", fill='white')
        draw.text((500, 250), "Çoklu Niş Bilgi Portalı", fill='white')

    twitter_header.save(f"{output_dir}/twitter-header.jpg", "JPEG", quality=90)

    print("✅ Tüm sosyal medya görselleri oluşturuldu!")
    print(f"📁 Klasör: {output_dir}")

if __name__ == "__main__":
    try:
        generate_social_media_assets()
    except ImportError:
        print("⚠️ PIL/Pillow kütüphanesi gerekli. Yüklemek için:")
        print("pip install Pillow")
    except Exception as e:
        print(f"❌ Hata: {e}")
