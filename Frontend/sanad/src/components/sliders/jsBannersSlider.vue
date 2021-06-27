<template>
<div>
  <swiper class="swiper q-mt-md" :options="swiperOptions">
    <swiper-slide
      v-for="banner in banners"
      :key="banner.id"
    >
      <router-link :to="banner.url">
        <q-img
          :src="banner.image"
          :ratio="1/1"
        >

        </q-img>
      </router-link>
    </swiper-slide>
  </swiper>
</div>
</template>

<script>

import {Swiper, SwiperSlide, directive} from 'vue-awesome-swiper'
import 'swiper/swiper-bundle.css'

export default {
  name: "jsBannersSlider",
  props: {
    banners: {
      type: Array,
      default: () => []
    }
  },
  components: {
    Swiper,
    SwiperSlide
  },
  directives: {
    swiper: directive
  },
  data() {
    return {
      swiperOptions: {
        spaceBetween: 20,
        autoplay: {
          delay: 3000,
          stopOnLastSlide: false,
          disableOnInteraction: true,
        },
        freeMode: true,
        breakpoints: {
          1279: {
            slidesPerView: 4.2,
          },
          1000: {
            slidesPerView: 3.3,
          },
          750: {
            slidesPerView: 3.2,
          },
          330: {
            slidesPerView: 1.1,
          }
        }
      }
    }
  },

}
</script>

<style scoped>

</style>
