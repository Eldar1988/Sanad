<template>
  <q-page style="min-height: 90vh">
    <script type="text/javascript" v-html="tag"></script>
    <page-header back-route-button title="Вернуться назад" />
    <q-card class="flex container-m flex-center column shadow-0" style="min-height: 60vh">
      <h1 class="text-h5 text-uppercase text-center q-mt-xl">
        Телефоны<br> горячей линии
      </h1>

      <q-list separator style="width: 300px" class="q-mt-lg">
        <q-item
          v-for="(phone, index) in phones"
          :key="index"
          clickable
        >
          <q-item-section class="q-pl-md text-bold text-h6 text-center">
            <a :href="`tel:${phone}`" class="text-dark">{{ phone }}</a>
          </q-item-section>
        </q-item>
      </q-list>

      <q-btn
        label="Написать на whatsapp"
        color="positive"
        stretch unelevated
        style="max-width: 300px"
        class="q-mx-auto q-mt-lg q-px-md text-bold letter-1"
        type="a"
        href="https://wa.me/77015425048"
      />
      <div class="text-center q-pt-lg">
        <q-btn
          flat dense
          label="Закрыть"
          icon="close"
          color="grey-8"
          stretch unelevated outline
          style="max-width: 120px"
          class="q-mx-auto q-px-md"
          @click="$router.go(-1)"
        />
      </div>
    </q-card>



    <page-footer />
  </q-page>
</template>

<script>
import PageFooter from "components/footer/page-footer";
import PageHeader from "components/utils/page-header";
export default {
  name: "Phone",
  components: {PageHeader, PageFooter},
  computed: {
    phones() {
      return this.$store.getters.getMainInfo.contacts.phones.split(',')
    }
  },
  data() {
    return {
      tag: "gtag('event', 'conversion', {'send_to': 'AW-385275721/LQxSCJrY8fQCEMmu27cB'});"
    }
  },
}
</script>

<style scoped>

</style>
