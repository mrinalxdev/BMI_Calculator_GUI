/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'custom-green' : '#16FF00',
        'custom-blue' : '#0F6292',
        'custom-yellow' : '#FFED00'
      }
    },
  },
  plugins: [],
}
