/* empty css                                  */
import { c as createAstro, a as createComponent, f as renderComponent, r as renderTemplate, m as maybeRenderHead, e as addAttribute } from '../chunks/astro/server_Dyg-ivk5.mjs';
import 'kleur/colors';
import { $ as $$Layout } from '../chunks/Layout_BpQYKfR2.mjs';
/* empty css                                 */
export { renderers } from '../renderers.mjs';

const $$Astro = createAstro("https://www.mindversedaily.com");
const $$Index = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro, $$props, $$slots);
  Astro2.self = $$Index;
  const categories = [
    { name: "Health", url: "/health", title: "Sa\u011Fl\u0131k", icon: "\u{1F3E5}" },
    { name: "Love", url: "/love", title: "A\u015Fk & \u0130li\u015Fkiler", icon: "\u2764\uFE0F" },
    { name: "History", url: "/history", title: "Tarih", icon: "\u{1F4DA}" },
    { name: "Psychology", url: "/psychology", title: "Psikoloji", icon: "\u{1F9E0}" },
    { name: "Space", url: "/space", title: "Uzay", icon: "\u{1F680}" },
    { name: "Quotes", url: "/quotes", title: "Al\u0131nt\u0131lar", icon: "\u{1F4AD}" },
    { name: "Astrology", url: "/astrology", title: "Astroloji", icon: "\u{1F52E}" }
  ];
  return renderTemplate`${renderComponent($$result, "Layout", $$Layout, { "title": "MindVerse - \xC7oklu Ni\u015F Bilgi Portal\u0131", "data-astro-cid-j7pv25f6": true }, { "default": ($$result2) => renderTemplate` ${maybeRenderHead()}<header class="relative flex flex-col items-center justify-center py-16 md:py-20 overflow-hidden" data-astro-cid-j7pv25f6> <div class="absolute inset-0 w-full h-full animate-gradient-move bg-gradient-to-br from-blue-100 via-pink-100 to-purple-100 opacity-60 blur-2xl z-0" data-astro-cid-j7pv25f6></div> <div class="relative z-10 flex flex-col items-center" data-astro-cid-j7pv25f6> <span class="inline-flex items-center justify-center w-28 h-28 md:w-32 md:h-32 rounded-full animate-gradient-move bg-gradient-to-br from-blue-500 via-purple-500 to-pink-400 shadow-2xl mb-6 border-4 border-white/80" data-astro-cid-j7pv25f6> <span class="text-6xl md:text-7xl drop-shadow-lg" data-astro-cid-j7pv25f6>🌌</span> </span> <h1 class="text-6xl md:text-7xl font-extrabold bg-gradient-to-r from-blue-600 via-purple-500 to-pink-400 bg-clip-text text-transparent tracking-tight drop-shadow-xl animate-gradient-move mb-2" data-astro-cid-j7pv25f6>
MindVerse
</h1> <p class="text-2xl md:text-3xl mb-2 font-semibold text-gray-800 drop-shadow-sm" data-astro-cid-j7pv25f6>Bilginin sonsuz evrenini keşfedin</p> <p class="text-lg md:text-xl opacity-90 font-medium text-gray-700 mb-2" data-astro-cid-j7pv25f6>Zengin içerikler • Güncel bilgiler • Uzman tavsiyeleri</p> </div> </header> <main class="container mx-auto px-4 py-10 md:py-16" data-astro-cid-j7pv25f6> <!-- Popüler içerikler hızlı erişim --> <div class="text-center mb-12" data-astro-cid-j7pv25f6> <a href="/popular" class="inline-flex items-center animate-gradient-move bg-gradient-to-r from-orange-400 via-pink-400 to-purple-400 text-white px-10 py-5 rounded-2xl font-bold shadow-2xl transition-all transform hover:scale-105 border-0 ring-2 ring-pink-200 hover:ring-purple-300 focus:outline-none focus:ring-4 focus:ring-blue-300 relative overflow-hidden pop-button" style="background-size:200% 200%;" data-astro-cid-j7pv25f6> <span class="mr-3 text-2xl" data-astro-cid-j7pv25f6>🔥</span> Popüler İçerikler
<svg class="w-6 h-6 ml-3 animate-bounce-x" fill="none" stroke="currentColor" viewBox="0 0 24 24" data-astro-cid-j7pv25f6> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" data-astro-cid-j7pv25f6></path> </svg> <span class="absolute inset-0 pointer-events-none pop-glow" data-astro-cid-j7pv25f6></span> </a> </div> <!-- AdSense ana sayfa reklam alanı --> <div class="flex justify-center mb-10" data-astro-cid-j7pv25f6> <div class="w-full max-w-lg" data-astro-cid-j7pv25f6> <ins class="adsbygoogle" style="display: block" data-ad-client="ca-pub-3096725438789562" data-ad-slot="1234567890" data-ad-format="auto" data-full-width-responsive="true" data-astro-cid-j7pv25f6></ins> </div> </div> <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8 md:gap-10" data-astro-cid-j7pv25f6> ${categories.map((category) => renderTemplate`<a${addAttribute(category.url, "href")}${addAttribute(`block rounded-2xl shadow-xl p-8 md:p-10 hover:shadow-2xl transition-all transform hover:scale-[1.04] border-l-8 font-semibold category-card-${category.name.toLowerCase()} group relative overflow-hidden`, "class")} data-astro-cid-j7pv25f6> <div class="flex flex-col items-center" data-astro-cid-j7pv25f6> <div class="text-5xl mb-5 bg-white/60 rounded-full p-4 shadow-md group-hover:scale-110 transition-transform duration-300" data-astro-cid-j7pv25f6> ${category.icon} </div> <h2 class="text-2xl md:text-3xl font-extrabold mb-2 bg-gradient-to-r from-blue-600 via-purple-500 to-pink-400 bg-clip-text text-transparent group-hover:from-pink-400 group-hover:to-blue-600 transition-colors duration-300" data-astro-cid-j7pv25f6> ${category.title} </h2> <p class="text-gray-700 text-base md:text-lg mb-4 text-center" data-astro-cid-j7pv25f6> ${category.name === "Health" && "Sa\u011Fl\u0131kl\u0131 ya\u015Fam ipu\xE7lar\u0131 ve medikal bilgiler"} ${category.name === "Love" && "\u0130li\u015Fkiler, a\u015Fk ve duygusal ba\u011Flar hakk\u0131nda"} ${category.name === "History" && "Tarihi olaylar ve ki\u015Filer"} ${category.name === "Psychology" && "\u0130nsan davran\u0131\u015Flar\u0131 ve zihin"} ${category.name === "Space" && "Uzay bilimleri ve astronomi"} ${category.name === "Quotes" && "\u0130lham verici s\xF6zler ve al\u0131nt\u0131lar"} ${category.name === "Astrology" && "Bur\xE7 yorumlar\u0131 ve astroloji rehberleri"} </p> <div class="mt-2 inline-block bg-gradient-to-r from-blue-600 via-purple-500 to-pink-400 text-white px-6 py-2 rounded-lg text-base font-bold shadow-md group-hover:from-pink-400 group-hover:to-blue-600 transition-colors duration-300" data-astro-cid-j7pv25f6>
Keşfet →
</div> </div> <span class="absolute inset-0 opacity-0 group-hover:opacity-20 transition-opacity duration-300 pointer-events-none bg-gradient-to-br from-pink-200 via-blue-200 to-purple-200" data-astro-cid-j7pv25f6></span> </a>`)} </div> <!-- Alt reklam alanı --> <div class="flex justify-center mt-16" data-astro-cid-j7pv25f6> <div class="w-full max-w-lg" data-astro-cid-j7pv25f6> <ins class="adsbygoogle" style="display: block" data-ad-client="ca-pub-3096725438789562" data-ad-slot="1234567890" data-ad-format="auto" data-full-width-responsive="true" data-astro-cid-j7pv25f6></ins> </div> </div> </main>  ` })}`;
}, "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/index.astro", void 0);

const $$file = "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/index.astro";
const $$url = "";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  default: $$Index,
  file: $$file,
  url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
