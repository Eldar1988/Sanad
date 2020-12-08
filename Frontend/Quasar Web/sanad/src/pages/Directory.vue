<template>
  <q-page class="q-pa-md" itemtype="http://schema.org/Product" itemscope>

    <!--Микроразметка   -->
    <div>

      <meta itemprop="name" :content="directionData.title"/>
      <link itemprop="image" :href="directionData.image"/>
      <meta itemprop="description" :content="directionData.short_description"/>
      <div itemprop="offers" itemtype="http://schema.org/Offer" itemscope>
        <link itemprop="url" :href="`${this.$store.state.siteUrl}/directions/${directionData.slug}`"/>
        <meta itemprop="priceCurrency" content="KZT"/>
        <meta itemprop="price" content="от 5000"/>
        <meta itemprop="priceValidUntil" content="2020-12-05"/>
      </div>
<!--      <div itemprop="aggregateRating" itemtype="http://schema.org/AggregateRating" itemscope>-->
<!--        <meta itemprop="reviewCount" content="569"/>-->
<!--        <meta itemprop="ratingValue" content="4.8"/>-->
<!--      </div>-->
      <div itemprop="review" itemtype="http://schema.org/Review" itemscope>
        <div itemprop="author" itemtype="http://schema.org/Person" itemscope>
          <meta itemprop="name" content="Министерство здравохранения"/>
        </div>
        <div itemprop="reviewRating" itemtype="http://schema.org/Rating" itemscope>
          <meta itemprop="ratingValue" content="5"/>
          <meta itemprop="bestRating" content="5"/>
        </div>
      </div>
      <meta itemprop="sku" content="0446310786"/>
      <div itemprop="brand" itemtype="http://schema.org/Brand" itemscope>
        <meta itemprop="name" content="Sanad"/>
      </div>

    </div>
    <!--    ==============   -->

    <!--    Заголовк с фоновой картинкой   -->
    <header>
      <q-img
        :src="directionData.image"
        class="rounded-borders home-slider-height shadow-15 img-overlay"
        spinner-color="secondary"
        :title="directionData.title"
      >
        <h1
          class="text-h3 slider-text block text-center text-white"
          style="width: 100%"
        >{{ directionData.title }}</h1>
      </q-img>
    </header>
    <!--    ==========================   -->
    <article>
      <!--Краткое описаие -->
      <div class="q-mt-xl text-dark">
        <h2 class="font-weight-500 short-description text-h6">
          {{ directionData.short_description }}
        </h2>
      </div>
      <!--    ======================   -->
      <!--    Полное описание   -->
      <div class="description q-mt-lg text-dark" v-html="directionData.description">
      </div>
      <!--    ==========================   -->
    </article>
    <!--    Врачи направления   -->
    <qSectionHeader :header="'Специалисты'"/>
    <div class="row q-mt-lg justify-center">
      <div class="col-lg-3 col-md-4 col-sm-6 col-12 pa-5" v-for="doctor in directionDoctors" :key="doctor.id">
        <article>
          <qDoctorCard :doctor="doctor"/>
        </article>
      </div>
    </div>
    <!--    =====================   -->
    <!--    Этапы лечения -->
    <qSectionHeader header="Этапы лечения"/>
    <div class="row justify-center q-mt-lg">
      <div class="col-lg-3 col-md-6 pa-5 col-sm-6" v-for="healing in directionHealings" :key="healing.id">
        <qTreatmentStage :healing="healing"/>
      </div>
    </div>
    <!--    ==================   -->
    <!--   Отзывы   -->
    <qTestimonialCardsSlider :reviews="directionReviews"/>
    <!--    =================   -->
    <!--    Истории выздоравления   -->
    <qSectionHeader header="Истории выздоравления"/>
    <div class="row q-mt-lg justify-center">
      <div class="col-lg-3 col-md-4 col-sm-6 pa-5" v-for="story in directionStories" :key="story.id">
        <article>
          <qStoryCard :story="story"/>
        </article>
      </div>
    </div>
  </q-page>


</template>

<script>
import qSectionHeader from "components/headers/qSectionHeader";
import qDoctorCard from "components/doctor/qDoctorCard";
import qTreatmentStage from "components/direction/qTreatmentStage";
import qTestimonialCardsSlider from "components/cards/qTestimonialCardsSlider";
import qStoryCard from "components/cards/qStoryCard";

export default {
  name: "Directory",
  components: {
    qSectionHeader,
    qDoctorCard,
    qTreatmentStage,
    qTestimonialCardsSlider,
    qStoryCard
  },

  data() {
    return {
      schema: ''
    }
  },
  mounted() {
    console.log(this.$route.params.slug)
  },

  computed: {
    // Информация о направлении
    directionData() {
      return this.$store.state.directionData[0]
    },
    // Специалисты направления
    directionDoctors() {
      return this.$store.state.directionData[1]
    },
    // Этапы лечения
    directionHealings() {
      return this.$store.state.directionData[2]
    },
    // Отзывы
    directionReviews() {
      return this.$store.state.directionData[3]
    },
    // Истории болезни
    directionStories() {
      return this.$store.state.directionData[4]
    },
  },

  preFetch({store, currentRoute}) {
    return store.dispatch('fetchDirectionData', currentRoute.params.slug)
  },

  meta() {
    let metaData = this.$store.state.directionData[0]
    return {
      title: metaData.title,
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
          content: metaData.title,
        },
        ogUrl: {
          property: "og:url",
          content: `${this.$store.state.siteURL}/directions/${metaData.slug}`,
        },
        ogDescription: {
          property: "og:description",
          content: metaData.short_description,
        },
        ogImage: {
          property: "og:image",
          content: metaData.image,
        }
      },
    };
  },

}
</script>

<style scoped>

</style>
