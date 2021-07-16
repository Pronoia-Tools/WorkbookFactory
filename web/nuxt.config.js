export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'workbook-factory',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: ['./assets/scss/colors.scss'],

  // You will have to add this new object if it doesn't exist already
  styleResources: {
    scss: ['./assets/scss/*.scss'],
  },

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    { src: '~/plugins/vuex-persist.js', ssr: false },
    { src: '~/plugins/axios.js', ssr: true },
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
    // https://go.nuxtjs.dev/stylelint
    '@nuxtjs/stylelint-module',
    // https://go.nuxtjs.dev/tailwindcss
    '@nuxtjs/tailwindcss',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    'cookie-universal-nuxt',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    '@nuxtjs/style-resources',
    // https://vue.chakra-ui.com/with-nuxt
    '@chakra-ui/nuxt',
    '@nuxtjs/emotion',
  ],
  /**
   * Add extend the plugin options under the `chakra` key.
   **/
  chakra: {
    extendTheme: {
      colors: {
        brand: {
          /* ... */
        },
      },
    },
  },
  publicRuntimeConfig: {
    axios: {
      baseURL: 'https://workbookfactory-api.herokuapp.com',
    },
  },

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    baseURL: 'https://workbookfactory-api.herokuapp.com',
  },

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: 'en',
    },
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {},
}
