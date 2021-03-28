import axios from 'axios'
import notifier from "src/utils/notifier"

export default {
  state: {
    homeReviews: null
  },
  actions: {
    async fetchHomeReviews({commit}) {
      try {
        await axios.get(`${this.getters.getServerURL}/clinic/home_reviews/`)
          .then(({data}) => commit('setHomeReviews', data))
      } catch (e) {
        notifier(`Не удалось загрузить отзывы. Ошибка: ${e.message}`)
      }
    }
  },
  mutations: {
    setHomeReviews(state, data) {
      state.homeReviews = data
    }
  },
  getters: {
    getHomeReviews: state => state.homeReviews
  }
}
