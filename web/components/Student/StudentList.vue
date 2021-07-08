<template>
  <div>
    <c-text font-size="30px" mb="5">Student List</c-text>
    <c-box height="300px">
      <Table size="lg">
        <Thead fixed>
          <Tr>
            <Th width="3%">ID</Th>
            <Th width="15%">Name</Th>
            <Th width="10%">Joining Date</Th>
            <Th width="20%">Email</Th>
            <Th width="20%">Address</Th>
            <Th width="20%">Latest Workbook</Th>
            <Th width="5%">Amount</Th>
            <Th width="7%">Action</Th>
          </Tr>
        </Thead>
        <Tbody>
          <Tr v-for="item in paginate" :key="item.id">
            <Td>{{ item.id }}</Td>
            <Td>{{ item.name }}-{{ item.id }}</Td>
            <Td>{{ item.date }}</Td>
            <Td>{{ item.email }}</Td>
            <Td>{{ item.address }}</Td>
            <Td>{{ item.workBook }}</Td>
            <Td>{{ item.amount }}</Td>
            <Td>
              <c-button>
                <router-link to="/student-details" class="nav-link">
                  Details
                </router-link>
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
  data() {
    return {
      items: [
        {
          id: 1,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          date: '06/02/2020',
          address: '96B Dinh Cong, Hoang Mai',
          workBook: 'Yesterday',
          amount: '129',
        },
        {
          id: 2,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          date: '06/02/2020',
          address: '96B Dinh Cong, Hoang Mai',
          workBook: 'Yesterday',
          amount: '129',
        },
        {
          id: 3,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          date: '06/02/2020',
          address: '96B Dinh Cong, Hoang Mai',
          workBook: 'Yesterday',
          amount: '129',
        },
        {
          id: 4,

          name: 'mrAky',
          email: 'mraky09@just.engineer',
          date: '06/02/2020',
          address: '96B Dinh Cong, Hoang Mai',
          workBook: 'Yesterday',
          amount: '129',
        },
        {
          id: 5,

          name: 'mrAky',
          email: 'mraky09@just.engineer',
          date: '06/02/2020',
          address: '96B Dinh Cong, Hoang Mai',
          workBook: 'Yesterday',
          amount: '129',
        },
        {
          id: 6,

          name: 'mrAky',
          email: 'mraky09@just.engineer',
          date: '06/02/2020',
          address: '96B Dinh Cong, Hoang Mai',
          workBook: 'Yesterday',
          amount: '129',
        },
        {
          id: 7,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          date: '06/02/2020',
          address: '96B Dinh Cong, Hoang Mai',
          workBook: 'Yesterday',
          amount: '129',
        },
        {
          id: 8,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          date: '06/02/2020',
          address: '96B Dinh Cong, Hoang Mai',
          workBook: 'Yesterday',
          amount: '129',
        },
        {
          id: 9,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          date: '06/02/2020',
          address: '96B Dinh Cong, Hoang Mai',
          workBook: 'Yesterday',
          amount: '129',
        },
        {
          id: 10,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          date: '06/02/2020',
          address: '96B Dinh Cong, Hoang Mai',
          workBook: 'Yesterday',
          amount: '129',
        },
        {
          id: 11,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          date: '06/02/2020',
          address: '96B Dinh Cong, Hoang Mai',
          workBook: 'Yesterday',
          amount: '129',
        },
        {
          id: 12,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          date: '06/02/2020',
          address: '96B Dinh Cong, Hoang Mai',
          workBook: 'Yesterday',
          amount: '129',
        },
        {
          id: 13,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          date: '06/02/2020',
          address: '96B Dinh Cong, Hoang Mai',
          workBook: 'Yesterday',
          amount: '129',
        },
        {
          id: 14,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          date: '06/02/2020',
          address: '96B Dinh Cong, Hoang Mai',
          workBook: 'Yesterday',
          amount: '129',
        },
        {
          id: 15,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          date: '06/02/2020',
          address: '96B Dinh Cong, Hoang Mai',
          workBook: 'Yesterday',
          amount: '129',
        },
        {
          id: 16,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          date: '06/02/2020',
          address: '96B Dinh Cong, Hoang Mai',
          workBook: 'Yesterday',
          amount: '129',
        },
        {
          id: 17,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          date: '06/02/2020',
          address: '96B Dinh Cong, Hoang Mai',
          workBook: 'Yesterday',
          amount: '129',
        },
        {
          id: 18,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          date: '06/02/2020',
          address: '96B Dinh Cong, Hoang Mai',
          workBook: 'Yesterday',
          amount: '129',
        },
        {
          id: 19,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          date: '06/02/2020',
          address: '96B Dinh Cong, Hoang Mai',
          workBook: 'Yesterday',
          amount: '129',
        },
        {
          id: 20,
          name: 'mrAky',
          email: 'mraky09@just.engineer',
          date: '06/02/2020',
          address: '96B Dinh Cong, Hoang Mai',
          workBook: 'Yesterday',
          amount: '129',
        },
        {
          id: 21,
          name: 'mikey',
          email: 'mraky09@just.engineer',
          date: '06/02/2020',
          address: '96B Dinh Cong, Hoang Mai',
          workBook: 'Yesterday',
          amount: '129',
        },
        {
          id: 22,
          name: 'quiet',
          email: 'mraky09@just.engineer',
          date: '06/02/2020',
          address: '96B Dinh Cong, Hoang Mai',
          workBook: 'Yesterday',
          amount: '129',
        },
      ],
      currentPage: 1,
      itemsPerPage: 3,
      total: 20,
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
table > thead > tr > th {
  padding: 10px 5px;
}

table > tbody > tr > td {
  text-align: center;
  padding: 10px 0;
}

.current {
  color: red;
}

.btn-pagination {
  margin: 5px 5px;
}
</style>
