<template>
  <q-page>
    <page-header title="Видео"/>
    <div class="container-m">
      <videos-grid/>
    </div>
    <page-footer />
  </q-page>
</template>

<script>
import PageHeader from "components/utils/page-header";
import VideosGrid from "components/videos/videos-grid";
import PageFooter from "components/footer/page-footer";

export default {
  name: "videos",
  components: {PageFooter, VideosGrid, PageHeader},
  data() {
    return {
      schema: {
        "@context": "https://schema.org",
        "@type": "Organization",
        "url": "https://sanadmed.kz",
        "logo": "https://res.cloudinary.com/space-developers/image/upload/v1630987428/cvetogis/logo/logo_e3tgqj.png"
      }
    }
  },
  meta() {
    return {
      title: "Видеогалерея | Клиника SANAD Караганда",
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
          content: "Видеогалерея | Клиника SANAD Караганда",
        },
        ogUrl: {
          property: "og:url",
          content: "https://sanadmed.kz",
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
