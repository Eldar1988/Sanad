<template>
  <div>

  <q-card class="my-card">
    <q-card-section horizontal>
      <q-img
        class="col-5"
        :src="direction.icon"
        @click="goTo(direction.slug)"
        spinner-color="primary"
      />
      <q-card-section>
        <div class="row no-wrap items-center">
          <qCardHeader :header="direction.title" :link="`/directions/${direction.slug}`" />
        </div>
        <p class="text-dark">
          {{ direction.short_description|textToLength }}
        </p>
<!--        Кнопки для дестопов   -->
        <q-card-actions class="justify-between hide-on-mobile q-mt-sm" style="margin-right: 10px">
          <q-btn flat color="secondary" icon="event" size="md" @click="dialog = true">
            Записаться
          </q-btn>
          <q-btn flat color="primary" icon="arrow_right" :to="`directions/${direction.slug}`">
            Подробнее
          </q-btn>
        </q-card-actions>
<!--        =====================   -->
      </q-card-section>
    </q-card-section>

<!--    Кнопки для мобильных  -->
    <q-card-actions class="justify-around hide-on-desktop d-flex-important pa-5">
      <q-btn flat color="secondary" icon="event" @click="dialog = true">
        Записаться
      </q-btn>
      <q-btn flat color="primary" icon="arrow_right" :to="`directions/${direction.slug}`">
        Подробнее
      </q-btn>
    </q-card-actions>
<!--    =====================   -->
  </q-card>
  <qAppointment v-if="dialog"
                @closeDialog="dialog = false"
                :direction="direction"
                :header="`Запись на прием - ${direction.title}`"
                :isAppointment="true"
                :btntext="'Записаться'"
  />
  </div>



</template>

<script>
import qCardHeader from "components/headers/qCardHeader";
import textToLength from "src/filters/textToLength";
import qAppointment from "components/forms/qAppointment";

export default {
  name: "qDirectionCard",

  props: ['direction'],

  components: {
    qCardHeader,
    qAppointment
  },

  filters: {
    textToLength
  },

  data () {
    return {
      dialog: false
    }
  },

  methods: {
    // Переход на страницу направления
    goTo(slug) {
      this.$router.push(`/directions/${slug}`)
    }
  }
}
</script>

<style scoped>

</style>
