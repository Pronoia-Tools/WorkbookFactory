<template font-size="sm">
  <c-box class="container mx-auto" my="10">
    <c-box color="#b5b4a1eb">
      <c-breadcrumb separator="›">
        <c-breadcrumb-item>
          <c-breadcrumb-link href="#">Home</c-breadcrumb-link>
        </c-breadcrumb-item>

        <c-breadcrumb-item>
          <c-breadcrumb-link href="#">The desire map</c-breadcrumb-link>
        </c-breadcrumb-item>
      </c-breadcrumb>
    </c-box>
    <c-box>
      <c-grid template-columns="repeat(2, 1fr)" gap="6" my="10">
        <c-grid-item col-span="1">
          <c-box>
            <c-image
              src="https://bit.ly/chakra-naruto-uzumaki"
              alt="Uzumaki naroto"
            />
          </c-box>
        </c-grid-item>
        <c-grid-item col-span="1">
          <c-heading as="h1" size="lg" text-transform="uppercase">
            THE DESIRE MAP
          </c-heading>
          <c-text mt="1" color="#b5b4a1eb" font-size="sm"
            >By Danielle LaPorte</c-text
          >
          <c-box mt="3">
            <c-box mt="4" color="#b5b4a1eb" font-size="sm">
              <span>Description:</span>
              <span>Loreem</span>
            </c-box>
            <c-box mt="4" color="#b5b4a1eb" font-size="sm">
              <span>Price: </span>
              <span>$30</span>
            </c-box>
          </c-box>
          <c-button
            mt="6"
            size="md"
            height="50px"
            width="250px"
            border="2px"
            border-color="green.500"
          >
            Add to cart
          </c-button>
        </c-grid-item>
      </c-grid>
      <c-box mt="10" font-size="sm">
        <c-heading as="h3" size="lg">About the workbook</c-heading>
        <c-box m="5" border="2px" border-color="#b5b4a1eb">
          <c-grid template-columns="repeat(2, 1fr)" gap="6" py="10">
            <c-grid-item col-span="1" px="3">
              <c-box mt="2">
                <span>Title: </span>
                <span>THE DESIRE MAP</span>
              </c-box>
              <c-box mt="2">
                <span>Author: </span>
                <span>
                  <nuxt-link
                    to="/author/1/profile"
                    class="font-medium text-indigo-600 hover:text-indigo-500"
                  >
                    Author,
                  </nuxt-link>
                  <nuxt-link
                    to="/author/1/profile"
                    class="font-medium text-indigo-600 hover:text-indigo-500"
                  >
                    Author 2,
                  </nuxt-link>
                  <nuxt-link
                    to="/author/1/profile"
                    class="font-medium text-indigo-600 hover:text-indigo-500"
                  >
                    Author 3
                  </nuxt-link>
                </span>
              </c-box>

              <c-box mt="2">
                <span>Categories: </span>
                <span>
                  <nuxt-link
                    to="/author/1/profile"
                    class="font-medium text-indigo-600 hover:text-indigo-500"
                  >
                    Category,
                  </nuxt-link>
                  <nuxt-link
                    to="/author/1/profile"
                    class="font-medium text-indigo-600 hover:text-indigo-500"
                  >
                    Category 2,
                  </nuxt-link>
                  <nuxt-link
                    to="/author/1/profile"
                    class="font-medium text-indigo-600 hover:text-indigo-500"
                  >
                    Category 3
                  </nuxt-link>
                </span>
              </c-box>
            </c-grid-item>
            <c-grid-item col-span="1" px="3">
              <c-box mt="2">
                <span>Language: </span>
                <span>
                  <nuxt-link
                    to="/author/1/profile"
                    class="font-medium text-indigo-600 hover:text-indigo-500"
                  >
                    Language,
                  </nuxt-link>
                  <nuxt-link
                    to="/author/1/profile"
                    class="font-medium text-indigo-600 hover:text-indigo-500"
                  >
                    Language 2,
                  </nuxt-link>
                  <nuxt-link
                    to="/author/1/profile"
                    class="font-medium text-indigo-600 hover:text-indigo-500"
                  >
                    Language 3
                  </nuxt-link>
                </span>
              </c-box>
              <c-box mt="2">
                <span>Edition: </span>
                <span>1 st</span>
              </c-box>
              <c-box mt="2">
                <span>Published: </span>
                <span>11-22-2018</span>
              </c-box>
            </c-grid-item>
          </c-grid>
        </c-box>
      </c-box>
    </c-box>
  </c-box>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      workbooks: [],
    }
  },
  async fetch() {
    this.workbooks = await this.$axios.$get('api/v1/workbooks')
  },
}
</script>
