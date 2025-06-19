import { g as getCollection } from '../chunks/_astro_content_DACpm5sP.mjs';
export { renderers } from '../renderers.mjs';

const categories = ["health", "love", "history", "psychology", "space", "quotes", "astrology"];
const allPosts = [];
for (const category of categories) {
  const posts = await getCollection(category);
  allPosts.push(...posts.map((post) => ({
    url: `/${category}/${post.slug}`,
    category,
    lastmod: post.data.date,
    changefreq: "weekly",
    priority: "0.8"
  })));
}
const staticPages = [
  { url: "/", lastmod: (/* @__PURE__ */ new Date()).toISOString().split("T")[0], changefreq: "daily", priority: "1.0" },
  { url: "/popular", lastmod: (/* @__PURE__ */ new Date()).toISOString().split("T")[0], changefreq: "daily", priority: "0.9" },
  { url: "/categories", lastmod: (/* @__PURE__ */ new Date()).toISOString().split("T")[0], changefreq: "weekly", priority: "0.8" },
  { url: "/search", lastmod: (/* @__PURE__ */ new Date()).toISOString().split("T")[0], changefreq: "weekly", priority: "0.7" },
  { url: "/health", lastmod: (/* @__PURE__ */ new Date()).toISOString().split("T")[0], changefreq: "daily", priority: "0.9" },
  { url: "/love", lastmod: (/* @__PURE__ */ new Date()).toISOString().split("T")[0], changefreq: "daily", priority: "0.9" },
  { url: "/history", lastmod: (/* @__PURE__ */ new Date()).toISOString().split("T")[0], changefreq: "daily", priority: "0.9" },
  { url: "/psychology", lastmod: (/* @__PURE__ */ new Date()).toISOString().split("T")[0], changefreq: "daily", priority: "0.9" },
  { url: "/space", lastmod: (/* @__PURE__ */ new Date()).toISOString().split("T")[0], changefreq: "daily", priority: "0.9" },
  { url: "/quotes", lastmod: (/* @__PURE__ */ new Date()).toISOString().split("T")[0], changefreq: "daily", priority: "0.9" },
  { url: "/astrology", lastmod: (/* @__PURE__ */ new Date()).toISOString().split("T")[0], changefreq: "daily", priority: "0.9" }
];
const siteUrl = "https://www.mindversedaily.com";
const allUrls = [...staticPages, ...allPosts];
const xmlContent = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${allUrls.map((page) => `  <url>
    <loc>${siteUrl}${page.url}</loc>
    <lastmod>${page.lastmod}</lastmod>
    <changefreq>${page.changefreq}</changefreq>
    <priority>${page.priority}</priority>
  </url>`).join("\n")}
</urlset>`;
async function GET() {
  return new Response(xmlContent, {
    headers: {
      "Content-Type": "application/xml",
      "Cache-Control": "public, max-age=3600"
    }
  });
}

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  GET
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
