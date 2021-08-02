<template>
  <div class="q-py-lg bg-info">
    <div class="container-m">
      <div class="flex items-center">
        <q-btn
          color="white"
          size="sm"
          v-if="backRouteButton"
          icon="las la-angle-left"
          text-color="warning"
          class="q-mr-md"
          padding="5px"
          dense stretch unelevated
          @click="routeBack"
        />
        <h2 class="page-section-title text-uppercase letter-1">
          {{ title }}
        </h2>
      </div>
    </div>
  </div>
</template>

<script>
import SectionTitle from "components/utils/section-title";

export default {
  name: "page-header",
  props: {
    title: String,
    backRouteButton: {
      type: Boolean,
      default: false
    },
    backURL: String
  },
  methods: {
    routeBack () {
      if (this.backURL) {
        this.$router.push(this.backURL)
      } else {
        this.$router.go(-1)
      }
    }
  }
}
</script>

<style lang="sass">
.page-section-title
  font-size: 18px
  color: $dark

@media screen and (max-width: 650px)
  .page-section-title
    font-size: 14px
</style>
