<template>
  <q-carousel
    swipeable
    animated
    v-model="slide"
    thumbnails
    infinite
    class="rounded-images shadow-10 q-mt-xl"
  >
    <q-carousel-slide v-for="image in photos" :key="image.id"
                      :name="image.id"
                      :img-src="image.url">
    </q-carousel-slide>
  </q-carousel>
</template>

<script>
export default {
  name: "qPhotoGallerySlider",
  props: {
    photos: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      slide: this.photos[0].id
    }
  }
}
</script>

<style scoped>

</style>
