/* empty css                                     */
import { a as createComponent, m as maybeRenderHead, h as renderScript, r as renderTemplate, c as createAstro, e as addAttribute, f as renderComponent } from '../../chunks/astro/server_Dyg-ivk5.mjs';
import 'kleur/colors';
import { $ as $$Layout } from '../../chunks/Layout_BpQYKfR2.mjs';
import 'clsx';
import { g as getCollection } from '../../chunks/_astro_content_DACpm5sP.mjs';
/* empty css                                     */
export { renderers } from '../../renderers.mjs';

const $$CTASection = createComponent(($$result, $$props, $$slots) => {
  return renderTemplate`${maybeRenderHead()}<div class="mt-12 space-y-8"> <!-- Yorum Teşvik Alanı --> <div class="bg-blue-50 border border-blue-200 rounded-xl p-6"> <div class="flex items-center mb-4"> <span class="text-3xl mr-3">💬</span> <h3 class="text-xl font-bold text-blue-800">Sizin Deneyimleriniz Neler?</h3> </div> <p class="text-blue-700 mb-4">
Bu konuda kişisel deneyimlerinizi aşağıdaki yorum bölümünde paylaşır mısınız?
      Hangi yaklaşımlar size en çok fayda sağladı? Başka okuyucular da sizin tecrübelerinizden öğrenebilir!
</p> <a href="#comments-list" class="inline-flex items-center bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors"> <span class="mr-2">👥</span>
Yorumları Görüntüle & Yorum Yap
</a> </div> <!-- İstatistik ve Motivasyon --> <div class="bg-yellow-50 border border-yellow-200 rounded-xl p-6"> <div class="flex items-center justify-between"> <div> <h4 class="font-bold text-yellow-800 mb-2">📊 Bu İçerik Hakkında</h4> <p class="text-yellow-700 text-sm"> <span id="estimated-read-time">~3 dakika</span> okuma süresi •
          Araştırma tabanlı güvenilir içerik
</p> </div> <div class="text-4xl">
🏆
</div> </div> </div> </div> ${renderScript($$result, "C:/Users/Jacob/MindVerse/mindverse_blog/src/components/CTASection.astro?astro&type=script&index=0&lang.ts")}`;
}, "C:/Users/Jacob/MindVerse/mindverse_blog/src/components/CTASection.astro", void 0);

const $$Astro$1 = createAstro("https://www.mindversedaily.com");
const $$RelatedPosts = createComponent(async ($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro$1, $$props, $$slots);
  Astro2.self = $$RelatedPosts;
  const { currentSlug, currentCategory, currentTags, maxResults = 4 } = Astro2.props;
  const allPosts = await getCollection(currentCategory);
  const relatedPosts = allPosts.filter((post) => post.slug !== currentSlug).map((post) => {
    let similarityScore = 0;
    const commonTags = post.data.tags?.filter(
      (tag) => currentTags.includes(tag)
    ).length || 0;
    similarityScore += commonTags * 10;
    const views = post.data.views || 0;
    similarityScore += Math.log(views + 1) * 2;
    const daysDiff = Math.abs(
      new Date(post.data.date).getTime() - (/* @__PURE__ */ new Date()).getTime()
    ) / (1e3 * 60 * 60 * 24);
    if (daysDiff < 30) similarityScore += 5;
    else if (daysDiff < 90) similarityScore += 2;
    return { ...post, similarityScore };
  }).sort((a, b) => b.similarityScore - a.similarityScore).slice(0, maxResults);
  const categoryIcons = {
    health: "\u{1F49A}",
    love: "\u2764\uFE0F",
    history: "\u{1F4DA}",
    psychology: "\u{1F9E0}",
    space: "\u{1F680}",
    quotes: "\u{1F4AD}"
  };
  const categoryColors = {
    health: "green",
    love: "red",
    history: "yellow",
    psychology: "purple",
    space: "blue",
    quotes: "gray"
  };
  return renderTemplate`${relatedPosts.length > 0 && renderTemplate`${maybeRenderHead()}<div class="mt-12 bg-gray-50 rounded-xl p-6" data-astro-cid-dpgbfi7r><div class="flex items-center mb-6" data-astro-cid-dpgbfi7r><span class="text-3xl mr-3" data-astro-cid-dpgbfi7r>🔗</span><h3 class="text-2xl font-bold text-gray-800" data-astro-cid-dpgbfi7r>Benzer İçerikler</h3></div><p class="text-gray-600 mb-6" data-astro-cid-dpgbfi7r>
Bu konuyla ilgili diğer kaliteli içeriklerimizi de keşfedebilirsiniz:
</p><div class="grid grid-cols-1 md:grid-cols-2 gap-4" data-astro-cid-dpgbfi7r>${relatedPosts.map((post) => {
    const categoryColor = categoryColors[currentCategory];
    const categoryIcon = categoryIcons[currentCategory];
    return renderTemplate`<article class="bg-white rounded-lg border border-gray-200 hover:border-gray-300 transition-all duration-200 hover:shadow-md" data-astro-cid-dpgbfi7r><div class="p-4" data-astro-cid-dpgbfi7r><!-- Kategori Badge --><div class="flex items-center justify-between mb-3" data-astro-cid-dpgbfi7r><span${addAttribute(`inline-flex items-center px-2 py-1 rounded-full text-xs font-medium bg-${categoryColor}-100 text-${categoryColor}-800`, "class")} data-astro-cid-dpgbfi7r><span class="mr-1" data-astro-cid-dpgbfi7r>${categoryIcon}</span>${currentCategory.charAt(0).toUpperCase() + currentCategory.slice(1)}</span><!-- Görüntülenme sayısı --><span class="text-xs text-gray-500 flex items-center" data-astro-cid-dpgbfi7r><span class="mr-1" data-astro-cid-dpgbfi7r>👁️</span>${post.data.views?.toLocaleString("tr-TR") || "0"}</span></div><!-- Başlık --><h4 class="font-semibold text-gray-900 mb-2 line-clamp-2 hover:text-blue-600 transition-colors" data-astro-cid-dpgbfi7r><a${addAttribute(`/${currentCategory}/${post.slug}`, "href")} class="hover:underline" data-astro-cid-dpgbfi7r>${post.data.title}</a></h4><!-- Özet --><p class="text-gray-600 text-sm mb-3 line-clamp-2" data-astro-cid-dpgbfi7r>${post.data.summary}</p><!-- Etiketler --><div class="flex flex-wrap gap-1 mb-3" data-astro-cid-dpgbfi7r>${post.data.tags?.slice(0, 3).map((tag) => renderTemplate`<span class="bg-gray-100 text-gray-600 text-xs px-2 py-1 rounded" data-astro-cid-dpgbfi7r>
#${tag}</span>`)}</div><!-- Okuma butonu --><a${addAttribute(`/${currentCategory}/${post.slug}`, "href")} class="inline-flex items-center text-blue-600 hover:text-blue-800 font-medium text-sm transition-colors" data-astro-cid-dpgbfi7r><span class="mr-1" data-astro-cid-dpgbfi7r>📖</span>
Devamını Oku
<span class="ml-1" data-astro-cid-dpgbfi7r>→</span></a></div></article>`;
  })}</div><!-- Daha fazla içerik linki --><div class="mt-6 text-center" data-astro-cid-dpgbfi7r><a${addAttribute(`/${currentCategory}`, "href")} class="inline-flex items-center bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition-colors font-medium" data-astro-cid-dpgbfi7r><span class="mr-2" data-astro-cid-dpgbfi7r>${categoryIcons[currentCategory]}</span>${currentCategory.charAt(0).toUpperCase() + currentCategory.slice(1)} Kategorisindeki Tüm İçerikleri Gör
<span class="ml-2" data-astro-cid-dpgbfi7r>🔍</span></a></div></div>`}${relatedPosts.length === 0 && renderTemplate`<div class="mt-12 bg-blue-50 border border-blue-200 rounded-xl p-6 text-center" data-astro-cid-dpgbfi7r><span class="text-4xl mb-3 block" data-astro-cid-dpgbfi7r>🔍</span><h3 class="text-lg font-semibold text-blue-800 mb-2" data-astro-cid-dpgbfi7r>Daha Fazla İçerik Yakında!</h3><p class="text-blue-700 mb-4" data-astro-cid-dpgbfi7r>
Bu konuda daha fazla içerik üzerinde çalışıyoruz.
      Diğer kategorilerdeki kaliteli yazılarımızı da keşfedebilirsiniz.
</p><a href="/categories" class="inline-flex items-center bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors" data-astro-cid-dpgbfi7r><span class="mr-2" data-astro-cid-dpgbfi7r>📁</span>
Tüm Kategorileri Keşfet
</a></div>`}`;
}, "C:/Users/Jacob/MindVerse/mindverse_blog/src/components/RelatedPosts.astro", void 0);

const $$Astro = createAstro("https://www.mindversedaily.com");
async function getStaticPaths() {
  const categories = ["health", "love", "history", "psychology", "space", "quotes", "astrology"];
  const paths = [];
  for (const category of categories) {
    try {
      const posts = await getCollection(category);
      for (const post of posts) {
        if (post.slug && post.slug.trim() !== "") {
          paths.push({
            params: { category, slug: post.slug },
            props: { post }
          });
        }
      }
    } catch (error) {
      console.warn(`Error loading category ${category}:`, error);
    }
  }
  return paths;
}
const $$slug = createComponent(async ($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro, $$props, $$slots);
  Astro2.self = $$slug;
  const { category, slug } = Astro2.params;
  const { post } = Astro2.props;
  const { Content } = await post.render();
  return renderTemplate`${renderComponent($$result, "Layout", $$Layout, { "title": post.data.title }, { "default": async ($$result2) => renderTemplate` ${maybeRenderHead()}<article class="max-w-4xl mx-auto px-4 py-8"> <!-- Article Header --> <header class="article-header"> <div class="mb-4"> <span class="bg-blue-100 text-blue-800 text-sm font-semibold px-3 py-1 rounded-full capitalize"> ${category} </span> </div> <h1 class="article-title">${post.data.title}</h1> <div class="article-meta"> <span>
📅 ${new Date(post.data.date).toLocaleDateString("tr-TR")} </span> <span>
👁️ ${post.data.views || 0} görüntülenme
</span> <span id="read-time">
⏱️ ~3 dakika okuma
</span> </div> ${post.data.summary && renderTemplate`<p class="text-xl text-gray-600 leading-relaxed mt-4 font-light italic"> ${post.data.summary} </p>`} ${post.data.tags && post.data.tags.length > 0 && renderTemplate`<div class="flex flex-wrap gap-2 mt-4"> ${post.data.tags.map((tag) => renderTemplate`<span class="bg-gray-100 text-gray-700 text-xs px-3 py-1 rounded-full hover:bg-gray-200 transition-colors">
#${tag} </span>`)} </div>`} </header><!-- AdSense reklam alanı --> <div class="flex justify-center mb-8"> <ins class="adsbygoogle" style="display: block" data-ad-client="ca-pub-3096725438789562" data-ad-slot="1234567890" data-ad-format="auto" data-full-width-responsive="true"></ins> </div> <div class="prose prose-lg max-w-none mb-12"> ${renderComponent($$result2, "Content", Content, {})} </div> <!-- CTA Bölümü --> ${renderComponent($$result2, "CTASection", $$CTASection, {})} <!-- Benzer İçerikler --> ${renderComponent($$result2, "RelatedPosts", $$RelatedPosts, { "currentSlug": post.slug, "currentCategory": category, "currentTags": post.data.tags || [], "maxResults": 4 })} <!-- Yorum sistemi --> <div class="border-t pt-8"> <h3 class="text-2xl font-bold mb-6">💬 Yorumlar</h3> <!-- Yorum formu --> <form id="comment-form" class="bg-gray-50 p-6 rounded-lg mb-8"> <div class="grid md:grid-cols-2 gap-4 mb-4"> <input type="text" id="comment-name" placeholder="Adınız" required class="border rounded px-3 py-2"> <input type="email" id="comment-email" placeholder="E-posta (gizli)" required class="border rounded px-3 py-2"> </div> <textarea id="comment-text" placeholder="Yorumunuzu yazın..." required rows="4" class="w-full border rounded px-3 py-2 mb-4"></textarea> <button type="submit" class="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 transition-colors">
Yorum Gönder
</button> </form> <!-- Yorumlar listesi --> <div id="comments-list" class="space-y-4"> <!-- Yorumlar JavaScript ile yüklenecek --> </div> </div> </article> ${renderScript($$result2, "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/[category]/[slug].astro?astro&type=script&index=0&lang.ts")} ` })}`;
}, "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/[category]/[slug].astro", void 0);

const $$file = "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/[category]/[slug].astro";
const $$url = "/[category]/[slug]";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  default: $$slug,
  file: $$file,
  getStaticPaths,
  url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
