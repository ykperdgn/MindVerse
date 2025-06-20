#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📄 Pagination & Search System Generator
Creates pagination and search functionality for MindVerse blog
"""

import os
import json
import math
from pathlib import Path
from collections import defaultdict

class PaginationSearchGenerator:
    def __init__(self):
        self.content_dir = Path("src/content")
        self.pages_dir = Path("src/pages")
        self.components_dir = Path("src/components")
        self.articles_per_page = 10

        # Ensure directories exist
        self.pages_dir.mkdir(exist_ok=True)
        self.components_dir.mkdir(exist_ok=True)

    def analyze_content_structure(self):
        """Analyze current content structure"""
        content_stats = {}

        for category_path in self.content_dir.iterdir():
            if category_path.is_dir():
                category = category_path.name
                md_files = list(category_path.glob("*.md"))

                # Separate Turkish and English files
                turkish_files = [f for f in md_files if not f.name.endswith('_en.md')]
                english_files = [f for f in md_files if f.name.endswith('_en.md')]

                content_stats[category] = {
                    'total': len(md_files),
                    'turkish': len(turkish_files),
                    'english': len(english_files),
                    'pages_needed': math.ceil(len(md_files) / self.articles_per_page)
                }

        return content_stats

    def create_search_component(self):
        """Create search component for categories"""
        search_component = '''
import React, { useState, useMemo } from 'react';
import { useRouter } from 'next/router';

interface SearchProps {
  articles: Array<{
    slug: string;
    title: string;
    summary: string;
    tags: string[];
    category: string;
  }>;
  category?: string;
}

export default function SearchComponent({ articles, category }: SearchProps) {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedTag, setSelectedTag] = useState('');
  const router = useRouter();

  // Filter articles based on search term and tag
  const filteredArticles = useMemo(() => {
    return articles.filter(article => {
      const matchesSearch = searchTerm === '' ||
        article.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
        article.summary.toLowerCase().includes(searchTerm.toLowerCase());

      const matchesTag = selectedTag === '' ||
        article.tags.includes(selectedTag);

      return matchesSearch && matchesTag;
    });
  }, [articles, searchTerm, selectedTag]);

  // Get all unique tags
  const allTags = useMemo(() => {
    const tags = new Set();
    articles.forEach(article => {
      article.tags.forEach(tag => tags.add(tag));
    });
    return Array.from(tags).sort();
  }, [articles]);

  return (
    <div className="search-container mb-8">
      <div className="search-controls flex flex-col md:flex-row gap-4 mb-6">
        {/* Search Input */}
        <div className="flex-1">
          <input
            type="text"
            placeholder={category ? `${category} içinde ara...` : "Makalelerde ara..."}
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
        </div>

        {/* Tag Filter */}
        <div className="md:w-48">
          <select
            value={selectedTag}
            onChange={(e) => setSelectedTag(e.target.value)}
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          >
            <option value="">Tüm etiketler</option>
            {allTags.map(tag => (
              <option key={tag} value={tag}>{tag}</option>
            ))}
          </select>
        </div>
      </div>

      {/* Search Results Count */}
      <div className="search-stats mb-4">
        <p className="text-gray-600">
          {filteredArticles.length} makale bulundu
          {searchTerm && ` "${searchTerm}" için`}
          {selectedTag && ` "${selectedTag}" etiketinde`}
        </p>
      </div>

      {/* Search Results */}
      <div className="search-results">
        {filteredArticles.length === 0 ? (
          <div className="no-results text-center py-8">
            <p className="text-gray-500 text-lg">Aradığınız kriterlere uygun makale bulunamadı.</p>
            <p className="text-gray-400 mt-2">Lütfen farklı anahtar kelimeler deneyin.</p>
          </div>
        ) : (
          <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
            {filteredArticles.map(article => (
              <div key={article.slug} className="article-card bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow p-6">
                <h3 className="text-xl font-semibold mb-3 text-gray-800 hover:text-blue-600">
                  <a href={`/${article.category}/${article.slug}`} className="hover:underline">
                    {article.title}
                  </a>
                </h3>
                <p className="text-gray-600 mb-4 line-clamp-3">{article.summary}</p>
                <div className="tags flex flex-wrap gap-2">
                  {article.tags.slice(0, 3).map(tag => (
                    <span key={tag} className="px-2 py-1 bg-blue-100 text-blue-800 text-sm rounded">
                      {tag}
                    </span>
                  ))}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
'''

        search_file = self.components_dir / "SearchComponent.tsx"
        with open(search_file, 'w', encoding='utf-8') as f:
            f.write(search_component)

        return str(search_file)

    def create_pagination_component(self):
        """Create pagination component"""
        pagination_component = '''
import React from 'react';
import Link from 'next/link';

interface PaginationProps {
  currentPage: number;
  totalPages: number;
  baseUrl: string;
  category?: string;
}

export default function Pagination({ currentPage, totalPages, baseUrl, category }: PaginationProps) {
  if (totalPages <= 1) return null;

  const getPageUrl = (page: number) => {
    if (page === 1) {
      return category ? `/${category}` : baseUrl;
    }
    return category ? `/${category}/page/${page}` : `${baseUrl}/page/${page}`;
  };

  const renderPageNumbers = () => {
    const pages = [];
    const maxVisiblePages = 5;

    let startPage = Math.max(1, currentPage - Math.floor(maxVisiblePages / 2));
    let endPage = Math.min(totalPages, startPage + maxVisiblePages - 1);

    // Adjust start page if we're near the end
    if (endPage - startPage < maxVisiblePages - 1) {
      startPage = Math.max(1, endPage - maxVisiblePages + 1);
    }

    // Previous page
    if (currentPage > 1) {
      pages.push(
        <Link key="prev" href={getPageUrl(currentPage - 1)}
              className="px-3 py-2 mx-1 text-gray-500 bg-white border border-gray-300 rounded-md hover:bg-gray-50">
          ‹ Önceki
        </Link>
      );
    }

    // First page
    if (startPage > 1) {
      pages.push(
        <Link key={1} href={getPageUrl(1)}
              className="px-3 py-2 mx-1 text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50">
          1
        </Link>
      );
      if (startPage > 2) {
        pages.push(<span key="dots1" className="px-3 py-2 mx-1 text-gray-500">...</span>);
      }
    }

    // Page numbers
    for (let i = startPage; i <= endPage; i++) {
      pages.push(
        <Link key={i} href={getPageUrl(i)}
              className={`px-3 py-2 mx-1 border rounded-md ${
                i === currentPage
                  ? 'text-white bg-blue-600 border-blue-600'
                  : 'text-gray-700 bg-white border-gray-300 hover:bg-gray-50'
              }`}>
          {i}
        </Link>
      );
    }

    // Last page
    if (endPage < totalPages) {
      if (endPage < totalPages - 1) {
        pages.push(<span key="dots2" className="px-3 py-2 mx-1 text-gray-500">...</span>);
      }
      pages.push(
        <Link key={totalPages} href={getPageUrl(totalPages)}
              className="px-3 py-2 mx-1 text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50">
          {totalPages}
        </Link>
      );
    }

    // Next page
    if (currentPage < totalPages) {
      pages.push(
        <Link key="next" href={getPageUrl(currentPage + 1)}
              className="px-3 py-2 mx-1 text-gray-500 bg-white border border-gray-300 rounded-md hover:bg-gray-50">
          Sonraki ›
        </Link>
      );
    }

    return pages;
  };

  return (
    <div className="pagination flex justify-center items-center mt-12 mb-8">
      <nav className="flex items-center space-x-1">
        {renderPageNumbers()}
      </nav>

      {/* Page info */}
      <div className="ml-8 text-sm text-gray-600">
        Sayfa {currentPage} / {totalPages}
      </div>
    </div>
  );
}
'''

        pagination_file = self.components_dir / "Pagination.tsx"
        with open(pagination_file, 'w', encoding='utf-8') as f:
            f.write(pagination_component)

        return str(pagination_file)

    def run_generation(self):
        """Main method to run pagination and search generation"""
        print("🚀 Starting Pagination & Search System Generation...")

        # Analyze current content
        print("📊 Analyzing content structure...")
        stats = self.analyze_content_structure()

        print("\n📈 Content Statistics:")
        for category, data in stats.items():
            print(f"  {category}: {data['total']} articles ({data['pages_needed']} pages)")

        # Create components
        print("\n🛠️ Creating React components...")
        search_component = self.create_search_component()
        print(f"✅ Created: {search_component}")

        pagination_component = self.create_pagination_component()
        print(f"✅ Created: {pagination_component}")

        print(f"\n✨ Pagination & Search System Generated Successfully!")
        return {
            'stats': stats,
            'components': [search_component, pagination_component],
        }
