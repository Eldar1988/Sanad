<template>
  <article>
    <q-card class="my-card" flat bordered>
      <router-link :to="`/story/${story.slug}`">
        <q-img
          :src="story.photo"
          :title="story.title"
          :alt="story.alt"
          height="250px"
          spinner-color="secondray"
        />
      </router-link>
      <q-card-section>
        <!--    Заголовок   -->
        <h5 class="text-h5 q-mb-xs">
          <qCardHeader :header="story.title" :link="`/story/${story.slug}`"/>
        </h5>
        <!--      ==========   -->
        <!--      Описание    -->
        <div class="text-dark">
          <p>{{ story.short_description|textToLength }}</p>
        </div>
        <!--      ===========    -->
      </q-card-section>
      <!--    Кнопки    -->
      <q-card-actions style="margin-left: 10px">
        <q-btn
          color="secondary"
          class="q-px-md"
          label="Читать далее"
          rounded unelevated
          :to="`/story/${story.slug}`"
        />
        <q-space/>
        <q-btn
          color="grey"
          round
          flat
          dense
          icon="keyboard_arrow_right"
          :to="`/story/${story.slug}`"
        />
      </q-card-actions>
      <!--    ================    -->
    </q-card>
  </article>
</template>

<script>
import qCardHeader from "components/headers/qCardHeader";
import textToLength from "src/filters/textToLength";

export default {
  name: "qStoryCard",
  filters: {
    textToLength
  },
  components: {
    qCardHeader
  },
  props: {
    story: {
      type: Object,
      default: null
    }
  }
}
</script>

<style scoped>

</style>
