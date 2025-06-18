# 🌌 MindVerse - Çoklu Niş Bilgi Portalı

MindVerse, sağlık, aşk, tarih, psikoloji, uzay ve alıntılar kategorilerinde zengin içerikler sunan çok nişli bir bilgi portalıdır. Astro ve Tailwind CSS kullanılarak modern ve responsive bir deneyim sunmak üzere geliştirilmiştir.

## ✨ Özellikler

- 🏥 **6 Farklı Kategori**: Sağlık, Aşk, Tarih, Psikoloji, Uzay, Alıntılar
- 📝 **Zengin İçerik**: Otomatik içerik üretimi sistemi
- 🔍 **Kategoriye Özel Arama**: Her kategoride gelişmiş arama
- 🔥 **Popüler İçerikler**: Görüntülenme bazlı sıralama
- 💬 **Yorum Sistemi**: Kullanıcı etkileşimi
- 📱 **Responsive Tasarım**: Mobil uyumlu
- 🎯 **SEO Optimizasyonu**: Meta etiketler, sitemap
- 💰 **AdSense Hazır**: Reklam alanları entegre

## 🚀 Kurulum

```bash
# Repository'yi klonlayın
git clone https://github.com/ykperdgn/MindVerse.git
cd MindVerse

# Bağımlılıkları yükleyin
npm install

# Geliştirme sunucusunu başlatın
npm run dev
```

## 📝 İçerik Yönetimi

### Otomatik İçerik Üretimi

```bash
# Tek seferlik içerik (her kategoriye 1 adet)
python content_bot.py

# Toplu içerik üretimi (her kategoriye 5 adet)
python content_bot.py batch 5

# Otomatik zamanlayıcı (günde 2 kez)
python content_bot.py scheduler
```

### Manuel İçerik Ekleme

İçerikleri `src/content/[kategori]/` klasörlerine markdown formatında ekleyebilirsiniz:

```markdown
---
title: "Makale Başlığı"
date: 2025-06-18
summary: "Makale özeti"
tags: ["etiket1", "etiket2"]
views: 1250
---

Makale içeriği buraya gelir...
```

## 🏗️ Proje Yapısı

The project is organized as follows:

```
mindverse_blog/
├── public/
│   ├── favicon.svg          # Website ikonu
│   ├── robots.txt           # SEO robots dosyası
│   └── sitemap.html         # Site haritası
├── src/
│   ├── components/          # Yeniden kullanılabilir bileşenler
│   │   ├── CategoryCard.astro
│   │   └── Layout.astro
│   ├── content/            # İçerik kategorileri
│   │   ├── health/         # Sağlık makaleleri
│   │   ├── love/           # Aşk & İlişkiler
│   │   ├── history/        # Tarih
│   │   ├── psychology/     # Psikoloji
│   │   ├── space/          # Uzay
│   │   └── quotes/         # Alıntılar
│   ├── pages/              # Sayfa bileşenleri
│   │   ├── index.astro     # Ana sayfa
│   │   ├── popular.astro   # Popüler içerikler
│   │   ├── categories.astro # Tüm kategoriler
│   │   ├── sitemap.astro   # Site haritası
│   │   └── [category]/
│   │       ├── index.astro # Kategori sayfası
│   │       └── [slug].astro # İçerik detay sayfası
│   └── styles/
│       └── global.css      # Global stiller
├── astro.config.mjs        # Astro konfigürasyonu
├── content_bot.py          # Otomatik içerik üretici
├── package.json            # npm konfigürasyonu
├── postcss.config.cjs      # PostCSS konfigürasyonu
└── tailwind.config.cjs     # Tailwind CSS konfigürasyonu
```

## 🌐 Sayfalar

- `/` - Ana sayfa (kategori kartları)
- `/popular` - Popüler içerikler
- `/categories` - Tüm kategoriler
- `/sitemap` - Site haritası
- `/[kategori]` - Kategori sayfaları (örn: `/health`)
- `/[kategori]/[slug]` - İçerik detay sayfaları

## 🔧 Komutlar

```bash
# Geliştirme
npm run dev              # Geliştirme sunucusu (port 4322)
npm run build           # Production build
npm run preview         # Build önizleme

# İçerik üretimi
python content_bot.py                # Günlük içerik
python content_bot.py batch 10       # Toplu içerik
python content_bot.py scheduler      # Otomatik zamanlayıcı
```

## 📈 SEO & Monetizasyon

- ✅ Meta etiketler ve Open Graph
- ✅ robots.txt ve sitemap.xml
- ✅ AdSense reklam alanları hazır
- ✅ Schema markup desteği
- ✅ Sosyal medya paylaşım butonları

## 🚀 Deploy

### Vercel (Önerilen)
1. GitHub'a push yapın
2. Vercel'e import edin
3. Otomatik deploy

### Netlify
1. GitHub'a push yapın
2. Netlify'a bağlayın
3. Build komutu: `npm run build`
4. Publish directory: `dist`

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Commit yapın (`git commit -m 'Add some AmazingFeature'`)
4. Push yapın (`git push origin feature/AmazingFeature`)
5. Pull Request açın

## 📄 Lisans

Bu proje MIT lisansı ile lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 📞 İletişim

Proje Linki: [https://github.com/ykperdgn/MindVerse](https://github.com/ykperdgn/MindVerse)