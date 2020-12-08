<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <!--        Логотип -->
        <router-link to="/">
          <q-toolbar-title class="text-weight-bold">
            <q-avatar>
              <img src="https://cdn.quasar.dev/logo/svg/quasar-logo.svg"/>
            </q-avatar>
            SANAD
          </q-toolbar-title>
        </router-link>
        <!--        =============================   -->

        <!--      Кнопки обратной связи -->
        <q-space/>
        <div class="flex hide-on-mobile">
          <q-call-back/>
        </div>
        <!--        Меню иконка -->
        <q-btn size="lg" dense flat round icon="view_list" @click="right = !right"/>
        <!--        =============================   -->
      </q-toolbar>
    </q-header>

    <!--    Правый сайдбар -->
    <q-drawer
      show-if-above
      v-model="right"
      side="right"
      bordered
      style="z-index: 1000"
    >
      <!--      Меню тулбар для мобильных -->
      <div class="hide-on-desktop">
        <q-toolbar class="bg-primary text-white text-uppercase">
          <q-toolbar-title class="font-weight-500">Меню</q-toolbar-title>
          <q-space/>
          <q-icon name="close" size="md" @click="right = !right"></q-icon>
        </q-toolbar>
      </div>
      <!--      ==================================   -->
      <!--      Кнопки обратной связи -->
      <div class="flex q-pa-md hide-on-desktop">
        <q-call-back/>
      </div>
      <!--      ============================   -->
      <!--      Меню - навигация -->
      <q-right-navigation-menu/>
      <!--      ==========================   -->
    </q-drawer>

    <q-page-container>
      <router-view/>
    </q-page-container>

    <!-- <q-footer elevated class="bg-grey-8 text-white">
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo/svg/quasar-logo.svg">
          </q-avatar>
          Footer
        </q-toolbar-title>
      </q-toolbar>
    </q-footer> -->
  </q-layout>
</template>

<script>
import qCallBack from "components/header/qCallBack";
import qRightNavigationMenu from "components/header/qRightNavigationMenu";

export default {
  components: {
    qCallBack,
    qRightNavigationMenu,
  },
  data() {
    return {
      search: "",
      right: false,
    };
  }
};
</script>
