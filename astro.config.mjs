import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
export default defineConfig({
  integrations: [tailwind()],
  site: 'https://yourdomain.com', // Replace with your site's URL
  build: {
    outDir: 'dist',
  },
  markdown: {
    shikiConfig: {
      theme: 'nord',
    },
  },
});