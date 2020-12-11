<template>
  <q-page class="q-pa-md">
    <!--  Заголовок страницы   -->
    <qPageHeader :header="title" :subtitle="description" :image="image"/>
    <!--  ======================   -->
    <!--  Список акций   -->
    <section>
      <div class="row q-mt-lg justify-center">
        <div class="col-lg-3 col-md-4 col-sm-6 col-12 pa-5" v-for="post in news" :key="post.id">
          <qPostCard :post="post"/>
        </div>
      </div>
    </section>
    <!--  ===============   -->
  </q-page>
</template>

<script>
import qPageHeader from "components/headers/qPageHeader";
import qPostCard from "components/cards/qPostCard";

export default {
  name: "Actions",
  components: {
    qPageHeader,
    qPostCard
  },
  computed: {
    title() {
      return this.$store.state.homeData[0].news_title
    },
    description() {
      return this.$store.state.homeData[0].news_description
    },
    image() {
      return this.$store.state.homeData[0].news_image
    },
    news() {
      return this.$store.state.news
    }
  },
  preFetch ({store}) {
    return store.dispatch('fetchNewsData')
  },
  meta() {
    let metaData = this.$store.state.homeData[0]
    return {
      title: metaData.news_title,
      meta: {
        description: {
          name: "description",
          content: metaData.news_description,
        },
        ogType: {
          property: "og:type",
          content: "website",
        },
        ogTitle: {
          property: "og:title",
          content: metaData.news_title,
        },
        ogUrl: {
          property: "og:url",
          content: `${this.$store.state.siteURL}/news`,
        },
        ogDescription: {
          property: "og:description",
          content: metaData.news_description,
        },
        ogImage: {
          property: "og:image",
          content: metaData.news_image,
        }
      },
    }
  }
}
</script>

<style scoped>

</style>
