<template>
  <div>
    <q-card class="my-card">
      <q-img :src="doctor.avatar" :title="doctor.name" height="300px" spinner-color="secondary"/>
      <q-card-section>
        <!--      Кнопка детали доктора   -->
        <q-btn
          fab
          color="primary"
          icon="arrow_forward"
          class="absolute"
          style="top: 0; right: 12px; transform: translateY(-50%);"
          title="Подробнее"
          :to="`/doctor/${doctor.slug}`"
        />
        <!--      =======================   -->
        <!--      Имя и рейтинг доктора   -->
        <div class="row no-wrap items-center">
          <div class="col ellipsis">
            <qCardHeader :header="doctor.name" :link="`/doctor/${doctor.slug}`"/>
          </div>
        </div>
      </q-card-section>
      <!--      ====================   -->
      <!--    Краткое описание   -->
      <q-card-section class="q-pt-none">
        <p class="text-dark">
          {{ doctor.short_description|textToLength }}
        </p>
      </q-card-section>
      <!--  ================    -->
      <q-separator/>
      <!--      Кнопки   -->
      <q-card-actions class="justify-between" style="margin: 0 10px 0 0">
        <div>
          <q-btn flat color="secondary" round icon="event" @click="dialog = true" title="Запись на прием"/>
          <q-btn flat color="secondary" @click="dialog = true" title="Запись на прием">
            Записаться
          </q-btn>
        </div>
        <div>
          <q-btn color="primary" flat :to="`/doctor/${doctor.slug}`">Подробнее</q-btn>
        </div>
      </q-card-actions>
      <!--      ==============   -->
      <!--      Запись на прием (компонент)   -->
      <qAppointment
        v-if="dialog"
        @closeDialog="dialog = false"
        :doctor="doctor"
        :header="`Запись на прием - ${doctor.name}`"
        :is-appointment="true"
        :btn-text="'Записаться'"
      />
    </q-card>

  </div>
</template>

<script>
import qCardHeader from "components/headers/qCardHeader";
import textToLength from "src/filters/textToLength";
import qAppointment from "components/forms/qAppointment";

export default {
  name: "qDoctorCard",
  components: {
    qCardHeader,
    qAppointment
  },
  filters: {
    textToLength
  },
  props: ['doctor'],
  data() {
    return {
      dialog: false
    }
  }
}
</script>

<style scoped>

</style>
