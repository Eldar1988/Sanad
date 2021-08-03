<template>
  <q-card
    square
    class="shadow-0 post-card-v2 bg-info"
  >
    <div>
      <q-img :src="post.miniature" height="120" :title="post.title + '. Фото'" :alt="post.title + '. Фото'">
        <template v-slot:loading>
          <q-skeleton class="full-width" height="120" square/>
        </template>
      </q-img>
    </div>
    <div>
      <router-link :to="`/post/${post.slug}`" title="Читать далее..." class="text-dark">
      <p class="sub_title ellipsis-3-lines">
        {{ post.title }} wdawdwad wdw da wdwad awd awdawd awdwa
      </p>
<!--        <q-icon  name="las la-angle-right" color="warning" class="text-right"/>-->
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
