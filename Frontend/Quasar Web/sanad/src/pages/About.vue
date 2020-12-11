<template>
  <q-page class="q-pa-md">
    <section>
      <!--      Заголовок   -->
      <qPageHeader :header="about.title" :image="about.image"/>
      <!--      ==================    -->
      <!--      Тело    -->
      <div class="q-mt-lg text-body" v-html="about.text"></div>
      <!--      =====================    -->
    </section>
    <!--      Направления   -->
    <section>
      <qDirections/>
    </section>
    <!--      ===============   -->
    <!--    Видео и фото галерея   -->
    <section>
      <qSectionHeader header="Фото и видео"/>
      <div class="row justify-center">
        <div class="col-12 col-lg-6 pa-5">
          <qVideoSlider :slides="videos"/>
        </div>
        <div class="col-12 col-lg-6 pa-5">
          <qPhotoGallerySlider :photos="photos"/>
        </div>
      </div>
    </section>
    <!--    =================   -->
  </q-page>
</template>

<script>
import qPageHeader from "components/headers/qPageHeader";
import qDirections from 'components/home/qDirections'
import qSectionHeader from "components/headers/qSectionHeader";
import qVideoSlider from "components/cards/qVideoSlider";
import qPhotoGallerySlider from "components/cards/qPhotoGallerySlider";

export default {
  name: "About",
  components: {
    qPageHeader,
    qDirections,
    qSectionHeader,
    qVideoSlider,
    qPhotoGallerySlider
  },
  computed: {
    about() {
      return this.$store.state.about[0]
    },
    videos() {
      return this.$store.state.about[2]
    },
    photos() {
      return this.$store.state.about[1]
    }
  },
  preFetch({store}) {
    return store.dispatch('fetchAboutData')
  },
  meta() {
    let metaData = this.$store.state.about[0]
    return {
      title: metaData.title,
      meta: {
        description: {
          name: "description",
          content: metaData.sub_title,
        },
        ogType: {
          property: "og:type",
          content: "website",
        },
        ogTitle: {
          property: "og:title",
          content: metaData.title,
        },
        ogUrl: {
          property: "og:url",
          content: `${this.$store.state.siteURL}/about`,
        },
        ogDescription: {
          property: "og:description",
          content: metaData.sub_title,
        },
        ogImage: {
          property: "og:image",
          content: metaData.image,
        }
      },
    }
  }
}
</script>

<style scoped>

</style>
