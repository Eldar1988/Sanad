<template>
  <q-page>
    <page-header title="Статьи"/>
    <div class="container-m">
      <div class="row q-col-gutter-md q-mt-md">
        <div
          v-for="post in posts"
          :key="post.id"
          class="col-12 col-sm-6 col-md-3 col-lg-3"
        >
          <div class="post-card">
            <router-link :to="`/post/${post.slug}`">
              <q-img :src="post.miniature" no-default-spinner/>
              <h3 class="bg-info q-pa-md ellipsis-3-lines text-dark" style="min-height: 100px"> {{ post.title }} </h3>
            </router-link>
          </div>
        </div>
      </div>
    </div>
    <page-footer/>
  </q-page>
</template>

<script>
import PageHeader from "components/utils/page-header";
import PageFooter from "components/footer/page-footer";

export default {
  name: "Posts",
  components: {PageFooter, PageHeader},
  computed: {
    posts() {
      return this.$store.getters.getHomePosts
    }
  },
  preFetch({store}) {
    return store.dispatch('loadPosts')
  },
  meta() {
    return {
      title: "Медицинские статьи | Клиника SANAD Караганда",
      meta: {
        description: {
          name: "description",
          content: "Медицинские статьи. Клинико-диагностический реабилитационный центр Sanad в Караганде",
        },
        ogType: {
          property: "og:type",
          content: "website",
        },
        ogTitle: {
          property: "og:title",
          content: "Медицинские статьи | Клиника SANAD Караганда",
        },
        ogUrl: {
          property: "og:url",
          content: "https://sanadmed.kz/posts",
        },
        ogDescription: {
          property: "og:description",
          content: "Медицинские статьи. Клинико-диагностический реабилитационный центр SANAD в Караганде",
        },
        ogImage: {
          property: "og:image",
          content: "https://res.cloudinary.com/space-developers/image/upload/v1630987428/cvetogis/logo/logo_e3tgqj.png"
        }
      }
    }
  }
}
</script>

<style scoped>

</style>
