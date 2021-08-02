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
        <div class="container-m">
          <div class="row" :class="$q.platform.is.desktop ? 'q-col-gutter-xl' : ''">
            <div class="col-12 col-md-6 section">
              <js-section-title title="Медицинские статьи" class=""/>
              <js-posts-list :posts="homePosts.slice(0, slice)" class=""/>
            </div>

            <div v-if="homePosts.slice(3,6).length > 0 && isDesktop" class="col-12 col-md-6 section">
              <js-section-title class="ml-15-m" style="margin-top: 44px"/>
              <js-posts-list :posts="homePosts.slice(3,6)" no-show-more class="q-px-sm"/>
            </div>
          </div>
        </div>
      </section>
    </div>
    <page-footer />
  </q-page>
</template>

<script>
import JsSlider from "components/sliders/home-slider";
import JsActionsSlider from "components/sliders/jsActionsSlider";
import JsSectionTitle from "components/utils/section-title";
import JsDirectionsTabs from "components/directions/direction-tabs";
import JsPostsList from "components/posts/posts-list";
import JsReviewsSlider from "components/reviews/reviews-slider";
import PageFooter from "components/footer/page-footer";

export default {
  name: 'PageIndex',
  components: {
    PageFooter,
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
    },
    slice () {
      return this.$q.platform.is.desktop ? 3 : 6
    },
    isDesktop () {
      return this.$q.platform.is.desktop
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
