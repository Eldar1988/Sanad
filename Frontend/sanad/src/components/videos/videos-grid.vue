<template>
  <div class="row q-col-gutter-md q-mt-lg">
    <div
      v-for="video in videos"
      :key="video.id"
      class="col-md-6 col-12 col-lg-4"
    >
      <review-card :video="video" height="200px"/>
    </div>
  </div>
</template>

<script>
import ReviewCard from "components/reviews/review-card";

export default {
  name: "videos-grid",
  components: {ReviewCard},
  computed: {
    videos() {
      return this.$store.getters.getVideos
    }
  },
  created() {
    this.$store.dispatch('loadVideos')
  }
}
</script>

<style scoped>

</style>
