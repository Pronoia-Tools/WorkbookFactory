<template>
  <div class="container">
    <editor v-model="content" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      content:
        '<p>A Vue.js wrapper component for tiptap to use <code>v-model</code>.</p>',
    }
  },
}
</script>

<style>
.container {
  @apply max-w-none max-h-screen flex justify-center items-center text-center mx-auto;
}
</style>
