<template>
  <div class="container scroll-x-nav">
    <nav class="">
      <q-list class="flex navigation no-wrap text-uppercase text-weight-bold x-scroll">
        <q-item
          v-for="link in links"
          :key="link.id"
          class="x-nav-item text-grey-6 q-mr-lg"
          @click="scrollTo(`#${link.id}`)"
          clickable manual-focus
          exact-active-class="text-dark" >
          <q-item-section class="text-dark">
            {{ link.title }}
          </q-item-section>
        </q-item>
      </q-list>
    </nav>
  </div>
</template>

<script>
export default {
  name: "js-scroll-x-page-nav",
  props: {
    links: {
      type  : Array,
      default: () => []
    }
  },
  methods: {
    async scrollTo(id) {
      let element = document.querySelector(id)
      await element.scrollIntoView({
        behavior: 'auto',
        block: 'start'
      })
      window.scrollBy(0, -80)
    }
  }
}
</script>

<style lang="sass">
.scroll-x-nav
  margin-top: 40px !important
  padding: 5px 0
  border-top: 1px solid #ebebeb
  border-bottom: 1px solid #ebebeb
</style>
