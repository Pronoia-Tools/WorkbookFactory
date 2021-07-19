<template>
  <c-flex direction="row" w="100%" h="95vh">
    <c-box w="20%">
      <side-bar>
        <editor-sidebar />
      </side-bar>
    </c-box>
    <c-box w="80%" overflow="hidden">
      <c-box mx="4" my="5" py="5" background-color="#fff">
        <c-box px="2rem">
          <c-box mt="20px" display="flex" justify-content="flex-end">
            <c-input-group>
              <c-input-left-element>
                <c-icon name="searchIcon" color="gray.300" />
              </c-input-left-element>
              <c-input type="text" placeholder="Search" />
            </c-input-group>
          </c-box>
          <c-box min-height="300px" mt="20px" width="100%">
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
                  <c-box as="th" width="3%"> # </c-box>
                  <c-box as="th" width="15%">Title</c-box>
                  <c-box as="th" width="10%">Published</c-box>
                  <c-box as="th" width="10%">Edition</c-box>
                  <c-box as="th" width="10%">Language</c-box>
                  <c-box as="th" width="10%">Price</c-box>
                  <c-box as="th" width="10%">Status</c-box>
                  <c-box as="th" width="10%"></c-box>
                </c-box>
              </c-box>
              <c-box
                v-if="workbooks.length > 0"
                as="tbody"
                py="4"
                font-size="sm"
              >
                <c-box v-for="workbook in workbooks" :key="workbook.id" as="tr">
                  <c-box as="td">{{ workbook.id }}</c-box>
                  <c-box as="td">{{ workbook.title }}</c-box>
                  <c-box as="td">{{ workbook.published || '---' }}</c-box>
                  <c-box as="td"></c-box>
                  <c-box as="td"></c-box>
                  <c-box as="td"></c-box>
                  <c-box as="td">
                    <span v-if="workbook.published">
                      Published to marketplace
                    </span>
                    <span v-else-if="!workbook.published && workbook.editable">
                      Uneditable
                    </span>
                    <span v-else> Daft </span>
                  </c-box>
                  <c-box as="td">
                    <nuxt-link :to="`/author/workbooks/${workbook.id}`">
                      <c-icon-button
                        variant="outline"
                        variant-color="vue"
                        icon="eyeIcon"
                        aria-label="Detail"
                      />
                    </nuxt-link>
                    <c-button-group :spacing="1">
                      <c-icon-button
                        variant="outline"
                        variant-color="vue"
                        icon="editIcon"
                        aria-label="Edit"
                      />
                    </c-button-group>
                  </c-box>
                </c-box>
              </c-box>
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
      workbooks: [],
    }
  },
  async fetch() {
    this.workbooks = await this.$axios.$get('api/v1/workbooks')
  },
}
</script>
