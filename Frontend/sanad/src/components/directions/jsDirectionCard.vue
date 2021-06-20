<template>
  <div class="direction-card" style="height: 100%">
    <router-link :to="`/direction/${direction.slug}`" :title="'Узнать подробнее о направлении ' + direction.title">
      <q-card
        square
        bordered
        class="shadow-0"
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
  name: "jsDirectionCard",
  props: {
    direction: {
      type: Object,
      default: null
    }
  }
}
</script>

<style lang="sass">
.direction-card .q-card--bordered
  border: .5px solid rgba(0, 0, 0, 0.12)

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
