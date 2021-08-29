<template>
  <q-page>
    <page-header :title="page.title" back-u-r-l="/" back-route-button/>
    <section class="container-m">
      <div class="section">
        <div v-html="page.content"></div>
      </div>
    </section>

    <page-footer />
  </q-page>
</template>

<script>
import PageHeader from "components/utils/page-header";
import PageFooter from "components/footer/page-footer";
export default {
  name: "InfoPage",
  components: {PageFooter, PageHeader},
  computed: {
    page () {
      return this.$store.getters.getInfoPage
    }
  },
  preFetch({ store, currentRoute }) {
    return store.dispatch('loadInfoPage', currentRoute.params.slug)
  }
}
</script>

<style scoped>

</style>
