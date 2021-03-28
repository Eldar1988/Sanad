<template>
<div>
  <q-card
    square
    class="shadow-0"
  >
    <router-link :to="`/review/${review.id}`" title="Читать далее...">
    <q-img
      :src="review.avatar"
      height="200px"
    >
      <template v-slot:loading>
        <q-skeleton class="full-width" height="200px" square/>
      </template>
    </q-img>
      <p class="sub_title text-dark q-pt-sm">Отзыв о враче:<br>{{ review.doctor.specialization }} {{ review.doctor.name }}</p>
    </router-link>
  </q-card>
</div>
</template>

<script>
export default {
  name: "jsReviewCard",
  props: {
    review: {
      type: Object,
      default: null
    }
  }
}
</script>

<style scoped>

</style>
