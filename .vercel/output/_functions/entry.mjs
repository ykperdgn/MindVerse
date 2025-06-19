import { renderers } from './renderers.mjs';
import { c as createExports } from './chunks/entrypoint_Di5gOWJg.mjs';
import { manifest } from './manifest_GR5eGD-y.mjs';

const serverIslandMap = new Map();;

const _page0 = () => import('./pages/_image.astro.mjs');
const _page1 = () => import('./pages/404.astro.mjs');
const _page2 = () => import('./pages/admin/dashboard.astro.mjs');
const _page3 = () => import('./pages/admin/logout.astro.mjs');
const _page4 = () => import('./pages/admin.astro.mjs');
const _page5 = () => import('./pages/categories.astro.mjs');
const _page6 = () => import('./pages/contact.astro.mjs');
const _page7 = () => import('./pages/faq.astro.mjs');
const _page8 = () => import('./pages/popular.astro.mjs');
const _page9 = () => import('./pages/privacy-policy.astro.mjs');
const _page10 = () => import('./pages/search.astro.mjs');
const _page11 = () => import('./pages/sitemap.astro.mjs');
const _page12 = () => import('./pages/sitemap.xml.astro.mjs');
const _page13 = () => import('./pages/terms.astro.mjs');
const _page14 = () => import('./pages/_category_/_slug_.astro.mjs');
const _page15 = () => import('./pages/_category_.astro.mjs');
const _page16 = () => import('./pages/index.astro.mjs');
const pageMap = new Map([
    ["node_modules/astro/dist/assets/endpoint/generic.js", _page0],
    ["src/pages/404.astro", _page1],
    ["src/pages/admin/dashboard.astro", _page2],
    ["src/pages/admin/logout.astro", _page3],
    ["src/pages/admin/index.astro", _page4],
    ["src/pages/categories.astro", _page5],
    ["src/pages/contact.astro", _page6],
    ["src/pages/faq.astro", _page7],
    ["src/pages/popular.astro", _page8],
    ["src/pages/privacy-policy.astro", _page9],
    ["src/pages/search.astro", _page10],
    ["src/pages/sitemap.astro", _page11],
    ["src/pages/sitemap.xml.ts", _page12],
    ["src/pages/terms.astro", _page13],
    ["src/pages/[category]/[slug].astro", _page14],
    ["src/pages/[category]/index.astro", _page15],
    ["src/pages/index.astro", _page16]
]);

const _manifest = Object.assign(manifest, {
    pageMap,
    serverIslandMap,
    renderers,
    actions: () => import('./_noop-actions.mjs'),
    middleware: () => import('./_noop-middleware.mjs')
});
const _args = {
    "middlewareSecret": "1e625894-f24b-4a15-a66a-71f89c656294",
    "skewProtection": false
};
const _exports = createExports(_manifest, _args);
const __astrojsSsrVirtualEntry = _exports.default;

export { __astrojsSsrVirtualEntry as default, pageMap };
