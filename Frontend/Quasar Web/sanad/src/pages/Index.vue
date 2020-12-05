<template>
  <q-page>
    <qSlider />
    {{ test }}
  </q-page>
</template>

<script>
import qSlider from "components/home/qSlider";
import Axios from "axios";

export default {
  components: {
    qSlider
  },
  name: "PageIndex",
  data() {
    return {
      test: []
    };
  },

  preFetch({ store }) {
    getHomeData();
    async function getHomeData() {
      let homeData = await store.dispatch("getHomeData"); // Данные для главной страницы
      homeData = homeData.data; // Получаем список
      let meta = homeData[0]; // Мета тэги
      console.log(meta, "1");
      this.setHomeData(meta)
    }

    this.meta.title = "test()";
    this.meta.meta.ogTitle.content = "REd";
    this.meta.meta.description.content = "store.state.homeData.title";
  },
  methods: {
    setHomeData(data) {
      this.test = data
    }
  },
  meta: {
    title: "",
    meta: {
      description: {
        name: "description"
      },
      ogTitle: {
        property: "og:title",
        content: "111"
      }
    }
  }
};
</script>
