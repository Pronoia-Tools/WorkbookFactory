<template>
  <div class="container">
    <c-list
      w="100%"
      h="5vh"
      border-bottom="1px"
      border-color="gray.400"
      py="auto"
    >
      <c-flex h="100%" direction="row" align="center">
        <c-list-item>
          <img
            src="../static/Sammy.svg"
            alt="logo-icon"
            srcset="../static/Sammy.svg"
            class="w-10 h-10"
          />
        </c-list-item>
        <c-list-item>
          <router-link to="/" class="nav-link">Home</router-link>
        </c-list-item>
        <c-list-item>
          <router-link to="/students" class="nav-link">Students</router-link>
        </c-list-item>
        <c-list-item>
          <router-link to="/login" class="nav-link">Login</router-link>
        </c-list-item>
        <router-view></router-view>
      </c-flex>
    </c-list>

    <c-flex direction="row" w="100%" h="95vh">
      <c-box w="20%" border-right="1px" border-color="gray.400" pt="4">
        <c-flex
          px="8"
          py="4"
          border-top="1px"
          border-bottom="1px"
          border-color="gray.400"
          font-size="20px"
          driection="row"
          justify="space-between"
          align="center"
        >
          <c-text>Students</c-text>
          <svg
            aria-hidden="true"
            focusable="false"
            data-prefix="fas"
            data-icon="chevron-down"
            class="svg-inline--fa fa-chevron-down fa-w-14"
            role="img"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 448 512"
            width="20"
            height="20"
          >
            <path
              fill="currentColor"
              d="M207.029 381.476L12.686 187.132c-9.373-9.373-9.373-24.569 0-33.941l22.667-22.667c9.357-9.357 24.522-9.375 33.901-.04L224 284.505l154.745-154.021c9.379-9.335 24.544-9.317 33.901.04l22.667 22.667c9.373 9.373 9.373 24.569 0 33.941L240.971 381.476c-9.373 9.372-24.569 9.372-33.942 0z"
            ></path>
          </svg>
        </c-flex>
        <c-list>
          <c-list-item px="8" py="4">
            <c-box> Student List </c-box>
          </c-list-item>
        </c-list>
        <!-- <c-collapse :is-open="show">
        </c-collapse> -->
      </c-box>
      <c-box w="80%" px="10" py="10">
        <student-list />
      </c-box>
    </c-flex>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showStudentList: false,
    }
  },
}
</script>

<style scoped>
ul > div > li {
  @apply px-8 py-2;
}

.container {
  @apply max-w-none max-h-screen flex flex-row flex-wrap mx-auto;
}
</style>
