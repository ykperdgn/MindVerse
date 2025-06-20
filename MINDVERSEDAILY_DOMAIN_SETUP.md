# 🌐 mindversedaily.com Domain Bağlama Rehberi

## 🎯 DOMAIN: mindversedaily.com

### 1. **Vercel'de Domain Ekleme**
```bash
# Vercel dashboard'a git
# Project Settings > Domains
# mindversedaily.com ekle
```

### 2. **DNS Kayıtları (Domain Provider'da)**
```
A Record:
@ → 76.76.19.61

CNAME Record:
www → mindversedaily.com

CNAME Record (Vercel'den alınacak):
_vercel → [Vercel'in vereceği değer]
```

### 3. **SSL Certificate**
- Vercel otomatik SSL certificate sağlayacak
- Let's Encrypt ile 24 saat içinde aktif olacak

### 4. **Test**
```bash
# Domain aktif olduktan sonra
https://mindversedaily.com
https://www.mindversedaily.com
```

## 🚀 SONUÇ
- mindversedaily.com ana domain olacak
- www.mindversedaily.com otomatik redirect
- SSL güvenli bağlantı
- Vercel'in CDN ağı aktif

---
*Domain bağlandıktan sonra random URL'ler son bulacak!*
