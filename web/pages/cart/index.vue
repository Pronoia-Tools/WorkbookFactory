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

        <c-breadcrumb-item is-current-page>
          <c-breadcrumb-link href="#">Cart</c-breadcrumb-link>
        </c-breadcrumb-item>
      </c-breadcrumb>
    </c-box>
    <c-box my="5">
      <c-heading as="h1" size="lg"> Cart </c-heading>

      <c-flex flex-direction="row" my="10">
        <c-flex py="5" pr="4" w="70%">
          <c-box w="100%">
            <c-flex
              align-items="center"
              border="1px"
              p="5"
              w="100%"
              background-color="white"
            >
              <c-box>
                <c-image
                  size="100px"
                  src="https://bit.ly/chakra-naruto-uzumaki"
                  alt="Jonathan Bakebwa"
                />
              </c-box>
              <c-box mx="5" flex="1">
                <c-text font-weight="bold">The desire map </c-text>
                <c-text font-size="xs" color="#b5b4a1eb">by blabla </c-text>
              </c-box>
              <c-box mx="5" w="30px">
                <c-text font-size="md" color="#b5b4a1eb">30$ </c-text>
              </c-box>

              <c-box mx="5" w="100px">
                <c-text font-size="md" color="#b5b4a1eb">Remove</c-text>
              </c-box>
            </c-flex>
          </c-box>
        </c-flex>
        <c-flex py="5" px="4" w="30%">
          <c-flex
            p="5"
            w="100%"
            background-color="white"
            border="1px"
            direction="column"
          >
            <c-heading as="h3" size="md"> Order summary </c-heading>
            <c-flex w="100%" direction="column">
              <c-flex my="4" justify-content="space-between">
                <c-text font-size="md" font-weight="bold">Subtotal: </c-text>
                <c-text font-size="md" color="#b5b4a1eb">30$ </c-text>
              </c-flex>
              <c-flex my="4" justify-content="space-between">
                <c-text font-size="md" font-weight="bold">Shipping: </c-text>
                <c-text font-size="md" color="#b5b4a1eb">30$ </c-text>
              </c-flex>
              <hr />
              <c-flex my="4" justify-content="space-between">
                <c-text font-size="md" font-weight="bold">Total: </c-text>
                <c-text font-size="md" color="#b5b4a1eb">30$ </c-text>
              </c-flex>
              <c-button variant-color="blue" variant="outline">
                Checkout
              </c-button>
            </c-flex>
          </c-flex>
        </c-flex>
      </c-flex>
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
