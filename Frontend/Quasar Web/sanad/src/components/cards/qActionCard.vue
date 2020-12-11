<template>
  <q-card class="bg-secondary-gradient text-white q-mt-md action-card shadow-0 text-center q-pb-xl">
    <h3 class="q-pt-xl text-h3">
      {{ action.title }}
    </h3>
    <p class="q-pa-md">{{ action.short_description }}</p>
    <q-btn color="White"
           outline
           rounded
           size="md"
           class="q-px-lg q-mt-md"
           icon-right="forward"
           :to="`/post/${action.slug}`"
    >Подробнее</q-btn>
  </q-card>
</template>

<script>
export default {
name: "qActionCard",
  props: {
    action: {
      type: Object,
      default: null
    }
  },
}
</script>

<style lang="sass">

</style>
