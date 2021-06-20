<template>
  <div>
    <q-carousel
      animated
      v-model="slide"
      infinite
      swipeable
      :autoplay="true"
      class="home-slider-image"
    >
      <q-carousel-slide
        v-for="(slide, index) in slides"
        :key="index"
        :name="index"
      >
        <q-img
          :src="slide.image"
          class="home-slider-image"
        >
          <div class="slider-text">
            <h1 class="text-weight-bold text-uppercase letter-1">
              <span>{{ slide.title }}</span><br>
              <span>{{ slide.title_2 }}</span>
            </h1>
          </div>
          <template v-slot:loading>
            <q-skeleton class="full-width home-slider-image" square/>
          </template>
        </q-img>
      </q-carousel-slide>
    </q-carousel>
  </div>
</template>

<script>
export default {
  name: "jsSlider",
  data() {
    return {
      slide: 0
    }
  },
  computed: {
    slides() {
      return this.$store.getters.getMainInfo.slides
    }
  }
}
</script>

<style lang="sass">
.home-slider-image
  height: 500px

.slider-text
  position: absolute
  bottom: 30px
  left: 0
  right: 0
  text-align: center

  h1
    font-size: 33px
    span
      background: #ffffff
      display: inline-block
      color: $dark
      padding: 5px 10px


@media screen and (max-width: 650px)
  .slider-text
    h1
      font-size: 20px
      span
        background: #ffffff
        display: inline-block
        color: $dark
        padding: 5px 10px
        margin-top: -1px

  .home-slider-image
    height: 300px

</style>
