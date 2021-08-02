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
  }
}
</script>

<style scoped>

</style>
