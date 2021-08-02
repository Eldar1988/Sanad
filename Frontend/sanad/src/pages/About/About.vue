<template>
<q-page>
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
  }
}
</script>

<style scoped>

</style>
