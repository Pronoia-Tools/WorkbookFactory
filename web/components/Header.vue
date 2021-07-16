<template>
  <c-list
    w="100%"
    h="5vh"
    border-bottom="1px"
    border-color="gray.100"
    box-shadow="0 4px 12px 0 rgba(0, 0, 0, 0.05)"
    py="auto"
  >
    <c-flex h="100%" direction="row" align="center" justify="space-between">
      <c-flex align="center">
        <c-list-item>
          <nuxt-link to="/" class="nav-link">
            <img
              src="../static/Sammy.svg"
              alt="logo-icon"
              srcset="../static/Sammy.svg"
              class="w-10 h-10"
            />
          </nuxt-link>
        </c-list-item>
        <c-list-item>
          <nuxt-link to="/" class="nav-link">Editor</nuxt-link>
        </c-list-item>
        <c-list-item>
          <nuxt-link to="/clients" class="nav-link">Clients</nuxt-link>
        </c-list-item>
      </c-flex>
      <c-list-item>
        <c-box cursor="pointer" @click="logout()">
          <span>Logout</span>
        </c-box>
      </c-list-item>
    </c-flex>
  </c-list>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  methods: {
    ...mapActions('auth', {
      actionLogout: 'logout',
    }),
    logout() {
      this.actionLogout()
      this.$router.go('/login')
    },
  },
}
</script>

<style scoped>
div > li {
  @apply px-8 py-2;
}
</style>
