<template>
  <c-box
    background-color="#fff"
    box-shadow="0 1px 3px 0 rgb(0 0 0 / 10%), 0 1px 2px 0 rgb(0 0 0 / 6%)"
  >
    <c-flex align="center" h="72px" px="15px">
      <c-link w="130px" href="">
        <c-image src="" alt="Image Logo" />
      </c-link>
      <c-box flex="1" as="nav" pl="10">
        <c-box display="flex" as="ul">
          <c-box as="li" px="4">
            <nuxt-link to=""> Your Library </nuxt-link>
          </c-box>
          <c-box as="li" px="4">
            <nuxt-link to="/author/workbooks"> Workbook Factory</nuxt-link>
          </c-box>
          <c-box as="li" px="4">
            <nuxt-link to=""> Coach's Dashboard</nuxt-link>
          </c-box>
          <c-box as="li" px="4">
            <nuxt-link to=""> Marketplace</nuxt-link>
          </c-box>
        </c-box>
      </c-box>

      <c-flex>
        <c-box display="flex" as="ul">
          <c-box as="li" px="2">
            <c-menu>
              <c-menu-button
                _hover="{backgroundColor:transparent }"
                _active="{backgroundColor:transparent}"
                _focus="{outline:none}"
                background-color="transparent"
                outline="none"
                px="4"
                py="2"
              >
                <c-image
                  rounded="full"
                  h="40px"
                  w="40px"
                  src="https://bit.ly/chakra-jonathan-bakebwa"
                  alt="Đặng Kiên"
                />
                <c-text font-size="sm" ml="2">Đặng Kiên</c-text>
                <c-icon name="chevron-down" />
              </c-menu-button>
              <c-menu-list>
                <c-menu-divider />
                <c-menu-item>
                  <c-box cursor="pointer" @click="logout()">
                    <span>Logout</span>
                  </c-box>
                </c-menu-item>
              </c-menu-list>
            </c-menu>
          </c-box>
        </c-box>
      </c-flex>
    </c-flex>
  </c-box>
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
