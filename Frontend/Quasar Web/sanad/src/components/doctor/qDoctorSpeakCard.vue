<template>
  <q-card class="my-card" flat>
    <q-card-section horizontal>
      <q-card-section class="q-pt-xs flex" style="align-items: center;">
        <div class="text-caption text-dark text-italic doctor-speak" v-html="text"></div>
        <h5 class="text-h5 q-mt-sm q-mb-xs float-right">{{ name }}</h5>
      </q-card-section>

      <q-card-section class="col-5 flex flex-center">
        <q-img
          class="rounded-borders shadow-5"
          :src="image"
        />
      </q-card-section>
    </q-card-section>
  </q-card>
</template>

<script>
export default {
  name: "qDoctorSpeakCard",
  props: {
    image: {
      type: String,
      default: null
    },
    text: {
      type: String,
      default: null
    },
    name: {
      type: String,
      default: null
    }
  }
}
</script>

<style lang="sass">
@media screen and (max-width: 650px)
  .doctor-speak p
    font-size: 12px !important

</style>
