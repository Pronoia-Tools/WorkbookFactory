<template>
  <login />
</template>

<script>
import Login from '../components/auth/Login.vue'

export default {
  components: {
    login: Login,
  },
  layout: 'login',
}
</script>
