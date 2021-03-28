<template>
  <div class="q-mt-md">
    <q-list separator>
      <q-item
        v-for="post in posts"
        :key="post.id"
        :to="story ? `/story/${post.slug}` : `/post/${post.slug}`"
        class="flex"
        style="align-items: center"
        :title="`Читать далее...`"
        manual-focus
      >
        <p class="sub_title ml-15-m">{{ post.title }}</p>
      </q-item>
      <q-item
        :to="story ? `/stories` : `/posts`"
        class="flex"
        style="align-items: center"
        manual-focus
      >
        <p class="sub_title ml-15-m text-primary text-bold q-pt-lg">{{ story ? `Читать все истории` : `Читать все статьи`}} >></p>
      </q-item>
    </q-list>
  </div>
</template>

<script>
export default {
  name: "jsPostsList",
  props: {
    posts: {
      type: Array,
      default: null
    },
    story: {
      type: Boolean,
      default: false
    }
  }
}
</script>

<style lang="sass">

</style>
