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

        <q-tab name="adults" label="Взрослым" class="text-bold" style="width: 50%"/>
        <q-tab name="child" label="Детям" class="" style="width: 50%"/>
      </q-tabs>
        <q-tab-panels
          v-model="tab"
          animated
          transition-prev="scale"
          transition-next="scale"
          class="q-mt-md"
        >
          <q-tab-panel name="adults">
            <div class="directions-grid">
              <div
                v-for="direction in adultsDirections"
                :key="direction.id"
                style="min-height: 100%"
              >
                <js-direction-card :direction="direction"/>
              </div>
            </div>
          </q-tab-panel>

          <q-tab-panel name="child">
            <div class="directions-grid">
              <div
                v-for="direction in childDirections"
                :key="direction.id"
                style="min-height: 100%"
              >
                <js-direction-card :direction="direction"/>
              </div>
            </div>
          </q-tab-panel>
        </q-tab-panels>

    </div>
  </div>
</template>

<script>
import JsDirectionCard from "components/directions/jsDirectionCard";
export default {
  name: "jsDirectionsTabs",
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
