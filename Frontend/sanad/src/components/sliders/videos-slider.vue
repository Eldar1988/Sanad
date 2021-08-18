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
    class="post-videos-slider"
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

<style lang="sass">
.post-videos-slider
  height: 600px

@media screen and (max-width: 992px)
  .post-videos-slider
    height: 400px

@media screen and (max-width: 700px)
  .post-videos-slider
    height: 210px
</style>
