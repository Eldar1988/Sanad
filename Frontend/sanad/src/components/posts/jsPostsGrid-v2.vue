<template>
<div class="q-mt-lg">
  <div class="posts-grid-v2">
    <div
      v-for="post in posts"
      :key="post.id"
    >
      <js-post-card-v2 :post="post"/>
    </div>
  </div>
</div>
</template>

<script>
import JsPostCardV2 from "components/posts/jsPostCard-v2";
export default {
  name: "jsPostsGrid-v2",
  components: {JsPostCardV2},
  // section Props
  props: {
    posts: {
      type: Array,
      default: null
    }
  }
}
</script>

<style lang="sass">
// section Styles
.posts-grid-v2
  display: grid
  grid-gap: 30px
  grid-template-columns: 1fr 1fr 1fr

@media screen and (max-width: 800px)
  .posts-grid-v2
    grid-template-columns: 1fr
    grid-gap: 20px
</style>
