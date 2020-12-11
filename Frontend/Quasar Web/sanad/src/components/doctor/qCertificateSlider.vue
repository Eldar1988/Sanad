<template>
  <div class="text-dark">
    <q-carousel
      swipeable
      animated
      arrows
      v-model="slide"
      :fullscreen.sync="fullscreen"
      infinite
      control-color="secondary"
      navigation
      autoplay="" transition-next="fade" transition-prev="fade"
      class="certificate-carousel"
    >
      <q-carousel-slide v-for="certificate in certificates" :key="certificate.id"
                        :name="certificate.id"
                        :img-src="certificate.image"
                        style="background-size: contain; background-repeat: no-repeat"
      >
      </q-carousel-slide>

      <template v-slot:control>
        <q-carousel-control
          position="bottom-right"
          :offset="[18, 18]"
        >
          <q-btn
            push round dense color="white" text-color="primary"
            :icon="fullscreen ? 'fullscreen_exit' : 'fullscreen'"
            @click="fullscreen = !fullscreen"
          />
        </q-carousel-control>
      </template>
    </q-carousel>
  </div>
</template>

<script>
export default {
  name: "qCertificateSlider",
  props: {
    certificates: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      slide: this.certificates[0].id,
      fullscreen: false
    }
  }
}
</script>

<style lang="sass">
.certificate-carousel
  min-height: 100% !important
</style>
