import axios from 'axios'
import notifier from "src/utils/notifier"

export default {
  state: {
    reviews: []
  },
  actions: {
    async loadReviews({commit}) {
      try {
        await axios.get(`${this.getters.getServerURL}/clinic/home_reviews/`)
          .then(({data}) => commit('mutationReviews', data))
      } catch (e) {
        notifier(`Не удалось загрузить отзывы. Ошибка сервера: ${e.message}`)
      }
    },
  },
  mutations: {
    mutationReviews (state, data) {
      state.reviews = data
    }
  },
  getters: {
    getReviews: (state) => state.reviews
  }
}
