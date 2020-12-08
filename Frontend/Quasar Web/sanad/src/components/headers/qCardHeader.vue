<template>
<router-link :to="link" title="Подробнее">
  <h4 class="col text-h6 ellipsis cursor-pointer text-dark">
    {{ header }}
  </h4>
</router-link>
</template>

<script>
export default {
name: "qCardHeader",
  props: ['header', 'link']
}
</script>

<style scoped>

</style>
