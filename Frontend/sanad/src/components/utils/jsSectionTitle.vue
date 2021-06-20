<template>
<div :class="colorClass">
  <h2 :class="'section-title text-uppercase text-bold letter-1 ' + colorClass">
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
    },
    colorClass: {
      type: String,
      default: 'text-dark'
    }
  }
}
</script>

<style lang="sass">
.section-title
  font-size: 24px
  color: $dark
  padding-bottom: 10px

@media screen and (max-width: 650px)
  .section-title
    font-size: 18px
</style>
