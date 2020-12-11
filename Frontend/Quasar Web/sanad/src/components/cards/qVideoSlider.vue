<template>
  <div class="q-gutter-sm q-mt-xl">
    <q-carousel
      animated
      v-model="slide"
      infinite
      class="shadow-10" style="overflow: hidden !important;"
    >
      <q-carousel-slide v-for="slide in slides" :key="slide.id"
                        :name="slide.id"
                        class="border-radius-video shadow-10"
      >
        <q-video
          class="absolute-full border-radius-video shadow-10"
          :src="slide.url"
        />
      </q-carousel-slide>
    </q-carousel>

    <div class="row justify-center">
      <q-btn-toggle
        v-model="slide"
        :options="options"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "qVideoSlider",
  props: {
    slides: {
      type: Array,
      default: null
    }
  },
  data () {
    return {
      slide: this.slides[0].id,
      options: []
    }
  },
  mounted() {
    this.getSliderOptions()
  },
  methods: {
    getSliderOptions() {
      this.slides.forEach((slide) => {
        let optionsItem = {}
        optionsItem.label = slide.title
        optionsItem.value = slide.id
        this.options.push(optionsItem)
      })
    }
  }
}
</script>

<style lang="sass">
.border-radius-video
  border-radius: 5px
  overflow: hidden

</style>
