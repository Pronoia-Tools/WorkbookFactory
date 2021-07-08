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
            ><c-box><strong>Name:&nbsp;</strong>zxc</c-box></c-list-item
          >
          <c-list-item
            ><c-box
              ><strong>Date of Birth:&nbsp;</strong>zxc</c-box
            ></c-list-item
          >
          <c-list-item
            ><c-box><strong>Email:&nbsp;</strong>zxc</c-box>
          </c-list-item>
          <c-list-item
            ><c-box><strong>Address:&nbsp;</strong>zxc</c-box></c-list-item
          >
          <c-list-item
            ><c-box><strong>Genre:&nbsp;</strong>zxc</c-box></c-list-item
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
          <Tr v-for="(item, index) in items" :key="index">
            <Td>{{ index }}</Td>
            <Td>{{ item.name }}</Td>
            <Td>{{ item.date }}</Td>
            <Td>{{ item.progress }}</Td>
            <Td>
              <c-button>
                <router-link to="/answer" class="nav-link">
                  Go to answer
                </router-link>
              </c-button>
            </Td>
          </Tr>
        </Tbody>
      </Table>
    </c-box>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          name: 'Yesterday',
          date: '05/02/2020',
          progress: '30/82',
        },
        {
          name: 'Today',
          date: '05/02/2020',
          progress: '30/82',
        },
        {
          name: 'Tomorow',
          date: '05/02/2020',
          progress: '30/82',
        },
        {
          name: 'Yesterday',
          date: '05/02/2020',
          progress: '30/82',
        },
        {
          name: 'Yesterday',
          date: '05/02/2020',
          progress: '30/82',
        },
        {
          name: 'Yesterday',
          date: '05/02/2020',
          progress: '30/82',
        },
        {
          name: 'Yesterday',
          date: '05/02/2020',
          progress: '30/82',
        },
      ],
    }
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
