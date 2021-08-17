<template>
  <q-carousel
    animated
    v-model="slide"
    infinite
    swipeable
    :autoplay="3000"
    navigation
    control-color="white"
    arrows
  >
    <q-carousel-slide
      v-for="(video, index) in slides"
      :key="index"
      :name="index">
      <q-video
        class="absolute-full"
        :src="`https://www.youtube.com/embed/${video.url}`"
      />
    </q-carousel-slide>
  </q-carousel>
</template>

<script>
export default {
  name: "videos-slider",
  props: {
    slides: Array
  },
  data() {
    return {
      slide: 0
    }
  },
}
</script>

<style scoped>

</style>
