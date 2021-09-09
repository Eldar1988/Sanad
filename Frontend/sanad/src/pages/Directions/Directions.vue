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
  components: {PageFooter, DirectionTabs, PageHeader},
  meta() {
    return {
      title: "Медицинские направления | Клиника SANAD Караганда",
      meta: {
        description: {
          name: "description",
          content: "Клинико-диагностический реабилитационный центр Sanad в Караганде",
        },
        ogType: {
          property: "og:type",
          content: "website",
        },
        ogTitle: {
          property: "og:title",
          content: "Медицинские направления | Клиника SANAD Караганда",
        },
        ogUrl: {
          property: "og:url",
          content: "https://sanadmed.kz/directions",
        },
        ogDescription: {
          property: "og:description",
          content: "Клинико-диагностический реабилитационный центр SANAD в Караганде",
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
