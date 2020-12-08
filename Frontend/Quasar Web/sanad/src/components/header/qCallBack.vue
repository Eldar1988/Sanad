<template>
  <div>
    <q-btn
      outline
      size="md"
      rounded
      color="white"
      class="text-weight-bold q-mr-lg hi hide-on-mobile"
      unelevated
      @click="dialog = true"
    >
      Обратный звонок
      <q-icon size="1.7em" name="phone_callback" class="q-ml-sm" />
    </q-btn>
    <q-btn
      size="md"
      rounded
      color="secondary"
      class="text-weight-bold q-mr-lg full-width hide-on-desktop"
      unelevated
      @click="dialog = true"
    >
      Обратный звонок
      <q-icon size="1.7em" name="phone_callback" class="q-ml-sm" />
    </q-btn>

    <q-btn
      rounded
      color="secondary"
      class="shadow-0 text-weight-bold q-mr-lg hide-on-mobile"
      unelevated
      @click="dialog = true"
    >
      Консултация
      <q-icon size="1.7em" name="support_agent" class="q-ml-sm" />
    </q-btn>
    <q-btn
      rounded
      color="primary"
      class="shadow-0 text-weight-bold q-mt-md full-width hide-on-desktop"
      unelevated
      @click="dialog = true"
    >
      Консултация
      <q-icon size="1.7em" name="support_agent" class="q-ml-sm" />
    </q-btn>

    <!--    Форма обратной связи  -->
    <qAppointment
      v-if="dialog"
      @closeDialog="dialog = false"
      :header="'Обратная связь'"
      :is-consult="true"
    />
  </div>
</template>

<script>
import qAppointment from "components/forms/qAppointment";

export default {
  name: "qCallBack",

  components: {
    qAppointment
  },

  data() {
    return {
      dialog: false,
      dialogHeader: "",
      headerCallBack: "Обратный звонок",
      headerConsult: "Консультация",
      callBackName: "",
      callBackPhone: "",
    };
  },

  mounted() {},

  methods: {
    openDialog(header) {
      this.dialog = true;
      this.dialogHeader = header;
    },
  }
};
</script>

<style scoped></style>
