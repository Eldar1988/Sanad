<template>
  <div>
    <swiper class="swiper" :options="swiperOptions">
      <swiper-slide
        v-for="action in actions"
        :key="action.id"
      >
        <js-action-card :action="action"/>
      </swiper-slide>
    </swiper>
  </div>
</template>

<script>
import {Swiper, SwiperSlide, directive} from 'vue-awesome-swiper'
import 'swiper/swiper-bundle.css'
import JsActionCard from "components/actions/jsActionCard";

export default {
  name: "jsActionsSlider",
  computed: {
    actions() {
      return this.$store.getters.getClinicActionsFroHomePage
    }
  },
  components: {
    JsActionCard,
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
            slidesPerView: 3.7,
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

<style lang="sass">



</style>
