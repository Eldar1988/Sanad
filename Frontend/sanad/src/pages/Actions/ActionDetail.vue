<template>
<q-page>
  <q-page>
    <page-header title="Акции" back-route-button/>
    <div class="container-m">
      <div class="row q-mt-sm" :class="$q.platform.is.desktop ? 'q-col-gutter-xl' : 'q-col-gutter-sm'">
        <div class="col-12 col-md-4">
          <q-img :src="action.image" no-default-spinner/>
        </div>
        <div class="col-12 col-md-8">
          <h1 class="page-title" :class="$q.platform.is.desktop ? '' : 'q-mt-lg' ">{{ action.title }} {{ action.title_2 }} {{ action.title_3 }}</h1>
          <div class="q-mt-md" v-html="action.description"></div>
        </div>
      </div>
    </div>
    <page-footer />
  </q-page>
</q-page>
</template>

<script>
import PageHeader from "components/utils/page-header";
import PageFooter from "components/footer/page-footer";
export default {
  name: "ActionDetail",
  components: {PageFooter, PageHeader},
  computed: {
    action () {
      return this.$store.getters.getClinicAction
    }
  },
  preFetch ({ store, currentRoute }) {
    return store.dispatch('loadClinicAction', currentRoute.params.slug)
  },
  meta() {
    return {
      title: `${this.action.title} ${this.action.title_2} ${this.action.title_3} | Клиника SANAD Караганда`,
      meta: {
        description: {
          name: "description",
          content: `${this.action.short_description}`,
        },
        ogType: {
          property: "og:type",
          content: "website",
        },
        ogTitle: {
          property: "og:title",
          content: `${this.action.title} ${this.action.title_2} ${this.action.title_3} | Клиника SANAD Караганда`,
        },
        ogUrl: {
          property: "og:url",
          content: 'https://sanadmed.kz' + this.$route.path,
        },
        ogDescription: {
          property: "og:description",
          content: `${this.action.short_description}`,
        },
        ogImage: {
          property: "og:image",
          content: `${this.action.image}`
        }
      }
    }
  }
}
</script>

<style scoped>

</style>
