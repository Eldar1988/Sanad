<template>
  <q-page>
    <div class="container-m">
      <!--      Doctors   -->
      <js-section-title :title="direction.title" class="q-mt-lg"/>
      <div class="q-mt-lg">
        <js-doctor-cards-grid :doctors="direction.doctors"/>
      </div>
      <!--      Videos   -->
      <section v-if="direction.videos && direction.videos.length > 0" class="section">
        <js-section-title title="Видео"/>
        <js-reviews-slider :reviews="direction.videos" :is-doctor-review="false"/>
      </section>
      <!--      Posts   -->
      <div class="section">
        <div class="row q-col-gutter-xl">
          <div v-if="direction.posts && direction.posts.length > 0" class="col-12 col-md-6 q-mt-xl">
            <js-section-title title="Медицинские статьи"/>
            <js-posts-list :posts="direction.posts" class="q-px-sm"/>
          </div>

          <div v-if="direction.stories && direction.stories.length > 0" class="col-12 col-md-6 q-mt-xl">
            <js-section-title title="Истории выздоровления"/>
            <js-posts-list :posts="direction.stories" :story="true" class="q-px-sm"/>
          </div>
        </div>
      </div>

<!--      Description   -->
      <div class="section">
        <js-section-title title="Информация"/>
        <div v-html="direction.description"></div>
        <js-images-slider v-if="direction.images" :slides="direction.images"/>
      </div>

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
import JsSectionTitle from "components/utils/jsSectionTitle";
import JsDoctorCardsGrid from "components/doctor/jsDoctorCardsGrid";
import JsPostsList from "components/home/jsPostsList";
import JsReviewsSlider from "components/reviews/jsReviewsSlider";
import JsImagesSlider from "components/sliders/jsImagesSlider";
import JsPostsSlider from "components/posts/jsPostsSlider";
import JsPostsGridV2 from "components/posts/jsPostsGrid-v2";

export default {
  name: "DirectionDetail",
  components: {
    JsPostsGridV2,
    JsPostsSlider, JsImagesSlider, JsReviewsSlider, JsPostsList, JsDoctorCardsGrid, JsSectionTitle},
  computed: {
    direction() {
      return this.$store.getters.getDirection
    },
    actualPosts() {
      return this.$store.getters.getActualPosts
    },
    clinicLifePosts() {
      return this.$store.getters.getClinicLifeActions
    }
  },
  preFetch({store, currentRoute}) {
    store.dispatch('loadDirection', currentRoute.params.slug)
  }
}
</script>

<style scoped>

</style>
