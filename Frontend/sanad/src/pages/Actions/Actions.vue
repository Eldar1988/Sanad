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
  },
  meta() {
    return {
      title: "Акции | Клиника SANAD Караганда",
      meta: {
        description: {
          name: "description",
          content: "Акции клиники. Клинико-диагностический реабилитационный центр Sanad в Караганде",
        },
        ogType: {
          property: "og:type",
          content: "website",
        },
        ogTitle: {
          property: "og:title",
          content: "Акции | Клиника SANAD Караганда",
        },
        ogUrl: {
          property: "og:url",
          content: "https://sanadmed.kz",
        },
        ogDescription: {
          property: "og:description",
          content: "Акции клиники. Клинико-диагностический реабилитационный центр Sanad в Караганде",
        },
        ogImage: {
          property: "og:image",
          content: "https://res.cloudinary.com/space-developers/image/upload/v1630987428/cvetogis/logo/logo_e3tgqj.png"
        }
      }
    }
  }
}
</script>

<style scoped>

</style>
