<template>
  <q-card flat bordered class="my-card">
    <q-card-section>
      <h4 class="text-h6">{{comment.name}}</h4>
      <p>{{comment.text}}</p>
      <div class="flex">
        <p class="text-white" style="font-size: 14px">
          <q-icon name="visibility" color="white" />
          {{ post.views }}
        </p>
        <p class="text-white q-pl-md" style="font-size: 14px">
          <q-icon name="textsms" color="white" />
          {{ post.reviews.length }}
        </p>
      </div>
    </q-card-section>
  </q-card>
</template>

<script>
export default {
  name: 'qCommentCard',
  props: {
    comment: {
      type: Object,
      default: null
    },
  },
}
</script>

<style lang="sass">

</style>
