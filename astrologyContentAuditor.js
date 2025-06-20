// astrologyContentAuditor.js
// Akıllı içerik denetim ve senkronizasyon scripti

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

const contentDir = path.join(__dirname, 'src/content/astrology');
const types = [
  { type: 'daily', tr: 'gunluk', en: 'daily' },
  { type: 'weekly', tr: 'haftalik', en: 'weekly' },
  { type: 'monthly', tr: 'aylik', en: 'monthly' }
];

function getAllDates(files, sign, type, lang) {
  // Extract all dates for a sign/type/lang from filenames
  const regex = lang === 'tr'
    ? new RegExp(`^${sign}-${type.tr}-(\\d{4}-\\d{2}-\\d{2})\\.md$`)
    : new RegExp(`^${sign}_${type.en}_(\\d{4}-\\d{2}-\\d{2})_en\\.md$`);
  return files
    .map(f => {
      const m = f.match(regex);
      return m ? m[1] : null;
    })
    .filter(Boolean);
}

function checkFileStructure(filePath, lang, type) {
  // Check if file contains all required sections
  const content = fs.readFileSync(filePath, 'utf8');
  const requiredSections = lang === 'tr'
    ? ['## Genel Bakış', '## Aşk & İlişkiler', '## Kariyer & Para', '## Sağlık & Enerji', '## Şanslı Detaylar', '## Tavsiyeler']
    : ['## General Overview', '## Love & Relationships', '## Career & Money', '## Health & Energy', '## Lucky Details', '## Tips'];
  return requiredSections.every(section => content.includes(section));
}

function auditContent() {
  const files = fs.readdirSync(contentDir);
  let report = [];
  for (const z of zodiac) {
    for (const t of types) {
      // Tüm tarihler için kontrol
      const trDates = getAllDates(files, z.tr, t, 'tr');
      const enDates = getAllDates(files, z.en, t, 'en');
      const allDates = Array.from(new Set([...trDates, ...enDates]));
      for (const date of allDates) {
        const trFile = `${z.tr}-${t.tr}-${date}.md`;
        const enFile = `${z.en}_${t.en}_${date}_en.md`;
        const trPath = path.join(contentDir, trFile);
        const enPath = path.join(contentDir, enFile);
        let trExists = fs.existsSync(trPath);
        let enExists = fs.existsSync(enPath);
        let trOk = trExists && checkFileStructure(trPath, 'tr', t.type);
        let enOk = enExists && checkFileStructure(enPath, 'en', t.type);
        if (!trExists || !enExists) {
          report.push(`[Eksik] ${z.trName}/${z.enName} (${t.type}, ${date}): ${!trExists ? 'TR yok' : ''} ${!enExists ? 'EN yok' : ''}`);
        } else if (!trOk || !enOk) {
          report.push(`[Eksik Bölüm] ${z.trName}/${z.enName} (${t.type}, ${date}): ${!trOk ? 'TR eksik bölüm' : ''} ${!enOk ? 'EN eksik bölüm' : ''}`);
        }
      }
    }
  }
  if (report.length === 0) {
    console.log('Tüm içerikler ve bölümler eksiksiz ve senkronize!');
  } else {
    console.log('Denetim Raporu:');
    report.forEach(r => console.log(r));
  }
}

auditContent();
