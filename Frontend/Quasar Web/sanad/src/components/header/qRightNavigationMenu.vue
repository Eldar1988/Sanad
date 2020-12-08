<template>
  <nav>
    <q-list class="text-dark" separator>
      <!--    Направления -->
      <q-toolbar class="bg-grey-3 text-dark text-uppercase">
        <q-toolbar-title class="font-weight-500">
          Направления
        </q-toolbar-title>
      </q-toolbar>
      <!--    Детям -->
      <q-expansion-item
        expand-separator
        icon="escalator_warning"
        label="Детям"
        class="menu-text"
      >
        <q-item
          clickable
          v-ripple
          to=""
          exact-active-class="text-primary"
          exact
          class="q-ml-md font-size-14"
        >
          <q-item-section avatar>
            <q-icon name="medical_services"/>
          </q-item-section>

          <q-item-section>Направление 1</q-item-section>
        </q-item>
      </q-expansion-item>
      <!--   ======================   -->
      <!--    Взрослым -->
      <q-expansion-item
        expand-separator
        icon="emoji_people"
        label="Взрослым"
        class="menu-text"
      >
        <q-item
          clickable
          v-ripple
          to=""
          exact-active-class="text-primary"
          exact
          class="q-ml-md font-size-14"
        >
          <q-item-section avatar>
            <q-icon name="medical_services"/>
          </q-item-section>

          <q-item-section>Направление 1</q-item-section>
        </q-item>
      </q-expansion-item>
      <!--    ======================= -->
      <!--   Инфо -->
      <q-toolbar class="bg-grey-3 text-dark text-uppercase">
        <q-toolbar-title class="font-weight-500">
          Информация
        </q-toolbar-title>
      </q-toolbar>
      <!--    Главная -->
      <q-item
        clickable
        v-ripple
        to="/"
        exact-active-class="text-primary"
        exact
        class="menu-text"
      >
        <q-item-section avatar>
          <q-icon name="home_work"/>
        </q-item-section>

        <q-item-section>Главная</q-item-section>
      </q-item>
      <!--   =================   -->
      <!--    О нас -->
      <q-item
        clickable
        v-ripple
        to="/about"
        exact-active-class="text-primary"
        exact
        class="menu-text"
      >
        <q-item-section avatar>
          <q-icon name="medical_services"/>
        </q-item-section>

        <q-item-section>О нас</q-item-section>
      </q-item>
      <!--   ================   -->
      <!--    Новости -->
      <q-item
        clickable
        v-ripple
        to="/news"
        exact-active-class="text-primary"
        exact
        class="menu-text"
      >
        <q-item-section avatar>
          <q-icon name="library_books"/>
        </q-item-section>

        <q-item-section>Наши новости</q-item-section>
      </q-item>
      <!--   ================   -->
      <!--    Акции -->
      <q-item
        clickable
        v-ripple
        to="/actions"
        exact-active-class="text-primary"
        exact
        class="menu-text"
      >
        <q-item-section avatar>
          <q-icon name="redeem"/>
        </q-item-section>

        <q-item-section>Акции</q-item-section>
      </q-item>
      <!--   ================   -->
      <!--    Контакты   -->
      <q-item
        clickable
        v-ripple
        to="/contacts"
        exact-active-class="text-primary"
        exact
        class="menu-text"
      >
        <q-item-section avatar>
          <q-icon name="place"/>
        </q-item-section>

        <q-item-section>Контакты</q-item-section>
      </q-item>
      <!--    ================   -->
    </q-list>
  </nav>
</template>

<script>
export default {
  name: "qRightNavigationMenu"
}
</script>

<style scoped>

</style>
