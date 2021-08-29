<template>
  <div class="container">
    <nav class="">
      <q-list class="flex navigation no-wrap text-uppercase text-weight-bold x-scroll" >
        <q-item class="x-nav-item text-grey-6" to="/" exact-active-class="text-dark" manual-focus>
          <q-item-section class="text-dark">
            Главная
          </q-item-section>
        </q-item>
        <q-item class="x-nav-item text-grey-6 q-ml-md" to="/directions" exact-active-class="text-dark" manual-focus>
          <q-item-section class="text-dark">
            Направления
          </q-item-section>
        </q-item>
        <q-item class="x-nav-item text-grey-6 q-ml-md" to="/doctors" exact-active-class="text-dark" manual-focus active-class="text-dark">
          <q-item-section class="text-dark" >
            Специалисты
          </q-item-section>
        </q-item>
        <q-item class="x-nav-item text-grey-6 q-ml-md" to="/actions" exact-active-class="text-dark" manual-focus>
          <q-item-section class="text-dark">
            Акции
          </q-item-section>
        </q-item>
        <q-item tag="a" class="x-nav-item text-grey-6 q-ml-md q-pr-lg" to="/price" exact-active-class="text-dark" manual-focus title="Прайс-лист цен на услуги">
          <q-item-section class="text-dark">
            Прайс
          </q-item-section>
        </q-item>
        <q-item class="x-nav-item text-grey-6 q-ml-md q-pr-lg" to="/posts" exact-active-class="text-dark" manual-focus>
          <q-item-section class="text-dark">
            Статьи
          </q-item-section>
        </q-item>
        <q-item class="x-nav-item text-grey-6 q-ml-md" to="/reviews" exact-active-class="text-dark" manual-focus>
          <q-item-section class="text-dark">
            Отзывы
          </q-item-section>
        </q-item>
        <q-item class="x-nav-item text-grey-6 q-ml-md" to="/videos" exact-active-class="text-dark" manual-focus>
          <q-item-section class="text-dark">
            Видео
          </q-item-section>
        </q-item>
        <q-item class="x-nav-item text-grey-6 q-ml-md" to="/about" exact-active-class="text-dark" manual-focus>
          <q-item-section class="text-dark no-wrap flex" style="min-width: 90px">
            О клинике
          </q-item-section>
        </q-item>
        <q-item class="x-nav-item text-grey-6 q-ml-md" @click="scrollTo('#contacts')" clickable exact-active-class="text-dark" manual-focus>
          <q-item-section class="text-dark">
            Контакты
          </q-item-section>
        </q-item>

      </q-list>
    </nav>
  </div>
</template>

<script>
export default {
  name: "header-navigation",
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

<style lang="sass">
.navigation
  padding-right: 50px
  display: flex
  overflow-x: scroll

.navigation::-webkit-scrollbar
  width: 3px
  /* ширина для вертикального скролла */
  height: 0
  /* высота для горизонтального скролла */
  background-color: #fff

</style>
