<template>
<div class="q-mt-md ml-15-m">
  <swiper class="swiper" :options="swiperOptions">
    <swiper-slide
      v-for="post in posts"
      :key="post.id"
    >
      <js-post-card-v1 :post="post"/>
    </swiper-slide>
  </swiper>
</div>
</template>

<script>
import {Swiper, SwiperSlide, directive} from 'vue-awesome-swiper'
import 'swiper/swiper-bundle.css'
import JsPostCardV1 from "components/posts/jsPostCard-v1";


export default {
  name: "jsPostsSlider",
  components: {
    JsPostCardV1,
    Swiper,
    SwiperSlide
  },
  props: {
    posts: {
      type: Array,
      default: null
    }
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
            slidesPerView: 1.5,
          }
        }
      }
    }
  },
}
</script>

<style scoped>

</style>
