<template>
<q-page>
  <script type="application/ld+json" v-html="schema"></script>
  <page-header :title="about.title"/>
  <div class="container-m section">
    <section-title :title="about.sub_title"/>
    <div class="q-mt-lg">
      <div v-html="about.text"></div>
    </div>
  </div>
  <div class="container-m section">
    <videos-grid />
  </div>
  <page-footer />
</q-page>
</template>

<script>
import PageHeader from "components/utils/page-header";
import SectionTitle from "components/utils/section-title";
import VideosGrid from "components/videos/videos-grid";
import PageFooter from "components/footer/page-footer";
export default {
  name: "About",
  components: {PageFooter, VideosGrid, SectionTitle, PageHeader},
  computed: {
    about () {
      return this.$store.getters.getAboutInfo
    }
  },
  preFetch ({ store }) {
    return store.dispatch('loadAboutInfo')
  },
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
      title: "О клинике | Клиника SANAD Караганда",
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
          content: "Клиника SANAD Караганда",
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
