<template>
  <div class="fullscreen bg-white text-center q-pa-md flex flex-center">
    <div>
      <div style="font-size: 20vh">
        404
      </div>

      <div class="text-h6" style="opacity:.4">
        Извините. Страница не найдена.<br>
        Но на нашем сайте есть много другой полезной информации.
      </div>

      <q-btn
        class="q-mt-xl"
        color="dark"
        unelevated stretch outline
        to="/"
        label="На главную"
        no-caps
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'Error404'
}
</script>
