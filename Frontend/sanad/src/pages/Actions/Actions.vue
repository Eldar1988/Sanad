<template>
  <q-page>
    <page-header title="Акции"/>
    <div class="container-m">
      <div class="row q-col-gutter-md q-mt-md">
        <div
          v-for="action in actions"
          :key="action.id"
          class="col-12 col-sm-6 col-md-3 col-lg-3"
        >
          <action-card :action="action"/>
        </div>
      </div>
    </div>
    <page-footer />
  </q-page>
</template>

<script>
import PageHeader from "components/utils/page-header";
import ActionCard from "components/actions/action-card";
import PageFooter from "components/footer/page-footer";

export default {
  name: "Actions",
  components: {PageFooter, ActionCard, PageHeader},
  computed: {
    actions() {
      return this.$store.getters.getClinicActions
    }
  }
}
</script>

<style scoped>

</style>
