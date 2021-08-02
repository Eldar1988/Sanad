<template>
  <q-page>
    <page-header title="Направления" back-u-r-l="/directions" back-route-button/>
    <div class="container-m">
      <!--      Doctors   -->
      <js-section-title :title="direction.title" class="q-mt-lg"/>
      <div class="q-mt-lg">
        <js-doctor-cards-grid :doctors="direction.doctors"/>
      </div>
      <js-scroll-x-page-nav :links="links"/>
      <!--      Videos   -->
      <section v-if="direction.videos && direction.videos.length > 0" class="section" id="video">
        <js-section-title title="Видео"/>
        <js-reviews-slider :reviews="direction.videos" :is-doctor-review="false"/>
      </section>
      <!--      Отзывы   -->
      <section v-if="reviews && reviews.length > 0" class="section" id="reviews">
        <js-section-title title="Отзывы"/>
        <js-reviews-slider :reviews="reviews" :is-doctor-review="false"/>
      </section>
      <!--      Posts   -->
      <div class="">
        <div class="row" :class="$q.platform.is.desktop ? 'q-col-gutter-xl' : ''">
          <div v-if="direction.posts && direction.posts.length > 0" class="col-12 col-md-6 q-mt-xl section" id="posts">
            <js-section-title title="Медицинские статьи"/>
            <js-posts-list :posts="direction.posts" class="q-px-sm"/>
          </div>

          <div v-if="direction.stories && direction.stories.length > 0" class="col-12 col-md-6 q-mt-xl section" id="stories">
            <js-section-title title="Истории выздоровления"/>
            <js-posts-list :posts="direction.stories" :story="true" class="q-px-sm"/>
          </div>
        </div>
      </div>

<!--      Description   -->
      <div class="q-pt-xl section" v-if="direction.description" id="info">
        <js-section-title title="Описание" class=""/>
        <div v-html="direction.description"></div>
        <js-images-slider v-if="direction.images && direction.images.length > 0" :slides="direction.images"/>
      </div>

    </div>
    <page-footer />
  </q-page>
</template>

<script>
import JsSectionTitle from "components/utils/section-title";
import JsDoctorCardsGrid from "components/doctor/doctor-cards-grid";
import JsPostsList from "components/posts/posts-list";
import JsReviewsSlider from "components/reviews/reviews-slider";
import JsImagesSlider from "components/sliders/jsImagesSlider";
import JsScrollXPageNav from "components/utils/js-scroll-x-page-nav";
import PageFooter from "components/footer/page-footer";
import PageHeader from "components/utils/page-header";

export default {
  name: "DirectionDetail",
  components: {
    PageHeader,
    PageFooter,
    JsScrollXPageNav,
    JsImagesSlider, JsReviewsSlider, JsPostsList, JsDoctorCardsGrid, JsSectionTitle},
  computed: {
    links() {
      const links = []
      if (this.direction.videos && this.direction.videos.length > 0) links.push({title: 'Видео', id: 'video'})
      if (this.reviews && this.reviews.length > 0) links.push({title: 'Отзывы', id: 'reviews'})
      if (this.direction.posts && this.direction.posts.length > 0) links.push({title: 'Статьи', id: 'posts'})
      if (this.direction.stories && this.direction.stories.length > 0) links.push({title: 'Истории', id: 'stories'})
      if (this.direction.description) links.push({title: 'Описание', id: 'info'})
      return links
    },
    direction() {
      return this.$store.getters.getDirection
    },
    clinicLifePosts() {
      return this.$store.getters.getClinicLifeActions
    },
    reviews () {
      const doctors = this.direction.doctors
      const doctorsReviews = []
      doctors?.forEach(doctor => doctor.doctor_reviews.forEach(review => doctorsReviews.push(review)))
      return doctorsReviews
    }
  },
  preFetch({store, currentRoute}) {
    store.dispatch('loadDirection', currentRoute.params.slug)
  }
}
</script>

<style scoped>

</style>
