<template>
  <div class="q-pa-md text-dark">
    <qSectionHeader :header="`Медицинские направления`" />
<!--    Табы - навигация   -->
    <q-tabs
      v-model="tab"
      align="justify"
      narrow-indicator
      class="q-my-md"
    >
      <q-tab class="text-primary" name="adults" label="Для взрослых" icon="emoji_people"/>
      <q-tab class="text-secondary" name="kids" label="Для детей" icon="escalator_warning"/>
    </q-tabs>
<!--    ======================   -->

<!--    Табы контент   -->
    <div class="q-gutter-y-sm q-mt-md">
      <q-tab-panels
        v-model="tab"
        animated
        transition-prev="scale"
        transition-next="scale"
      >
        <q-tab-panel name="adults" style="padding: 0;">
          <div class="row justify-center">
            <div class="col-lg-4 col-sm-6 col-12 pa-5 pa-3-m"
                 v-for="direction in directions"
                 :key="direction.id"
            >
              <qDirectionCard :direction="direction" />
            </div>
          </div>
        </q-tab-panel>

        <q-tab-panel name="kids" style="padding: 0;">
          <div class="row justify-center" >
            <div class="col-lg-4 col-sm-6 col-12 pa-5 pa-3-m"
                 v-for="direction in kidsDirections"
                 :key="direction.id"
            >
              <qDirectionCard :direction="direction" />
            </div>
          </div>
        </q-tab-panel>

      </q-tab-panels>
    </div>
<!--    ==================   -->
  </div>
</template>

<script>
import qDirectionCard from "components/home/qDirectionCard";
import qSectionHeader from "components/headers/qSectionHeader";
export default {
  name: 'qSirections',
  components: {
    qDirectionCard,
    qSectionHeader
  },
  data() {
    return {
      tab: 'adults',
    }
  },
  computed: {
    directions() {
      return this.$store.state.homeData[2] // Медицинские направления взрослые
    },
    kidsDirections() {
      return this.$store.state.homeData[3] // Медицинские направления детские
    }
  },
}
</script>

<style lang="sass">

</style>
