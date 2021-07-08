<template>
  <div class="container">
    <div class="header fixed w-full bg-white border-b border-gray-400">
      <ul class="flex flex-row items-center">
        <li>
          <img
            src="../static/Sammy.svg"
            alt="logo-icon"
            srcset="../static/Sammy.svg"
            class="w-10 h-10"
          />
        </li>
        <li>
          <router-link to="/" class="nav-link">Home</router-link>
        </li>
        <li>Editor</li>
        <li>
          <router-link to="/students" class="nav-link">Students</router-link>
        </li>
        <li>
          <router-link to="/login" class="nav-link">Login</router-link>
        </li>
        <li @click="logout()">
          <router-link to="/login" class="nav-link">Logout</router-link>
        </li>
      </ul>
      <router-view></router-view>
    </div>
    <div class="content-wrapper flex flex-row w-full">
      <draggable class="list-group w-1/5" :list="preDefinedComponents">
        <side-bar />
      </draggable>
      <div class="h-screen w-4/5 pt-24 px-10">
        <editor v-model="content" class="h-full overflow-y-auto" />
      </div>
    </div>
  </div>
</template>

<script>
import draggable from 'vuedraggable'
import { mapActions } from 'vuex'

export default {
  components: {
    draggable,
  },
  middleware: 'auth',
  data() {
    return {
      preDefinedComponents: [],
      content: `<toc></toc>
        <h2>1 heading</h2>
        <p>paragraph</p>
        <h3>1.1 heading</h3>
        <p>paragraph</p>
        <h3>1.2 heading</h3>
        <p>paragraph</p>
        <h2>2 heading</h2>
        <p>paragraph</p>
        <h3>2.1 heading</h3>
        <p>paragraph</p>`,
    }
  },
  methods: {
    ...mapActions('auth', {
      actionLogout: 'logout',
    }),
    async logout() {
      await this.actionLogout()
    },
  },
}
</script>

<style>
.header ul > li {
  @apply px-8 py-2;
}

.container {
  @apply max-w-none max-h-screen flex flex-row flex-wrap mx-auto;
}
</style>
