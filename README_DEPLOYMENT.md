# MindVerse Deployment Guide

## 🚀 Vercel Deployment (Current)

Bu proje **Vercel** üzerinde deploy edilmektedir.

### Domain Configuration
- **Primary Domain**: www.mindversedaily.com
- **Platform**: Vercel
- **Auto Deploy**: main branch push'ları otomatik deploy olur

### Features Enabled
- ✅ Vercel Speed Insights
- ✅ Automatic SSL
- ✅ CDN
- ✅ Server-side rendering (SSR)
- ✅ Static optimization

### Build Settings
- **Framework**: Astro
- **Build Command**: `npm run build`
- **Output Directory**: `dist`
- **Node Version**: 18.x

### Environment Variables (Vercel Dashboard)
- NODE_VERSION=18
- (Add any other env variables as needed)

## 📝 Notes
- GitHub Pages devre dışı bırakılmıştır
- Tüm deployment işlemleri Vercel üzerinden yapılmaktadır
- Domain DNS'i Vercel'e point etmelidir
