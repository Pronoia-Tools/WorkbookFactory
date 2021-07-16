<template>
  <CThemeProvider>
    <CReset />
    <Nuxt />
  </CThemeProvider>
</template>

<script>
import { CThemeProvider, CReset } from '@chakra-ui/vue'

export default {
  components: {
    CThemeProvider,
    CReset,
  },
  middleware: 'auth',
}
</script>
