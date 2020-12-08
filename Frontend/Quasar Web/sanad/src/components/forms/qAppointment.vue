<template>
  <q-dialog v-model="dialog" persistent>
    <q-layout view="Lhh lpR fff" container class="bg-white">

      <q-header class="bg-primary">
        <q-toolbar>
          <q-toolbar-title>{{ header }}</q-toolbar-title>
          <q-btn flat round dense icon="close" @click="$emit('closeDialog')"/>
        </q-toolbar>
      </q-header>

      <q-footer class="bg-white text-white">
        <q-card-actions class="text-primary" style="margin: 0 10px 10px">
          <q-btn :label="btnText"
                 rounded
                 unelevated
                 icon-right="done_outline"
                 color="secondary" class="full-width"/>
        </q-card-actions>
      </q-footer>

      <q-page-container>
        <q-page padding>

          <q-card-section class="q-pt-none">
            <p style="font-size: 16px" class="text-dark">
              Пожалуйста, заполните форму ниже<br>
              Мы свяжемся с вами в ближайшее время
            </p>
            <q-input v-model="name" color="secondary" label="Ваше имя"/>
            <q-input v-model="phone" color="secondary" type="number" label="Номер телефона"/>

            <div v-if="isAppointment">
              <q-input v-model="date" color="secondary" mask="date" label="Удобная дата приема"/>
              <q-date v-model="date" class="shadow-0" :locale="myLocale" minimal today-btn
                      style="width: 100%; margin-top: 25px"/>
            </div>
            <q-input v-if="isConsult"
                     color="secondary"
                     class="q-mt-lg"
                     v-model="comment"
                     label="Комментарий (необязательно)"
                     type="textarea"
            />
          </q-card-section>
        </q-page>
      </q-page-container>
    </q-layout>
  </q-dialog>
</template>

<script>
export default {
  name: "qAppointment",

  props: {
    doctor: {
      type: Object,
      default: null
    },
    direction: {
      type: Object,
      default: null
    },
    header: {
      type: String,
      default: 'Заявка'
    },
    btnText: {
      type: String,
      default: 'Оптравить'
    },
    isConsult: {
      type: Boolean,
      default: false
    },
    isAppointment: {
      type: Boolean,
      default: false
    }
  },

  data() {
    return {
      dialog: true,
      name: '',
      phone: '',
      locale: '',
      date: '',
      comment: '',
      myLocale: {
        days: 'Понедельник_Вторник_Среда_Четверг_Пятница_Суббота_Воскресенье'.split('_'),
        daysShort: 'Пн_Вт_Ср_Чт_Пт_Сб_Вс'.split('_'),
        months: 'Январь_Февраль_Март_Апрель_Май_Июнь_Июль_Август_Сентябрь_Октябрь_Ноябрь_Декабрь'.split('_'),
        monthsShort: '01_02_03_04_05_06_07_08_09_10_11_12'.split('_'),
        firstDayOfWeek: 1
      }
    }
  },

  mounted() {
    // Дата по умолчанию в форме
    let toDayDate = new Date()
    this.date = `${toDayDate.getFullYear()}/${toDayDate.getMonth() + 1}/${toDayDate.getDate() + 1}`
  }
}
</script>

<style scoped>

</style>
