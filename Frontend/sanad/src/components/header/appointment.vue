<template>
  <q-btn
    icon="eva-calendar-outline"
    :color="color"
    stretch
    :text-color="textColor"
    :flat="flat"
    :outline="outlined"
    :no-caps="!caps"
    :label="label"
    :class="classes"
    unelevated
    padding="12px"
    @click="$store.dispatch('changeAppointDialog')"
  />
</template>

<script>
export default {
  name: "appointment",
  props: {
    label: {
      type: String,
      default: ''
    },
    textColor: {
      type: String,
      default: 'white'
    },
    color: {
      type: String,
      default: 'dark'
    },
    caps: {
      type: Boolean,
      default: false
    },
    flat: {
      type: Boolean,
      default: false
    },
    outlined: {
      type: Boolean,
      default: true
    },
    classes: {
      type: String,
      default: ''
    }
  }
}
</script>

<style scoped>

</style>
