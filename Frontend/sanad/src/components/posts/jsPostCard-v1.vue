<template>
<div>
  <q-card
    square
    class="shadow-0"
  >
    <router-link :to="`/post/${post.slug}`" title="Подробнее...">
      <q-img :src="post.miniature" class="action-card-image" :title="post.title" :alt="post.title + ' фото'">
        <p class="action-text q-pa-sm">
          <span class="action-title text-bold text-uppercase text-dark card-title">{{ post.title }}</span>
        </p>
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
      type: Array,
      default: null
    }
  }
}
</script>

<style lang="sass">
.action-text
  position: absolute
  bottom: 0
  left: 0
  right: 0
  background: rgba(255,255,255,.9) !important

.action-card-image
  height: 220px
</style>
