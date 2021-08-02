<template>
  <q-page>
    <page-header title="Видео"/>
    <div class="container-m">
      <videos-grid/>
    </div>
    <page-footer />
  </q-page>
</template>

<script>
import PageHeader from "components/utils/page-header";
import VideosGrid from "components/videos/videos-grid";
import PageFooter from "components/footer/page-footer";

export default {
  name: "videos",
  components: {PageFooter, VideosGrid, PageHeader}
}
</script>

<style scoped>

</style>
