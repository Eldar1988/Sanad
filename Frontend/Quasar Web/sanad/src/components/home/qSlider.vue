<template>
  <div class="q-pa-md">
    <q-carousel
      v-model="slide"
      navigation-position="top"
      transition-prev="fade"
      transition-next="fade"
      swipeable
      animated
      control-color="secondary"
      navigation-icon="radio_button_unchecked"
      navigation
      padding
      autoplay=""
      infinite
      class="text-white shadow-1 rounded-borders shadow-15 home-slider-height"
    >
      <!-- Первый слайд    -->
      <q-carousel-slide
        name="slide"
        class="column no-wrap flex-center img-overlay q-parallax__media"
        :img-src="firstSlide.image"
      >
        <div class="slider-text text-center">
          <h1 class="text-h3 text-shadow font-weight-500">{{ firstSlide.title }}</h1>
          <p class="q-py-sm subtitle">{{ firstSlide.text }}</p>
          <q-btn
            color="secondary"
            rounded
            class="q-px-md"
            unelevated
            :to="firstSlide.button_url"
            >{{ firstSlide.button_text }}</q-btn
          >
        </div>
      </q-carousel-slide>
      <!-- ====================    -->
      <!-- Остальные слайды   -->
      <q-carousel-slide
        v-for="slide in secondarySlides"
        :key="slide.id"
        :name="slide.title"
        class="column no-wrap flex-center img-overlay"
        style="background-size: cover; background-repeat: no-repeat"
        :img-src="slide.image"
      >
        <div class="slider-text text-center">
          <h2 class="text-h3 text-shadow font-weight-500">{{ slide.title }}</h2>
          <p class="q-py-sm subtitle">{{ slide.text }}</p>
          <q-btn
            color="secondary"
            rounded
            class="q-px-md"
            unelevated
            :to="slide.button_url"
            >{{ slide.button_text }}</q-btn
          >
        </div>
      </q-carousel-slide>
      <!-- =======================    -->
    </q-carousel>
  </div>
</template>

<script>
export default {
  name: "qSlider",
  props: ["slides"],
  data() {
    return {
      firstSlide: this.slides[0], // Получаем первый слайд для того, чтобы отделить его от остальных и присвоить h1  заголовок
      secondarySlides: this.slides.slice(1), // Остальные слайды
      slide: "slide",
      sliderHeight: "",
      isMobile: this.$q.platform.is.mobile,
    };
  },
  mounted() {
    // Устанавливаем высоту слайдера в зависимости от устройства
    if (this.$q.platform.is.mobile) {
      this.sliderHeight = "300px";
    } else {
      this.sliderHeight = "500px";
    }
  },
};
</script>

<style scoped></style>
