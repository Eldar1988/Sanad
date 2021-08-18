<template>
  <q-carousel
    animated
    v-model="slide"
    infinite
    swipeable
    :autoplay="true"
    class="post-slider-image"
  >
    <q-carousel-slide
      v-for="(slide, index) in images"
      :key="index"
      :name="index"
    >
      <q-img
        :src="slide.url"
        class="post-slider-image"
      >
      </q-img>
    </q-carousel-slide>
  </q-carousel>
</template>

<script>
export default {
  name: "post-photo-slider",
  props: {
    images: Array
  },
  data() {
    return {
      slide: 0
    }
  },
}
</script>

<style lang="sass">
.post-slider-image
  height: 770px

@media screen and (max-width: 992px)
  .post-slider-image
    height: 500px

@media screen and (max-width: 700px)
  .post-slider-image
    height: 250px
</style>
