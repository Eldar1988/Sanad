<template>
  <q-page class="">
    <div class="container">
      <section>
        <js-slider/>
      </section>
      <section class="q-mt-lg ml-15-m">
        <js-section-title title="Акции клиники"/>
        <js-actions-slider class="q-mt-md"/>
      </section>
    </div>
  </q-page>
</template>

<script>
import JsSlider from "components/home/jsSlider";
import JsActionsSlider from "components/sliders/jsActionsSlider";
import JsSectionTitle from "components/utils/jsSectionTitle";

export default {
  name: 'PageIndex',
  components: {JsSectionTitle, JsActionsSlider, JsSlider}
}
</script>
