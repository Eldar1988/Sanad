<template>
  <div class="text-dark">
    <!--    Направления -->
    <q-toolbar class="bg-grey-3 text-uppercase">
      <q-toolbar-title class="font-weight-500">
        Направления
      </q-toolbar-title>
    </q-toolbar>
    <!--    Детям -->
    <q-expansion-item
      expand-separator
      icon="escalator_warning"
      label="Детям"
      class="menu-text"
    >
      <div v-for="direction in kidsDirections" :key="direction.id">
      <q-item
        clickable
        v-ripple
        exact-active-class="text-primary"
        exact
        class="q-ml-md font-size-14"
        :to="`/directions/${direction.slug}`"
      >
        <q-item-section avatar>
          <q-icon name="forward"/>
        </q-item-section>

        <q-item-section>{{ direction.title }}</q-item-section>
      </q-item>
      </div>
    </q-expansion-item>
    <!--   ======================   -->
    <!--    Взрослым -->
    <q-expansion-item
      expand-separator
      icon="emoji_people"
      label="Взрослым"
      class="menu-text"
    >
      <div v-for="direction in directions" :key="direction.id">
        <q-item
          clickable
          v-ripple
          exact-active-class="text-primary"
          exact
          class="q-ml-md font-size-14"
          :to="`/directions/${direction.slug}`"
        >
          <q-item-section avatar>
            <q-icon name="forward"/>
          </q-item-section>

          <q-item-section>{{ direction.title }}</q-item-section>
        </q-item>
      </div>

    </q-expansion-item>
    <!--    ======================= -->
  </div>
</template>

<script>
export default {
  name: "qMenuDirections",
  data() {
    return {
      directions: [],
      kidsDirections: []
    }
  },
  mounted() {
    this.directions = this.$store.state.homeData[2] // Медицинские направления взрослые
    this.kidsDirections = this.$store.state.homeData[3] // Медицинские направления детские
  }
}
</script>

<style scoped>

</style>
