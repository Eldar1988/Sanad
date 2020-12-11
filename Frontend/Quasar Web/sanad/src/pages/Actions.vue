<template>
<q-page class="q-pa-md">
<!--  Заголовок страницы   -->
  <qPageHeader :header="title" :subtitle="description" :image="image"/>
<!--  ======================   -->
<!--  Список акций   -->
  <section>
    <div class="row q-mt-lg justify-center">
      <div class="col-lg-3 col-md-4 col-sm-6 col-12 pa-5" v-for="post in actions" :key="post.id">
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
      return this.$store.state.homeData[0].action_title
    },
    description() {
      return this.$store.state.homeData[0].action_description
    },
    image() {
      return this.$store.state.homeData[0].action_image
    },
    actions() {
      return this.$store.state.actions
    }
  },
  preFetch ({store}) {
    return store.dispatch('fetchActionsData')
  },
  meta() {
    let metaData = this.$store.state.homeData[0]
    return {
      title: metaData.action_title,
      meta: {
        description: {
          name: "description",
          content: metaData.action_description,
        },
        ogType: {
          property: "og:type",
          content: "website",
        },
        ogTitle: {
          property: "og:title",
          content: metaData.action_title,
        },
        ogUrl: {
          property: "og:url",
          content: `${this.$store.state.siteURL}/actions`,
        },
        ogDescription: {
          property: "og:description",
          content: metaData.action_description,
        },
        ogImage: {
          property: "og:image",
          content: metaData.action_image,
        }
      },
    }
  }
}
</script>

<style scoped>

</style>
