<template>
  <q-carousel
    animated
    v-model="slide"
    infinite
    swipeable
    :autoplay="true"
    height="auto"
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
  min-height: 550px
</style>
