<template>
<q-page>
  <page-header title="Специалисты"/>
  <div class="container-m">
    <doctor-cards-grid class="q-mt-xl" :doctors="doctors"/>
  </div>
  <page-footer />
</q-page>
</template>

<script>
import PageHeader from "components/utils/page-header";
import PageFooter from "components/footer/page-footer";
import DoctorCardsGrid from "components/doctor/doctor-cards-grid";
export default {
  name: "Doctors",
  components: {DoctorCardsGrid, PageFooter, PageHeader},
  computed: {
    doctors () {
      const vm = this
      const doctors = JSON.parse(JSON.stringify(vm.$store.getters.getDoctors))
      doctors.sort((a,b) => {
        if (a.name > b.name) {
          return 1
        } else {
          return -1
        }
      })
      return doctors
    }
  }
}
</script>

<style scoped>

</style>
