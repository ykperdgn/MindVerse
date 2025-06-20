import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import vercel from '@astrojs/vercel';

// https://astro.build/config
export default defineConfig({
  integrations: [tailwind()],
  site: 'https://www.mindversedaily.com',
  base: '/',
  output: 'server',
  adapter: vercel({
    webAnalytics: {
      enabled: true,
    },
    edgeMiddleware: false,
    functionPerRoute: false,
  }),
  markdown: {
    shikiConfig: {
      theme: 'nord',
    },
  },
  build: {
    inlineStylesheets: 'auto',
  },
  compressHTML: false,
  vite: {
    define: {
      __DATE__: `"${new Date().toISOString()}"`,
    },
  },
});