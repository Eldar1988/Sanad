<template>
<q-page>
  <page-header title="Направления"/>
  <div class="container-m">
    <direction-tabs class="section"/>
  </div>
  <page-footer />
</q-page>
</template>

<script>
import PageHeader from "components/utils/page-header";
import DirectionTabs from "components/directions/direction-tabs";
import PageFooter from "components/footer/page-footer";
export default {
  name: "Directions",
  components: {PageFooter, DirectionTabs, PageHeader}
}
</script>

<style scoped>

</style>
