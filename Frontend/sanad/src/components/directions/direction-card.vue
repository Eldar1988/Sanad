<template>
  <div class="q-card--bordered mt--1 no-top-border" style="height: 100%" :class="directionCardSpacer">
    <router-link :to="`/direction/${direction.slug}`" :title="'Узнать подробнее о направлении ' + direction.title">
      <q-card
        square
        class="shadow-0 grey-gradient"
        style="height: 100%"
      >
        <div class="q-pt-md q-px-md">
          <q-img v-once :src="direction.icon" class="direction-card-image" contain :title="direction.title" :alt="direction.title + ' фото'">
            <template v-slot:loading>
              <q-skeleton class="full-width direction-card-image" square/>
            </template>
          </q-img>
        </div>
        <div class="q-mb-sm">
        <p class="text-center sub_title q-pa-sm text-dark">{{ direction.title }}</p>
        </div>
      </q-card>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "direction-card",
  props: {
    direction: {
      type: Object,
      default: null
    },
    index: {
      type: Number
    }
  },
  computed: {
    directionCardSpacer () {
      const mobile = this.$q.platform.is.mobile
      let classes = []
      if (!mobile && this.index > 0 && this.index !== 5) classes.push('ml--1')
      if (mobile && this.index > 0) classes.push('ml--1')
      return classes.join(' ')
    }
  }
}
</script>

<style lang="sass">
.direction-card-image
  height: 100px

.direction-card-title
  font-size: 22px

@media screen and (max-width: 800px)
  .direction-card-image
    height: 150px

  .direction-card-title
    font-size: 18px

@media screen and (max-width: 650px)
  .direction-card-image
    height: 80px

  .direction-card-title
    font-size: 15px

</style>
