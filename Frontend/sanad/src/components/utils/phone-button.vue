<template>
<div class="phone-button">
  <q-btn
    icon="phone"
    round
    color="positive"
    size="lg"
    to="/phone"
    class="phone-btn-animate"
  >
    <span></span>
  </q-btn>
</div>
</template>

<script>
export default {
  name: "phone-button"
}
</script>

<style lang="sass">
.phone-button
  position: fixed
  bottom: 30px
  right: 30px
  z-index: 1000

.phone-btn-animate
  position: relative
  overflow: hidden

  &:after
    content: ""
    position: absolute
    top: 0
    bottom: 0
    left: -30%
    width: 30px
    background: rgba(255,255,255,.3)
    box-shadow: 0 0 10px 0 rgba(255,255,255,.5)
    animation-name: phone-btn
    animation-duration: 3s
    animation-iteration-count: infinite
    animation-fill-mode: forwards

@keyframes phone-btn
  0%
    left: -30%
  30%
    left: 100%

  100%
    left: 100%

@media screen and (max-width: 700px)
  .phone-button
    bottom: 15px
    right: 15px
</style>
