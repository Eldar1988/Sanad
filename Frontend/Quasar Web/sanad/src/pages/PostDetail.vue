<template>
  <q-page class="q-pa-md">
    <script type="application/ld+json" v-html="schema"></script>
    <section>
      <article>
        <!--        Заголовок с картинкой   -->
        <qPageHeader :header="post.title" :image="post.photo"/>
        <!--        =================    -->
        <!--        Краткое описание   -->
        <div class="q-mt-xl text-dark">
          <h2 class="font-weight-500 short-description text-h6">
            {{ post.short_description }}
          </h2>
        </div>
        <!--        =====================    -->
        <!--        Тело поста    -->
        <div class="q-mt-lg text-dark" v-html="post.body"></div>
        <!--        ===================   -->
        <qShare class="q-mt-lg"/>
      </article>
    </section>
    <!--    Читайте также   -->
    <section v-if="posts.length > 0">
      <qSectionHeader :header="moreHeader"/>
      <div class="row q-mt-lg justify-center">
        <div class="col-lg-3 col-md-4 col-sm-6 col-12 pa-5" v-for="post in posts" :key="post.id">
          <qPostCard :post="post"/>
        </div>
      </div>
    </section>
    <!--    ==============   -->
<!--&lt;!&ndash;    Комментарии   &ndash;&gt;-->
<!--    <section v-if="comments.length > 0">-->
<!--      <qSectionHeader header="Комментарии" :badge="comments.length"/>-->
<!--      <div class="row q-mt-lg justify-center">-->
<!--        <div v-for="comment in comments" :key="comment.id" class="text-dark">-->
<!--          <qCommentCard :comment="comment"/>-->
<!--        </div>-->
<!--      </div>-->
<!--    </section>-->
<!--&lt;!&ndash;    ================   &ndash;&gt;-->
  </q-page>
</template>

<script>
import qPageHeader from "components/headers/qPageHeader";
import qShare from "components/cards/qShare";
import qSectionHeader from "components/headers/qSectionHeader";
import qPostCard from "components/cards/qPostCard";
// import qCommentCard from "components/cards/qCommentCard";

export default {
  name: "PostDetail",
  components: {
    qPageHeader,
    qShare,
    qSectionHeader,
    qPostCard,
    // qCommentCard
  },
  data() {
    return {
      comments: [],
      schema: {
        "@context": "https://schema.org",
        "@type": "NewsArticle",
        "headline": this.$store.state.postDetail[0].title,
        "image": [
          this.$store.state.postDetail[0].photo,
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
  computed: {
    post() {
      return this.$store.state.postDetail[0]
    },
    posts() {
      return this.$store.state.postDetail[1]
    },
    moreHeader() {
      if(this.post.is_action) {
        return `Другие акции`
      } else if(this.post.is_news) {
        return `Другие новости`
      } else {
        return `Читайте также`
      }
    }
  },
  mounted() {
    this.loadComments()
  },
  methods: {
    loadComments() {
      return this.$axios.get(`${this.$store.state.serverUrl}/post_reviews/${this.post.slug}`).then(
        (({data}) => {
          this.comments = data
      })
      )
    }
  },

  preFetch({store, currentRoute}) {
    return store.dispatch('fetchPostData', currentRoute.params.slug)
  },
  meta() {
    let metaData = this.$store.state.postDetail[0]
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
