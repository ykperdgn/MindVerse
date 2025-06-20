// @ts-ignore
import { getCollection } from 'astro:content';

const categories = ['health', 'love', 'history', 'psychology', 'space', 'quotes'];

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

export async function GET() {
  const allPosts: Array<{ url: string; category: string; lastmod: string; changefreq: string; priority: string }> = [];
  for (const category of categories) {
    // @ts-ignore
    const posts = await getCollection(category);
    allPosts.push(...(posts as any[]).map((post: any) => ({
      url: `/${category}/${post.slug}`,
      category,
      lastmod: post.data.date,
      changefreq: 'weekly',
      priority: '0.8'
    })));
  }
  const allUrls = [...staticPages, ...allPosts];
  const xmlContent = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${allUrls.map(page => `  <url>\n    <loc>${siteUrl}${page.url}</loc>\n    <lastmod>${page.lastmod}</lastmod>\n    <changefreq>${page.changefreq}</changefreq>\n    <priority>${page.priority}</priority>\n  </url>`).join('\n')}\n</urlset>`;
  return new Response(xmlContent, {
    headers: {
      'Content-Type': 'application/xml',
      'Cache-Control': 'public, max-age=3600'
    }
  });
}
