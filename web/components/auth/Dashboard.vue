<template>
  <div>
    <h1>Dashboard Page</h1>
    <div>UserName -- {{ gettersAuthData.email }}</div>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  computed: {
    ...mapGetters('auth', {
      gettersAuthData: 'getAuthData',
    }),
  },
}
</script>
