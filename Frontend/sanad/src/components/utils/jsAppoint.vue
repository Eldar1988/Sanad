<template>
<q-dialog
  v-model="appDialog"
>
  <q-card
    style="width: 500px; max-width: 100%"
    square
    class="flex column"
  >
    <q-toolbar class="bg-primary text-white">
      <q-toolbar-title>Запись на прием</q-toolbar-title>
      <q-btn icon="close" dense flat @click="closeDialog"/>
    </q-toolbar>

    <q-card-section style="width: 430px; max-width: 95%; margin: auto" class="">
      <p class="text-subtitle1 q-py-lg">Для записи на прием необходимо заполнить форму.</p>
      <div class="q-mt-md">
        <q-input
          v-model="formData.name"
          outlined
          label="Ваше имя*"
          :error="nameError"
          error-message="Это обязательное поле"
        />
        <q-input
          v-model="formData.phone"
          outlined
          type="tel"
          prefix="+7 "
          mask="### ### ####"
          label="Номер телефона*"
          :error="nameError"
          error-message="Это обязательное поле"
        />
        <q-input
          outlined
          v-model="formData.comment"
          label="Дополнительные пожелания (необязательно)" stack-label
          type="textarea"
        />
      </div>

      <q-btn
        label="Отправить"
        class="full-width q-py-sm q-mt-md"
        unelevated
        color="negative"
        :loading="loading"
        @click="createAppoint"
      />
    </q-card-section>
  </q-card>
</q-dialog>
</template>

<script>
import notifier from "src/utils/notifier";

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
      loading: false,
      nameError: false,
      phoneError: false,
      formData: {
        name: '',
        phone: '',
        comment: '',
        doctor: ''
      }
    }
  },
  methods: {
    closeDialog () {
      this.$store.dispatch('changeAppointDialog')
    },
    async createAppoint () {
      this.loading = true
      const data = this.formData
      if (!data.name) {
        this.nameError = true
        this.loading = false
        return null
      }

      if (!data.phone) {
        this.phoneError = true
        this.loading = false
        return null
      }

      await this.$axios.post(`${this.$store.getters.getServerURL}/clinic/create_appointment/`,{
        name: data.name,
        phone: data.phone,
        comment: data.comment,
        doctor: parseInt(this.$route.query.doctorId) || null
      }).then(response => {
        notifier('Спасибо! Ваша заявка принята.', 'positive')
      }).finally(
        setTimeout(() => {
          this.loading = false
          this.closeDialog()
        }, 2000)
      )
    }
  }
}
</script>

<style scoped>

</style>
