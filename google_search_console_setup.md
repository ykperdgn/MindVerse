# Google Search Console Setup Guide for MindVerse Daily

## Overview
Setting up Google Search Console for the new domain `www.mindversedaily.com` to monitor search performance and indexing.

## Step-by-Step Setup Instructions

### 1. Access Google Search Console
- Go to [Google Search Console](https://search.google.com/search-console)
- Sign in with your Google account

### 2. Add New Property
- Click "Add Property"
- Select "URL prefix" option
- Enter: `https://www.mindversedaily.com`
- Click "Continue"

### 3. Verify Domain Ownership
Choose one of the verification methods:

#### Option A: HTML File Upload (Recommended)
1. Download the verification HTML file from Google
2. Upload it to the `public/` folder in the project
3. The file should be accessible at: `https://www.mindversedaily.com/[verification-file].html`
4. Click "Verify"

#### Option B: HTML Meta Tag
1. Add the meta tag to the `<head>` section in `src/components/Layout.astro`
2. The verification code will look like: `<meta name="google-site-verification" content="[verification-code]" />`
3. Deploy the site and click "Verify"

#### Option C: DNS Verification
1. Add TXT record to domain DNS settings
2. Wait for DNS propagation
3. Click "Verify"

### 4. Submit Sitemap
After verification:
1. Go to "Sitemaps" in the left sidebar
2. Add sitemap URL: `https://www.mindversedaily.com/sitemap.xml`
3. Click "Submit"

### 5. Check Indexing Status
1. Go to "URL Inspection"
2. Test important pages:
   - Homepage: `https://www.mindversedaily.com`
   - Categories: `https://www.mindversedaily.com/health`
   - Sample articles
3. Request indexing for unindexed pages

## Post-Setup Monitoring

### Weekly Tasks
- [ ] Check "Coverage" report for indexing issues
- [ ] Monitor "Performance" report for search impressions
- [ ] Review "Enhancements" for any technical issues
- [ ] Check "Security & Manual Actions" for warnings

### Monthly Analysis
- [ ] Analyze top-performing queries
- [ ] Identify pages with high impressions but low CTR
- [ ] Monitor Core Web Vitals scores
- [ ] Review internal linking opportunities

## Key Metrics to Track

### Search Performance
- **Impressions**: How often pages appear in search results
- **Clicks**: Actual traffic from search
- **CTR (Click-Through Rate)**: Clicks/Impressions ratio
- **Average Position**: Where pages rank on average

### Coverage Reports
- **Valid pages**: Successfully indexed content
- **Warnings**: Pages with minor issues
- **Errors**: Pages that couldn't be indexed
- **Excluded**: Pages intentionally not indexed

### Core Web Vitals
- **LCP (Largest Contentful Paint)**: Loading performance
- **FID (First Input Delay)**: Interactivity
- **CLS (Cumulative Layout Shift)**: Visual stability

## Expected Timeline

### Week 1
- Setup and verification complete
- Sitemap submitted
- Initial crawling begins

### Week 2-4
- More pages get indexed
- First search performance data appears
- Identify any technical issues

### Month 2-3
- Sufficient data for analysis
- Optimization opportunities identified
- Regular monitoring routine established

## Integration with Current SEO Strategy

### Content Optimization
- Use GSC data to identify high-opportunity keywords
- Optimize pages with high impressions but low CTR
- Create content for queries where you rank 4-10

### Technical SEO
- Fix any crawl errors identified
- Improve Core Web Vitals scores
- Optimize internal linking based on data

### Traffic Growth
- Focus on pages ranking 4-10 for optimization
- Identify seasonal trends in queries
- Monitor competitor ranking changes

## Current Status
- ✅ Domain migration completed: `www.mindversedaily.com`
- ✅ Sitemap.xml available and updated
- ✅ Robots.txt configured properly
- ⏳ Google Search Console setup needed
- ⏳ Submit sitemap to GSC
- ⏳ Monitor indexing progress

## Next Actions
1. **Immediate (Today)**: Set up Google Search Console property
2. **This Week**: Submit sitemap and verify indexing
3. **Ongoing**: Weekly monitoring and monthly analysis
4. **Month 2**: First comprehensive SEO analysis

## Notes
- The site already has proper meta tags and structured data
- All articles have SEO-optimized titles and descriptions
- Social media meta tags are configured for better sharing
- Auto-generated articles include proper frontmatter for SEO

## Verification File Location
If using HTML file verification, place the file in:
```
public/google[verification-code].html
```

This will make it accessible at:
```
https://www.mindversedaily.com/google[verification-code].html
```
