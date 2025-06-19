
# 📧 Mailchimp Entegrasyon Rehberi

## 1. Mailchimp Hesap Kurulumu (ÜCRETSİZ)
1. https://mailchimp.com adresine git
2. "Sign Up Free" butonuna tıkla
3. Email, username ve şifre belirle
4. Hesabını doğrula

### Ücretsiz Plan Limitleri:
- 2,000 contact
- 10,000 email/month
- Basic templates
- Email automation
- Analytics

## 2. Audience (Liste) Oluşturma
1. Dashboard'da "Audience" tıkla
2. "Create Audience" seç
3. Liste bilgilerini doldur:
   - **List name:** MindVerse Newsletter
   - **Default from email:** info@yourdomain.com
   - **Default from name:** MindVerse
   - **Default subject:** MindVerse Günlük Bilgi Dozu

## 3. Signup Form (Kayıt Formu) Oluşturma
1. "Audience" → "Signup forms"
2. "Embedded forms" seç
3. Form tasarımını özelleştir
4. Generated kodu kopyala
5. MindVerse'e entegre et

### CTASection.astro Entegrasyonu:
```html
<!-- Mevcut form yerine Mailchimp form -->
<div id="mc_embed_signup">
<form action="https://yourdomain.us1.list-manage.com/subscribe/post?u=USER_ID&amp;id=LIST_ID"
      method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form"
      class="validate" target="_blank" novalidate>
    <div id="mc_embed_signup_scroll">
        <input type="email" value="" name="EMAIL" class="email"
               placeholder="E-posta adresiniz..." required>
        <div style="position: absolute; left: -5000px;" aria-hidden="true">
            <input type="text" name="b_USER_ID_LIST_ID" tabindex="-1" value="">
        </div>
        <div class="clear">
            <input type="submit" value="Bültene Katıl" name="subscribe"
                   id="mc-embedded-subscribe" class="button">
        </div>
    </div>
</form>
</div>
```

## 4. Email Templates Oluşturma
1. "Templates" bölümüne git
2. "Create Template" tıkla
3. "Code your own" seç
4. HTML template'ları kopyala/yapıştır

### Template Listesi:
- Welcome Email (Hoş geldin)
- Daily Digest (Günlük özet)
- Weekly Roundup (Haftalık özet)
- Re-engagement (Geri kazanım)

## 5. Automation Kurulumu
1. "Automations" tıkla
2. "Create" → "Email"
3. "Welcome new subscribers" seç

### Automation Akışı:
```
Abone olur → Hoş geldin email (0 gün)
           → Günlük digest (1 gün)
           → Anket email (3 gün)
           → Haftalık özet (7 gün)
```

## 6. Campaign Oluşturma (Günlük/Haftalık)
1. "Campaigns" tıkla
2. "Create Campaign" → "Email"
3. "Regular" seç
4. Template seç ve içerik ekle
5. Schedule veya Send

## 7. Newsletter Analytics
### Takip Edilecek Metrikler:
- **Open Rate:** %20+ (iyi)
- **Click Rate:** %3+ (iyi)
- **Unsubscribe Rate:** %2'nin altı
- **Growth Rate:** Aylık %10+

### Optimizasyon:
- A/B test subject lines
- Send time optimization
- Content personalization
- Mobile optimization

## 8. Segment Oluşturma
İleri seviye targeting için:
1. "Audience" → "Segments"
2. "Create Segment" tıkla
3. Kriterleri belirle:
   - Engagement level
   - Signup date
   - Geographic location
   - Email activity

## 9. API Entegrasyonu (Gelişmiş)
Newsletter admin paneli için:

```javascript
// Mailchimp API v3.0
const listId = 'YOUR_LIST_ID';
const apiKey = 'YOUR_API_KEY';
const serverPrefix = 'us1'; // API key'den çıkar

async function addSubscriber(email) {
    const url = `https://${serverPrefix}.api.mailchimp.com/3.0/lists/${listId}/members`;

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Authorization': `Basic ${btoa(`anystring:${apiKey}`)}`
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email_address: email,
            status: 'subscribed'
        })
    });

    return response.json();
}
```

## 10. Günlük Workflow
### Pazartesi - Campaign Planning
- [ ] Haftalık content calendar
- [ ] Subject line ideas
- [ ] Segment analysis

### Salı-Cuma - Daily Digest
- [ ] Content selection
- [ ] Template customization
- [ ] Schedule sending (09:00)

### Cuma - Weekly Roundup
- [ ] Week performance analysis
- [ ] Top content compilation
- [ ] Next week preview

### Analytics Review (Haftalık)
- [ ] Open rates analysis
- [ ] Click-through optimization
- [ ] A/B test results
- [ ] List growth review

---
Generated: 2025-06-19 04:19
Site: https://www.mindversedaily.com
