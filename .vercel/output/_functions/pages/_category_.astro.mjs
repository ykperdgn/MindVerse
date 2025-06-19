/* empty css                                  */
import { c as createAstro, a as createComponent, f as renderComponent, r as renderTemplate, m as maybeRenderHead, h as renderScript, e as addAttribute } from '../chunks/astro/server_Dyg-ivk5.mjs';
import 'kleur/colors';
import { $ as $$Layout } from '../chunks/Layout_BpQYKfR2.mjs';
import { g as getCollection } from '../chunks/_astro_content_DACpm5sP.mjs';
export { renderers } from '../renderers.mjs';

const $$Astro = createAstro("https://www.mindversedaily.com");
async function getStaticPaths() {
  const categories = ["health", "love", "history", "psychology", "space", "quotes", "astrology"];
  return categories.map((category) => ({
    params: { category }
  }));
}
const $$Index = createComponent(async ($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro, $$props, $$slots);
  Astro2.self = $$Index;
  const { category } = Astro2.params;
  const articles = await getCollection(category);
  return renderTemplate`${renderComponent($$result, "Layout", $$Layout, { "title": `${category.charAt(0).toUpperCase() + category.slice(1)} - MindVerse` }, { "default": async ($$result2) => renderTemplate` ${maybeRenderHead()}<div class="container mx-auto px-4"> <h1 class="text-3xl font-bold mb-4 capitalize">${category}</h1> <!-- Kategoriye özel arama alanı --> <form method="get" class="mb-6 flex justify-center"> <input type="text" name="q" placeholder="Bu kategoride ara..." class="border rounded-l px-4 py-2 w-64"> <button type="submit" class="bg-blue-600 text-white px-4 py-2 rounded-r">Ara</button> </form> <!-- Kategori sayfası reklam alanı --> <div class="flex justify-center mb-6"> <div class="w-full max-w-lg"> <ins class="adsbygoogle" style="display: block" data-ad-client="ca-pub-3096725438789562" data-ad-slot="1234567890" data-ad-format="auto" data-full-width-responsive="true"></ins> </div> </div> <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4"> ${articles.length === 0 ? renderTemplate`<div class="col-span-full text-center text-gray-500">Bu kategoride henüz içerik bulunmuyor.</div>` : articles.map((article) => renderTemplate`<div class="border p-4 rounded-lg shadow-md"> <h2 class="text-xl font-semibold mb-2"> <a${addAttribute(`/${category}/${article.slug}`, "href")} class="hover:text-blue-600 transition-colors"> ${article.data.title} </a> </h2> <p class="text-gray-600 mb-3">${article.data.summary}</p> <div class="flex flex-wrap gap-1 mb-3"> ${article.data.tags?.map((tag) => renderTemplate`<span class="bg-gray-100 text-gray-600 text-xs px-2 py-1 rounded">#${tag}</span>`)} </div> <a${addAttribute(`/${category}/${article.slug}`, "href")} class="inline-block bg-blue-600 text-white px-4 py-2 rounded text-sm hover:bg-blue-700 transition-colors">
Devamını Oku
</a> </div>`)} </div> <!-- Arama fonksiyonalitesi için JavaScript --> ${renderScript($$result2, "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/[category]/index.astro?astro&type=script&index=0&lang.ts")} </div> ` })}`;
}, "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/[category]/index.astro", void 0);

const $$file = "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/[category]/index.astro";
const $$url = "/[category]";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  default: $$Index,
  file: $$file,
  getStaticPaths,
  url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
