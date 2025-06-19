/* empty css                                     */
import { c as createAstro, a as createComponent, d as renderHead, r as renderTemplate } from '../../chunks/astro/server_Dyg-ivk5.mjs';
import 'kleur/colors';
import 'clsx';
export { renderers } from '../../renderers.mjs';

const $$Astro = createAstro("https://www.mindversedaily.com");
const $$Dashboard = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro, $$props, $$slots);
  Astro2.self = $$Dashboard;
  const { cookies } = Astro2;
  if (cookies.get("admin_auth")?.value !== "true") {
    return Astro2.redirect("/admin");
  }
  return renderTemplate`<html lang="tr"> <head><title>Admin Paneli | MindVerse</title><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link rel="stylesheet" href="/src/styles/global.css">${renderHead()}</head> <body class="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-blue-100 via-pink-100 to-purple-100"> <div class="bg-white rounded-2xl shadow-2xl p-10 w-full max-w-2xl flex flex-col gap-6 items-center"> <h1 class="text-3xl font-extrabold mb-2 bg-gradient-to-r from-blue-600 via-purple-500 to-pink-400 bg-clip-text text-transparent">MindVerse Admin Paneli</h1> <p class="text-lg text-gray-700 mb-4">Hoş geldiniz, <b>ykperdgn</b>! Buradan site içeriklerinizi ve ayarlarınızı yönetebilirsiniz.</p> <div class="flex flex-wrap gap-4 justify-center"> <a href="/" class="px-6 py-3 rounded-lg bg-blue-100 text-blue-800 font-bold hover:bg-blue-200 transition">Siteye Dön</a> <form method="POST" action="/admin/logout" class="inline"> <button type="submit" class="px-6 py-3 rounded-lg bg-red-100 text-red-800 font-bold hover:bg-red-200 transition">Çıkış Yap</button> </form> </div> <div class="w-full mt-8"> <h2 class="text-xl font-bold mb-2">Yönetim Özellikleri</h2> <ul class="list-disc pl-6 text-gray-700"> <li>İçerik ekleme, düzenleme ve silme (manuel dosya ile)</li> <li>Kategori yönetimi (manuel dosya ile)</li> <li>Gelişmiş yönetim için özel geliştirme yapılabilir</li> </ul> </div> </div> </body></html>`;
}, "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/admin/dashboard.astro", void 0);

const $$file = "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/admin/dashboard.astro";
const $$url = "/admin/dashboard";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  default: $$Dashboard,
  file: $$file,
  url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
