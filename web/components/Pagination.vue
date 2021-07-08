<template>
  <c-flex justify="space-between">
    <c-list>
      <c-flex align="center">
        <c-list-item v-if="hasPrev()" pr="6">
          <a href="#" class="nav-link" @click.prevent="changePage(prevPage)">
            <c-flex
              justify="center"
              align="center"
              :_hover="{ borderColor: 'gray.200', bg: 'gray.200' }"
              transform="rotate-45"
              h="6"
              w="6"
            >
              <c-box transform="-rotate-45">
                <svg
                  class="h-4 w-4"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M15 19l-7-7 7-7"
                  />
                </svg>
              </c-box>
            </c-flex>
          </a>
        </c-list-item>

        <c-list-item v-if="hasFirst()" class="pr-6">
          <a href="#" @click.prevent="changePage(1)">
            <c-flex
              justify="center"
              align="center"
              :_hover="{ bg: 'gray.200' }"
              transfrom="rotate-45"
              h="6"
              w="6"
            >
              <c-text transform="-rotate-45"> 1 </c-text>
            </c-flex>
          </a>
        </c-list-item>

        <c-list-item v-if="hasFirst()" pr="6">...</c-list-item>

        <c-list-item v-for="(page, index) in pages" :key="index" pr="6">
          <a href="#" @click.prevent="changePage(page)">
            <c-flex
              :class="{
                'bg-gradient-to-r from-blue-400 to-indigo-400':
                  currentPage === page,
              }"
              justify="center"
              align="center"
              :_hover="{ bg: 'gray.200' }"
              transfrom="rotate-45"
              h="6"
              w="6"
            >
              <c-text transfrom="-rotate-45">{{ page }}</c-text>
            </c-flex>
          </a>
        </c-list-item>

        <c-list-item v-if="hasLast()" pr="6">">...</c-list-item>

        <c-list-item v-if="hasLast()" pr="6">
          <a href="#" @click.prevent="changePage(totalPages)">
            <c-flex
              justify="center"
              align="center"
              :_hover="{ bg: 'gray.200' }"
              transfrom="rotate-45"
              h="6"
              w="6"
            >
              <c-text transfrom="-rotate-45">{{ totalPages }}</c-text>
            </c-flex>
          </a>
        </c-list-item>

        <c-list-item v-if="hasNext()" class="pr-6">
          <a href="#" @click.prevent="changePage(nextPage)">
            <c-flex
              justify="center"
              align="center"
              :_hover="{ bg: 'gray.200' }"
              transfrom="rotate-45"
              h="6"
              w="6"
            >
              <div transfrom="-rotate-45">
                <svg
                  class="h-4 w-4"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M9 5l7 7-7 7"
                  />
                </svg>
              </div>
            </c-flex>
          </a>
        </c-list-item>
      </c-flex>
    </c-list>

    <c-flex align="center">
      <c-box pr="2">
        <c-text color="gray.400" font-weight="600">
          {{ textBeforeInput }}
        </c-text>
      </c-box>

      <c-box w="16" pr="3">
        <c-input v-model.number="input" type="text" />
      </c-box>

      <c-box @click.prevent="changePage(input)">
        <c-flex align="center">
          <c-text font-weight="600" cursor="pointer">
            {{ textAfterInput }}
          </c-text>
          <svg
            class="h-4 w-4"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M9 5l7 7-7 7"
            />
          </svg>
        </c-flex>
      </c-box>
    </c-flex>
  </c-flex>
</template>

<script>
export default {
  name: 'Pagination',
  props: {
    currentPage: {
      type: Number,
      default: 1,
    },
    total: {
      type: Number,
      default: 0,
    },
    perPage: {
      type: Number,
      default: 9,
    },
    pageRange: {
      type: Number,
      default: 9,
    },
    textBeforeInput: {
      type: String,
      default: 'Go to page',
    },
    textAfterInput: {
      type: String,
      default: 'Go',
    },
  },
  data() {
    return {
      input: '',
    }
  },
  computed: {
    pages() {
      const pages = []

      for (let i = this.rangeStart; i <= this.rangeEnd; i++) {
        pages.push(i)
      }

      return pages
    },
    rangeStart() {
      // const start = this.currentPage - this.pageRange

      return this.currentPage - this.pageRange > 0
        ? this.currentPage - this.pageRange
        : 1
    },
    rangeEnd() {
      // const end = this.currentPage + this.pageRange

      return this.currentPage + this.pageRange < this.totalPages
        ? this.currentPage + this.pageRange
        : this.totalPages
    },
    totalPages() {
      return Math.ceil(this.total / this.perPage)
    },
    nextPage() {
      return this.currentPage + 1
    },
    prevPage() {
      return this.currentPage - 1
    },
  },
  methods: {
    hasFirst() {
      return this.rangeStart !== 1
    },
    hasLast() {
      return this.rangeEnd < this.totalPages
    },
    hasPrev() {
      return this.currentPage > 1
    },
    hasNext() {
      return this.currentPage < this.totalPages
    },
    changePage(page) {
      console.log(
        '🚀 ~ file: Pagination.vue ~ line 236 ~ changePage ~ page',
        page
      )
      if (page > 0 && page <= this.totalPages) {
        this.$emit('page-changed', page)
      }
    },
  },
}
</script>
