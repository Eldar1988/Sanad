<template>
  <q-page>
    <qSlider :slides="slides"/>
    <qDirections />
  </q-page>
</template>

<script>
import qSlider from 'components/home/qSlider'
import qDirections from 'components/home/qDirections'

export default {
  components: {
    qSlider,
    qDirections
  },
  name: "PageIndex",
  preFetch({ store }) {
    return store.dispatch("fetchHomeData");
  },
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
