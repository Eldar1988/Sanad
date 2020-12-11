<template>
<q-page class="q-pa-md">
  <section>
    <article>
      <!--        Заголовок с картинкой   -->
      <qPageHeader :header="story.title" :image="story.photo"/>
      <!--        =================    -->
      <!--        Краткое описание   -->
      <div class="q-mt-xl text-dark">
        <h2 class="font-weight-500 short-description text-h6">
          {{ story.short_description }}
        </h2>
      </div>
      <!--        =====================    -->
      <!--        Тело поста    -->
      <div class="q-mt-lg text-dark text-body" v-html="story.body"></div>
      <!--        ===================   -->
      <qShare class="q-mt-lg"/>
    </article>
  </section>
  <!--    Читайте также   -->
  <section v-if="stories.length > 0">
    <qSectionHeader header="Читайте также"/>
    <div class="row q-mt-lg justify-center">
      <div class="col-lg-3 col-md-4 col-sm-6 col-12 pa-5" v-for="post in stories" :key="post.id">
        <qStoryCard :story="post"/>
      </div>
    </div>
  </section>
</q-page>
</template>

<script>
import qPageHeader from "components/headers/qPageHeader";
import qShare from "components/cards/qShare";
import qSectionHeader from "components/headers/qSectionHeader";
import qStoryCard from "components/cards/qStoryCard";

export default {
name: "Story",
  components: {
    qPageHeader,
    qShare,
    qSectionHeader,
    qStoryCard
  },
  computed: {
    story() {
      return this.$store.state.storyDetail[0]
    },
    stories() {
      return this.$store.state.storyDetail[1]
    }
  },
  preFetch({store, currentRoute}) {
    return store.dispatch('fetchStoryData', currentRoute.params.slug)
  },
  meta() {
    let metaData = this.$store.state.storyDetail[0]
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
          content: `${this.$store.state.siteURL}/post/${metaData.slug}`,
        },
        ogDescription: {
          property: "og:description",
          content: metaData.short_description,
        },
        ogImage: {
          property: "og:image",
          content: metaData.photo,
        }
      },
    }
  }
}
</script>

<style scoped>

</style>
