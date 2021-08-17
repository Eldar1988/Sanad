<template>
  <q-page>
    <page-header title="Статьи" back-route-button/>
    <div class="container-m">
      <div class="row q-mt-lg bg-info">
        <!--        Photo-->
        <div class="col-12 col-md-3">
          <q-img :src="post.photo"
                 :style="photoStyle"
          >
            <template v-slot:loading>
              <q-skeleton square class="fit" height="200"/>
            </template>
          </q-img>
        </div>
        <!--        Title & author-->
        <div class="items-center flex col-12 col-md-9">
          <div class="q-pa-lg ">
            <h2 class="page-title">{{ post.title }}</h2>
            <!--            post author-->
            <div v-if="doctor" class="post-author row bg-white q-mt-lg">
              <div class="col-auto">
                <q-img :src="doctor.avatar" width="80px" height="100%" spinner-color="info"/>
              </div>
              <div class="col-auto col-9 q-py-sm q-px-md" style="max-width: 400px">
                <div class="flex" style="align-items: center; min-height: 100%">
                  <div style="max-width: 100%">
                    <p class="text-subtitle1 text-bold ellipsis">Автор: {{ doctor.name }}</p>
                    <p>{{ doctor.specialization }} / Стаж работы {{ doctor.experience }} </p>
                  </div>
                </div>
              </div>
            </div>
            <!--                Author buttons-->
            <div v-if="doctor" class="row q-col-gutter-md q-mt-sm">
              <div class="col-auto">
                <q-btn
                  label="Записаться"
                  outline stretch unelevated
                  color="primary"
                  class="letter-1 q-px-md"
                />
              </div>
              <div class="col-auto">
                <q-btn
                  label="О враче"
                  outline stretch unelevated
                  color="primary"
                  class="letter-1 q-px-md"
                  :to="`/doctor/${doctor.slug}`"
                />
              </div>
            </div>
          </div>

        </div>
      </div>
<!--      Content-->
      <div class="q-mt-lg">
        <div v-html="post.body"></div>
      </div>
      <div class="section" v-if="post.images.length">
        <post-photo-slider :images="post.images"/>
      </div>
      <div class="section" v-if="post.videos.length">
        <videos-slider :slides="post.videos"/>
      </div>
    </div>
    <page-footer/>
  </q-page>
</template>

<script>
import PageHeader from "components/utils/page-header";
import PageFooter from "components/footer/page-footer";
import PostPhotoSlider from "components/sliders/post-photo-slider";
import VideosSlider from "components/sliders/videos-slider";

export default {
  name: "PostDetail",
  components: {VideosSlider, PostPhotoSlider, PageFooter, PageHeader},
  computed: {
    photoStyle () {
      if (!this.doctor && this.$q.platform.is.desktop) {
        return 'width: 150px; height: 150px'
      } else {
        return 'width: 100%'
      }
    },
    post() {
      return this.$store.getters.getPost
    },
    doctor() {
      return this.$store.getters.getDoctors.find(item => item.id === this.post.doctor[0]) || ''
    }
  },
  preFetch({store, currentRoute}) {
    return store.dispatch('loadPost', currentRoute.params.slug)
  }
}
</script>

<style scoped>

</style>
