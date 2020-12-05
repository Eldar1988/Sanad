<template>
  <q-layout view="hHh lpR fFf">

    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <!--        Логотип -->
        <q-toolbar-title class="text-weight-bold">
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo/svg/quasar-logo.svg">
          </q-avatar>
          SANAD
        </q-toolbar-title>
        <!--        =============================   -->
        <!--        Поиск -->
        <q-space v-if="!isMobile"/>
        <q-input v-if="!isMobile" dark dense standout v-model="search" input-class="text-right" class="q-ml-md">
          <template v-slot:append>
            <q-icon v-if="search === ''" name="search"/>
            <q-icon v-else name="play_arrow" class="cursor-pointer" @click="search = ''"/>
          </template>
        </q-input>
        <!--        ==============================   -->
        <!--      Кнопки обратной связи -->
        <q-space/>
        <div v-if="!isMobile" class="flex">
          <q-call-back/>
        </div>
        <!--        Меню иконка -->
        <q-btn size="lg" dense flat round icon="view_list" @click="right = !right"/>
        <!--        =============================   -->
      </q-toolbar>
    </q-header>

    <!--    Правый сайдбар -->
    <q-drawer show-if-above v-model="right" side="right" :bordered="!isMobile">
      <!--      Меню тулбар для мобильных -->
      <q-toolbar class="bg-primary text-white text-uppercase" v-if="isMobile">
        <q-toolbar-title class="font-weight-500">
          Меню
        </q-toolbar-title>
        <q-space/>
        <q-icon name="close" size="md" @click="right = !right"></q-icon>
      </q-toolbar>
      <!--      ==================================   -->
      <!--      Кнопки обратной связи -->
      <div v-if="isMobile" class="flex q-pa-md">
        <q-call-back/>
      </div>
      <!--      ============================   -->
      <!--      Меню - навигация -->
      <q-right-navigation-menu/>
      <!--      ==========================   -->
    </q-drawer>

    <q-page-container>
      <transition leave-active-class="animated fadeOut"
                  appear
                  :duration="400"
      >
        <router-view/>
      </transition>
    </q-page-container>


    <q-footer elevated class="bg-grey-8 text-white">
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo/svg/quasar-logo.svg">
          </q-avatar>
          Footer
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>

  </q-layout>
</template>

<script>
import qCallBack from "components/header/qCallBack"
import qRightNavigationMenu from "components/header/qRightNavigationMenu";


export default {
  components: {
    qCallBack,
    qRightNavigationMenu
  },
  data() {
    return {
      search: '',
      right: false,
      isMobile: this.$q.platform.is.mobile
    }
  }
}
</script>
