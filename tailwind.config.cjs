/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'cusotm-black' : '#3D3B3B3',
        'custom-green' : '#16FF00',
        'custom-green-1': '#30E0A1',
        'custom-green-2': '#E3D35A',
        'custom-blue' : '#0F6292',
        'custom-yellow' : '#FFED00'
      }
    },
  },
  plugins: [],
}
