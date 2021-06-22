<template>
  <div class="container">
    <div class="header fixed w-full bg-white border-b border-gray-400">
      <ul class="flex flex-row items-center">
        <li>
          <img
            src="../static/Sammy.svg"
            alt="logo-icon"
            srcset="../static/Sammy.svg"
            class="w-10 h-10"
          />
        </li>
        <li>Home</li>
        <li>Editor</li>
      </ul>
    </div>
    <div class="content-wrapper flex flex-row w-full">
      <SideBar />
      <div class="h-screen w-4/5 pt-24 px-10">
        <editor v-model="content" class="h-full overflow-y-auto" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      content: `<p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.A Vue.js wrapper component for tiptap to use <code>v-model</code>.</p>`,
    }
  },
}
</script>

<style>
.header ul > li {
  @apply px-8 py-2;
}
.container {
  @apply max-w-none max-h-screen flex flex-row flex-wrap mx-auto;
}
</style>
