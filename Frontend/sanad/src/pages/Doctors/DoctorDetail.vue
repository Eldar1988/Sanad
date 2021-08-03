<template>
  <q-page>
    <page-header :title="doctor.directions[0].title" back-route-button/>
    <section class="container-m">
      <article>
        <div class="row q-col-gutter-lg q-mt-lg">
          <div class="col-12 col-sm-6">
            <images-slider :slides="images"/>
          </div>
          <div class="col-12 col-sm-6">
            <js-section-title :title="doctor.name"/>
            <p class="sub_title q-mt-sm">{{ doctor.specialization }}</p>
            <p class="sub_title q-mt-sm text-bold">Стаж работы: {{ doctor.experience }}</p>
            <p class="q-mt-md">{{ doctor.short_description }}</p>
            <div>
              <q-btn
                label="Записаться на прием"
                stretch unelevated
                color="negative"
                class="full-width letter-1 q-py-sm"
                style="margin-top: 34px;"
                @click="$store.dispatch('changeAppointDialog')"
              />
            </div>
          </div>
        </div>
        <js-scroll-x-page-nav :links="links"/>
        <div style="margin-top: 34px; margin-bottom: 70px" id="info">
          <div v-html="doctor.description"></div>
        </div>
      </article>
    </section>
    <section class="container-m">
      <!--      Posts   -->
      <div class="" id="posts">
        <div class="row q-col-gutter-xl">
          <div v-if="doctor.posts && doctor.posts.length > 0" class="col-12 col-md-6 q-mt-xl">
            <js-section-title title="Медицинские статьи"/>
            <js-posts-list :posts="doctor.posts" class="q-px-sm"/>
          </div>

          <div v-if="doctor.stories && doctor.stories.length > 0" class="col-12 col-md-6 q-mt-xl" id="stories">
            <js-section-title title="Истории выздоровления"/>
            <js-posts-list :posts="doctor.stories" :story="true" class="q-px-sm"/>
          </div>
        </div>
      </div>
    </section>
    <!--    Video   -->
    <div class="section">
      <section v-if="doctor.doctor_reviews && doctor.doctor_reviews.length > 0" class="container" id="videoReviews">
        <js-section-title title="Отзывы пациентов" class="ml-15-m"/>
        <js-reviews-slider :reviews="doctor.doctor_reviews"/>
      </section>
    </div>
    <section v-if="doctor.videos && doctor.videos.length > 0" class="section container" id="video">
      <js-section-title title="Видео" class="ml-15-m"/>
      <js-reviews-slider :reviews="doctor.videos" :is-doctor-review="false"/>
    </section>
    <page-footer/>
  </q-page>
</template>

<script>
import JsSectionTitle from "components/utils/section-title";
import JsPostsList from "components/posts/posts-list";
import JsReviewsSlider from "components/reviews/reviews-slider";
import JsScrollXPageNav from "components/utils/js-scroll-x-page-nav";
import PageFooter from "components/footer/page-footer";
import PageHeader from "components/utils/page-header";
import ImagesSlider from "components/sliders/images-slider";

export default {
  name: "DoctorDetail",
  components: {ImagesSlider, PageHeader, PageFooter, JsScrollXPageNav, JsReviewsSlider, JsPostsList, JsSectionTitle},
  computed: {
    images () {
      const images = []
      images.push(this.doctor.photo)
      this.doctor.images.forEach(item => images.push(item.source))
      return images
    },
    doctor() {
      return this.$store.getters.getDoctor
    },
    links() {
      const links = [{title: 'Информация', id: 'info'}]
      if (this.doctor.posts && this.doctor.posts.length > 0) links.push({title: 'Статьи', id: 'posts'})
      if (this.doctor.stories && this.doctor.stories.length > 0) links.push({title: 'Истории', id: 'stories'})
      if (this.doctor.doctor_reviews && this.doctor.doctor_reviews.length > 0) links.push({
        title: 'Отзывы',
        id: 'videoReviews'
      })
      if (this.doctor.videos && this.doctor.videos.length > 0) links.push({title: 'Видео', id: 'video'})
      return links
    }
  },
  preFetch({store, currentRoute}) {
    return store.dispatch('loadDoctor', currentRoute.params.slug)
  }
}
</script>

<style scoped>

</style>
