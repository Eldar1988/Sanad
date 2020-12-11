<template>
  <article>
    <router-link :to="`/post/${post.slug}`">
      <q-img
        :src="post.photo"
        class="rounded-borders home-slider-height img-overlay-2"
        spinner-color="secondary"
        :title="post.title"
      >
        <div class="page-header-text text-center text-white">
          <h6 class="text-h5">
            {{ post.title }}
          </h6>
        </div>

      </q-img>
    </router-link>
  </article>
</template>

<script>
export default {
  name: "qActionCardSecondary",
  props: {
    post: {
      type: Object,
      default: null
    }
  }
}
</script>

<style>

</style>
