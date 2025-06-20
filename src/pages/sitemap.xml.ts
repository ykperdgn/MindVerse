import { getCollection } from 'astro:content';

// Tüm kategorileri al
const categories = ['health', 'love', 'history', 'psychology', 'space', 'quotes'];
const allPosts = [];

for (const category of categories) {
  const posts = await getCollection(category);
  allPosts.push(...posts.map(post => ({
    url: `/${category}/${post.slug}`,
    category,
    lastmod: post.data.date,
    changefreq: 'weekly',
    priority: '0.8'
  })));
}

// Statik sayfalar
const staticPages = [
  { url: '/', lastmod: new Date().toISOString().split('T')[0], changefreq: 'daily', priority: '1.0' },
  { url: '/popular', lastmod: new Date().toISOString().split('T')[0], changefreq: 'daily', priority: '0.9' },
  { url: '/categories', lastmod: new Date().toISOString().split('T')[0], changefreq: 'weekly', priority: '0.8' },
  { url: '/health', lastmod: new Date().toISOString().split('T')[0], changefreq: 'daily', priority: '0.9' },
  { url: '/love', lastmod: new Date().toISOString().split('T')[0], changefreq: 'daily', priority: '0.9' },
  { url: '/history', lastmod: new Date().toISOString().split('T')[0], changefreq: 'daily', priority: '0.9' },
  { url: '/psychology', lastmod: new Date().toISOString().split('T')[0], changefreq: 'daily', priority: '0.9' },
  { url: '/space', lastmod: new Date().toISOString().split('T')[0], changefreq: 'daily', priority: '0.9' },
  { url: '/quotes', lastmod: new Date().toISOString().split('T')[0], changefreq: 'daily', priority: '0.9' },
];

const siteUrl = 'https://www.mindversedaily.com';
const allUrls = [...staticPages, ...allPosts];

// XML sitemap içeriği
const xmlContent = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${allUrls.map(page => `  <url>
    <loc>${siteUrl}${page.url}</loc>
    <lastmod>${page.lastmod}</lastmod>
    <changefreq>${page.changefreq}</changefreq>
    <priority>${page.priority}</priority>
  </url>`).join('\n')}
</urlset>`;

export async function GET() {
  return new Response(xmlContent, {
    headers: {
      'Content-Type': 'application/xml',
      'Cache-Control': 'public, max-age=3600'
    }
  });
}
