/* empty css                                  */
import { a as createComponent, f as renderComponent, r as renderTemplate, m as maybeRenderHead } from '../chunks/astro/server_Dyg-ivk5.mjs';
import 'kleur/colors';
import { $ as $$Layout } from '../chunks/Layout_BpQYKfR2.mjs';
export { renderers } from '../renderers.mjs';

const $$Terms = createComponent(($$result, $$props, $$slots) => {
  return renderTemplate`${renderComponent($$result, "Layout", $$Layout, { "title": "Kullan\u0131m Ko\u015Fullar\u0131 - MindVerse Daily" }, { "default": ($$result2) => renderTemplate` ${maybeRenderHead()}<main class="prose mx-auto my-12"> <h1>Kullanım Koşulları</h1> <p>Bu sayfa, MindVerse Daily web sitesinin kullanım koşullarını özetler. Siteyi kullanan herkes aşağıdaki şartları kabul etmiş sayılır:</p> <ul> <li>Sunulan içerikler yalnızca bilgilendirme amaçlıdır.</li> <li>Hiçbir içerik tıbbi, hukuki veya profesyonel tavsiye yerine geçmez.</li> <li>Kullanıcılar, sitedeki bilgileri kendi sorumluluğunda kullanır.</li> <li>Site üzerinde herhangi bir üyelik, iletişim veya kişisel veri toplama sistemi yoktur.</li> <li>Site yönetimi, içeriklerde değişiklik yapma hakkını saklı tutar.</li> </ul> <p>Herhangi bir soru veya talep için iletişim kanalı bulunmamaktadır.</p> </main> ` })}`;
}, "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/terms.astro", void 0);

const $$file = "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/terms.astro";
const $$url = "/terms";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  default: $$Terms,
  file: $$file,
  url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
