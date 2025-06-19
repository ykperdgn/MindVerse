import { c as createAstro, a as createComponent, r as renderTemplate, b as renderSlot, d as renderHead, e as addAttribute } from './astro/server_Dyg-ivk5.mjs';
import 'kleur/colors';
import 'clsx';

var __freeze = Object.freeze;
var __defProp = Object.defineProperty;
var __template = (cooked, raw) => __freeze(__defProp(cooked, "raw", { value: __freeze(cooked.slice()) }));
var _a;
const $$Astro = createAstro("https://www.mindversedaily.com");
const $$Layout = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro, $$props, $$slots);
  Astro2.self = $$Layout;
  const { title, description, keywords, image, canonicalUrl } = Astro2.props;
  const siteTitle = title ? `${title} | MindVerse` : "MindVerse - \xC7oklu Ni\u015F Bilgi Portal\u0131";
  const siteDescription = description || "Sa\u011Fl\u0131k, a\u015Fk, tarih, psikoloji, uzay ve al\u0131nt\u0131lar kategorilerinde zengin i\xE7erikler. G\xFCncel ara\u015Ft\u0131rmalar, uzman g\xF6r\xFC\u015Fleri ve pratik \xF6neriler.";
  const siteKeywords = keywords || "sa\u011Fl\u0131k, a\u015Fk, tarih, psikoloji, uzay, al\u0131nt\u0131lar, bilgi, ara\u015Ft\u0131rma, uzman, rehber";
  const siteImage = image || "https://www.mindversedaily.com/social-media/og-image.jpg";
  const currentUrl = canonicalUrl || Astro2.url.href;
  return renderTemplate(_a || (_a = __template(['<html lang="tr"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><!-- Google Fonts --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet"><!-- SEO Meta Tags --><title>', '</title><meta name="description"', '><meta name="keywords"', '><meta name="author" content="MindVerse"><meta name="robots" content="index, follow"><link rel="canonical"', '><!-- Google AdSense --><meta name="google-adsense-account" content="ca-pub-3096725438789562"><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3096725438789562" crossorigin="anonymous"><\/script><!-- Open Graph / Facebook --><meta property="og:type" content="website"><meta property="og:url"', '><meta property="og:title"', '><meta property="og:description"', '><meta property="og:image"', '><meta property="og:locale" content="tr_TR"><meta property="og:site_name" content="MindVerse"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url"', '><meta property="twitter:title"', '><meta property="twitter:description"', '><meta property="twitter:image"', `><!-- Favicon --><link rel="icon" type="image/svg+xml" href="/favicon.svg"><!-- Google Search Console (Do\u011Frulama kodunu buraya ekleyin) --><meta name="google-site-verification" content="google88e7e5bbe464e115.html"><!-- Preconnect for performance --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://www.google-analytics.com"><link rel="preconnect" href="https://www.googletagmanager.com"><!-- Google Analytics (GA4) - Active Configuration --><script async src="https://www.googletagmanager.com/gtag/js?id=G-MINDVERSE2025"><\/script><script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-MINDVERSE2025', {
      page_title: document.title,
      page_location: window.location.href,
      send_page_view: true,
      custom_map: {
        'content_category': 'category',
        'article_length': 'word_count'
      }
    });

    // Custom event tracking
    function trackContentView(category, title) {
      gtag('event', 'content_view', {
        'content_category': category,
        'content_title': title,
        'page_title': document.title
      });
    }
  <\/script><!-- JSON-LD Structured Data --><script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "MindVerse",
      "description": "\xC7oklu ni\u015F bilgi portal\u0131 - Sa\u011Fl\u0131k, a\u015Fk, tarih, psikoloji, uzay ve al\u0131nt\u0131lar",
      "url": "https://www.mindversedaily.com",
      "publisher": {
        "@type": "Organization",
        "name": "MindVerse",
        "url": "https://www.mindversedaily.com"
      },
      "potentialAction": {
        "@type": "SearchAction",
        "target": "https://www.mindversedaily.com/search?q={search_term_string}",
        "query-input": "required name=search_term_string"
      }
    }
  <\/script><link rel="stylesheet" href="/src/styles/global.css">`, '</head> <body> <div class="min-h-screen flex flex-col"> <header class="bg-white border-b border-gray-200 shadow-sm"> <nav class="container mx-auto px-4 py-4 flex justify-between items-center"> <div class="flex items-center"> <span class="inline-flex items-center justify-center w-12 h-12 rounded-full bg-gradient-to-br from-blue-500 via-purple-500 to-pink-400 shadow-lg mr-3"> <span class="text-3xl">\u{1F30C}</span> </span> <a href="/" class="text-2xl font-extrabold bg-gradient-to-r from-blue-600 via-purple-500 to-pink-400 bg-clip-text text-transparent tracking-tight drop-shadow-sm hover:from-blue-700 hover:to-purple-700 transition-all">\nMindVerse\n</a> </div> <div class="flex space-x-6 text-gray-700"> <a href="/" class="hover:text-blue-600 transition-colors font-medium">\u{1F3E0} Ana Sayfa</a> <a href="/popular" class="hover:text-blue-600 transition-colors font-medium">\u{1F525} Pop\xFCler</a> <a href="/categories" class="hover:text-blue-600 transition-colors font-medium">\u{1F4C1} Kategoriler</a> <a href="/astrology" class="hover:text-blue-600 transition-colors font-medium">\u{1F52E} Astroloji</a> </div> </nav> <!-- AdSense Header Ad --> <div class="border-t border-gray-100 py-3 bg-gray-50"> <div class="container mx-auto flex justify-center"> <div class="w-full max-w-lg"> <ins class="adsbygoogle" style="display: block" data-ad-client="ca-pub-3096725438789562" data-ad-slot="1234567890" data-ad-format="auto" data-full-width-responsive="true"></ins> </div> </div> </div> </header> <main class="flex-grow py-6" style="background-color:#F7F0E8;"> <div class="container mx-auto px-4"> ', ' </div> </main> <footer class="bg-white text-gray-800 border-t border-gray-200 p-6"> <div class="container mx-auto"> <div class="flex flex-col md:flex-row md:items-center md:justify-between mb-6 gap-6"> <div> <h3 class="font-bold text-xl mb-3 text-blue-600">\u{1F30C} MindVerse Daily</h3> <p class="text-gray-600 mb-4">Bilginin sonsuz evrenini ke\u015Ffedin. Kaliteli, ara\u015Ft\u0131rma temelli i\xE7eriklerle hayat\u0131n\u0131za de\u011Fer kat\u0131n.</p> <div class="flex flex-wrap gap-3 md:gap-4 items-center"> <a href="/health" class="flex flex-col items-center bg-blue-100 text-blue-800 px-4 py-2 rounded-full text-lg hover:bg-blue-200 transition-colors shadow-sm"> <span class="text-2xl">\u{1F3E5}</span> <span class="text-xs font-medium mt-1">Sa\u011Fl\u0131k</span> </a> <a href="/love" class="flex flex-col items-center bg-red-100 text-red-800 px-4 py-2 rounded-full text-lg hover:bg-red-200 transition-colors shadow-sm"> <span class="text-2xl">\u2764\uFE0F</span> <span class="text-xs font-medium mt-1">A\u015Fk</span> </a> <a href="/history" class="flex flex-col items-center bg-yellow-100 text-yellow-800 px-4 py-2 rounded-full text-lg hover:bg-yellow-200 transition-colors shadow-sm"> <span class="text-2xl">\u{1F4DA}</span> <span class="text-xs font-medium mt-1">Tarih</span> </a> <a href="/astrology" class="flex flex-col items-center bg-purple-100 text-purple-800 px-4 py-2 rounded-full text-lg hover:bg-purple-200 transition-colors shadow-sm"> <span class="text-2xl">\u{1F52E}</span> <span class="text-xs font-medium mt-1">Astroloji</span> </a> <a href="/psychology" class="flex flex-col items-center bg-pink-100 text-pink-800 px-4 py-2 rounded-full text-lg hover:bg-pink-200 transition-colors shadow-sm"> <span class="text-2xl">\u{1F9E0}</span> <span class="text-xs font-medium mt-1">Psikoloji</span> </a> <a href="/space" class="flex flex-col items-center bg-green-100 text-green-800 px-4 py-2 rounded-full text-lg hover:bg-green-200 transition-colors shadow-sm"> <span class="text-2xl">\u{1F680}</span> <span class="text-xs font-medium mt-1">Uzay</span> </a> <a href="/quotes" class="flex flex-col items-center bg-gray-100 text-gray-800 px-4 py-2 rounded-full text-lg hover:bg-gray-200 transition-colors shadow-sm"> <span class="text-2xl">\u{1F4AD}</span> <span class="text-xs font-medium mt-1">Al\u0131nt\u0131lar</span> </a> </div> </div> </div> <div class="border-t border-gray-200 pt-4 text-center"> <p class="text-sm text-gray-600">\n\xA9 2025 MindVerse Daily. T\xFCm haklar\u0131 sakl\u0131d\u0131r. |\n<a href="/privacy-policy" class="text-blue-600 hover:text-blue-800">Gizlilik Politikas\u0131</a> |\n<a href="/terms" class="text-blue-600 hover:text-blue-800">Kullan\u0131m Ko\u015Fullar\u0131</a> </p> <p class="text-xs text-gray-500 mt-2">\n\u{1F31F} Kaliteli i\xE7erikler g\xFCnl\xFCk olarak yay\u0131nlan\u0131r \u2022 \u{1F50D} Bilginin sonsuz evrenini ke\u015Ffedin\n</p> </div> </div> </footer> </div> </body></html>'])), siteTitle, addAttribute(siteDescription, "content"), addAttribute(siteKeywords, "content"), addAttribute(currentUrl, "href"), addAttribute(currentUrl, "content"), addAttribute(siteTitle, "content"), addAttribute(siteDescription, "content"), addAttribute(siteImage, "content"), addAttribute(currentUrl, "content"), addAttribute(siteTitle, "content"), addAttribute(siteDescription, "content"), addAttribute(siteImage, "content"), renderHead(), renderSlot($$result, $$slots["default"]));
}, "C:/Users/Jacob/MindVerse/mindverse_blog/src/components/Layout.astro", void 0);

export { $$Layout as $ };
