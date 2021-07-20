<template>
  <c-flex direction="row" w="100%" min-h="95vh">
    <c-box w="20%">
      <side-bar> </side-bar>
    </c-box>
    <c-box w="80%">
      <c-box mx="4" my="5" py="5" background-color="#fff">
        <c-box px="2rem">
          <c-box>
            <c-heading as="h2" size="md"> eWorkbook Information </c-heading>
          </c-box>

          <c-box py="10">
            <c-grid template-columns="repeat(3, 1fr)" gap="6">
              <c-grid-item col-span="1" bg="blue.300" />
              <c-grid-item col-span="2">
                <c-stack :spacing="5">
                  <c-form-control display="flex" align-items="center">
                    <c-form-label width="100px" font-size="sm"
                      >Title</c-form-label
                    >
                    <c-input
                      flex="1"
                      type="text"
                      size="sm"
                      :value="workbook.title"
                    />
                  </c-form-control>

                  <c-form-control display="flex" align-items="center">
                    <c-form-label width="100px" font-size="sm">By</c-form-label>
                    <c-input flex="1" type="text" size="sm" />
                  </c-form-control>

                  <c-form-control display="flex" align-items="center">
                    <c-box display="flex" w="50%">
                      <c-form-label width="100px" font-size="sm">
                        Edition
                      </c-form-label>
                      <c-input flex="1" type="text" size="sm" />
                    </c-box>
                    <c-box display="flex" w="50%">
                      <c-form-label width="100px" font-size="sm" px="2">
                        Languge
                      </c-form-label>
                      <c-input flex="1" type="text" size="sm" />
                    </c-box>
                  </c-form-control>

                  <c-form-control display="flex" align-items="center">
                    <c-box display="flex" w="80%">
                      <c-form-label width="100px" font-size="sm">
                        Price
                      </c-form-label>
                      <c-input flex="1" type="text" size="sm" />
                    </c-box>
                    <c-box display="flex" w="20%" pl="2">
                      <c-select size="sm">
                        <option selected>USD</option>
                      </c-select>
                    </c-box>
                  </c-form-control>

                  <c-form-control display="flex" align-items="center">
                    <c-form-label width="100px" font-size="sm">
                      Categories
                    </c-form-label>
                    <c-input flex="1" type="text" size="sm" />
                  </c-form-control>
                </c-stack>
              </c-grid-item>
            </c-grid>

            <c-box mt="4">
              <c-textarea placeholder="Description" text-size="sm">{{
                workbook.front_matter
              }}</c-textarea>
            </c-box>

            <c-box my="10">
              <c-heading as="h2" size="md"> For Coaches </c-heading>
              <c-flex my="5">
                <c-box w="50%" px="2">
                  <c-heading as="h4" size="sm">
                    Send a copy to a client
                  </c-heading>
                  <c-flex direction="column">
                    <c-checkbox my="2" default-is-checked size="sm">
                      Create custom Client Workbook
                    </c-checkbox>
                    <c-checkbox my="2" size="sm">
                      Client Pays for Workbook
                    </c-checkbox>
                    <c-form-control display="flex" align-items="center">
                      <c-input flex="1" type="text" size="sm" />
                    </c-form-control>
                    <c-button mt="10" variant-color="blue" size="sm">
                      Send invation
                    </c-button>
                  </c-flex>
                </c-box>

                <c-box w="50%" px="2">
                  <c-heading as="h4" size="sm">
                    Send a copy to a client
                  </c-heading>
                  <c-flex direction="column">
                    <c-checkbox my="2" default-is-checked size="sm">
                      eWorkbook is available for purchase by clients leaving the
                      practice
                    </c-checkbox>
                    <c-text font-size="sm"
                      >Active Clients Using this eWorkbook</c-text
                    >
                    <c-box mt="20px" width="100%">
                      <c-box as="table" width="100%">
                        <c-box as="thead">
                          <c-box
                            as="tr"
                            color="#B5B5C3 !important"
                            background-color="#F3F6F9"
                            letter-spacing="1px"
                            px="5px"
                            font-size="0.8rem"
                            text-transform="uppercase"
                            font-weight="600"
                            text-align="left"
                          >
                            <c-box as="th" width="10%">Name</c-box>
                            <c-box as="th" width="10%">Email</c-box>
                            <c-box as="th" width="10%">Answers</c-box>
                          </c-box>
                        </c-box>
                        <c-box as="tbody" py="4" font-size="sm">
                          <c-box as="tr">
                            <c-box as="td">Fish Fisherman</c-box>
                            <c-box as="td">fish@fish.com</c-box>
                            <c-box as="td"></c-box>
                          </c-box>
                        </c-box>
                      </c-box>
                    </c-box>
                  </c-flex>
                </c-box>
              </c-flex>
            </c-box>
          </c-box>
        </c-box>
      </c-box>
    </c-box>
  </c-flex>
</template>

<script>
import SideBar from '@/components/SideBar.vue'
export default {
  components: {
    'side-bar': SideBar,
  },
  data() {
    return {
      workbook: {},
    }
  },
  async fetch() {
    const id = this.$route.params.id
    this.workbook = await this.$axios.$get(`api/v1/workbooks/${id}`)
  },
}
</script>
