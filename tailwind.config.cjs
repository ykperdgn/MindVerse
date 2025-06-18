module.exports = {
  content: [
    "./src/**/*.{astro,html,js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
  safelist: [
    // Dinamik renk sınıfları için
    'bg-green-100', 'text-green-800', 'border-green-200', 'bg-green-600', 'hover:bg-green-700',
    'bg-red-100', 'text-red-800', 'border-red-200', 'bg-red-600', 'hover:bg-red-700',
    'bg-yellow-100', 'text-yellow-800', 'border-yellow-200', 'bg-yellow-600', 'hover:bg-yellow-700',
    'bg-purple-100', 'text-purple-800', 'border-purple-200', 'bg-purple-600', 'hover:bg-purple-700',
    'bg-blue-100', 'text-blue-800', 'border-blue-200', 'bg-blue-600', 'hover:bg-blue-700',
    'bg-gray-100', 'text-gray-800', 'border-gray-200', 'bg-gray-600', 'hover:bg-gray-700',
  ],
};