<template>
  <c-flex direction="row" w="100%" h="95vh">
    <c-box w="20%">
      <side-bar>
        <editor-sidebar />
      </side-bar>
    </c-box>
    <c-box w="80%" px="10" py="10">
      <editor
        v-model="content"
        class="h-full overflow-y-auto focus:outline-none"
      />
    </c-box>
  </c-flex>
</template>

<script>
import SideBar from '../components/SideBar.vue'
import EditorSidebar from '../components/SideBar/EditorSidebar.vue'

export default {
  components: {
    'side-bar': SideBar,
    'editor-sidebar': EditorSidebar,
  },
  data() {
    return {
      preDefinedComponents: [],
      content: `<toc></toc>
        <h2>1 heading</h2>
        <p>paragraph</p>
        <h3>1.1 heading</h3>
        <p>paragraph</p>
        <h3>1.2 heading</h3>
        <p>paragraph</p>
        <h2>2 heading</h2>
        <p>paragraph</p>
        <h3>2.1 heading</h3>
        <p>paragraph</p>`,
    }
  },
}
</script>
