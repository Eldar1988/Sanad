<template>
<div>
  <div class="hide-on-mobile">
    <div class="flex">
      <call-back label="Запись на прием"/>
      <q-btn-dropdown
        color="dark"
        class="q-ml-md"
        label="Телефоны"
        icon="eva-phone-outline"
        no-caps unelevated flat stretch dense
        content-class="br-0 q-mt-sm"
      >
        <q-list separator>
          <q-item
            clickable
            v-for="(phone, index) in phones"
            :key="index"
          >
              <q-btn
                class="full-width"
                color="dark"
                type="a"
                :label="phone"
                flat
                :href="`tel:${phone}`"
              />
          </q-item>
        </q-list>
      </q-btn-dropdown>
    </div>
  </div>
  <div class="hide-on-desktop">
    <div class="flex">
      <call-back :outlined="false" :flat="true"/>
      <q-btn-dropdown
        color="dark"
        class="q-ml-md"
        label=""
        icon="eva-phone-outline"
        no-caps unelevated stretch flat dense
        content-class="br-0 q-mt-sm"
      >
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
      </q-btn-dropdown>
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
  },
  mounted() {
    console.log(this.phones)
  }
}
</script>

<style scoped>

</style>
