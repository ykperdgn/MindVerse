import { defineCollection, z } from 'astro:content';

const blogSchema = z.object({
  title: z.string(),
  date: z.date().transform((date) => date.toISOString().split('T')[0]),
  summary: z.string(),
  tags: z.array(z.string()),
  views: z.number().optional(),
});

// Astroloji için özel schema
const astrologySchema = z.object({
  title: z.string(),
  description: z.string(),
  pubDate: z.date().transform((date) => date.toISOString().split('T')[0]),
  category: z.string(),
  tags: z.array(z.string()),
  heroImage: z.string().optional(),
  keywords: z.string().optional(),
  author: z.string().optional(),
  summary: z.string().optional(),
  views: z.number().optional(),
});

const health = defineCollection({
  type: 'content',
  schema: blogSchema,
});

const love = defineCollection({
  type: 'content',
  schema: blogSchema,
});

const history = defineCollection({
  type: 'content',
  schema: blogSchema,
});

const psychology = defineCollection({
  type: 'content',
  schema: blogSchema,
});

const space = defineCollection({
  type: 'content',
  schema: blogSchema,
});

const quotes = defineCollection({
  type: 'content',
  schema: blogSchema,
});

const astrology = defineCollection({
  type: 'content',
  schema: astrologySchema,
});

export const collections = {
  health,
  love,
  history,
  psychology,
  space,
  quotes,
  astrology,
};
