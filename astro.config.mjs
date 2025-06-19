import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
export default defineConfig({
  integrations: [tailwind()],
  site: 'https://www.mindversedaily.com',
  output: 'static',
  build: {
    outDir: 'dist',
  },
  markdown: {
    shikiConfig: {
      theme: 'nord',
    },
  },
});