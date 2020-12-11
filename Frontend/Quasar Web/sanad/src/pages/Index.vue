<template>
  <q-page>
    <!--    Слайдер   -->
    <section>
      <qSlider :slides="slides"/>
    </section>
    <!--    ================   -->
    <!--    Направления   -->
    <section>
      <qDirections/>
    </section>
    <!--    =================   -->
<!--    Карусели   -->
    <section>
      <qCarouselsSection />
    </section>
  </q-page>
</template>

<script>
import qSlider from 'components/home/qSlider'
import qDirections from 'components/home/qDirections'
import qCarouselsSection from "components/home/qCarouselsSection";

export default {
  components: {
    qSlider,
    qDirections,
    qCarouselsSection
  },
  name: "PageIndex",

  computed: {
    slides() {
      return this.$store.state.homeData[1];
    },
  },
  meta() {
    let metaData = this.$store.state.homeData[0]
    return {
      title: metaData.title,
      meta: {
        description: {
          name: "description",
          content: metaData.description,
        },
        ogType: {
          property: "og:type",
          content: "website",
        },
        ogTitle: {
          property: "og:title",
          content: "website",
        },
      },
    };
  },
};
</script>
