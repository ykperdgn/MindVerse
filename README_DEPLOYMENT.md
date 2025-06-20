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
- **Framework**: Astro (Auto-detected)
- **Build Command**: `npm run build` (Auto-detected)
- **Output Directory**: `dist` (Auto-detected)
- **Node Version**: 18.x (Auto-configured by @astrojs/vercel)

### Vercel Configuration
- ✅ No manual vercel.json needed
- ✅ Astro adapter handles all configuration
- ✅ Auto-detects framework and settings
- ✅ SSR functions automatically configured

### Environment Variables (Vercel Dashboard)
- No manual environment variables needed
- Node.js version automatically set to 18.x

## 📝 Notes
- GitHub Pages devre dışı bırakılmıştır
- Tüm deployment işlemleri Vercel üzerinden yapılmaktadır
- Domain DNS'i Vercel'e point etmelidir
