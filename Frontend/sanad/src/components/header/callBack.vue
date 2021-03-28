<template>
<div>
  <q-btn
    icon="eva-calendar-outline"
    :color="color"
    stretch
    :flat="flat"
    :outline="outlined"
    :no-caps="!caps"
    :label="label"
    :class="classes"
  />
</div>
</template>

<script>
export default {
  name: "callBack",
  props: {
    label: {
      type: String,
      default: ''
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
