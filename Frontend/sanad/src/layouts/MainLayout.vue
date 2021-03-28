<template>
  <q-layout view="hHh LpR fFf">

    <q-header class="bg-white" bordered>
      <q-toolbar>
        <q-btn dense flat round icon="eva-menu-outline" @click="left = !left" color="dark" size="lg" padding="0"/>

        <q-toolbar-title>
          <img src="../assets/logo.png" title="Sanad" alt="logo" class="logo">
        </q-toolbar-title>
        <js-header-actions />
      </q-toolbar>

    </q-header>


    <q-drawer v-model="left" side="left" bordered>

    </q-drawer>

    <q-page-container>
      <js-header-navigation class="q-pa-sm"/>
      <router-view/>
    </q-page-container>

    <js-footer />
  </q-layout>
</template>

<script>
import JsHeaderActions from "components/header/jsHeaderActions";
import JsHeaderNavigation from "components/header/jsHeaderNavigation";
import JsFooter from "components/footer/jsFooter";
export default {
  components: {JsFooter, JsHeaderNavigation, JsHeaderActions},
  computed: {
    slides() {
      return this.$store.getters.getMainInfo.slides
    }
  },
  async mounted() {
    await this.$store.dispatch('fetchClinicActions')
    await this.$store.dispatch('fetchDirections')
    await this.$store.dispatch('fetchHomePosts')
    await this.$store.dispatch('fetchHomeStories')
    await this.$store.dispatch('fetchHomeReviews')
    await this.$store.dispatch('fetchActualPosts')
    await this.$store.dispatch('fetchClinicLifePosts')
  },
  data() {
    return {
      left: false
    }
  },
  preFetch({store}) {
    return store.dispatch('fetchMainInfo')
  }
}
</script>

<style lang="sass">
.logo
  height: 50px
  padding-top: 5px

@media screen and (max-width: 650px)
  .logo
    height: 40px

</style>
