<template>
<div>
  <q-page style="min-height: 90vh">
    <q-card class="flex flex-center column shadow-0" style="min-height: 80vh">
      <h1 class="text-h6 text-uppercase text-bold">
        Спасибо за вашу заявку!
      </h1>
      <p class="q-py-lg text-center text-subtitle1">Наш специалист свяжется с вами <br>для уточнения времени<br> и деталей приема.</p>

      <q-btn
        label="На главную"
        color="primary"
        stretch unelevated outline
        style="max-width: 300px"
        class="q-mx-auto q-mt-lg q-px-md"
        to="/"
      />
    </q-card>

    <page-footer />
  </q-page>

</div>
</template>

<script>
import PageFooter from "components/footer/page-footer";
export default {
  name: "Thanks",
  components: {PageFooter},
  data() {
    return {
      dialog: true
    }
  },
}
</script>

<style lang="sass">
.thanks-page
  position: fixed
  top: 0
  left: 0
  right: 0
  bottom: 0
  z-index: 100

</style>
