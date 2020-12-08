<template>
  <q-card flat bordered class="my-card healing-card text-dark">
    <q-card-section>
      <h5 class="text-h6 text-center">{{ healing.title }}</h5>
    </q-card-section>
    <q-separator inset />
    <q-card-section class="q-pt-none" v-html="healing.description">

    </q-card-section>
  </q-card>
</template>

<script>
export default {
  name: "qTreatmentStage",
  props: {
    healing: {
      type: Object,
      default: null
    }
  }
}
</script>

<style lang="sass">
.healing-card
  border-color: lightgrey
</style>
