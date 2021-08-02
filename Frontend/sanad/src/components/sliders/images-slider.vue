<template>
  <q-carousel
    animated
    v-model="slide"
    infinite
    swipeable
    :autoplay="2000"
    class="home-slider-image"
  >
    <q-carousel-slide
      v-for="(slide, index) in slides"
      :key="index"
      :name="index"
      :img-src="slide"
    >
    </q-carousel-slide>
  </q-carousel>
</template>

<script>
export default {
  name: "images-slider",
  props: {
    slides: Array
  },
  data() {
    return {
      slide: 0
    }
  }
}
</script>

<style scoped>

</style>
