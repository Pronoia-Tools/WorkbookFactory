<template>
  <student-answers />
</template>

<script>
export default {
  layout: 'layout',
  data() {
    return {}
  },
}
</script>

<style scoped>
ul > div > li {
  @apply px-8 py-2;
}

.container {
  @apply max-w-none max-h-screen flex flex-row flex-wrap mx-auto;
}
</style>
