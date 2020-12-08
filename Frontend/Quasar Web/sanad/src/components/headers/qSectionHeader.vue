<template>
  <h3 class="text-center section-header text-h4 font-weight-500 text-dark">{{ header }}</h3>
</template>

<script>
export default {
name: "qSectionHeader",
  props: ['header']
}
</script>

<style lang="sass">
.section-header
  margin-top: 80px

</style>
