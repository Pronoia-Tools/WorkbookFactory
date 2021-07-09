<template>
  <div>
    <c-flex direction="row" mb="60px">
      <c-box width="40%">
        <c-image
          src="https://st2.depositphotos.com/1104517/11967/v/950/depositphotos_119675554-stock-illustration-male-avatar-profile-picture-vector.jpg"
          size="400px"
          object-fit="cover"
          alt="avatar"
          mx="auto"
        ></c-image>
      </c-box>

      <c-box width="60%" pt="20" px="10">
        <c-list>
          <c-list-item
            ><c-box
              ><strong>Name:&nbsp;</strong>{{ studentData.name }}</c-box
            ></c-list-item
          >
          <c-list-item
            ><c-box
              ><strong>Date of Birth:&nbsp;</strong
              >{{ studentData.birth }}</c-box
            ></c-list-item
          >
          <c-list-item
            ><c-box><strong>Email:&nbsp;</strong>{{ studentData.email }}</c-box>
          </c-list-item>
          <c-list-item
            ><c-box
              ><strong>Address:&nbsp;</strong>{{ studentData.address }}</c-box
            ></c-list-item
          >
          <c-list-item
            ><c-box
              ><strong>Genre:&nbsp;</strong>{{ studentData.genre }}</c-box
            ></c-list-item
          >
        </c-list>
      </c-box>
    </c-flex>

    <c-box
      class="hidden-scrollbar"
      overflow-y="auto"
      max-height="300px"
      width="100%"
    >
      <Table size="lg">
        <Thead fixed>
          <Tr>
            <Th width="10%">ID</Th>
            <Th width="30%">Book's name</Th>
            <Th width="15%">Buy Date</Th>
            <Th width="30%">Progress</Th>
            <Th width="15%">Solution</Th>
          </Tr>
        </Thead>
        <Tbody>
          <Tr v-for="item in paginate" :key="item.id">
            <Td>{{ item.id }}</Td>
            <Td>{{ item.name }}</Td>
            <Td>{{ item.date }}</Td>
            <Td>{{ item.progress }}</Td>
            <Td>
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
            </Td>
          </Tr>
        </Tbody>
      </Table>
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
  props: {
    studentData: {
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
