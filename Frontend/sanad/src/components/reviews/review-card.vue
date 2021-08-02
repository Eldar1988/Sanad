<template>
  <div>
    <q-card
      square
      class="shadow-0 cursor-pointer"
      @click="dialog = true"
    >
      <q-img
        :src="video.avatar || video.image"
        :height="height"
        :ratio="19/9"
      >
        <q-icon
          name="smart_display"
          color="primary"
          unelevated
          size="58px"
          class="play-icon"
        />
        <template v-slot:loading>
          <q-skeleton class="full-width" height="200px" square/>
        </template>
      </q-img>
<!--      <p class="sub_title text-dark q-pt-md">{{ video.title }}</p>-->
    </q-card>

    <q-dialog v-model="dialog">
      <q-card
        style="width: 800px; max-width: 100%"
        square
      >
        <q-toolbar class="bg-primary text-white text-right q-py-sm">
          <q-space/>
          <q-btn
            label="Закрыть"
            icon-right="close"
            stretch flat dense
            v-close-popup
          />
        </q-toolbar>
        <q-video
          :ratio="16/9"
          :src="`https://www.youtube.com/embed/${video.video}`"
        />
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
export default {
  name: "review-card",
  props: {
    video: {
      type: Object,
      default: null
    },
    isDoctorReview: {
      type: Boolean,
      default: true
    },
    height: {
      type: String,
      default: "180px"
    }
  },
  data() {
    return {
      dialog: false
    }
  },
}
</script>

<style lang="sass">
.play-icon
  position: absolute
  width: 47px
  height: 38px
  background: #ffffff
  left: 50%
  top: 50%
  border-radius: 4px
  margin-left: -33.5px
  margin-top: -19px
</style>
