<template>
  <q-card
    class="shadow-0 doctor-card"
    square
  >
    <q-img :src="doctor.avatar" :ratio="1" spinner-color="info"/>
    <div class="doctor-card-meta flex" style="align-items: center">
      <div>
        <h3 class="sub_title text-uppercase">{{ doctor.name }}</h3>
        <p class="sub_title q-mt-sm text-bold">{{ doctor.specialization }}</p>
        <p class="sub_title q-mt-sm">Стаж работы: {{ doctor.experience }}</p>
        <div>
          <q-btn
            label="Записаться"
            outline stretch unelevated
            color="primary"
            class="full-width q-mt-lg"
            @click="appointToDoctor"
          />
          <q-btn
            label="Подробнее"
            outline stretch unelevated
            color="primary"
            class="full-width q-mt-md"
            @click="goToDoctor"
          />
        </div>
      </div>
    </div>
  </q-card>
</template>

<script>
export default {
  name: "doctor-card",
  props: {
    doctor: {
      type: Object,
      default: () => {
      }
    }
  },
  methods: {
    async appointToDoctor () {
      if (this.doctor.id.toString() !== this.$route.query.doctorId) {
        await this.$router.replace({
          query: {
            doctorId: this.doctor.id
          }
        })
      }
      await this.$store.dispatch('changeAppointDialog')
    },
    goToDoctor () {
      this.$router.push({
        path: `/doctor/${this.doctor.slug}`,
        query: {
          doctorId: this.doctor.id
        }
      })
    }
  },
}
</script>

<style lang="sass">
.doctor-card
  display: grid
  grid-template-columns: 1fr 1fr
  grid-gap: 20px
</style>
