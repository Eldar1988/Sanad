<template>
<div>
  <q-btn
    icon="eva-calendar-outline"
    color="dark"
    flat no-caps stretch dense
    :label="label"
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
    }
  }
}
</script>

<style scoped>

</style>
