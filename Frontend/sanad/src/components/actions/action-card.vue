<template>
  <q-card
    square
    class="shadow-0"
  >
    <router-link :to="`/action/${action.slug}`" title="Подробнее об акции">
      <q-img :src="action.image" class="action-card-image" :title="action.title" :alt="action.title + ' фото'">
        <p class="action-text q-pa-sm">
          <span class="action-title text-bold text-uppercase text-dark card-title bg-white">{{ action.title }}</span><br>
          <span v-if="action.title_2" class="action-title text-bold text-uppercase text-dark card-title bg-white">{{ action.title_2 }}</span><br>
          <span v-if="action.title_3" class="action-title text-bold text-uppercase text-dark card-title bg-white">{{ action.title_3 }}</span>
        </p>
        <q-btn class="absolute-top-right q-mt-md q-mr-md" icon="las la-angle-right" color="white" text-color="warning" dense stretch unelevated/>
        <template v-slot:loading>
          <q-skeleton class="full-width action-card-image" square/>
        </template>
      </q-img>
    </router-link>
  </q-card>
</template>

<script>
export default {
  name: "action-card",
  props: {
    action: {
      type: Object,
      default: null
    }
  }
}
</script>

<style lang="sass">
.action-text
  position: absolute
  bottom: 10px
  left: 10px

.action-title
  padding: 5px 10px
  line-height: 1.5 !important

.action-card-image
  height: 220px
</style>
