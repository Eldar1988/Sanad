<template>
<q-dialog
  v-model="appDialog"
>
  <q-card
    style="width: 500px; max-width: 100%"
    square
  >
    <q-toolbar class="bg-primary text-white">
      <q-toolbar-title>Запись на прием</q-toolbar-title>
      <q-btn icon="close" dense flat @click="closeDialog"/>
    </q-toolbar>

    <q-card-section>
      <p class="text-subtitle1 q-pt-md">Для записи на прием необходимо форму.</p>
      <div class="q-mt-md">
        <q-input
          v-model="formData.name"
          label="Ваше имя*"
          :error="nameError"
          error-message="Это обязательное поле"
        />
        <q-input
          v-model="formData.phone"
          label="Номер телефона*"
          :error="nameError"
          error-message="Это обязательное поле"
        />
      </div>

      <q-btn
        label="Отправить"
        class="full-width q-py-sm q-mt-md"
        stretch outline
        color="primary"
      />
    </q-card-section>
  </q-card>
</q-dialog>
</template>

<script>
export default {
  name: "jsAppoint",
  created() {

  },
  computed: {
    appDialog () {
      return this.$store.getters.getAppointDialog
    }
  },
  data() {
    return {
      nameError: false,
      phoneError: false,
      formData: {
        name: '',
        phone: '',
        doctor: this.$route.query.doctorId || null
      }
    }
  },
}
</script>

<style scoped>

</style>
