import axios from 'axios'
import notifier from "src/utils/notifier"

export default {
  state: {
    homeStories: null
  },
  actions: {
    async fetchHomeStories({commit}) {
      try {
        await axios.get(`${this.getters.getServerURL}/blog/home_page_medical_stories/`)
          .then(({data}) => commit('setHomeStories', data))
      } catch (e) {
        notifier(`Не удалось загрузить истории болезней. Ошибка сервера: ${e.message}`)
      }
    }
  },
  mutations: {
    setHomeStories(state, data) {
      state.homeStories = data
    }
  },
  getters: {
    getHomeStories: state => state.homeStories
  }
}
