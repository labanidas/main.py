/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html"],
  theme: {
    extend: {
      colors: {
        chatblack: {50: "#343541"},
        sidebar: {
          50: '#202123',
          20: '#434547'
        },
      }
      
    },
  },
  plugins: [],
}

