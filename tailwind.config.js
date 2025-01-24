/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      "./public/index.html",
      "./src/**/*.{js,jsx,ts,tsx}",
      "./src/components/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
        colors: {
            primary: "var(--primary)",
            secondary: "var(--secondary)",
            text: "var(--text)",
            bgPrimary: "var(--bg-primary)",
            bgSecondary: "var(--bg-secondary)",
            header: "var(--header)",
            success: "var(--success)",
            failure: "var(--failure)",
            button: "var(--button)",
        }
    },
  },
  plugins: [],
}

