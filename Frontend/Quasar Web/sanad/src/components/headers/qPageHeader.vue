<template>
  <header>
    <q-img
      :src="image"
      class="rounded-borders home-slider-height shadow-15 img-overlay"
      spinner-color="secondary"
      :title="header"
    >
      <div class="page-header-text text-center text-white">
        <h1 class="text-h3 text-shadow">
          {{ header }}
        </h1>
        <h2 class="q-py-sm page-header-subtitle">
          {{ subtitle }}
        </h2>
      </div>

    </q-img>
  </header>
</template>

<script>
export default {
  name: "qPageHeader",
  props: {
    image: {
      type: String,
      default: 'https://www.westchesterhospital.com/wp-content/uploads/2018/01/doctor-1461911723OIY.jpg'
    },
    header: {
      type: String,
      default: 'Page Header'
    },
    subtitle: {
      type: String,
      default: ''
    }
  }

}
</script>

<style lang="sass">





</style>
