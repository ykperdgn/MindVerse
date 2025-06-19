/* empty css                                  */
import { a as createComponent, f as renderComponent, r as renderTemplate, m as maybeRenderHead, e as addAttribute } from '../chunks/astro/server_Dyg-ivk5.mjs';
import 'kleur/colors';
import { $ as $$Layout } from '../chunks/Layout_BpQYKfR2.mjs';
export { renderers } from '../renderers.mjs';

const $$Popular = createComponent(($$result, $$props, $$slots) => {
  const popularPosts = [
    {
      title: "Sa\u011Fl\u0131kl\u0131 Ya\u015Fam\u0131n 5 Alt\u0131n Kural\u0131",
      category: "health",
      views: 1250,
      url: "/health",
      summary: "G\xFCnl\xFCk hayat\u0131n\u0131zda uygulayabilece\u011Finiz 5 basit sa\u011Fl\u0131k \xF6nerisi."
    },
    {
      title: "A\u015Fk\u0131n Bilimi: Beyinde Neler Oluyor?",
      category: "love",
      views: 980,
      url: "/love",
      summary: "A\u015F\u0131k oldu\u011Fumuzda beynimizde hangi kimyasallar salg\u0131lan\u0131r?"
    },
    {
      title: "Evrenin S\u0131rlar\u0131: Karanl\u0131k Madde",
      category: "space",
      views: 875,
      url: "/space",
      summary: "Karanl\u0131k madde nedir ve neden g\xF6remiyoruz?"
    },
    {
      title: "Psikolojik Dayan\u0131kl\u0131l\u0131k Nedir?",
      category: "psychology",
      views: 745,
      url: "/psychology",
      summary: "Zorluklar kar\u015F\u0131s\u0131nda g\xFC\xE7l\xFC kalman\u0131n yollar\u0131."
    },
    {
      title: "Tarihte Bug\xFCn: 18 Haziran",
      category: "history",
      views: 630,
      url: "/history",
      summary: "18 Haziran'da ya\u015Fanan \xF6nemli tarihi olaylar."
    }
  ];
  const sortedPopular = popularPosts.sort((a, b) => b.views - a.views);
  return renderTemplate`${renderComponent($$result, "Layout", $$Layout, { "title": "Pop\xFCler \u0130\xE7erikler" }, { "default": ($$result2) => renderTemplate` ${maybeRenderHead()}<div class="container mx-auto px-4"> <h1 class="text-4xl font-bold text-center mb-8">🔥 Popüler İçerikler</h1> <!-- Reklam alanı --> <div class="flex justify-center mb-8"> <div class="w-full max-w-lg"> <ins class="adsbygoogle" style="display: block" data-ad-client="ca-pub-3096725438789562" data-ad-slot="1234567890" data-ad-format="auto" data-full-width-responsive="true"></ins> </div> </div> <div class="grid gap-6"> ${sortedPopular.map((post, index) => renderTemplate`<div class="bg-white rounded-lg shadow-md p-6 border-l-4 border-blue-500"> <div class="flex items-center justify-between mb-3"> <span class="bg-blue-100 text-blue-800 text-xs font-semibold px-2.5 py-0.5 rounded capitalize"> ${post.category} </span> <div class="flex items-center text-gray-500 text-sm"> <svg class="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20"> <path d="M10 12a2 2 0 100-4 2 2 0 000 4z"></path> <path fill-rule="evenodd" d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z" clip-rule="evenodd"></path> </svg> ${post.views} görüntülenme
</div> </div> <h2 class="text-xl font-bold mb-2"> <a${addAttribute(`${post.url}/${post.slug || "2025-06-18-01"}`, "href")} class="hover:text-blue-600 transition-colors"> ${post.title} </a> </h2> <p class="text-gray-600 mb-4">${post.summary}</p> <div class="flex items-center justify-between"> <span class="text-2xl font-bold text-yellow-500">#${index + 1}</span> <a${addAttribute(`${post.url}/${post.slug || "2025-06-18-01"}`, "href")} class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition-colors">
Devamını Oku
</a> </div> </div>`)} </div> </div> ` })}`;
}, "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/popular.astro", void 0);

const $$file = "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/popular.astro";
const $$url = "/popular";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  default: $$Popular,
  file: $$file,
  url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
