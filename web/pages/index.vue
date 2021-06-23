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
      <side-bar />
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
      content: `<p>
          This is still the text editor you’re used to, but enriched with node views.
        </p>
        <vue-component>
          <p>This is editable.</p>
        </vue-component>
        <p>
          Did you see that? That’s a Vue component. We are really living in the future.
      </p>`,
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
