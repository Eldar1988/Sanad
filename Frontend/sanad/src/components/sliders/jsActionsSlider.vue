<template>
  <div>
    <swiper class="swiper" :options="swiperOptions">
      <swiper-slide
        v-for="action in actions"
        :key="action.id"
      >
        <q-card
         square
         class="shadow-0"
        >
          <router-link :to="`/action/${action.slug}`">
          <q-img :src="action.image" class="action-card-image">
            <p class="action-text q-pa-sm">
              <span class="action-title text-bold text-uppercase text-dark card-title">{{ action.title }}</span>
            </p>
            <template v-slot:loading>
              <q-skeleton class="full-width action-card-image" square/>
            </template>
          </q-img>
          </router-link>
        </q-card>
      </swiper-slide>
    </swiper>
  </div>
</template>

<script>
import {Swiper, SwiperSlide, directive} from 'vue-awesome-swiper'
import 'swiper/swiper-bundle.css'

export default {
  name: "jsActionsSlider",
  computed: {
    actions() {
      return this.$store.getters.getClinicActionsFroHomePage
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
        spaceBetween: 10,
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



.action-text
  position: absolute
  bottom: 0
  left: 0
  right: 0
  background: rgba(255,255,255,.7) !important

.action-card-image
  height: 220px


</style>
