<template>
  <div class="" style="margin-top: 80px">
    <q-carousel
      v-model="slide"
      transition-prev="slide-right"
      transition-next="slide-left"
      swipeable
      animated
      control-color="secondary"
      navigation-icon="radio_button_unchecked"
      navigation
      padding
      arrows
      height="auto"
      class="rounded-borders"
    >
      <q-carousel-slide
        name="slide"
        class="column no-wrap bg-primary-gradient"
      >
        <h3 class="text-center text-h4 font-weight-500 text-white q-mt-lg">{{ header }}</h3>
        <div class="testimonial">
          <div>
            <div class="row full-height justify-center" style="align-items: center; margin-top: 50px">
              <div v-if="!firstSlide.video"  class="col-sm-4">
                <div class="row" style="align-items: center; justify-content: center">
                  <div class="col-12 text-center">
                    <q-avatar class="testimonial-avatar shadow-0 text-center">
                      <img :src="firstSlide.avatar" style="object-fit: cover">
                    </q-avatar>
                  </div>
                  <div class="col-12">
                    <div class="testimonial-name q-mt-sm">
                      <h6 class="text-center text-white">{{ firstSlide.name }}</h6>
                    </div>
                  </div>
                </div>
              </div>

              <div v-if="!firstSlide.video"  class="col-sm-8 col-md-6 q-mt-sm text-right">
                <q-chat-message
                  :text="[`${firstSlide.text}`]"
                  bg-color="white" size="sm" class="text-h6 text-left" text-color="dark"
                />
                <q-rating v-model="firstSlide.rating" :max="5" size="32px" class="text-right" readonly/>
              </div>

              <div v-if="firstSlide.video" class="col-12 col-md-8 col-lg-6 text-right testimonial-video">
                <q-video
                  :ratio="16/9"
                  :src="review.video"
                />
                <q-rating v-model="firstSlide.rating" :max="5" size="32px" class="text-right q-mt-md" readonly/>
              </div>

            </div>

          </div>
        </div>
      </q-carousel-slide>
      <q-carousel-slide
        v-for="review in reviews.slice(1)"
        :key="review.id"
        :name="review.id"
        class="column no-wrap bg-primary-gradient"
      >
        <h3 class="text-center text-h4 font-weight-500 text-white q-mt-lg">{{ header }}</h3>
        <div class="testimonial">
          <div>
            <div class="row full-height justify-center" style="align-items: center; margin-top: 50px">
              <div v-if="!review.video"  class="col-sm-4">
                <div class="row" style="align-items: center; justify-content: center">
                  <div class="col-12 text-center">
                    <q-avatar class="testimonial-avatar shadow-0 text-center">
                      <img :src="review.avatar" style="object-fit: cover">
                    </q-avatar>
                  </div>
                  <div class="col-12">
                    <div class="testimonial-name q-mt-sm">
                      <h6 class="text-center text-white">{{ review.name }}</h6>
                    </div>
                  </div>
                </div>
              </div>

              <div v-if="!review.video"  class="col-sm-8 col-md-6 q-mt-sm text-right">
                <q-chat-message
                  :text="[`${review.text}`]"
                  bg-color="white" size="sm" class="text-h6 text-left" text-color="dark"
                />
                <q-rating v-model="review.rating" :max="5" size="32px" class="text-right" readonly/>
              </div>

              <div v-if="review.video" class="col-12 col-md-8 col-lg-6 text-right testimonial-video">
                <q-video
                  :ratio="16/9"
                  :src="review.video"
                />
                <q-rating v-model="review.rating" :max="5" size="32px" class="text-right q-mt-md" readonly/>
              </div>

            </div>

          </div>
        </div>
      </q-carousel-slide>
    </q-carousel>
  </div>
</template>

<script>
export default {
  name: "qTestimonialCardsSlider",
  props: {
    reviews: {
      type: Array,
      default: null
    },
    header: {
      type: String,
      default: 'Отзывы наших клиентов'
    }
  },
  data() {
    return {
      slide: 'slide',
      firstSlide: {}
    }
  },
  mounted() {
    this.firstSlide = this.reviews[0]
  }
}
</script>

<style lang="sass">
.testimonial-avatar
  width: 200px
  height: 200px

  img
    border: 2px solid #fff

.testimonial-video
  border-radius: 10px

.q-carousel--navigation-right.q-carousel--with-padding .q-carousel__slide, .q-carousel--navigation-right .q-carousel--padding, .q-carousel--arrows-horizontal.q-carousel--with-padding .q-carousel__slide, .q-carousel--arrows-horizontal .q-carousel--padding
  padding-right: 25px !important

.q-carousel--navigation-left.q-carousel--with-padding .q-carousel__slide, .q-carousel--navigation-left .q-carousel--padding, .q-carousel--arrows-horizontal.q-carousel--with-padding .q-carousel__slide, .q-carousel--arrows-horizontal .q-carousel--padding
  padding-left: 25px

</style>
