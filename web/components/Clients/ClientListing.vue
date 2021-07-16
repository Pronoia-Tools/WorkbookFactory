<template>
  <div>
    <c-text font-size="30px" mb="32">Client List</c-text>
    <c-box height="300px">
      <c-box as="table" border="1px" border-color="gray.200" border-radius="5%">
        <c-box as="thead" fixed>
          <c-box as="tr">
            <c-box as="th" width="5%">ID</c-box>
            <c-box as="th" width="15%">Name</c-box>
            <c-box as="th" width="20%">Email</c-box>
            <c-box as="th" width="10%">Start Date</c-box>
            <c-box as="th" width="10%">Last Login</c-box>
            <c-box as="th" width="5%">Outcomes</c-box>
            <c-box as="th" width="15%">Action</c-box>
          </c-box>
        </c-box>
        <c-box as="tbody">
          <c-box v-for="item in paginate" :key="item.id" as="tr">
            <c-box as="td">{{ item.id }}</c-box>
            <c-box as="td">{{ item.name }}-{{ item.id }}</c-box>
            <c-box as="td">{{ item.email }}</c-box>
            <c-box as="td">{{ item.start_date }}</c-box>
            <c-box as="td">{{ item.last_login }}</c-box>
            <c-box as="td">{{ item.outcomes }}</c-box>
            <c-box as="td">
              <c-button>
                <nuxt-link
                  :to="{
                    name: 'clients-id',
                    params: { id: item.id },
                  }"
                  class="nav-link"
                >
                  Details
                </nuxt-link>
              </c-button>
            </c-box>
          </c-box>
        </c-box>
      </c-box>
    </c-box>
    <pagination
      :current-page="currentPage"
      :total="items.length"
      :per-page="itemsPerPage"
      text-before-input="Go to page"
      text-after-input="Go"
      @page-changed="currentPage = $event"
    />
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          id: 1,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          start_date: '06/02/2020',
          last_login: '09/02/2020',
          workBook: 'Yesterday',
          outcomes: '129',
        },
        {
          id: 2,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          start_date: '06/02/2020',
          last_login: '09/02/2020',
          workBook: 'Yesterday',
          outcomes: '129',
        },
        {
          id: 3,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          start_date: '06/02/2020',
          last_login: '09/02/2020',
          workBook: 'Yesterday',
          outcomes: '129',
        },
        {
          id: 4,

          name: 'mrAky',
          email: 'mraky09@just.engineer',
          start_date: '06/02/2020',
          last_login: '09/02/2020',
          workBook: 'Yesterday',
          outcomes: '129',
        },
        {
          id: 5,

          name: 'mrAky',
          email: 'mraky09@just.engineer',
          start_date: '06/02/2020',
          last_login: '09/02/2020',
          workBook: 'Yesterday',
          outcomes: '129',
        },
        {
          id: 6,

          name: 'mrAky',
          email: 'mraky09@just.engineer',
          start_date: '06/02/2020',
          last_login: '09/02/2020',
          workBook: 'Yesterday',
          outcomes: '129',
        },
        {
          id: 7,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          start_date: '06/02/2020',
          last_login: '09/02/2020',
          workBook: 'Yesterday',
          outcomes: '129',
        },
        {
          id: 8,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          start_date: '06/02/2020',
          last_login: '09/02/2020',
          workBook: 'Yesterday',
          outcomes: '129',
        },
        {
          id: 9,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          start_date: '06/02/2020',
          last_login: '09/02/2020',
          workBook: 'Yesterday',
          outcomes: '129',
        },
        {
          id: 10,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          start_date: '06/02/2020',
          last_login: '09/02/2020',
          workBook: 'Yesterday',
          outcomes: '129',
        },
        {
          id: 11,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          start_date: '06/02/2020',
          last_login: '09/02/2020',
          workBook: 'Yesterday',
          outcomes: '129',
        },
        {
          id: 12,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          start_date: '06/02/2020',
          last_login: '09/02/2020',
          workBook: 'Yesterday',
          outcomes: '129',
        },
        {
          id: 13,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          start_date: '06/02/2020',
          last_login: '09/02/2020',
          workBook: 'Yesterday',
          outcomes: '129',
        },
        {
          id: 14,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          start_date: '06/02/2020',
          last_login: '09/02/2020',
          workBook: 'Yesterday',
          outcomes: '129',
        },
        {
          id: 15,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          start_date: '06/02/2020',
          last_login: '09/02/2020',
          workBook: 'Yesterday',
          outcomes: '129',
        },
        {
          id: 16,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          start_date: '06/02/2020',
          last_login: '09/02/2020',
          workBook: 'Yesterday',
          outcomes: '129',
        },
        {
          id: 17,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          start_date: '06/02/2020',
          last_login: '09/02/2020',
          workBook: 'Yesterday',
          outcomes: '129',
        },
        {
          id: 18,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          start_date: '06/02/2020',
          last_login: '09/02/2020',
          workBook: 'Yesterday',
          outcomes: '129',
        },
        {
          id: 19,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          start_date: '06/02/2020',
          last_login: '09/02/2020',
          workBook: 'Yesterday',
          outcomes: '129',
        },
        {
          id: 20,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          start_date: '06/02/2020',
          last_login: '09/02/2020',
          workBook: 'Yesterday',
          outcomes: '129',
        },
      ],
      // items: [],
      currentPage: 1,
      itemsPerPage: 1,
    }
  },
  // async fetch() {
  //   this.items = await this.$axios.$get('/api/v1/workbooks')
  // },
  computed: {
    paginate() {
      if (this.items.length <= this.itemsPerPage) {
        return this.items
      } else {
        const index = this.currentPage * this.itemsPerPage - this.itemsPerPage
        return this.items.slice(index, index + this.itemsPerPage)
      }
    },
  },
}
</script>

<style scoped>
table > thead > tr > th,
td {
  padding: 10px 0;
}

table > tbody > tr > td {
  text-align: center;
}
</style>
