/* empty css                                  */
import { a as createComponent, f as renderComponent, r as renderTemplate, m as maybeRenderHead } from '../chunks/astro/server_Dyg-ivk5.mjs';
import 'kleur/colors';
import { $ as $$Layout } from '../chunks/Layout_BpQYKfR2.mjs';
export { renderers } from '../renderers.mjs';

const $$Contact = createComponent(($$result, $$props, $$slots) => {
  return renderTemplate`${renderComponent($$result, "Layout", $$Layout, { "title": "\u0130leti\u015Fim - MindVerse Daily" }, { "default": ($$result2) => renderTemplate` ${maybeRenderHead()}<main class="prose mx-auto my-12 text-center"> <h1>İletişim</h1> <p>Bu sayfa artık aktif değildir.</p> <p>MindVerse Daily ile iletişime geçilemez. Herhangi bir iletişim veya başvuru kanalı bulunmamaktadır.</p> </main> ` })}`;
}, "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/contact.astro", void 0);

const $$file = "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/contact.astro";
const $$url = "/contact";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  default: $$Contact,
  file: $$file,
  url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
