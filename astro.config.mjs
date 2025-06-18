import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
export default defineConfig({
  integrations: [tailwind()],
  site: 'https://mindverse.vercel.app', // Deploy URL'ini buraya yazabilirsin
  build: {
    outDir: 'dist',
  },
  markdown: {
    shikiConfig: {
      theme: 'nord',
    },
  },
});