<template>
  <div
    class="
      left-side-bar
      bg-white
      border-r border-gray-400
      h-screen
      w-1/5
      px-2
      pt-24
    "
  >
    <div class="py-8 pl-4 border border-gray-400 mb-10">
      <p>Cover Title</p>
    </div>

    <div
      class="
        flex flex-row
        justify-between
        uppercase
        text-lg
        border-b border-t border-gray-400
        py-2
        mb-5
        pl-4
      "
    >
      <p>new chapter</p>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="25"
        height="25"
        fill="currentColor"
        class="bi bi-plus-square mr-4"
        viewBox="0 0 16 16"
      >
        <path
          d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"
        />
        <path
          d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"
        />
      </svg>
    </div>
    <ul class="flex flex-col">
      <li>Section Title</li>
      <li>Text Area</li>
      <li>Question & Answer box</li>
      <li>Image/Media</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'SideBar',
}
</script>

<style lang="scss" scoped>
.left-side-bar ul > li {
  @apply w-full py-8 pl-4 border border-gray-400 my-2;
}
</style>
