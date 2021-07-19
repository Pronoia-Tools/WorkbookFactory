<template>
  <c-flex direction="row" w="100%" h="95vh">
    <c-box w="20%">
      <side-bar>
        <clients-sidebar />
      </side-bar>
    </c-box>
    <c-box w="80%" px="10" py="10">
      <client-details :client-data="item" />
    </c-box>
  </c-flex>
</template>

<script>
import ClientsSidebar from '../../components/SideBar/ClientsSidebar.vue'
import ClientDetails from '../../components/Clients/ClientDetails.vue'

export default {
  components: {
    'clients-sidebar': ClientsSidebar,
    'client-details': ClientDetails,
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
