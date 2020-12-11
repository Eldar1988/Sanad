<template>
  <!--    Кнопка выезжающая сверху   -->
  <transition name="btn">
    <div class="call-to-action shadow-10" v-if="showToActionBtn">
      <q-btn outline rounded class="q-px-lg" color="white" icon-right="event" @click="dialog = true">
        Записаться на прием
      </q-btn>
    </div>
  </transition>
  <!--    =====================   -->
</template>

<script>
export default {
name: "qCallToActionTop"
}
</script>

<style scoped>

</style>
