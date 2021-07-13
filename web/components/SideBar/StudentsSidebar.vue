<template>
  <c-flex direction="column" w="100%" align="flex-start" as="nav" class="nav">
    <c-flex
      my="10px"
      w="100%"
      border-bottom="1px"
      border-color="gray.200"
      py="8"
      pl="8"
      justify="space-between"
      align="center"
    >
      <c-text font-size="20px" cursor="default">Students</c-text>
      <svg
        aria-hidden="true"
        focusable="false"
        data-prefix="fas"
        data-icon="chevron-down"
        class="svg-inline--fa fa-chevron-down fa-w-14"
        role="img"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 448 512"
        width="15"
        height="15"
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
  </c-flex>
</template>
