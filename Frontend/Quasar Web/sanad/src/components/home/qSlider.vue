<template>
<div class="q-pa-md">
  <q-carousel
    v-model="slide"
    vertical
    transition-prev="slide-down"
    transition-next="slide-up"
    swipeable
    animated
    control-color="white"
    navigation-icon="radio_button_unchecked"
    navigation
    padding
    arrows
    :height="sliderHeight"
    class="text-white shadow-1 rounded-borders shadow-15"
  >
    <q-carousel-slide name="style" class="column no-wrap flex-center"
                      img-src="https://files.medelement.com/uploads/co/92401378980547/information/ed8d6dc0918c6f9a2a8f9a0f278779a5.jpg"
    >
      <div class="q-mt-md text-center">
        1
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
