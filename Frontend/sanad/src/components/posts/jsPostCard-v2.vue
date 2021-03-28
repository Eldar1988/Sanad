<template>
  <q-card
    square
    class="shadow-0 post-card-v2"
  >
    <div>
      <q-img :src="post.miniature" height="150px" :title="post.title + '. Фото'" :alt="post.title + '. Фото'">
        <template v-slot:loading>
          <q-skeleton class="full-width" height="150px" square/>
        </template>
      </q-img>
    </div>
    <div>
      <router-link :to="`/post/${post.slug}`" title="Читать далее..." class="text-dark">
      <p class="sub_title q-pa-sm">
        {{ post.title }} <q-icon  name="east" color="primary"/>
      </p>
      </router-link>
    </div>
  </q-card>
</template>

<script>
export default {
  name: "jsPostCard-v2",
  props: {
    post: {
      type: Object,
      default: null
    }
  }
}
</script>

<style lang="sass">
.post-card-v2
  display: grid
  grid-template-columns: 1fr 2fr
  grid-gap: 20px
  align-items: center

@media screen and (max-width: 800px)
  .post-card-v2
    grid-template-columns: 2fr 3fr
</style>
