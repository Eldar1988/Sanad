<template>
<div>
  <h2 class="section-title text-uppercase text-bold">
    {{ title }}
  </h2>
</div>
</template>

<script>
export default {
  name: "jsSectionTitle",
  props: {
    title: {
      type: String,
      default: ''
    }
  }
}
</script>

<style lang="sass">
.section-title
  font-size: 24px
  color: $dark

@media screen and (max-width: 650px)
  .section-title
    font-size: 18px
</style>
