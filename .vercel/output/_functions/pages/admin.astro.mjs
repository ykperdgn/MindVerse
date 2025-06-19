/* empty css                                  */
import { c as createAstro, a as createComponent, d as renderHead, r as renderTemplate } from '../chunks/astro/server_Dyg-ivk5.mjs';
import 'kleur/colors';
import 'clsx';
export { renderers } from '../renderers.mjs';

const $$Astro = createAstro("https://www.mindversedaily.com");
const $$Index = createComponent(async ($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro, $$props, $$slots);
  Astro2.self = $$Index;
  const { request } = Astro2;
  let error = "";
  if (request.method === "POST") {
    const form = await request.formData();
    const username = form.get("username");
    const password = form.get("password");
    if (username === "ykperdgn" && password === "13592718Y.e") {
      Astro2.cookies.set("admin_auth", "true", { path: "/", httpOnly: true });
      return Astro2.redirect("/admin/dashboard");
    } else {
      error = "Kullan\u0131c\u0131 ad\u0131 veya \u015Fifre yanl\u0131\u015F.";
    }
  }
  return renderTemplate`<html lang="tr"> <head><title>Admin Giriş | MindVerse</title><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link rel="stylesheet" href="/src/styles/global.css">${renderHead()}</head> <body class="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-100 via-pink-100 to-purple-100"> <form method="POST" class="bg-white rounded-2xl shadow-2xl p-8 w-full max-w-sm flex flex-col gap-4"> <h1 class="text-2xl font-bold text-center mb-2">Admin Panel Girişi</h1> ${error && renderTemplate`<div class="text-red-600 text-sm text-center">${error}</div>`} <input name="username" type="text" placeholder="Kullanıcı Adı" class="border rounded px-3 py-2" required> <input name="password" type="password" placeholder="Şifre" class="border rounded px-3 py-2" required> <button type="submit" class="bg-gradient-to-r from-blue-500 to-pink-500 text-white font-bold py-2 rounded hover:from-pink-500 hover:to-blue-500 transition-all">Giriş Yap</button> </form> </body></html>`;
}, "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/admin/index.astro", void 0);

const $$file = "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/admin/index.astro";
const $$url = "/admin";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  default: $$Index,
  file: $$file,
  url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
