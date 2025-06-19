/* empty css                                  */
import { c as createAstro, a as createComponent, f as renderComponent, r as renderTemplate, m as maybeRenderHead, e as addAttribute } from '../chunks/astro/server_Dyg-ivk5.mjs';
import 'kleur/colors';
import { $ as $$Layout } from '../chunks/Layout_BpQYKfR2.mjs';
export { renderers } from '../renderers.mjs';

const $$Astro = createAstro("https://www.mindversedaily.com");
const $$Categories = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro, $$props, $$slots);
  Astro2.self = $$Categories;
  const categories = ["health", "love", "history", "psychology", "space", "quotes", "astrology"];
  const categoryInfo = {
    health: { name: "Sa\u011Fl\u0131k", icon: "\u{1F3E5}", color: "green" },
    love: { name: "A\u015Fk & \u0130li\u015Fkiler", icon: "\u2764\uFE0F", color: "red" },
    history: { name: "Tarih", icon: "\u{1F4DA}", color: "yellow" },
    psychology: { name: "Psikoloji", icon: "\u{1F9E0}", color: "purple" },
    space: { name: "Uzay", icon: "\u{1F680}", color: "blue" },
    quotes: { name: "Al\u0131nt\u0131lar", icon: "\u{1F4AD}", color: "gray" },
    astrology: { name: "Astroloji", icon: "\u{1F52E}", color: "indigo" }
  };
  return renderTemplate`${renderComponent($$result, "Layout", $$Layout, { "title": "T\xFCm Kategoriler" }, { "default": ($$result2) => renderTemplate` ${maybeRenderHead()}<div class="container mx-auto px-4 py-8"> <h1 class="text-4xl font-bold text-center mb-8">📁 Tüm Kategoriler</h1> <!-- Reklam alanı --> <div class="flex justify-center mb-8"> <div class="w-full max-w-lg"> <ins class="adsbygoogle" style="display: block" data-ad-client="ca-pub-3096725438789562" data-ad-slot="1234567890" data-ad-format="auto" data-full-width-responsive="true"></ins> </div> </div> <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"> ${categories.map((category) => {
    const info = categoryInfo[category];
    return renderTemplate`<a${addAttribute(`/${category}`, "href")} class="block bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow border-l-4 border-blue-500 hover:border-blue-600"> <div class="text-center"> <div class="text-4xl mb-4">${info.icon}</div> <h2 class="text-xl font-bold mb-2">${info.name}</h2> <p class="text-gray-600 text-sm"> ${category === "health" && "Sa\u011Fl\u0131kl\u0131 ya\u015Fam ipu\xE7lar\u0131 ve medikal bilgiler"} ${category === "love" && "\u0130li\u015Fkiler, a\u015Fk ve duygusal ba\u011Flar hakk\u0131nda"} ${category === "history" && "Tarihi olaylar ve ki\u015Filer"} ${category === "psychology" && "\u0130nsan davran\u0131\u015Flar\u0131 ve zihin"} ${category === "space" && "Uzay bilimleri ve astronomi"} ${category === "quotes" && "\u0130lham verici s\xF6zler ve al\u0131nt\u0131lar"} ${category === "astrology" && "Bur\xE7 yorumlar\u0131 ve astroloji rehberleri"} </p> </div> </a>`;
  })} </div> </div> ` })}`;
}, "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/categories.astro", void 0);

const $$file = "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/categories.astro";
const $$url = "/categories";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  default: $$Categories,
  file: $$file,
  url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
