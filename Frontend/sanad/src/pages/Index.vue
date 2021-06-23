<template>
  <q-page class="">
    <div class="container">

      <section>
        <js-slider/>
      </section>

      <section class="section ml-15-m">
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

      <section class="">
        <div class="container">
          <div class="row q-col-gutter-xl">
            <div class="col-12 col-md-6 q-mt-xl">
              <js-section-title title="Медицинские статьи" class="ml-15-m"/>
              <js-posts-list :posts="homePosts" class="q-px-sm"/>
            </div>

            <div class="col-12 col-md-6 q-mt-xl">
              <js-section-title title="Истории выздоровления" class="ml-15-m"/>
              <js-posts-list :posts="homeStories" :story="true" class="q-px-sm"/>
            </div>
          </div>
        </div>
      </section>

      <section class="section">
        <js-section-title title="Актуальное" class="ml-15-m"/>
        <js-posts-slider :posts="actualPosts"/>
      </section>

      <section class="section">
        <js-section-title title="Жизнь клиники Sanad" class="ml-15-m"/>
        <js-posts-grid-v2 :posts="clinicLifePosts" />
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
import JsPostsSlider from "components/posts/jsPostsSlider";
import JsPostsGridV2 from "components/posts/jsPostsGrid-v2";

export default {
  name: 'PageIndex',
  components: {
    JsPostsGridV2,
    JsPostsSlider, JsReviewsSlider, JsPostsList, JsDirectionsTabs, JsSectionTitle, JsActionsSlider, JsSlider},
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
    actualPosts() {
      return this.$store.getters.getActualPosts
    },
    clinicLifePosts() {
      return this.$store.getters.getClinicLifeActions
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
