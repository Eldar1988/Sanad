<template>
  <article>
    <router-link :to="isStory ? `/story/${post.slug}` : `/post/${post.slug}`">
    <q-img
      :src="post.photo"
      class="rounded-borders home-slider-height img-overlay"
      spinner-color="secondary"
      :title="post.title"
    >
      <div class="page-header-text text-center text-white">
        <h6 class="text-h5">
          {{ post.title }}
        </h6>
        <div class="flex meta">
          <p class="text-white" style="font-size: 14px">
            <q-icon name="visibility" color="white" />
            {{ post.views }}
          </p>
          <p class="text-white q-pl-md" style="font-size: 14px" v-if="post.reviews">
            <q-icon name="textsms" color="white" />
            {{ post.reviews.length }}
          </p>
        </div>
      </div>

    </q-img>
    </router-link>
  </article>
</template>

<script>
export default {
  name: "qPostCard",
  props: {
    post: {
      type: Object,
      default: null
    },
    isStory: {
      type: Boolean,
      default: false
    }
  }
}
</script>

<style>

</style>
