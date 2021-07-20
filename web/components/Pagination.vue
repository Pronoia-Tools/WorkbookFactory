<template>
  <c-flex justify="space-between" align="center">
    <c-list w="80%">
      <c-flex align="center" justify="center">
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

        <c-list-item v-for="(page, index) in pages" :key="index" pr="4">
          <a href="#" @click.prevent="changePage(page)">
            <c-flex
              :class="{
                'bg-gradient-to-r from-gray-400 to-indigo-400':
                  currentPage === page,
              }"
              justify="center"
              align="center"
              rounded="full"
              transfrom="rotate-45"
              h="6"
              w="6"
            >
              <c-text transfrom="-rotate-45">{{ page }}</c-text>
            </c-flex>
          </a>
        </c-list-item>

        <c-list-item v-if="hasLast()" pr="6">...</c-list-item>

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

    <c-flex v-if="totalPages !== 1" w="20%" justify="flex-end" align="center">
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
      default: 5,
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
      if (this.totalPages === 1) {
        return pages
      }

      for (let i = this.rangeStart; i <= this.rangeEnd; i++) {
        pages.push(i)
      }
      return pages
    },
    rangeStart() {
      if (
        this.currentPage > this.totalPages - this.pageRange &&
        this.totalPages > this.pageRange
      ) {
        return this.totalPages - this.pageRange - 1
      } else {
        return this.currentPage - this.pageRange >= 1 ? this.currentPage - 2 : 1
      }
    },
    rangeEnd() {
      if (
        this.currentPage <= this.pageRange &&
        this.totalPages > this.pageRange
      ) {
        return this.pageRange + 2
      } else {
        return this.currentPage > this.totalPages - this.pageRange
          ? this.totalPages
          : this.currentPage + 2
      }
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
      return this.pages.length !== 0 ? this.rangeStart !== 1 : null
    },
    hasLast() {
      return this.rangeEnd < this.totalPages
    },
    hasPrev() {
      return this.pages.length !== 0 ? this.currentPage >= 1 : null
    },
    hasNext() {
      return this.pages.length !== 0
        ? this.currentPage <= this.totalPages
        : null
    },
    changePage(page) {
      if (page > 0 && page <= this.totalPages) {
        this.$emit('page-changed', page)
      }
    },
  },
}
</script>
