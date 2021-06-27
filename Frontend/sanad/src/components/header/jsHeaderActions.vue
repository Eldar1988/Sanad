<template>
<div class="h-60">
  <div class="fit">
    <div class="flex fit">
      <q-btn
        color="dark"
        text-color="dark"
        label=""
        icon="lab la-instagram"
        class="grey-gradient q-card--bordered mb--1"
        no-caps unelevated stretch
        size="16px"
        type="a"
        href="https://www.instagram.com/klinika_sanad/"
      />
      <call-back :outlined="false" :flat="false" text-color="dark" classes="q-card--bordered grey-gradient mb--1 ml--1"/>
      <q-btn
        color="dark"
        text-color="dark"
        label=""
        icon="eva-phone-outline"
        class="grey-gradient q-card--bordered ml--1 mb--1"
        no-caps unelevated stretch
      >
        <q-menu square>
        <q-list separator>
          <q-item
            clickable
            v-for="(phone, index) in phones"
            :key="index"
          >
            <q-btn
              class="full-width"
              type="a"
              :label="phone"
              flat
              color="dark"
              :href="`tel:${phone}`"
            />
          </q-item>
        </q-list>
        </q-menu>
      </q-btn>
    </div>
  </div>
</div>

</template>

<script>
import CallBack from "components/header/callBack";
export default {
  name: "jsHeaderActions",
  components: {CallBack},
  computed: {
    phones() {
      return this.$store.getters.getMainInfo.contacts.phones.split(',')
    }
  }
}
</script>

<style scoped>

</style>
