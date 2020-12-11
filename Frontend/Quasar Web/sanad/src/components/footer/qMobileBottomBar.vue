<template>
  <div class="hide-on-desktop">
  <div class=" mobile-bottom-bar shadow-3">

    <!--    Позвонить   -->
    <div class="text-center">
      <div>
        <a :href="`tel:${contacts.phone}`">
          <q-btn flat size="18px" icon="call" color="secondary"></q-btn>
        </a>
      </div>
      <div class="btn-text text-dark text-center">
        Позвонить
      </div>
    </div>
    <!--    ==============   -->
    <!--    Whatsapp   -->
    <div class="text-center">
      <div>
        <a :href="`https://wa.me/${contacts.phone_2}`">
          <q-btn flat size="18px" icon="sms" color="secondary"></q-btn>
        </a>
      </div>
      <div class="btn-text text-dark text-center">
        Whatsapp
      </div>
    </div>
    <!--    ===================  -->
    <div class="relative-position text-center">
      <div class="nav-btn">
        <q-btn-dropdown class="q-btn--round" round color="primary" size="20px" icon="enhanced_encryption" dr unelevated dropdown-icon="none">
          <qMenuDirections />
        </q-btn-dropdown>
      </div>
    </div>
    <!--    Главная   -->
    <div class="text-center">
      <div>
        <router-link to="/">
          <q-btn flat size="18px" icon="home" color="secondary"></q-btn>
        </router-link>
      </div>
      <div class="btn-text text-dark text-center">
        Главная
      </div>
    </div>
    <!--    ===================  -->
    <!--    Контакты   -->
    <div class="text-center">
      <div>
        <router-link to="/contacts">
          <q-btn flat size="18px" icon="add_location" color="secondary"></q-btn>
        </router-link>
      </div>
      <div class="btn-text text-dark text-center">
        Контакты
      </div>
    </div>
    <!--    ===================  -->

  </div>
  </div>
</template>

<script>
import qMenuDirections from "components/header/qMenuDirections";
export default {
  name: "qMobileBottomBar",
  components: {
    qMenuDirections
  },
  props: {
    contacts: {
      type: Object,
      default: null
    }
  }
}
</script>

<style lang="sass">
.mobile-bottom-bar
  position: fixed
  bottom: 0
  left: 0
  right: 0
  width: 100%
  background: #fff
  display: grid
  grid-template-columns: repeat(5, 1fr)
  align-items: center
  height: 50px
  z-index: 5555

  .q-btn-dropdown__arrow-container
    display: none

.q-menu
  min-width: 90% !important
  margin-left: 5% !important
  min-height: 500px !important

.btn-text
  font-size: 10px
  margin-top: -10px

.nav-btn
  position: absolute
  top: -40px
  width: 70px
  left: 50%
  margin-left: -35px
</style>
