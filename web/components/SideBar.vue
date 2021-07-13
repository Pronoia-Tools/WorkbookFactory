<template>
  <c-flex
    box-shadow="0 4px 12px 0 rgba(0, 0, 0, 0.05)"
    direction="column"
    justify="space-between"
    h="95vh"
    px="4"
    border="1px"
    border-color="gray.100"
  >
    <slot></slot>
  </c-flex>
</template>

<script>
export default {
  name: 'SideBar',
}
</script>
