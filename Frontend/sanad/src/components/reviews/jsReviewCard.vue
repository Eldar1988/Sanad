<template>
  <div>
    <q-card
      square
      class="shadow-0 cursor-pointer"
      @click="dialog = true"
    >
      <q-img
        v-if="isDoctorReview"
        :src="review.avatar"
        height="200px"
      >
        <q-btn
          icon="eva-play-circle-outline"
          class="grey-gradient text-dark"
          text-color="dark"
          unelevated round
          style="position: absolute; right: 50%; top: 50%; width: 42px; margin: -21px -21px 0 0"
        />
        <template v-slot:loading>
          <q-skeleton class="full-width" height="200px" square/>
        </template>
      </q-img>
      <div v-else>
        <q-video
          :ratio="16/9"
          :src="`https://www.youtube.com/embed/${review.video}`"
        />
      </div>
      <p v-if="isDoctorReview" class="sub_title text-dark q-pt-md">Отзыв о враче:<br>{{ review.doctor.specialization }}
        {{ review.doctor.name }}</p>
      <p v-else class="sub_title text-dark q-pt-md">{{ review.title }}</p>
    </q-card>

    <q-dialog v-model="dialog" v-if="isDoctorReview">
      <q-card
        style="width: 800px; max-width: 100%"
        square
      >
        <q-toolbar class="bg-dark text-white text-right q-py-sm">
          <q-space/>
          <q-btn
            label="Закрыть"
            icon-right="close"
            outline stretch
            v-close-popup
          />
        </q-toolbar>
        <q-video
          :ratio="16/9"
          :src="`https://www.youtube.com/embed/${review.video}`"
        />
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
export default {
  name: "jsReviewCard",
  props: {
    review: {
      type: Object,
      default: null
    },
    isDoctorReview: {
      type: Boolean,
      default: true
    }
  },
  data() {
    return {
      dialog: false
    }
  },
}
</script>

<style scoped>

</style>
