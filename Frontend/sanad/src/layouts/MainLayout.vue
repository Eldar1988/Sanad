<template>
  <q-layout view="hHh LpR fFf">

    <q-header class="bg-white" bordered>
      <q-toolbar class="q-pr-none">
        <q-btn dense flat round :icon="!left ? 'eva-menu-outline' : 'close'" @click="left = !left" color="dark"
               size="lg" padding="0"/>
        <q-toolbar-title :class="$q.platform.is.desktop ? '' : 'flex justify-center'">
          <router-link to="/">
            <img src="../assets/logo.png" title="Sanad" alt="logo" class="logo">
          </router-link>
        </q-toolbar-title>
        <js-header-actions/>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="left" side="left" bordered>
      <left-drawer-navigation/>
    </q-drawer>

    <q-page-container>
      <js-header-navigation class="ml-15-m"/>
      <keep-alive>
        <router-view/>
      </keep-alive>
    </q-page-container>

    <js-appoint />
  </q-layout>
</template>

<script>
import JsHeaderActions from "components/header/header-buttons";
import JsHeaderNavigation from "components/header/header-navigation";
import LeftDrawerNavigation from "components/header/left-drawer-navigation";
import JsAppoint from "components/utils/jsAppoint";

export default {
  components: {JsAppoint, LeftDrawerNavigation, JsHeaderNavigation, JsHeaderActions},
  computed: {
    slides() {
      return this.$store.getters.getMainInfo.slides
    }
  },
  created() {
    this.$store.dispatch('init')
  },
  data() {
    return {
      left: false
    }
  },
  preFetch({store}) {
    return store.dispatch('fetchMainInfo')
  },
  watch: {
    '$route' () {
      this.left ? this.left = false : null
    }
  }
}
</script>

<style lang="sass">
.logo
  height: 50px

@media screen and (max-width: 650px)
  .logo
    height: 40px

</style>
