<template>
  <c-flex
    as="ul"
    class="pt-5 lg:p-0 flex flex-col lg:flex-row h-full lg:h-auto"
  >
    <c-box as="li" class="px-8 py-3 lg:px-4 lg:py-0">
      <nuxt-link to=""> Your Library </nuxt-link>
    </c-box>
    <c-box as="li" class="px-8 py-3 lg:px-4 lg:py-0">
      <nuxt-link to="/author/workbooks"> Workbook Factory</nuxt-link>
    </c-box>
    <c-box as="li" class="px-8 py-3 lg:px-4 lg:py-0">
      <nuxt-link to=""> Coach's Dashboard</nuxt-link>
    </c-box>
    <c-box as="li" class="px-8 py-3 lg:px-4 lg:py-0">
      <nuxt-link to="/marketplace"> Marketplace</nuxt-link>
    </c-box>
  </c-flex>
</template>
