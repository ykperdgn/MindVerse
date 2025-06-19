/* empty css                                  */
import { c as createAstro, a as createComponent, f as renderComponent, r as renderTemplate, m as maybeRenderHead } from '../chunks/astro/server_Dyg-ivk5.mjs';
import 'kleur/colors';
import { $ as $$Layout } from '../chunks/Layout_BpQYKfR2.mjs';
export { renderers } from '../renderers.mjs';

const $$Astro = createAstro("https://www.mindversedaily.com");
const $$Faq = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro, $$props, $$slots);
  Astro2.self = $$Faq;
  return renderTemplate`${renderComponent($$result, "Layout", $$Layout, { "title": "S\u0131k Sorulan Sorular - MindVerse" }, { "default": ($$result2) => renderTemplate` ${maybeRenderHead()}<div class="container mx-auto px-4 py-8"> <div class="prose prose-lg max-w-none">
---
title: "Sık Sorulan Sorular - MindVerse"
date: 2025-06-18
summary: "MindVerse'te en çok merak edilen sorular ve detaylı cevapları. Tüm kategorilerde uzman rehberleri."
tags: ["faq", "sorular", "rehber", "yardım"]
views: 0
---

# 🤔 Sık Sorulan Sorular

MindVerse topluluğumuzun en çok merak ettiği sorular ve detaylı cevapları burada!

## 📚 Kategorilere Göre FAQ'ler

### 🏥 Sağlık
- [Sağlık konusunda sık sorulan sorular](https://mindverse-orcin.vercel.app/health/faq-health)
- Beslenme, egzersiz, mental sağlık rehberleri

### ❤️ Aşk & İlişkiler
- [İlişkiler konusunda sık sorulan sorular](https://mindverse-orcin.vercel.app/love/faq-love)
- İletişim, aşk psikolojisi, evlilik önerileri

### 📚 Tarih
- [Tarih konusunda sık sorulan sorular](https://mindverse-orcin.vercel.app/history/faq-history)
- Antik çağlar, keşifler, kültürel miras

### 🧠 Psikoloji
- [Psikoloji konusunda sık sorulan sorular](https://mindverse-orcin.vercel.app/psychology/faq-psychology)
- Motivasyon, zihin, davranış analizi

### 🚀 Uzay
- [Uzay konusunda sık sorulan sorular](https://mindverse-orcin.vercel.app/space/faq-space)
- Astronomi, gezegen bilimi, uzay keşifleri

### 💭 Alıntılar
- [Alıntılar konusunda sık sorulan sorular](https://mindverse-orcin.vercel.app/quotes/faq-quotes)
- Motivasyonel sözler, ilham kaynakları

## 🔍 Hızlı Arama

Aradığınızı bulamadınız mı? [Site içi arama](https://mindverse-orcin.vercel.app/search) ile tüm içeriklerimizde arama yapabilirsiniz.

## 📧 Soru Gönderin

Aklınıza takılan sorular için:
- Yorumlar bölümünde soru sorabilirsiniz
- Ana sayfada güncel içerikleri takip edebilirsiniz

---
*Bu sayfa düzenli olarak güncellenmektedir. En son güncellenme: 18.06.2025*
</div> </div> ` })}`;
}, "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/faq.astro", void 0);

const $$file = "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/faq.astro";
const $$url = "/faq";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  default: $$Faq,
  file: $$file,
  url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
