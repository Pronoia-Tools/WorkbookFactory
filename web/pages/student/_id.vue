<template>
  <student-details :student-data="item" />
</template>

<script>
export default {
  layout: 'layout',
  data() {
    return {
      showStudentList: false,
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
