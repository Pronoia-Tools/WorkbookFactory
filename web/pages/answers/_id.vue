<template>
  <c-flex direction="row" w="100%" h="95vh">
    <c-box w="20%">
      <side-bar>
        <clients-sidebar />
      </side-bar>
    </c-box>
    <c-box w="80%" px="10" py="10">
      <client-answers />
    </c-box>
  </c-flex>
</template>

<script>
import ClientsSidebar from '../../components/SideBar/ClientsSidebar.vue'
import ClientAnswers from '../../components/Clients/ClientAnswers.vue'

export default {
  components: {
    'clients-sidebar': ClientsSidebar,
    'client-answers': ClientAnswers,
  },
}
</script>
