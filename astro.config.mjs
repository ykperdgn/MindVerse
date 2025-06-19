import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import vercel from '@astrojs/vercel';

// https://astro.build/config
export default defineConfig({
  integrations: [tailwind()],
  site: 'https://www.mindversedaily.com', // Updated to correct domain
  build: {
    outDir: 'dist',
    inlineStylesheets: 'auto',
  },
  vite: {
    build: {
      cssMinify: true,
      minify: true,
    },
  },
  markdown: {
    shikiConfig: {
      theme: 'nord',
    },
  },
  compressHTML: true,
  output: 'server',
  adapter: vercel(),
});