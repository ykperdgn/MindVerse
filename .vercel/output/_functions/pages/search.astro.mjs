/* empty css                                  */
import { a as createComponent, f as renderComponent, r as renderTemplate, g as defineScriptVars, e as addAttribute, m as maybeRenderHead } from '../chunks/astro/server_Dyg-ivk5.mjs';
import 'kleur/colors';
import { $ as $$Layout } from '../chunks/Layout_BpQYKfR2.mjs';
import { g as getCollection } from '../chunks/_astro_content_DACpm5sP.mjs';
/* empty css                                  */
export { renderers } from '../renderers.mjs';

var __freeze = Object.freeze;
var __defProp = Object.defineProperty;
var __template = (cooked, raw) => __freeze(__defProp(cooked, "raw", { value: __freeze(raw || cooked.slice()) }));
var _a;
const $$Search = createComponent(async ($$result, $$props, $$slots) => {
  const categories = ["health", "love", "history", "psychology", "space", "quotes"];
  const allPosts = [];
  for (const category of categories) {
    const posts = await getCollection(category);
    allPosts.push(...posts.map((post) => ({
      ...post,
      category,
      url: `/${category}/${post.slug}`
    })));
  }
  const searchData = allPosts.map((post) => ({
    title: post.data.title,
    summary: post.data.summary,
    content: post.body || "",
    category: post.category,
    tags: post.data.tags || [],
    url: post.url,
    views: post.data.views || 0,
    date: post.data.date
  }));
  return renderTemplate`${renderComponent($$result, "Layout", $$Layout, { "title": "Site \u0130\xE7i Arama - MindVerse", "description": "MindVerse'te arad\u0131\u011F\u0131n\u0131z konularda detayl\u0131 makaleler bulun. Sa\u011Fl\u0131k, a\u015Fk, tarih, psikoloji, uzay ve al\u0131nt\u0131lar kategorilerinde arama yap\u0131n.", "keywords": "arama, makale, sa\u011Fl\u0131k, a\u015Fk, tarih, psikoloji, uzay, al\u0131nt\u0131lar", "data-astro-cid-ipsxrsrh": true }, { "default": async ($$result2) => renderTemplate(_a || (_a = __template([" ", '<div class="container mx-auto px-4 py-8" data-astro-cid-ipsxrsrh> <!-- Arama Ba\u015Fl\u0131\u011F\u0131 --> <div class="text-center mb-8" data-astro-cid-ipsxrsrh> <h1 class="text-4xl font-bold text-gray-900 mb-4" data-astro-cid-ipsxrsrh>\u{1F50D} Site \u0130\xE7i Arama</h1> <p class="text-lg text-gray-600 max-w-2xl mx-auto" data-astro-cid-ipsxrsrh>\nArad\u0131\u011F\u0131n\u0131z konuda detayl\u0131 makaleler bulun. 6 farkl\u0131 kategoride\n', ' makale i\xE7inden arama yapabilirsiniz.\n</p> </div> <!-- Arama Kutusu --> <div class="max-w-4xl mx-auto mb-8" data-astro-cid-ipsxrsrh> <div class="relative" data-astro-cid-ipsxrsrh> <input type="text" id="search-input" placeholder="Arama yapmak istedi\u011Finiz konuyu yaz\u0131n... (\xF6rn: stres y\xF6netimi)" class="w-full px-6 py-4 text-lg border-2 border-gray-300 rounded-xl focus:border-blue-500 focus:outline-none" autocomplete="off" data-astro-cid-ipsxrsrh> <div class="absolute right-4 top-1/2 transform -translate-y-1/2" data-astro-cid-ipsxrsrh> <span class="text-gray-400 text-xl" data-astro-cid-ipsxrsrh>\u{1F50D}</span> </div> </div> <!-- Arama Filtreleri --> <div class="flex flex-wrap gap-3 mt-4 justify-center" data-astro-cid-ipsxrsrh> <button class="filter-btn active" data-category="all" data-astro-cid-ipsxrsrh>\n\u{1F31F} T\xFCm\xFC (', ')\n</button> <button class="filter-btn" data-category="health" data-astro-cid-ipsxrsrh>\n\u{1F49A} Sa\u011Fl\u0131k\n</button> <button class="filter-btn" data-category="love" data-astro-cid-ipsxrsrh>\n\u2764\uFE0F A\u015Fk\n</button> <button class="filter-btn" data-category="history" data-astro-cid-ipsxrsrh>\n\u{1F4DA} Tarih\n</button> <button class="filter-btn" data-category="psychology" data-astro-cid-ipsxrsrh>\n\u{1F9E0} Psikoloji\n</button> <button class="filter-btn" data-category="space" data-astro-cid-ipsxrsrh>\n\u{1F680} Uzay\n</button> <button class="filter-btn" data-category="quotes" data-astro-cid-ipsxrsrh>\n\u{1F4AD} Al\u0131nt\u0131lar\n</button> </div> </div> <!-- Arama Sonu\xE7lar\u0131 --> <div id="search-results" class="max-w-6xl mx-auto" data-astro-cid-ipsxrsrh> <!-- Ba\u015Flang\u0131\xE7ta pop\xFCler makaleler g\xF6ster --> <div id="initial-content" data-astro-cid-ipsxrsrh> <h2 class="text-2xl font-bold text-gray-800 mb-6 text-center" data-astro-cid-ipsxrsrh>\u{1F525} Pop\xFCler Makaleler</h2> <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" data-astro-cid-ipsxrsrh> ', ' </div> </div> <!-- Arama sonu\xE7lar\u0131 (JavaScript ile doldurulacak) --> <div id="search-content" class="hidden" data-astro-cid-ipsxrsrh> <div id="search-header" class="mb-6" data-astro-cid-ipsxrsrh></div> <div id="search-items" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" data-astro-cid-ipsxrsrh></div> <div id="no-results" class="hidden text-center py-12" data-astro-cid-ipsxrsrh> <span class="text-6xl mb-4 block" data-astro-cid-ipsxrsrh>\u{1F50D}</span> <h3 class="text-xl font-semibold text-gray-700 mb-2" data-astro-cid-ipsxrsrh>Sonu\xE7 Bulunamad\u0131</h3> <p class="text-gray-500 mb-4" data-astro-cid-ipsxrsrh>Arad\u0131\u011F\u0131n\u0131z terime uygun makale bulunamad\u0131.</p> <button onclick="clearSearch()" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700" data-astro-cid-ipsxrsrh>\nAramay\u0131 Temizle\n</button> </div> </div> </div> </div> <script>(function(){', `
    let currentFilter = 'all';
    let searchTerm = '';

    // Arama verilerini haz\u0131rla
    const allArticles = searchData;

    // Arama fonksiyonu
    function performSearch(query, category = 'all') {
      if (!query.trim()) {
        showInitialContent();
        return;
      }

      searchTerm = query.toLowerCase();
      currentFilter = category;

      // Kategori filtreleme
      let filteredArticles = category === 'all'
        ? allArticles
        : allArticles.filter(article => article.category === category);

      // Arama skoru hesaplama
      const results = filteredArticles.map(article => {
        let score = 0;
        const searchWords = searchTerm.split(' ').filter(word => word.length > 1);

        searchWords.forEach(word => {
          // Ba\u015Fl\u0131kta ge\xE7erse y\xFCksek skor
          if (article.title.toLowerCase().includes(word)) score += 10;

          // \xD6zette ge\xE7erse orta skor
          if (article.summary.toLowerCase().includes(word)) score += 5;

          // Etiketlerde ge\xE7erse orta skor
          article.tags.forEach(tag => {
            if (tag.toLowerCase().includes(word)) score += 5;
          });

          // \u0130\xE7erikte ge\xE7erse d\xFC\u015F\xFCk skor
          if (article.content.toLowerCase().includes(word)) score += 2;
        });

        return { ...article, score };
      })
      .filter(article => article.score > 0)
      .sort((a, b) => b.score - a.score);

      showSearchResults(results, query, category);
    }

    // Arama sonu\xE7lar\u0131n\u0131 g\xF6ster
    function showSearchResults(results, query, category) {
      document.getElementById('initial-content').classList.add('hidden');
      document.getElementById('search-content').classList.remove('hidden');

      const header = document.getElementById('search-header');
      const items = document.getElementById('search-items');
      const noResults = document.getElementById('no-results');

      if (results.length === 0) {
        header.innerHTML = '';
        items.innerHTML = '';
        noResults.classList.remove('hidden');
        return;
      }

      noResults.classList.add('hidden');

      // Ba\u015Fl\u0131k
      const categoryText = category === 'all' ? 'T\xFCm Kategorilerde' : getCategoryName(category);
      header.innerHTML = \`
        <h2 class="text-2xl font-bold text-gray-800 text-center">
          "\${query}" i\xE7in \${categoryText} \${results.length} sonu\xE7 bulundu
        </h2>
      \`;

      // Sonu\xE7lar
      items.innerHTML = results.map(article => \`
        <article class="bg-white border border-gray-200 rounded-lg hover:shadow-lg transition-shadow p-4">
          <div class="flex items-center mb-3">
            <span class="px-2 py-1 rounded-full text-xs font-medium \${getCategoryClass(article.category)}">
              \${getCategoryIcon(article.category)} \${getCategoryName(article.category)}
            </span>
            <span class="ml-auto text-xs text-gray-500">
              \u{1F441}\uFE0F \${article.views.toLocaleString('tr-TR')}
            </span>
          </div>

          <h3 class="font-semibold text-gray-900 mb-2 line-clamp-2">
            <a href="\${article.url}" class="hover:text-blue-600 transition-colors">
              \${highlightText(article.title, query)}
            </a>
          </h3>

          <p class="text-gray-600 text-sm mb-3 line-clamp-2">
            \${highlightText(article.summary, query)}
          </p>

          <div class="flex flex-wrap gap-1 mb-3">
            \${article.tags.slice(0, 3).map(tag =>
              \`<span class="bg-gray-100 text-gray-600 text-xs px-2 py-1 rounded">#\${tag}</span>\`
            ).join('')}
          </div>

          <a href="\${article.url}" class="inline-flex items-center text-blue-600 hover:text-blue-800 font-medium text-sm">
            \u{1F4D6} Devam\u0131n\u0131 Oku \u2192
          </a>
        </article>
      \`).join('');
    }

    // \u0130lk i\xE7eri\u011Fi g\xF6ster
    function showInitialContent() {
      document.getElementById('search-content').classList.add('hidden');
      document.getElementById('initial-content').classList.remove('hidden');
    }

    // Aramay\u0131 temizle
    function clearSearch() {
      document.getElementById('search-input').value = '';
      showInitialContent();
      updateFilterButtons('all');
    }

    // Metin vurgulama
    function highlightText(text, query) {
      if (!query.trim()) return text;

      const words = query.split(' ').filter(word => word.length > 1);
      let highlightedText = text;

      words.forEach(word => {
        const regex = new RegExp(\`(\${word})\`, 'gi');
        highlightedText = highlightedText.replace(regex, '<mark class="bg-yellow-200">$1</mark>');
      });

      return highlightedText;
    }

    // Kategori helper fonksiyonlar
    function getCategoryName(category) {
      const names = {
        health: 'Sa\u011Fl\u0131k',
        love: 'A\u015Fk',
        history: 'Tarih',
        psychology: 'Psikoloji',
        space: 'Uzay',
        quotes: 'Al\u0131nt\u0131lar'
      };
      return names[category] || category;
    }

    function getCategoryIcon(category) {
      const icons = {
        health: '\u{1F49A}',
        love: '\u2764\uFE0F',
        history: '\u{1F4DA}',
        psychology: '\u{1F9E0}',
        space: '\u{1F680}',
        quotes: '\u{1F4AD}'
      };
      return icons[category] || '\u{1F4C4}';
    }

    function getCategoryClass(category) {
      const classes = {
        health: 'bg-green-100 text-green-800',
        love: 'bg-red-100 text-red-800',
        history: 'bg-yellow-100 text-yellow-800',
        psychology: 'bg-purple-100 text-purple-800',
        space: 'bg-blue-100 text-blue-800',
        quotes: 'bg-gray-100 text-gray-800'
      };
      return classes[category] || 'bg-gray-100 text-gray-800';
    }

    // Filtre butonlar\u0131n\u0131 g\xFCncelle
    function updateFilterButtons(activeCategory) {
      document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.dataset.category === activeCategory) {
          btn.classList.add('active');
        }
      });
    }

    // Event listener'lar
    document.addEventListener('DOMContentLoaded', function() {
      const searchInput = document.getElementById('search-input');

      // Arama input eventi
      searchInput.addEventListener('input', function() {
        const query = this.value;
        if (query.length >= 2 || query.length === 0) {
          performSearch(query, currentFilter);
        }
      });

      // Enter tu\u015Fu
      searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
          performSearch(this.value, currentFilter);
        }
      });

      // Filtre butonlar\u0131
      document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.addEventListener('click', function() {
          const category = this.dataset.category;
          currentFilter = category;
          updateFilterButtons(category);

          const query = searchInput.value;
          if (query.trim()) {
            performSearch(query, category);
          }
        });
      });

      // URL'den arama parametresi al
      const urlParams = new URLSearchParams(window.location.search);
      const searchQuery = urlParams.get('q');
      if (searchQuery) {
        searchInput.value = searchQuery;
        performSearch(searchQuery, 'all');
      }
    });
  })();<\/script>  `], [" ", '<div class="container mx-auto px-4 py-8" data-astro-cid-ipsxrsrh> <!-- Arama Ba\u015Fl\u0131\u011F\u0131 --> <div class="text-center mb-8" data-astro-cid-ipsxrsrh> <h1 class="text-4xl font-bold text-gray-900 mb-4" data-astro-cid-ipsxrsrh>\u{1F50D} Site \u0130\xE7i Arama</h1> <p class="text-lg text-gray-600 max-w-2xl mx-auto" data-astro-cid-ipsxrsrh>\nArad\u0131\u011F\u0131n\u0131z konuda detayl\u0131 makaleler bulun. 6 farkl\u0131 kategoride\n', ' makale i\xE7inden arama yapabilirsiniz.\n</p> </div> <!-- Arama Kutusu --> <div class="max-w-4xl mx-auto mb-8" data-astro-cid-ipsxrsrh> <div class="relative" data-astro-cid-ipsxrsrh> <input type="text" id="search-input" placeholder="Arama yapmak istedi\u011Finiz konuyu yaz\u0131n... (\xF6rn: stres y\xF6netimi)" class="w-full px-6 py-4 text-lg border-2 border-gray-300 rounded-xl focus:border-blue-500 focus:outline-none" autocomplete="off" data-astro-cid-ipsxrsrh> <div class="absolute right-4 top-1/2 transform -translate-y-1/2" data-astro-cid-ipsxrsrh> <span class="text-gray-400 text-xl" data-astro-cid-ipsxrsrh>\u{1F50D}</span> </div> </div> <!-- Arama Filtreleri --> <div class="flex flex-wrap gap-3 mt-4 justify-center" data-astro-cid-ipsxrsrh> <button class="filter-btn active" data-category="all" data-astro-cid-ipsxrsrh>\n\u{1F31F} T\xFCm\xFC (', ')\n</button> <button class="filter-btn" data-category="health" data-astro-cid-ipsxrsrh>\n\u{1F49A} Sa\u011Fl\u0131k\n</button> <button class="filter-btn" data-category="love" data-astro-cid-ipsxrsrh>\n\u2764\uFE0F A\u015Fk\n</button> <button class="filter-btn" data-category="history" data-astro-cid-ipsxrsrh>\n\u{1F4DA} Tarih\n</button> <button class="filter-btn" data-category="psychology" data-astro-cid-ipsxrsrh>\n\u{1F9E0} Psikoloji\n</button> <button class="filter-btn" data-category="space" data-astro-cid-ipsxrsrh>\n\u{1F680} Uzay\n</button> <button class="filter-btn" data-category="quotes" data-astro-cid-ipsxrsrh>\n\u{1F4AD} Al\u0131nt\u0131lar\n</button> </div> </div> <!-- Arama Sonu\xE7lar\u0131 --> <div id="search-results" class="max-w-6xl mx-auto" data-astro-cid-ipsxrsrh> <!-- Ba\u015Flang\u0131\xE7ta pop\xFCler makaleler g\xF6ster --> <div id="initial-content" data-astro-cid-ipsxrsrh> <h2 class="text-2xl font-bold text-gray-800 mb-6 text-center" data-astro-cid-ipsxrsrh>\u{1F525} Pop\xFCler Makaleler</h2> <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" data-astro-cid-ipsxrsrh> ', ' </div> </div> <!-- Arama sonu\xE7lar\u0131 (JavaScript ile doldurulacak) --> <div id="search-content" class="hidden" data-astro-cid-ipsxrsrh> <div id="search-header" class="mb-6" data-astro-cid-ipsxrsrh></div> <div id="search-items" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" data-astro-cid-ipsxrsrh></div> <div id="no-results" class="hidden text-center py-12" data-astro-cid-ipsxrsrh> <span class="text-6xl mb-4 block" data-astro-cid-ipsxrsrh>\u{1F50D}</span> <h3 class="text-xl font-semibold text-gray-700 mb-2" data-astro-cid-ipsxrsrh>Sonu\xE7 Bulunamad\u0131</h3> <p class="text-gray-500 mb-4" data-astro-cid-ipsxrsrh>Arad\u0131\u011F\u0131n\u0131z terime uygun makale bulunamad\u0131.</p> <button onclick="clearSearch()" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700" data-astro-cid-ipsxrsrh>\nAramay\u0131 Temizle\n</button> </div> </div> </div> </div> <script>(function(){', `
    let currentFilter = 'all';
    let searchTerm = '';

    // Arama verilerini haz\u0131rla
    const allArticles = searchData;

    // Arama fonksiyonu
    function performSearch(query, category = 'all') {
      if (!query.trim()) {
        showInitialContent();
        return;
      }

      searchTerm = query.toLowerCase();
      currentFilter = category;

      // Kategori filtreleme
      let filteredArticles = category === 'all'
        ? allArticles
        : allArticles.filter(article => article.category === category);

      // Arama skoru hesaplama
      const results = filteredArticles.map(article => {
        let score = 0;
        const searchWords = searchTerm.split(' ').filter(word => word.length > 1);

        searchWords.forEach(word => {
          // Ba\u015Fl\u0131kta ge\xE7erse y\xFCksek skor
          if (article.title.toLowerCase().includes(word)) score += 10;

          // \xD6zette ge\xE7erse orta skor
          if (article.summary.toLowerCase().includes(word)) score += 5;

          // Etiketlerde ge\xE7erse orta skor
          article.tags.forEach(tag => {
            if (tag.toLowerCase().includes(word)) score += 5;
          });

          // \u0130\xE7erikte ge\xE7erse d\xFC\u015F\xFCk skor
          if (article.content.toLowerCase().includes(word)) score += 2;
        });

        return { ...article, score };
      })
      .filter(article => article.score > 0)
      .sort((a, b) => b.score - a.score);

      showSearchResults(results, query, category);
    }

    // Arama sonu\xE7lar\u0131n\u0131 g\xF6ster
    function showSearchResults(results, query, category) {
      document.getElementById('initial-content').classList.add('hidden');
      document.getElementById('search-content').classList.remove('hidden');

      const header = document.getElementById('search-header');
      const items = document.getElementById('search-items');
      const noResults = document.getElementById('no-results');

      if (results.length === 0) {
        header.innerHTML = '';
        items.innerHTML = '';
        noResults.classList.remove('hidden');
        return;
      }

      noResults.classList.add('hidden');

      // Ba\u015Fl\u0131k
      const categoryText = category === 'all' ? 'T\xFCm Kategorilerde' : getCategoryName(category);
      header.innerHTML = \\\`
        <h2 class="text-2xl font-bold text-gray-800 text-center">
          "\\\${query}" i\xE7in \\\${categoryText} \\\${results.length} sonu\xE7 bulundu
        </h2>
      \\\`;

      // Sonu\xE7lar
      items.innerHTML = results.map(article => \\\`
        <article class="bg-white border border-gray-200 rounded-lg hover:shadow-lg transition-shadow p-4">
          <div class="flex items-center mb-3">
            <span class="px-2 py-1 rounded-full text-xs font-medium \\\${getCategoryClass(article.category)}">
              \\\${getCategoryIcon(article.category)} \\\${getCategoryName(article.category)}
            </span>
            <span class="ml-auto text-xs text-gray-500">
              \u{1F441}\uFE0F \\\${article.views.toLocaleString('tr-TR')}
            </span>
          </div>

          <h3 class="font-semibold text-gray-900 mb-2 line-clamp-2">
            <a href="\\\${article.url}" class="hover:text-blue-600 transition-colors">
              \\\${highlightText(article.title, query)}
            </a>
          </h3>

          <p class="text-gray-600 text-sm mb-3 line-clamp-2">
            \\\${highlightText(article.summary, query)}
          </p>

          <div class="flex flex-wrap gap-1 mb-3">
            \\\${article.tags.slice(0, 3).map(tag =>
              \\\`<span class="bg-gray-100 text-gray-600 text-xs px-2 py-1 rounded">#\\\${tag}</span>\\\`
            ).join('')}
          </div>

          <a href="\\\${article.url}" class="inline-flex items-center text-blue-600 hover:text-blue-800 font-medium text-sm">
            \u{1F4D6} Devam\u0131n\u0131 Oku \u2192
          </a>
        </article>
      \\\`).join('');
    }

    // \u0130lk i\xE7eri\u011Fi g\xF6ster
    function showInitialContent() {
      document.getElementById('search-content').classList.add('hidden');
      document.getElementById('initial-content').classList.remove('hidden');
    }

    // Aramay\u0131 temizle
    function clearSearch() {
      document.getElementById('search-input').value = '';
      showInitialContent();
      updateFilterButtons('all');
    }

    // Metin vurgulama
    function highlightText(text, query) {
      if (!query.trim()) return text;

      const words = query.split(' ').filter(word => word.length > 1);
      let highlightedText = text;

      words.forEach(word => {
        const regex = new RegExp(\\\`(\\\${word})\\\`, 'gi');
        highlightedText = highlightedText.replace(regex, '<mark class="bg-yellow-200">$1</mark>');
      });

      return highlightedText;
    }

    // Kategori helper fonksiyonlar
    function getCategoryName(category) {
      const names = {
        health: 'Sa\u011Fl\u0131k',
        love: 'A\u015Fk',
        history: 'Tarih',
        psychology: 'Psikoloji',
        space: 'Uzay',
        quotes: 'Al\u0131nt\u0131lar'
      };
      return names[category] || category;
    }

    function getCategoryIcon(category) {
      const icons = {
        health: '\u{1F49A}',
        love: '\u2764\uFE0F',
        history: '\u{1F4DA}',
        psychology: '\u{1F9E0}',
        space: '\u{1F680}',
        quotes: '\u{1F4AD}'
      };
      return icons[category] || '\u{1F4C4}';
    }

    function getCategoryClass(category) {
      const classes = {
        health: 'bg-green-100 text-green-800',
        love: 'bg-red-100 text-red-800',
        history: 'bg-yellow-100 text-yellow-800',
        psychology: 'bg-purple-100 text-purple-800',
        space: 'bg-blue-100 text-blue-800',
        quotes: 'bg-gray-100 text-gray-800'
      };
      return classes[category] || 'bg-gray-100 text-gray-800';
    }

    // Filtre butonlar\u0131n\u0131 g\xFCncelle
    function updateFilterButtons(activeCategory) {
      document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.dataset.category === activeCategory) {
          btn.classList.add('active');
        }
      });
    }

    // Event listener'lar
    document.addEventListener('DOMContentLoaded', function() {
      const searchInput = document.getElementById('search-input');

      // Arama input eventi
      searchInput.addEventListener('input', function() {
        const query = this.value;
        if (query.length >= 2 || query.length === 0) {
          performSearch(query, currentFilter);
        }
      });

      // Enter tu\u015Fu
      searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
          performSearch(this.value, currentFilter);
        }
      });

      // Filtre butonlar\u0131
      document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.addEventListener('click', function() {
          const category = this.dataset.category;
          currentFilter = category;
          updateFilterButtons(category);

          const query = searchInput.value;
          if (query.trim()) {
            performSearch(query, category);
          }
        });
      });

      // URL'den arama parametresi al
      const urlParams = new URLSearchParams(window.location.search);
      const searchQuery = urlParams.get('q');
      if (searchQuery) {
        searchInput.value = searchQuery;
        performSearch(searchQuery, 'all');
      }
    });
  })();<\/script>  `])), maybeRenderHead(), allPosts.length, allPosts.length, allPosts.sort((a, b) => (b.data.views || 0) - (a.data.views || 0)).slice(0, 6).map((post) => renderTemplate`<article class="bg-white border border-gray-200 rounded-lg hover:shadow-lg transition-shadow p-4" data-astro-cid-ipsxrsrh> <div class="flex items-center mb-3" data-astro-cid-ipsxrsrh> <span${addAttribute(`px-2 py-1 rounded-full text-xs font-medium ${post.category === "health" ? "bg-green-100 text-green-800" : post.category === "love" ? "bg-red-100 text-red-800" : post.category === "history" ? "bg-yellow-100 text-yellow-800" : post.category === "psychology" ? "bg-purple-100 text-purple-800" : post.category === "space" ? "bg-blue-100 text-blue-800" : "bg-gray-100 text-gray-800"}`, "class")} data-astro-cid-ipsxrsrh> ${post.category === "health" ? "\u{1F49A} Sa\u011Fl\u0131k" : post.category === "love" ? "\u2764\uFE0F A\u015Fk" : post.category === "history" ? "\u{1F4DA} Tarih" : post.category === "psychology" ? "\u{1F9E0} Psikoloji" : post.category === "space" ? "\u{1F680} Uzay" : "\u{1F4AD} Al\u0131nt\u0131lar"} </span> <span class="ml-auto text-xs text-gray-500" data-astro-cid-ipsxrsrh>
👁️ ${(post.data.views || 0).toLocaleString("tr-TR")} </span> </div> <h3 class="font-semibold text-gray-900 mb-2 line-clamp-2" data-astro-cid-ipsxrsrh> <a${addAttribute(post.url, "href")} class="hover:text-blue-600 transition-colors" data-astro-cid-ipsxrsrh> ${post.data.title} </a> </h3> <p class="text-gray-600 text-sm mb-3 line-clamp-2" data-astro-cid-ipsxrsrh> ${post.data.summary} </p> <div class="flex flex-wrap gap-1 mb-3" data-astro-cid-ipsxrsrh> ${post.data.tags?.slice(0, 3).map((tag) => renderTemplate`<span class="bg-gray-100 text-gray-600 text-xs px-2 py-1 rounded" data-astro-cid-ipsxrsrh>
#${tag} </span>`)} </div> <a${addAttribute(post.url, "href")} class="inline-flex items-center text-blue-600 hover:text-blue-800 font-medium text-sm" data-astro-cid-ipsxrsrh>
📖 Devamını Oku →
</a> </article>`), defineScriptVars({ searchData })) })}`;
}, "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/search.astro", void 0);

const $$file = "C:/Users/Jacob/MindVerse/mindverse_blog/src/pages/search.astro";
const $$url = "/search";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  default: $$Search,
  file: $$file,
  url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
