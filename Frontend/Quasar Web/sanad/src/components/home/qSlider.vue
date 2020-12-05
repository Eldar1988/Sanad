<template>
<div class="q-pa-md">
  <q-carousel
    v-model="slide"
    navigation-position="top"
    transition-prev="slide-down"
    transition-next="slide-up"
    swipeable
    animated
    control-color="secondary"
    navigation-icon="radio_button_unchecked"
    navigation
    padding
    arrows
    autoplay=""
    infinite
    :height="sliderHeight"
    class="text-white shadow-1 rounded-borders shadow-15"
  >
    <q-carousel-slide name="style" class="column no-wrap flex-center img-overlay" style="background-size: cover; background-repeat: no-repeat"
                      img-src="https://www.westchesterhospital.com/wp-content/uploads/2018/01/doctor-1461911723OIY.jpg"
    >
      <div class="slider-text text-center">
        <h1 class="text-h3 text-shadow">Slider title</h1>
        <p class="q-pt-sm subtitle">Slider subtitle text</p>
        <q-btn color="secondary" rounded class="q-px-md" unelevated>Button text</q-btn>
      </div>
    </q-carousel-slide>

    <q-carousel-slide name="slider 2" class="column no-wrap flex-center img-overlay" style="background-size: cover; background-repeat: no-repeat"
                      img-src="https://www.westchesterhospital.com/wp-content/uploads/2018/01/doctor-1461911723OIY.jpg"
    >
      <div class="slider-text text-center">
        <h1 class="text-h3 text-shadow">Slider title 2</h1>
        <p class="q-pt-sm subtitle">Slider subtitle text</p>
        <q-btn color="secondary" rounded class="q-px-md" unelevated>Button text</q-btn>
      </div>
    </q-carousel-slide>



  </q-carousel>
</div>
</template>

<script>
export default {
  name: "qSlider",
  data() {
    return {
      slide: 'style',
      sliderHeight: '',
      isMobile: this.$q.platform.is.mobile
    }
  },
  mounted() {
    if (this.$q.platform.is.mobile) {
      this.sliderHeight = '300px'
    } else {
      this.sliderHeight = '500px'
    }
  }
}
</script>

<style scoped>

</style>
