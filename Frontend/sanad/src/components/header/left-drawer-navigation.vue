<template>
  <q-list separator class="no-wrap text-uppercase text-weight-bold">
    <q-item class="text-grey-6" to="/" exact-active-class="text-dark  bg-info">
      <q-item-section class="text-dark q-pl-md">
        Главная
      </q-item-section>
    </q-item>
    <q-item class="text-grey-6" to="/directions" exact-active-class="text-dark  bg-info">
      <q-item-section class="text-dark q-pl-md">
        Направления
      </q-item-section>
    </q-item>
    <q-item class="text-grey-6" to="/doctors" exact-active-class="text-dark" active-class="text-dark  bg-info">
      <q-item-section class="text-dark q-pl-md" >
        Специалисты
      </q-item-section>
    </q-item>
    <q-item class="text-grey-6" to="/actions" exact-active-class="text-dark  bg-info">
      <q-item-section class="text-dark q-pl-md">
        Акции
      </q-item-section>
    </q-item>
    <q-item class=" text-grey-6 q-pr-lg" to="/posts" exact-active-class="text-dark  bg-info">
      <q-item-section class="text-dark q-pl-md">
        Статьи
      </q-item-section>
    </q-item>
    <q-item class="text-grey-6" to="/reviews" exact-active-class="text-dark  bg-info">
      <q-item-section class="text-dark q-pl-md">
        Отзывы
      </q-item-section>
    </q-item>
    <q-item class="text-grey-6" to="/videos" exact-active-class="text-dark  bg-info">
      <q-item-section class="text-dark q-pl-md">
        Видео
      </q-item-section>
    </q-item>
    <q-item class="text-grey-6" to="/about" exact-active-class="text-dark bg-info">
      <q-item-section class="text-dark no-wrap flex q-pl-md" style="min-width: 90px">
        О клинике
      </q-item-section>
    </q-item>
    <q-item class="text-grey-6" @click="scrollTo('#contacts')" clickable exact-active-class="text-dark">
      <q-item-section class="text-dark q-pl-md">
        Контакты
      </q-item-section>
    </q-item>

  </q-list>
</template>

<script>
export default {
  name: "left-drawer-navigation",
  methods: {
    scrollTo(id) {
      document.querySelector(id).scrollIntoView({
        behavior: 'smooth',
        block: 'center'
      })
    }
  }
}
</script>

<style scoped>

</style>
