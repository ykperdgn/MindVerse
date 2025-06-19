/* empty css                                     */
import { c as createAstro, a as createComponent } from '../../chunks/astro/server_Dyg-ivk5.mjs';
import 'kleur/colors';
import 'clsx';
export { renderers } from '../../renderers.mjs';

const $$Astro = createAstro("https://www.mindversedaily.com");
const prerender = false;
const $$Logout = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro, $$props, $$slots);
  Astro2.self = $$Logout;
  const { cookies } = Astro2;
  cookies.delete("admin_auth", { path: "/" });
  return Astro2.redirect("/admin");
}, "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/admin/logout.astro", void 0);

const $$file = "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/admin/logout.astro";
const $$url = "/admin/logout";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
	__proto__: null,
	default: $$Logout,
	file: $$file,
	prerender,
	url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
