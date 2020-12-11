<template>
  <q-page class="q-pa-md">
    <!--    Schema org   -->
    <script type="application/ld+json" v-html="schema"></script>
    <!--    ===================   -->
    <!--    О докторе   -->
    <article class="text-dark">
      <!--      Заголовок с картинкой   -->
      <q-page-header :header="doctorData.name" :image="doctorData.photo" :subtitle="doctorData.short_description"/>
      <!--      Акции   -->
      <div class="action-wrapper" v-for="action in doctorData.actions" :key="action.id">
        <article v-for="post in doctorData.posts" :key="post.id">
          <qActionCard v-if="post.is_action" :action="post"/>
        </article>
      </div>
      <!--    =====================   -->
      <!--      Описание -->
      <div class="q-mt-lg text-body" v-html="doctorData.description"></div>
      <!--    =====================   -->
    </article>
    <!--    =================   -->
    <!--    Видео и фото галерея   -->
    <section>
      <qSectionHeader header="Фото и видео"/>
      <div class="row justify-center">
        <div class="col-12 col-lg-6 pa-5">
          <qVideoSlider :slides="doctorData.videos"/>
        </div>
        <div class="col-12 col-lg-6 pa-5">
          <qPhotoGallerySlider :photos="doctorData.images"/>
        </div>
      </div>
    </section>
    <!--    =================   -->
    <!--    Статьи   -->
    <section>
      <qSectionHeader header="Статьи"/>
      <div class="row q-mt-lg justify-center">
        <div class="col-lg-3 col-md-4 col-sm-6 col-12 pa-5" v-for="post in doctorData.posts" :key="post.id">
          <div v-if="post.public">
            <qPostCard :post="post"/>
          </div>
        </div>
      </div>
    </section>
    <!--    =================   -->
    <!--      Слово и грамоты  -->
    <section>
      <div class="row justify-center">
        <div class="col-lg-6 col-12 pa-5">
          <qSectionHeader header="Грамоты"/>
          <qCertificateSlider :certificates="doctorData.certificates" style="margin-top: 30px"/>
        </div>
        <div class="col-lg-6 col-12" style="margin-top: 110px">
          <article>
            <qDoctorSpeakCard :image="doctorData.avatar" :text="doctorData.say" :name="doctorData.name"/>
          </article>
        </div>
      </div>
    </section>
    <!--    =====================   -->
    <!--      Отзывы  -->
    <section>
      <qTestimonialCardsSlider header="Отзывы о докторе" :reviews="doctorData.reviews"/>
    </section>
    <!--    =================   -->
    <!--      Поделиться в сети -->
    <qShare class="q-mt-lg"/>
    <!--    =====================   -->
    <!--    Истори болезней   -->
    <section>
      <qSectionHeader header="Истории выздоравлений"/>
      <div class="row q-mt-lg justify-center">
        <div class="col-lg-3 col-md-4 col-sm-6 pa-5" v-for="story in doctorData.stories" :key="story.id">
          <article v-if="story.public">
            <qStoryCard :story="story"/>
          </article>
        </div>
      </div>
    </section>
    <!--    =================   -->
    <qAppointmentButton :header="`${doctorData.name} - запись на прием`" :isAppointment="true"/>
  </q-page>
</template>

<script>
import qPageHeader from "components/headers/qPageHeader";
import qActionCard from "components/cards/qActionCard";
import qTestimonialCardsSlider from "components/cards/qTestimonialCardsSlider";
import qShare from "components/cards/qShare";
import qCertificateSlider from "components/doctor/qCertificateSlider";
import qSectionHeader from "components/headers/qSectionHeader";
import qStoryCard from "components/cards/qStoryCard";
import qVideoSlider from "components/cards/qVideoSlider";
import qPhotoGallerySlider from "components/cards/qPhotoGallerySlider";
import qDoctorSpeakCard from "components/doctor/qDoctorSpeakCard";
import qPostCard from "components/cards/qPostCard";
import qAppointmentButton from "components/forms/qAppointmentButton";

export default {
  name: "Doctor",
  components: {
    qPageHeader,
    qActionCard,
    qTestimonialCardsSlider,
    qShare,
    qCertificateSlider,
    qSectionHeader,
    qStoryCard,
    qVideoSlider,
    qPhotoGallerySlider,
    qDoctorSpeakCard,
    qPostCard,
    qAppointmentButton
  },
  data() {
    return {
      schema: {
        "@context": "https://schema.org",
        "@type": "NewsArticle",
        "headline": this.$store.state.doctorData.name,
        "image": [
          this.$store.state.doctorData.avatar,
        ],
        "publisher": {
          "@type": "Organization",
          "name": "Sanad",
          "logo": {
            "@type": "ImageObject",
            "url": `${this.$store.state.siteURL}/img/logo.png`
          }
        }
      }
    }
  },


  preFetch({store, currentRoute}) {
    return store.dispatch('fetchDoctorData', currentRoute.params.slug)
  },
  computed: {
    doctorData() {
      return this.$store.state.doctorData
    }
  },

  meta() {
    let metaData = this.$store.state.doctorData
    return {
      title: metaData.name,
      meta: {
        description: {
          name: "description",
          content: metaData.short_description,
        },
        ogType: {
          property: "og:type",
          content: "website",
        },
        ogTitle: {
          property: "og:title",
          content: metaData.name,
        },
        ogUrl: {
          property: "og:url",
          content: `${this.$store.state.siteURL}/doctor/${metaData.slug}`,
        },
        ogDescription: {
          property: "og:description",
          content: metaData.short_description,
        },
        ogImage: {
          property: "og:image",
          content: metaData.avatar,
        }
      },
    }
  }
}
</script>

<style lang="sass">

</style>
