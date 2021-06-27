<template>
  <q-page class="">
    <div class="container">

      <section>
        <js-slider/>
      </section>

      <section v-if="actions && actions.length > 0" class="section ml-15-m">
        <js-section-title title="Акции клиники"/>
        <js-actions-slider class="q-mt-md"/>
      </section>

      <section class="section">
        <js-section-title title="Направления" class="ml-15-m"/>
        <js-directions-tabs/>
      </section>

      <section class="section">
        <js-section-title title="Отзывы наших пациентов" class="ml-15-m"/>
        <js-reviews-slider :reviews="reviews"/>
      </section>

      <section>
        <div class="container">
          <div class="row" :class="$q.platform.is.desktop ? 'q-col-gutter-xl' : ''">
            <div class="col-12 col-md-6 section">
              <js-section-title title="Медицинские статьи" class="ml-15-m"/>
              <js-posts-list :posts="homePosts" class=""/>
            </div>

            <div class="col-12 col-md-6 section">
              <js-section-title title="Истории выздоровления" class="ml-15-m"/>
              <js-posts-list :posts="homeStories" :story="true" class="q-px-sm"/>
            </div>
          </div>
        </div>
      </section>

    </div>
  </q-page>
</template>

<script>
import JsSlider from "components/home/jsSlider";
import JsActionsSlider from "components/sliders/jsActionsSlider";
import JsSectionTitle from "components/utils/jsSectionTitle";
import JsDirectionsTabs from "components/home/jsDirectionsTabs";
import JsPostsList from "components/home/jsPostsList";
import JsReviewsSlider from "components/reviews/jsReviewsSlider";

export default {
  name: 'PageIndex',
  components: {
    JsReviewsSlider, JsPostsList, JsDirectionsTabs, JsSectionTitle, JsActionsSlider, JsSlider
  },
  computed: {
    homePosts() {
      return this.$store.getters.getHomePosts
    },
    homeStories() {
      return this.$store.getters.getHomeStories
    },
    reviews() {
      return this.$store.getters.getHomeReviews
    },
    actions() {
      return this.$store.getters.getClinicActionsFroHomePage
    }
  }
}
</script>

<style lang="sass">
.posts-grid
  display: grid
  grid-template-columns: 1fr 1fr
  grid-gap: 30px

@media screen and (max-width: 650px)
  .posts-grid
    grid-template-columns: 1fr
    grid-gap: 70px
</style>
