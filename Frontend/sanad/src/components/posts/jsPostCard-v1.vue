<template>
<div>
  <q-card
    square
    class="shadow-0"
  >
    <router-link :to="`/post/${post.slug}`" title="Подробнее...">
      <q-img :src="post.miniature" class="action-card-image" :title="post.title" :alt="post.title + ' фото'">
        <span class="action-text q-pa-sm">
          {{ post.title }}
        </span>
        <template v-slot:loading>
          <q-skeleton class="full-width action-card-image" square/>
        </template>
      </q-img>
    </router-link>
  </q-card>
</div>
</template>

<script>
export default {
  name: "jsPostCard-v1",
  props: {
    post: {
      type: Object,
      default: () => {}
    }
  }
}
</script>

<style lang="sass">
.action-card-image
  height: 220px
</style>
