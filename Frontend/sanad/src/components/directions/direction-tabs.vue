<template>
  <div class="q-mt-md">
    <div class="container">
      <q-tabs
        v-model="tab"
        class="text-grey "
        active-color="primary"
        indicator-color="transparent"
        align="justify"
      >
        <q-tab name="adults" label="Взрослым" class="text-bold q-card--bordered grey-gradient"
               style="width: 50%; padding: 15px 0"/>
        <q-tab name="child" label="Детям" class="q-card--bordered ml--1 grey-gradient"
               style="width: 50%; padding: 15px 0"/>
      </q-tabs>
      <q-tab-panels
        v-model="tab"
        animated
        transition-prev="scale"
        transition-next="scale"
      >
        <q-tab-panel name="adults">
          <div class="directions-grid">
            <div
              v-for="(direction, index) in adultsDirections"
              :key="direction.id"
              style="min-height: 100%"
            >
              <js-direction-card :direction="direction" :index="index"/>
            </div>
          </div>
        </q-tab-panel>

        <q-tab-panel name="child">
          <div class="directions-grid">
            <div
              v-for="(direction, index) in childDirections"
              :key="direction.id"
              style="min-height: 100%"
            >
              <js-direction-card :direction="direction" :index="index"/>
            </div>
          </div>
        </q-tab-panel>
      </q-tab-panels>
    </div>
  </div>
</template>

<script>
import JsDirectionCard from "components/directions/direction-card";

export default {
  name: "direction-tabs",
  components: {JsDirectionCard},
  data() {
    return {
      tab: 'adults'
    }
  },
  computed: {
    childDirections() {
      return this.$store.getters.getChildDirections
    },
    adultsDirections() {
      return this.$store.getters.getAdultsDirections
    }
  }
}
</script>

<style lang="sass">
.directions-grid
  display: grid
  grid-template-columns: repeat(5, 1fr)

@media screen and (max-width: 1100px)
  .directions-grid
    grid-template-columns: repeat(4, 1fr)

@media screen and (max-width: 650px)
  .directions-grid
    grid-template-columns: repeat(2, 1fr)
</style>
