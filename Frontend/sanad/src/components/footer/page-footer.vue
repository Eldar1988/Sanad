<template>
  <div>
    <footer>
      <section class="container section">
        <js-section-title title="Актуальное" class="ml-15-m"/>
        <keep-alive>
          <js-banners-slider :banners="banners" class="ml-15-m"/>
        </keep-alive>
      </section>

      <section class="container-m section">
        <js-section-title title="Жизнь клиники Sanad"/>
        <js-posts-grid-v2 :posts="clinicLifePosts"/>
      </section>
      <js-section-title id="contacts" title="Карта проезда" class="text-center section"/>
      <p class="sub_title text-center q-mt-xs">{{ contacts.address }}</p>
      <div v-html="contacts.frame" class="q-mt-lg">
      </div>
      <div class="bg-primary q-pt-xl" style="margin-top: -10px">
        <div class="container">
          <div class="footer-menu">
            <div class="row">
              <div class="col-md-6 col-12 q-px-sm">

                <js-section-title title="Контактая информация" class="text-white container-m" color-class="text-white"/>

                <q-list class="text-white q-mt-lg" dense separator dark>
                  <q-item
                    v-for="phone in contacts.phones.split(',')"
                    :key="phone"
                    class="text-h6 text-weight-light q-py-md "
                  >
                    <a :href="`tel:${phone}`" class="q-py-sm text-white q-pl-md">
                      {{ phone }}
                    </a>
                  </q-item>
                </q-list>
                <call-back label="Записаться на прием" color="white" :caps="true" classes="full-width q-py-sm q-mt-lg" @click="$store.dispatch('changeAppointDialog')"/>
              </div>

              <div class="col-md-6 col-12 q-px-sm">
                <q-list
                  dark dense
                  class="menu-list"
                >
                  <q-item class="sub_title underline" to="/doctors" manual-focus>
                    Специалисты
                  </q-item>
                  <q-item class="sub_title underline" to="/directions" manual-focus>
                    Направления
                  </q-item>
                  <q-item class="sub_title underline" to="/actions" manual-focus>
                    Акции
                  </q-item>
                  <q-item class="sub_title underline" to="/posts" manual-focus>
                    Новости
                  </q-item>
                  <q-item class="sub_title underline" to="/posts" manual-focus>
                    Статьи
                  </q-item>
                  <q-item class="sub_title underline" to="/about" manual-focus>
                    О клинике
                  </q-item>
                </q-list>
              </div>
            </div>

            <div class="section text-white q-pb-md q-pl-sm ml-15-m">
              <p>Copyright © {{ getYear }}. КДРЦ SANAD. <br>Все права защищены</p>
            </div>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import JsSectionTitle from "components/utils/section-title";
import CallBack from "components/header/appointment";
import JsPostsGridV2 from "components/posts/jsPostsGrid-v2";
import JsBannersSlider from "components/sliders/jsBannersSlider";

export default {
  name: "page-footer",
  components: {JsBannersSlider, JsPostsGridV2, CallBack, JsSectionTitle},
  computed: {
    banners() {
      return this.$store.getters.getBanners
    },
    contacts() {
      return this.$store.getters.getMainInfo.contacts
    },
    getYear() {
      let date = new Date()
      return date.getFullYear()
    },
    clinicLifePosts() {
      return this.$store.getters.getClinicLifeActions
    }
  },
  created() {
    this.$store.dispatch('fetchBanners')
  }
}
</script>

<style lang="sass">
iframe
  min-width: 100%
  max-width: 100%

.menu-list
  margin-left: 20px

@media screen and (max-width: 800px)
  .menu-list
    margin-top: 50px
</style>
