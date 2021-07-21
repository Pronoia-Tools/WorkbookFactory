<template>
  <c-box class="container mx-auto py-24">
    <c-box class="px-6 md:px-12">
      <!-- New releases -->
      <c-box class="mb-12">
        <c-text class="mb-3" font-size="28px">New releases</c-text>
        <c-box
          class="border border-gray-200 p-4"
          box-shadow="0px 0px 1px 1px #E2E8F0"
        >
          <swiper class="swiper" :options="swiperOption">
            <swiper-slide>
              <c-image
                :src="require('@/static/default.png')"
                alt="new-release"
              />
            </swiper-slide>
            <swiper-slide>
              <c-image
                :src="require('@/static/default.png')"
                alt="new-release"
              />
            </swiper-slide>
            <swiper-slide>
              <c-image
                :src="require('@/static/default.png')"
                alt="new-release"
              />
            </swiper-slide>
            <swiper-slide>
              <c-image
                :src="require('@/static/default.png')"
                alt="new-release"
              />
            </swiper-slide>
            <swiper-slide>
              <c-image
                :src="require('@/static/default.png')"
                alt="new-release"
              />
            </swiper-slide>
            <swiper-slide>
              <c-image
                :src="require('@/static/default.png')"
                alt="new-release"
              />
            </swiper-slide>
            <swiper-slide>
              <c-image
                :src="require('@/static/default.png')"
                alt="new-release"
              />
            </swiper-slide>
            <div slot="pagination" class="swiper-pagination"></div>
          </swiper>
        </c-box>
      </c-box>

      <!-- Most popular -->
      <c-box class="mb-12">
        <c-text class="mb-3" font-size="28px" x>Most popular</c-text>
        <c-box
          class="boder border-gray-200 p-4"
          box-shadow="0px 0px 1px 1px #E2E8F0"
        >
          <swiper class="swiper" :options="swiperOption">
            <swiper-slide>
              <c-image
                :src="require('@/static/default.png')"
                alt="new-release"
              />
            </swiper-slide>
            <swiper-slide>
              <c-image
                :src="require('@/static/default.png')"
                alt="new-release"
              />
            </swiper-slide>
            <swiper-slide>
              <c-image
                :src="require('@/static/default.png')"
                alt="new-release"
              />
            </swiper-slide>
            <swiper-slide>
              <c-image
                :src="require('@/static/default.png')"
                alt="new-release"
              />
            </swiper-slide>
            <swiper-slide>
              <c-image
                :src="require('@/static/default.png')"
                alt="new-release"
              />
            </swiper-slide>
            <swiper-slide>
              <c-image
                :src="require('@/static/default.png')"
                alt="new-release"
              />
            </swiper-slide>
            <swiper-slide>
              <c-image
                :src="require('@/static/default.png')"
                alt="new-release"
              />
            </swiper-slide>
            <div slot="pagination" class="swiper-pagination"></div>
          </swiper>
        </c-box>
      </c-box>

      <!-- All workbooks -->
      <c-box>
        <c-text class="mb-3" font-size="28px">All workbooks</c-text>
        <c-box
          class="border border-gray-200"
          box-shadow="0px 0px 1px 1px #E2E8F0"
        >
          <c-box class="mb-10 p-8 border-bottom border-gray-100">
            <c-flex class="mb-6 items-center">
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
              <c-text class="font-semibold ml-2" font-size="20px"
                >Filter</c-text
              >
            </c-flex>

            <!-- filter form -->
            <c-flex class="items-center mb-8 flex-wrap">
              <c-box
                class="w-full mb-3 px-4 md:px-10 lg:w-1/2 xl:w-1/3 xl:mb-0"
              >
                <c-input class="mb-3" placeholder="Title" />
                <c-input placeholder="Author" />
              </c-box>

              <c-box
                class="w-full mb-3 px-4 md:px-10 lg:w-1/2 xl:w-1/3 xl:mb-0"
              >
                <c-select class="mb-3" placeholder="Select language">
                  <option value="english">English</option>
                  <option value="germany">Germany</option>
                  <option value="vietnamese">Vietnamese</option>
                </c-select>

                <c-select placeholder="Select category">
                  <option value="hisotry">History</option>
                  <option value="conqueor">Conqueor</option>
                  <option value="physics">Physics</option>
                </c-select>
              </c-box>

              <c-box
                class="
                  w-full
                  px-4
                  mb-3
                  md:px-10
                  lg:flex
                  xl:inline-block xl:w-1/3 xl:mb-0
                "
              >
                <c-flex
                  class="
                    items-center
                    mb-3
                    lg:w-1/2 lg:pr-10 lg:mb-0
                    xl:w-full xl:pr-0 xl:mb-3
                  "
                >
                  <c-flex class="items-center">
                    <c-text class="text-gray-600 mr-3" font-size="1.4rem">
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

                  <c-flex class="items-center">
                    <c-text class="text-gray-600 mr-3" font-size="1.4rem">
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
                </c-flex>

                <c-box class="lg:w-1/2 lg:pl-10 xl:w-full xl:pl-0">
                  <c-select placeholder="Arrange by">
                    <option value="release-date">Release date</option>
                    <option value="most-views">Most views</option>
                    <option value="price">Price</option>
                  </c-select>
                </c-box>
              </c-box>
            </c-flex>

            <!-- button submit -->
            <c-flex class="w-full flex-row-reverse items-center -ml-10">
              <c-button variant-color="blue">Apply Filters</c-button>
              <c-button class="mr-4">Cancel</c-button>
            </c-flex>
          </c-box>

          <c-box class="p-8">
            <c-flex class="items-center flex-wrap">
              <c-box class="w-full p-3 md:w-1/3 md:p-2 lg:w-1/4 lg:p-4">
                <c-image
                  :src="require('@/static/default.png')"
                  alt="img-workbooks"
                />
              </c-box>
              <c-box class="w-full p-3 md:w-1/3 md:p-2 lg:w-1/4 lg:p-4">
                <c-image
                  :src="require('@/static/default.png')"
                  alt="img-workbooks"
                />
              </c-box>
              <c-box class="w-full p-3 md:w-1/3 md:p-2 lg:w-1/4 lg:p-4">
                <c-image
                  :src="require('@/static/default.png')"
                  alt="img-workbooks"
                />
              </c-box>
              <c-box class="w-full p-3 md:w-1/3 md:p-2 lg:w-1/4 lg:p-4">
                <c-image
                  :src="require('@/static/default.png')"
                  alt="img-workbooks"
                />
              </c-box>
            </c-flex>
          </c-box>
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
        breakpoints: {
          1024: {
            slidesPerView: 4,
            spaceBetween: 40,
          },
          768: {
            slidesPerView: 3,
            spaceBetween: 30,
          },
          640: {
            slidesPerView: 2,
            spaceBetween: 20,
          },
          320: {
            slidesPerView: 1,
            spaceBetween: 10,
          },
        },
      },
    }
  },
}
</script>

<style lang="scss" scoped>
.swiper {
  // height: 300px;
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
