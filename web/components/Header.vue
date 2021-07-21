<template>
  <c-box box-shadow="0 1px 3px 0 rgb(0 0 0 / 10%), 0 1px 2px 0 rgb(0 0 0 / 6%)">
    <c-flex
      class="justify-between"
      align="center"
      h="60px"
      px="15px"
      background-color="white"
    >
      <c-box w="40px" h="40px">
        <nuxt-link to="/">
          <c-image :src="require('@/static/Sammy.svg')" alt="Image Logo" />
        </nuxt-link>
      </c-box>

      <c-box flex="1" as="nav" pl="10" class="hidden md:flex">
        <navigator />
      </c-box>

      <c-flex>
        <c-box>
          <c-box class="block md:hidden">
            <c-button
              _hover="{backgroundColor:transparent }"
              _active="{backgroundColor:transparent}"
              _focus="{outline:none}"
              background-color="transparent"
              outline="none"
              p="2"
              @click="showNavigator"
            >
              <c-icon name="menuIcon" />
            </c-button>
          </c-box>
        </c-box>
        <c-box as="ul" class="flex">
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
                  h="30px"
                  w="30px"
                  src="https://bit.ly/chakra-jonathan-bakebwa"
                  alt="Đặng Kiên"
                />
                <c-text class="hidden lg:block" font-size="sm" ml="2">
                  Đặng Kiên
                </c-text>
                <c-icon name="chevron-down" />
              </c-menu-button>
              <c-menu-list>
                <c-menu-divider />
                <c-menu-item cursor="pointer" @click="logout()">
                  <span>Logout</span>
                </c-menu-item>
              </c-menu-list>
            </c-menu>
          </c-box>
        </c-box>
      </c-flex>
      <c-box
        v-show="isShowNavigator"
        class="fixed top-0 left-0 h-full w-full z-10"
      >
        <c-box
          class="bg-black h-full w-full opacity-20"
          @click="hideNavigator"
        ></c-box>
        <c-box
          box-shadow="0 1px 9px -3px rgb(0 0 0 / 75%)"
          class="
            absolute
            left-0
            top-0
            flex-col
            bg-white
            h-full
            w-3/4
            z-20
            lg:w-auto lg:h-auto lg:bg-transparent
          "
        >
          <navigator />
        </c-box>
      </c-box>
    </c-flex>
  </c-box>
</template>

<script>
import { mapActions } from 'vuex'
import Navigator from '@/components/Headers/Navigator.vue'

export default {
  components: {
    navigator: Navigator,
  },
  data() {
    return {
      isShowNavigator: false,
    }
  },
  methods: {
    ...mapActions('auth', {
      actionLogout: 'logout',
    }),
    logout() {
      this.actionLogout()
      this.$router.go('/login')
    },
    showNavigator() {
      this.isShowNavigator = true
    },
    hideNavigator() {
      this.isShowNavigator = false
    },
  },
}
</script>

<style scoped>
div > li {
  @apply px-8 py-2;
}
</style>
