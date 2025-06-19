/* empty css                                  */
import { a as createComponent, f as renderComponent, r as renderTemplate, m as maybeRenderHead } from '../chunks/astro/server_Dyg-ivk5.mjs';
import 'kleur/colors';
import { $ as $$Layout } from '../chunks/Layout_BpQYKfR2.mjs';
export { renderers } from '../renderers.mjs';

const $$PrivacyPolicy = createComponent(($$result, $$props, $$slots) => {
  return renderTemplate`${renderComponent($$result, "Layout", $$Layout, { "title": "Gizlilik Politikas\u0131 - MindVerse Daily" }, { "default": ($$result2) => renderTemplate` ${maybeRenderHead()}<main class="prose mx-auto my-12"> <h1>Gizlilik Politikası</h1> <p>Bu sayfa, MindVerse Daily web sitesinin gizlilik uygulamalarını özetler. Kişisel veri toplama, çerez kullanımı veya kullanıcıya özel izleme yapılmaz. Sitemizi ziyaret eden kullanıcıların gizliliği korunur.</p> <ul> <li>Herhangi bir kişisel veri toplanmaz.</li> <li>İletişim veya üyelik sistemi bulunmamaktadır.</li> <li>Çerezler yalnızca site performansı ve anonim analiz için kullanılabilir.</li> <li>Üçüncü parti reklam ve analiz servisleri (ör. Google AdSense, Analytics) yalnızca anonim veriler toplar.</li> </ul> <p>Gizlilikle ilgili sorularınız için lütfen siteyi kullanmaya devam etmeyin; herhangi bir iletişim kanalı sunulmamaktadır.</p> </main> ` })}`;
}, "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/privacy-policy.astro", void 0);

const $$file = "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/privacy-policy.astro";
const $$url = "/privacy-policy";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  default: $$PrivacyPolicy,
  file: $$file,
  url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
