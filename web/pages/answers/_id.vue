<template>
  <c-flex direction="row" w="100%" h="95vh">
    <c-box w="20%">
      <side-bar>
        <students-sidebar />
      </side-bar>
    </c-box>
    <c-box w="80%" px="10" py="10">
      <student-answers />
    </c-box>
  </c-flex>
</template>

<script>
import StudentsSidebar from '../../components/SideBar/StudentsSidebar.vue'

export default {
  components: {
    'students-sidebar': StudentsSidebar,
  },
}
</script>
