<template>
<q-page>
  <q-page>
    <page-header title="Акции" back-route-button/>
    <div class="container-m">
      <div class="row q-mt-sm" :class="$q.platform.is.desktop ? 'q-col-gutter-xl' : 'q-col-gutter-sm'">
        <div class="col-12 col-md-4">
          <q-img :src="action.image" no-default-spinner/>
        </div>
        <div class="col-12 col-md-8">
          <h1 class="page-title" :class="$q.platform.is.desktop ? '' : 'q-mt-lg' ">{{ action.title }} {{ action.title_2 }} {{ action.title_3 }}</h1>
          <div class="q-mt-md" v-html="action.description"></div>
        </div>
      </div>
    </div>
    <page-footer />
  </q-page>
</q-page>
</template>

<script>
import PageHeader from "components/utils/page-header";
import PageFooter from "components/footer/page-footer";
export default {
  name: "ActionDetail",
  components: {PageFooter, PageHeader},
  computed: {
    action () {
      return this.$store.getters.getClinicAction
    }
  },
  preFetch ({ store, currentRoute }) {
    return store.dispatch('loadClinicAction', currentRoute.params.slug)
  }
}
</script>

<style scoped>

</style>
