<template>
  <c-flex direction="column" w="100%" align="center" as="nav" class="nav">
    <draggable>
      <c-flex
        my="10px"
        w="100%"
        border="1px"
        border-color="gray.200"
        border-radius="8px"
        py="8"
        justify="center"
      >
        <c-text cursor="default">Action</c-text>
      </c-flex>
    </draggable>

    <draggable>
      <c-flex
        my="10px"
        w="100%"
        border="1px"
        border-color="gray.200"
        border-radius="8px"
        py="8"
        justify="center"
      >
        <c-text cursor="default">Editor</c-text>
      </c-flex>
    </draggable>

    <draggable>
      <c-flex
        my="10px"
        w="100%"
        border="1px"
        border-color="gray.200"
        border-radius="8px"
        py="8"
        justify="center"
      >
        <c-text ml="{5}" display="flex">Create</c-text>
      </c-flex>
    </draggable>
  </c-flex>
</template>

<script>
import draggable from 'vuedraggable'

export default {
  name: 'EditorSidebar',
  components: {
    draggable,
  },
  data() {
    return {
      navSize: 'large',
    }
  },
}
</script>

<style scoped>
.nav > div {
  width: 100%;
}
</style>
