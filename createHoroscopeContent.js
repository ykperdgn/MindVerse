// createHoroscopeContent.js
// Node.js script to create synchronized Turkish and English horoscope markdown files

const fs = require('fs');
const path = require('path');

const zodiac = [
  { tr: 'koc', en: 'aries', trName: 'Koç', enName: 'Aries' },
  { tr: 'boga', en: 'taurus', trName: 'Boğa', enName: 'Taurus' },
  { tr: 'ikizler', en: 'gemini', trName: 'İkizler', enName: 'Gemini' },
  { tr: 'yengec', en: 'cancer', trName: 'Yengeç', enName: 'Cancer' },
  { tr: 'aslan', en: 'leo', trName: 'Aslan', enName: 'Leo' },
  { tr: 'basak', en: 'virgo', trName: 'Başak', enName: 'Virgo' },
  { tr: 'terazi', en: 'libra', trName: 'Terazi', enName: 'Libra' },
  { tr: 'akrep', en: 'scorpio', trName: 'Akrep', enName: 'Scorpio' },
  { tr: 'yay', en: 'sagittarius', trName: 'Yay', enName: 'Sagittarius' },
  { tr: 'oglak', en: 'capricorn', trName: 'Oğlak', enName: 'Capricorn' },
  { tr: 'kova', en: 'aquarius', trName: 'Kova', enName: 'Aquarius' },
  { tr: 'balik', en: 'pisces', trName: 'Balık', enName: 'Pisces' }
];

function createFiles(sign, date, type = 'daily') {
  const z = zodiac.find(z => z.tr === sign || z.en === sign);
  if (!z) throw new Error('Invalid sign');

  let trFile, enFile, trContent, enContent;
  if (type === 'daily') {
    trFile = path.join(__dirname, `src/content/astrology/${z.tr}-gunluk-${date}.md`);
    enFile = path.join(__dirname, `src/content/astrology/${z.en}_daily_${date}_en.md`);
    trContent = `---
title: "${z.trName} Burcu Günlük Yorum (${date})"
zodiacSign: "${z.tr}"
pubDate: "${date}"
lang: "tr"
---

## Genel Bakış

Burç yorumu buraya gelecek.

## Aşk & İlişkiler

Aşk yorumu buraya gelecek.

## Kariyer & Para

Kariyer yorumu buraya gelecek.

## Sağlık & Enerji

Sağlık yorumu buraya gelecek.

## Şanslı Detaylar

- Şanslı Sayılar:
- Şanslı Renk:
- En İyi Zaman:

## Tavsiyeler

Tavsiye buraya gelecek.
`;
    enContent = `---
title: "${z.enName} Daily Horoscope (${date})"
zodiacSign: "${z.en}"
pubDate: "${date}"
lang: "en"
---

## General Overview

Horoscope content goes here.

## Love & Relationships

Love content goes here.

## Career & Money

Career content goes here.

## Health & Energy

Health content goes here.

## Lucky Details

- Lucky Numbers:
- Lucky Color:
- Best Time:

## Tips

Tip content goes here.
`;
  } else if (type === 'weekly') {
    trFile = path.join(__dirname, `src/content/astrology/${z.tr}-haftalik-${date}.md`);
    enFile = path.join(__dirname, `src/content/astrology/${z.en}_weekly_${date}_en.md`);
    trContent = `---
title: "${z.trName} Burcu Haftalık Yorum (${date})"
zodiacSign: "${z.tr}"
pubDate: "${date}"
lang: "tr"
---

## Genel Bakış

Haftalık burç yorumu buraya gelecek.

## Aşk & İlişkiler

Aşk yorumu buraya gelecek.

## Kariyer & Para

Kariyer yorumu buraya gelecek.

## Sağlık & Enerji

Sağlık yorumu buraya gelecek.

## Şanslı Detaylar

- Şanslı Sayılar:
- Şanslı Renk:
- En İyi Zaman:

## Tavsiyeler

Tavsiye buraya gelecek.
`;
    enContent = `---
title: "${z.enName} Weekly Horoscope (${date})"
zodiacSign: "${z.en}"
pubDate: "${date}"
lang: "en"
---

## General Overview

Weekly horoscope content goes here.

## Love & Relationships

Love content goes here.

## Career & Money

Career content goes here.

## Health & Energy

Health content goes here.

## Lucky Details

- Lucky Numbers:
- Lucky Color:
- Best Time:

## Tips

Tip content goes here.
`;
  } else if (type === 'monthly') {
    trFile = path.join(__dirname, `src/content/astrology/${z.tr}-aylik-${date}.md`);
    enFile = path.join(__dirname, `src/content/astrology/${z.en}_monthly_${date}_en.md`);
    trContent = `---
title: "${z.trName} Burcu Aylık Yorum (${date})"
zodiacSign: "${z.tr}"
pubDate: "${date}"
lang: "tr"
---

## Genel Bakış

Aylık burç yorumu buraya gelecek.

## Aşk & İlişkiler

Aşk yorumu buraya gelecek.

## Kariyer & Para

Kariyer yorumu buraya gelecek.

## Sağlık & Enerji

Sağlık yorumu buraya gelecek.

## Şanslı Detaylar

- Şanslı Sayılar:
- Şanslı Renk:
- En İyi Zaman:

## Tavsiyeler

Tavsiye buraya gelecek.
`;
    enContent = `---
title: "${z.enName} Monthly Horoscope (${date})"
zodiacSign: "${z.en}"
pubDate: "${date}"
lang: "en"
---

## General Overview

Monthly horoscope content goes here.

## Love & Relationships

Love content goes here.

## Career & Money

Career content goes here.

## Health & Energy

Health content goes here.

## Lucky Details

- Lucky Numbers:
- Lucky Color:
- Best Time:

## Tips

Tip content goes here.
`;
  } else {
    throw new Error('Invalid type. Use daily, weekly, or monthly.');
  }

  // Dosya var ise yazma!
  if (fs.existsSync(trFile) || fs.existsSync(enFile)) {
    console.log('One or both files already exist! No files were overwritten.');
    return;
  }

  fs.writeFileSync(trFile, trContent, 'utf8');
  fs.writeFileSync(enFile, enContent, 'utf8');
  console.log('Files created:', trFile, enFile);
}

// Usage: node createHoroscopeContent.js koc 2025-06-01 [daily|weekly|monthly]
if (require.main === module) {
  const [,, sign, date, type] = process.argv;
  if (!sign || !date) {
    console.log('Usage: node createHoroscopeContent.js <sign> <YYYY-MM-DD> [daily|weekly|monthly]');
    process.exit(1);
  }
  createFiles(sign, date, type || 'daily');
}
