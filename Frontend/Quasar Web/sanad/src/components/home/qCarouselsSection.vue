<template>
  <div class="row" style="margin-top: 30px">

    <!--  Статьи    -->
    <div class="col-12 col-md-4" v-if="posts">
      <qSectionSmallHeader header="Статьи"/>
      <q-carousel
        animated
        v-model="postsSlide"
        navigation swipeable
        autoplay=""
        infinite navigation-position="top"
        class="home-carousels"
      >
        <q-carousel-slide v-for="post in posts" :key="post.id"
                          :name="post.id">
          <qPostCard :post="post"/>
        </q-carousel-slide>
      </q-carousel>
    </div>
    <!--  ===================   -->
    <!--  Акции    -->
    <div class="col-12 col-md-4" v-if="actions">
      <qSectionSmallHeader header="Акции"/>
      <q-carousel
        animated
        v-model="actionsSlide"
        navigation swipeable
        autoplay=""
        infinite navigation-position="top"
        class="home-carousels"
      >
        <q-carousel-slide v-for="post in actions" :key="post.id"
                          :name="post.id">
          <qActionCardSecondary :post="post"/>
        </q-carousel-slide>
      </q-carousel>
    </div>
    <!--    ===================   -->
    <!--  Истории    -->
    <div class="col-12 col-md-4" v-if="stories">
      <qSectionSmallHeader header="Истории выздоравления"/>
      <q-carousel
        animated
        v-model="storiesSlide"
        navigation swipeable
        autoplay=""
        infinite navigation-position="top"
        class="home-carousels"
      >
        <q-carousel-slide v-for="post in stories" :key="post.id"
                          :name="post.id">
          <qPostCard :post="post" isStory/>
        </q-carousel-slide>
      </q-carousel>
    </div>
    <!--    ===================   -->
  </div>
</template>

<script>
import qPostCard from "components/cards/qPostCard";
import qActionCardSecondary from "components/cards/qActionCardSecondary";
import qSectionSmallHeader from "components/headers/qSectionSmallHeader";

export default {
  name: "qCarouselsSection",
  components: {
    qPostCard,
    qActionCardSecondary,
    qSectionSmallHeader
  },
  data() {
    return {
      postsSlide: this.$store.state.homeData[4][0].id,
      actionsSlide: this.$store.state.homeData[5][0].id,
      storiesSlide: this.$store.state.homeData[6][0].id
    }
  },
  computed: {
    posts() {
      return this.$store.state.homeData[4]
    },
    actions() {
      return this.$store.state.homeData[5]
    }
    ,
    stories() {
      return this.$store.state.homeData[6]
    }
  }
}
</script>

<style lang="sass">
.home-carousels
  height: 500px

@media screen and (max-width: 800px)
  .home-carousels
    height: 350px

</style>
