<template>
  <c-box>
    <c-flex direction="row" mb="60px" align="center">
      <c-box width="40%">
        <img
          src="../../static/default.png"
          src-set="../../static/default.png"
          class="w-80 h-80 bg-cover bg-no-repeat bg-center rounded-full mx-auto"
          alt="avatar"
        />
      </c-box>

      <c-box width="60%" px="10">
        <c-list>
          <c-list-item>
            <c-box> <strong>Name:&nbsp;</strong>{{ clientData.name }} </c-box>
          </c-list-item>
          <c-list-item>
            <c-box>
              <strong>Date of Birth:&nbsp;</strong>{{ clientData.birth }}
            </c-box>
          </c-list-item>
          <c-list-item>
            <c-box> <strong>Email:&nbsp;</strong>{{ clientData.email }} </c-box>
          </c-list-item>
          <c-list-item>
            <c-box>
              <strong>Address:&nbsp;</strong>{{ clientData.address }}
            </c-box>
          </c-list-item>
          <c-list-item>
            <c-box> <strong>Genre:&nbsp;</strong>{{ clientData.genre }} </c-box>
          </c-list-item>
        </c-list>
      </c-box>
    </c-flex>

    <c-flex class="hidden-scrollbar" height="300px" mb="10">
      <c-box as="table" width="100%" border="1px" border-color="gray.200">
        <c-box as="thead">
          <c-box as="tr">
            <c-box as="th" width="10%">ID</c-box>
            <c-box as="th" width="30%">Book's name</c-box>
            <c-box as="th" width="15%">Buy Date</c-box>
            <c-box as="th" width="30%">Progress</c-box>
            <c-box as="th" width="15%">Solution</c-box>
          </c-box>
        </c-box>
        <c-box as="tbody">
          <c-box v-for="item in paginate" :key="item.id" as="tr">
            <c-box as="td">{{ item.id }}</c-box>
            <c-box as="td">{{ item.name }}</c-box>
            <c-box as="td">{{ item.date }}</c-box>
            <c-box as="td">{{ item.progress }}</c-box>
            <c-box as="td">
              <c-button>
                <nuxt-link
                  :to="{
                    name: 'answers-id',
                    params: { id: item.id },
                  }"
                  class="nav-link"
                >
                  Go to answer
                </nuxt-link>
              </c-button>
            </c-box>
          </c-box>
        </c-box>
      </c-box>
    </c-flex>

    <pagination
      :current-page="currentPage"
      :total="items.length"
      :per-page="itemsPerPage"
      text-before-input="Go to page"
      text-after-input="Go"
      @page-changed="currentPage = $event"
    />
  </c-box>
</template>

<script>
export default {
  props: {
    clientData: {
      type: Object,
      default() {},
    },
  },
  data() {
    return {
      items: [
        {
          id: 1,
          name: 'Yesterday',
          date: '05/02/2020',
          progress: '30/82',
        },
        {
          id: 2,
          name: 'Today',
          date: '05/02/2020',
          progress: '30/82',
        },
        {
          id: 3,
          name: 'Tomorow',
          date: '05/02/2020',
          progress: '30/82',
        },
        {
          id: 4,
          name: 'Yesterday',
          date: '05/02/2020',
          progress: '30/82',
        },
        {
          id: 5,
          name: 'Yesterday',
          date: '05/02/2020',
          progress: '30/82',
        },
        {
          id: 6,
          name: 'Yesterday',
          date: '05/02/2020',
          progress: '30/82',
        },
        {
          id: 7,
          name: 'Yesterday',
          date: '05/02/2020',
          progress: '30/82',
        },
      ],
      currentPage: 1,
      itemsPerPage: 1,
    }
  },
  computed: {
    paginate() {
      const index = this.currentPage * this.itemsPerPage - this.itemsPerPage
      return this.items.slice(index, index + this.itemsPerPage)
    },
  },
}
</script>

<style scoped>
ul > li > div {
  padding: 10px 0;
}

.hidden-scrollbar::-webkit-scrollbar {
  display: none;
}

table > thead > tr > th {
  padding: 10px 5px;
}

table > tbody > tr > td {
  text-align: center;
  padding: 10px 0;
}
</style>
