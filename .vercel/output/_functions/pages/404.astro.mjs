/* empty css                                  */
import { a as createComponent, f as renderComponent, r as renderTemplate, m as maybeRenderHead } from '../chunks/astro/server_Dyg-ivk5.mjs';
import 'kleur/colors';
import { $ as $$Layout } from '../chunks/Layout_BpQYKfR2.mjs';
export { renderers } from '../renderers.mjs';

const $$404 = createComponent(($$result, $$props, $$slots) => {
  return renderTemplate`${renderComponent($$result, "Layout", $$Layout, { "title": "Sayfa Bulunamad\u0131 - MindVerse" }, { "default": ($$result2) => renderTemplate` ${maybeRenderHead()}<div class="text-center py-16"> <h1 class="text-6xl font-bold text-gray-300 mb-4">404</h1> <h2 class="text-3xl font-bold mb-4">Sayfa Bulunamadı</h2> <p class="text-gray-600 mb-8">Aradığınız sayfa mevcut değil veya taşınmış olabilir.</p> <div class="space-y-4"> <a href="/" class="inline-block bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition-colors">
Ana Sayfaya Dön
</a> <div class="mt-8"> <h3 class="text-xl font-semibold mb-4">Popüler Kategoriler</h3> <div class="flex flex-wrap justify-center gap-4"> <a href="/health" class="bg-green-100 text-green-800 px-4 py-2 rounded-full hover:bg-green-200 transition-colors">
💚 Sağlık
</a> <a href="/love" class="bg-red-100 text-red-800 px-4 py-2 rounded-full hover:bg-red-200 transition-colors">
❤️ Aşk
</a> <a href="/history" class="bg-yellow-100 text-yellow-800 px-4 py-2 rounded-full hover:bg-yellow-200 transition-colors">
📜 Tarih
</a> <a href="/psychology" class="bg-purple-100 text-purple-800 px-4 py-2 rounded-full hover:bg-purple-200 transition-colors">
🧠 Psikoloji
</a> <a href="/space" class="bg-blue-100 text-blue-800 px-4 py-2 rounded-full hover:bg-blue-200 transition-colors">
🚀 Uzay
</a> <a href="/quotes" class="bg-gray-100 text-gray-800 px-4 py-2 rounded-full hover:bg-gray-200 transition-colors">
💭 Alıntılar
</a> </div> </div> </div> </div> ` })}`;
}, "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/404.astro", void 0);

const $$file = "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/404.astro";
const $$url = "/404";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  default: $$404,
  file: $$file,
  url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
