<template>
  <c-flex direction="row" w="100%" h="95vh">
    <c-box w="20%">
      <side-bar>
        <students-sidebar />
      </side-bar>
    </c-box>
    <c-box w="80%" px="10" py="10">
      <student-list />
    </c-box>
  </c-flex>
</template>

<script>
import StudentsSidebar from '../components/SideBar/StudentsSidebar.vue'

export default {
  components: {
    'students-sidebar': StudentsSidebar,
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
