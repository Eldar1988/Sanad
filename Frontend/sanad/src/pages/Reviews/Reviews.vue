<template>
  <q-page>
    <page-header title="Отзывы"/>
    <div class="container-m">
      <div class="row q-col-gutter-md q-mt-lg">
        <div
          v-for="review in reviews"
          :key="review.id"
          class="col-md-6 col-12 col-lg-4"
        >
          <review-card :video="review" height="200px"/>
        </div>
      </div>
    </div>
    <page-footer />
  </q-page>
</template>

<script>
import PageHeader from "components/utils/page-header";
import ReviewCard from "components/reviews/review-card";
import PageFooter from "components/footer/page-footer";

export default {
  name: "Reviews",
  components: {PageFooter, ReviewCard, PageHeader},
  computed: {
    reviews() {
      return this.$store.getters.getReviews
    }
  },
  preFetch({store}) {
    return store.dispatch('loadReviews')
  }
}
</script>

<style scoped>

</style>
