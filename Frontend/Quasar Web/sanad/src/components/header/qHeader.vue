<template>>
  <div>
    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <q-toolbar-title class="text-weight-bold">
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo/svg/quasar-logo.svg">
          </q-avatar>
          SANAD
        </q-toolbar-title>

        <q-btn dense flat round icon="menu" @click="right = !right"/>
      </q-toolbar>
    </q-header>
    <q-drawer show-if-above v-model="right" side="right" bordered>
      <!-- drawer content -->
    </q-drawer>
  </div>
</template>

<script>
export default {
  name: "qHeader",

}
</script>

<style scoped>

</style>
