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
        <q-item class="x-nav-item text-grey-6 q-ml-md" to="/" exact-active-class="text-dark" manual-focus>
          <q-item-section class="text-dark">
            Акции
          </q-item-section>
        </q-item>

        <q-item class="x-nav-item text-grey-6 q-ml-md" to="/" exact-active-class="text-dark" manual-focus>
          <q-item-section class="text-dark">
            Акции
          </q-item-section>
        </q-item>
        <q-item class="x-nav-item text-grey-6 q-ml-md" to="/" exact-active-class="text-dark" manual-focus>
          <q-item-section class="text-dark">
            Акции
          </q-item-section>
        </q-item>
      </q-list>
    </nav>
  </div>
</template>

<script>
export default {
  name: "jsHeaderNavigation"
}
</script>

<style lang="sass">
.navigation
  display: flex
  overflow-x: scroll

.navigation::-webkit-scrollbar
  width: 3px
  /* ширина для вертикального скролла */
  height: 0
  /* высота для горизонтального скролла */
  background-color: #fff

</style>
