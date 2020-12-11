<template>
  <h3 class="text-center section-header text-h4 font-weight-500 text-dark">{{ header }}
    <q-badge v-if="badge" align="top">{{ badge }}</q-badge>
  </h3>
</template>

<script>
export default {
name: "qSectionHeader",
  props: {
    header: {
      type: String,
      default: 'Заголовок секции'
    },
    badge: {
      type: Number,
      default: null
    }
  }
}
</script>

<style lang="sass">
.section-header
  margin-top: 80px

</style>
