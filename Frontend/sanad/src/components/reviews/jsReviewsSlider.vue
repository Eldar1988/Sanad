<template>
  <div class="q-mt-md ml-15-m">
    <swiper class="swiper" :options="swiperOptions">
      <swiper-slide
        v-for="review in reviews"
        :key="review.id"
      >
        <js-review-card :review="review" :is-doctor-review="isDoctorReview"/>
      </swiper-slide>
    </swiper>
    <router-link v-if="isDoctorReview" to="/" class="q-mt-lg block sub_title text-bold text-primary" title="Читать все отзывы">Смотреть все отзывы >></router-link>
  </div>
</template>

<script>
import {Swiper, SwiperSlide, directive} from 'vue-awesome-swiper'
import 'swiper/swiper-bundle.css'
import JsReviewCard from "components/reviews/jsReviewCard";

export default {
  name: "jsReviewsSlider",
  components: {
    JsReviewCard,
    Swiper,
    SwiperSlide
  },
  props: {
    reviews: {
      type: Array,
      default: null
    },
    isDoctorReview: {
      type: Boolean,
      default: true
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

<style scoped>

</style>
