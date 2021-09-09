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
  },
  meta() {
    return {
      title: "Специалисты | Клиника SANAD Караганда",
      meta: {
        description: {
          name: "description",
          content: "Специалисты клиники. Клинико-диагностический реабилитационный центр Sanad в Караганде",
        },
        ogType: {
          property: "og:type",
          content: "website",
        },
        ogTitle: {
          property: "og:title",
          content: "Специалисты | Клиника SANAD Караганда",
        },
        ogUrl: {
          property: "og:url",
          content: "https://sanadmed.kz",
        },
        ogDescription: {
          property: "og:description",
          content: "Специалисты клиники. Клинико-диагностический реабилитационный центр Sanad в Караганде",
        },
        ogImage: {
          property: "og:image",
          content: "https://res.cloudinary.com/space-developers/image/upload/v1630987428/cvetogis/logo/logo_e3tgqj.png"
        }
      }
    }
  }
}
</script>

<style scoped>

</style>
