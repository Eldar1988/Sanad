<template>
<div class="doctor-cards-grid">
 <div
  v-for="doctor in doctors"
  :key="doctor.id"
 >
   <js-doctor-card :doctor="doctor"/>
 </div>
</div>
</template>

<script>
import JsDoctorCard from "components/doctor/jsDoctorCard";
export default {
  name: "jsDoctorCardsGrid",
  components: {JsDoctorCard},
  props: {
    doctors: {
      type: Array,
      default: () => []
    }
  }
}
</script>

<style lang="sass">
.doctor-cards-grid
  display: grid
  grid-template-columns: 1fr 1fr
  grid-gap: 30px

@media screen and (max-width: 992px)
  .doctor-cards-grid
    grid-template-columns: 1fr
    grid-gap: 50px
</style>
