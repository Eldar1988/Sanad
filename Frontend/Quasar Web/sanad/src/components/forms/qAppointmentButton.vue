<template>
  <div>
    <!--    Кнопка выезжающая сверху   -->
    <transition name="btn">
      <div class="call-to-action shadow-10" v-if="showToActionBtn">
        <q-btn rounded class="q-px-lg" color="secondary" icon-right="event" @click="dialog = true">
          Записаться на прием
        </q-btn>
      </div>
    </transition>
    <!--    =====================   -->
    <!--    Всплавыющая форма записи   -->
    <qAppointment v-if="dialog"
                  @closeDialog="dialog = false"
                  :header="header"
                  :isAppointment="isAppointment"
                  :btntext="'Записаться'"
    />
    <!--    ================   -->
  </div>
</template>

<script>
import qAppointment from "components/forms/qAppointment";

export default {
  name: "qAppointmentButton",
  props: {
    header: {
      type: String,
      default: ''
    },
    isAppointment: {
      type: Boolean,
      default: false
    }
  },
  components: {
    qAppointment
  },
  data() {
    return {
      showToActionBtn: false,
      dialog: false,
    }
  },
  mounted() {
    this.showToActionBtnOnScroll()
  },
  methods: {
    showToActionBtnOnScroll() {
      document.addEventListener('scroll', () => {
          this.showToActionBtn = window.pageYOffset > 100;
        }
      )
    }
  },
}
</script>

<style scoped>

</style>
