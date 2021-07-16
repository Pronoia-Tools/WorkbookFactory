<template>
  <c-box mb="5">
    <c-button mt="3" variant-color="blue" @click="show = !show">
      Comment
    </c-button>
    <c-collapse :is-open="show" mt="3">
      <c-textarea placeholder="Here is a sample placeholder" />
    </c-collapse>
  </c-box>
</template>

<script>
export default {
  data() {
    return {
      show: false,
    }
  },
}
</script>
