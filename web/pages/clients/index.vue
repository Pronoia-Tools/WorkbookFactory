<template>
  <c-flex direction="row" w="100%" h="95vh">
    <c-box w="20%">
      <side-bar>
        <clients-sidebar />
      </side-bar>
    </c-box>
    <c-box w="80%" px="10" py="10">
      <client-listing />
    </c-box>
  </c-flex>
</template>

<script>
import ClientsSidebar from '../../components/SideBar/ClientsSidebar.vue'
import ClientListing from '../../components/Clients/ClientListing.vue'

export default {
  components: {
    'clients-sidebar': ClientsSidebar,
    'client-listing': ClientListing,
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
