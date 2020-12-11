<template>
<div class="q-card--bordered share-card q-pa-md text-dark">
  <p class="font-weight-500 q-pb-sm">Поделиться в сети:</p>
  <YandexShare :services="['whatsapp', 'telegram', 'vkontakte','facebook','twitter', 'odnoklassniki', 'pinterest ']" counter/>
</div>
</template>

<script>
import YandexShare from '@cookieseater/vue-yandex-share'

export default {
  name: "qShare",
  components: {
    YandexShare
  }
}
</script>

<style lang="sass">
.share-card
  border-radius: 5px
</style>
