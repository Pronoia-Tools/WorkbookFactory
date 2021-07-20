<template>
  <c-box px="12" py="24">
    <!-- New releases -->
    <c-box mb="12">
      <c-text font-size="20px" mb="3">New releases</c-text>
      <c-box
        border="1px"
        border-color="gray.200"
        box-shadow="0px 0px 1px 1px #E2E8F0"
        p="4"
      >
        <swiper class="swiper" :options="swiperOption">
          <swiper-slide>
            <img src="@/static/default.png" alt="new-release" />
          </swiper-slide>
          <swiper-slide>
            <img src="@/static/default.png" alt="new-release" />
          </swiper-slide>
          <swiper-slide>
            <img src="@/static/default.png" alt="new-release" />
          </swiper-slide>
          <swiper-slide>
            <img src="@/static/default.png" alt="new-release" />
          </swiper-slide>
          <swiper-slide>
            <img src="@/static/default.png" alt="new-release" />
          </swiper-slide>
          <swiper-slide>
            <img src="@/static/default.png" alt="new-release" />
          </swiper-slide>
          <swiper-slide>
            <img src="@/static/default.png" alt="new-release" />
          </swiper-slide>
          <div slot="pagination" class="swiper-pagination"></div>
        </swiper>
      </c-box>
    </c-box>

    <!-- Most popular -->
    <c-box mb="12">
      <c-text font-size="20px" mb="3">Most popular</c-text>
      <c-box
        border="1px"
        border-color="gray.200"
        box-shadow="0px 0px 1px 1px #E2E8F0"
        p="4"
      >
        <swiper class="swiper" :options="swiperOption">
          <swiper-slide>
            <img src="@/static/default.png" alt="new-release" />
          </swiper-slide>
          <swiper-slide>
            <img src="@/static/default.png" alt="new-release" />
          </swiper-slide>
          <swiper-slide>
            <img src="@/static/default.png" alt="new-release" />
          </swiper-slide>
          <swiper-slide>
            <img src="@/static/default.png" alt="new-release" />
          </swiper-slide>
          <swiper-slide>
            <img src="@/static/default.png" alt="new-release" />
          </swiper-slide>
          <swiper-slide>
            <img src="@/static/default.png" alt="new-release" />
          </swiper-slide>
          <swiper-slide>
            <img src="@/static/default.png" alt="new-release" />
          </swiper-slide>
          <div slot="pagination" class="swiper-pagination"></div>
        </swiper>
      </c-box>
    </c-box>

    <!-- All workbooks -->
    <c-box>
      <c-text font-size="20px" mb="3">All workbooks</c-text>
      <c-box
        border="1px"
        border-color="gray.200"
        box-shadow="0px 0px 1px 1px #E2E8F0"
      >
        <c-box p="8" border-bottom="1px" border-color="gray.100">
          <c-flex align="center" mb="6">
            <svg
              id="Capa_1"
              enable-background="new 0 0 512 512"
              height="15"
              width="15"
              viewBox="0 0 512 512"
              xmlns="http://www.w3.org/2000/svg"
            >
              <g>
                <path
                  d="m187.304 252.717c8.045 11.642 5.64 1.941 5.64 233.997 0 20.766 23.692 32.651 40.39 20.23 71.353-53.797 85.609-58.456 85.609-83.619 0-169.104-1.971-159.594 5.64-170.608l115.869-157.718h-369.016z"
                />
                <path
                  d="m484.221 12.86c-4.14-7.93-12.26-12.86-21.199-12.86h-414.156c-19.305 0-30.664 21.777-19.59 37.6.091.152-1.257-1.693 20.12 27.4h413.095c18.217-24.793 30.394-35.505 21.73-52.14z"
                />
              </g>
            </svg>
            <c-text font-size="18px" font-weight="bold" ml="2">Filter</c-text>
          </c-flex>
          <!-- filter form -->
          <c-flex align="center" mb="8">
            <c-box w="33%" px="10">
              <c-input placeholder="Title" mb="3" />
              <c-input placeholder="Author" />
            </c-box>

            <c-box w="33%" px="10">
              <c-select placeholder="Select language" mb="3">
                <option value="grilled">English</option>
                <option value="pub-style">Germany</option>
                <option value="jucy-lucy">Vietnamese</option>
              </c-select>

              <c-select placeholder="Select category">
                <option value="grilled">History</option>
                <option value="pub-style">Conqueor</option>
                <option value="jucy-lucy">Physics</option>
              </c-select>
            </c-box>

            <c-box w="33%" px="10">
              <c-flex align="center" mb="3">
                <c-flex align="center">
                  <c-text color="gray.600" font-size="1.4rem" mr="3">
                    $
                  </c-text>
                  <c-number-input :min="0">
                    <c-number-input-field />
                    <c-number-input-stepper>
                      <c-number-increment-stepper />
                      <c-number-decrement-stepper />
                    </c-number-input-stepper>
                  </c-number-input>
                </c-flex>

                <svg
                  id="Capa_1"
                  version="1.1"
                  xmlns="http://www.w3.org/2000/svg"
                  xmlns:xlink="http://www.w3.org/1999/xlink"
                  x="0px"
                  y="0px"
                  width="35px"
                  height="15px"
                  viewBox="0 0 357 357"
                  style="enable-background: new 0 0 357 357"
                  xml:space="preserve"
                  class="mx-4"
                >
                  <g>
                    <g id="remove">
                      <path d="M357,204H0v-51h357V204z" />
                    </g>
                  </g>
                  <g></g>
                  <g></g>
                  <g></g>
                  <g></g>
                  <g></g>
                  <g></g>
                  <g></g>
                  <g></g>
                  <g></g>
                  <g></g>
                  <g></g>
                  <g></g>
                  <g></g>
                  <g></g>
                  <g></g>
                </svg>

                <c-flex align="center">
                  <c-text color="gray.600" font-size="1.4rem" mr="3">
                    $
                  </c-text>
                  <c-number-input :min="0" mb="3">
                    <c-number-input-field />
                    <c-number-input-stepper>
                      <c-number-increment-stepper />
                      <c-number-decrement-stepper />
                    </c-number-input-stepper>
                  </c-number-input>
                </c-flex>
              </c-flex>

              <c-select placeholder="Arrange by">
                <option value="grilled">Release date</option>
                <option value="pub-style">Most views</option>
                <option value="jucy-lucy">Price</option>
              </c-select>
            </c-box>
          </c-flex>

          <!-- button submit -->
          <c-flex align="center" direction="row-reverse" w="100%">
            <c-button variant-color="blue">Apply Filters</c-button>
            <c-button mr="4">Cancel</c-button>
          </c-flex>
        </c-box>

        <c-box p="16">
          <c-flex align="center" flex-wrap="wrap">
            <c-box w="25%" px="4" py="8">
              <img src="@/static/default.png" alt="img-workbooks" />
            </c-box>
            <c-box w="25%" px="4" py="8">
              <img src="@/static/default.png" alt="img-workbooks" />
            </c-box>
            <c-box w="25%" px="4" py="8">
              <img src="@/static/default.png" alt="img-workbooks" />
            </c-box>
            <c-box w="25%" px="4" py="8">
              <img src="@/static/default.png" alt="img-workbooks" />
            </c-box>
            <c-box w="25%" px="4" py="8">
              <img src="@/static/default.png" alt="img-workbooks" />
            </c-box>
            <c-box w="25%" px="4" py="8">
              <img src="@/static/default.png" alt="img-workbooks" />
            </c-box>
            <c-box w="25%" px="4" py="8">
              <img src="@/static/default.png" alt="img-workbooks" />
            </c-box>
            <c-box w="25%" px="4" py="8">
              <img src="@/static/default.png" alt="img-workbooks" />
            </c-box>
          </c-flex>
        </c-box>
      </c-box>
    </c-box>
  </c-box>
</template>

<script>
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'

export default {
  components: {
    Swiper,
    SwiperSlide,
  },
  data() {
    return {
      swiperOption: {
        slidesPerView: 4,
        spaceBetween: 50,
        freeMode: true,
      },
    }
  },
}
</script>

<style lang="scss" scoped>
.swiper {
  height: 300px;
  width: 100%;
  .swiper-slide {
    display: flex;
    direction: row;
    justify-content: center;
    align-items: center;
    background-color: white;
  }
}
</style>
