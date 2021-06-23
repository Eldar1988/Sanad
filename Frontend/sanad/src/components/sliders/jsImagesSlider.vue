<template>
  <q-carousel
    animated
    v-model="slide"
    navigation
    infinite
    swipeable
    :autoplay="true"
    class="image-slider"
  >
    <q-carousel-slide
      v-for="(image, index) in slides"
      :key="index"
      :name="index"
      :img-src="image.source"
    />
  </q-carousel>
</template>

<script>
export default {
  name: "jsImagesSlider",
  props: {
    slides: {
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      slide: 0
    }
  },
}
</script>

<style lang="sass">
.image-slider
  height: 650px

@media screen and (max-width: 800px)
  .image-slider
    height: 600px

@media screen and (max-width: 650px)
  .image-slider
    height: 350px
</style>
