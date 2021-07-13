<template>
  <c-flex direction="row" w="100%" h="95vh">
    <c-box w="20%">
      <side-bar>
        <students-sidebar />
      </side-bar>
    </c-box>
    <c-box w="80%" px="10" py="10">
      <student-details :student-data="item" />
    </c-box>
  </c-flex>
</template>

<script>
import StudentsSidebar from '../../components/SideBar/StudentsSidebar.vue'

export default {
  components: {
    'students-sidebar': StudentsSidebar,
  },
  data() {
    return {
      item: {
        name: 'mrAky',
        birth: '06/02/2020',
        email: 'mraky09@gmail.com',
        address: '96B Dinh Cong, Hoang Mai',
        genre: 'Male',
      },
    }
  },
}
</script>
