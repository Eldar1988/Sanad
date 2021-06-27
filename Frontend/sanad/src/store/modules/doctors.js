import axios from 'axios'
import notifier from "src/utils/notifier"

export default {
  state: {
    homeReviews: null,
    doctor: {}
  },
  actions: {
    async fetchHomeReviews({commit}) {
      try {
        await axios.get(`${this.getters.getServerURL}/clinic/home_reviews/`)
          .then(({data}) => commit('setHomeReviews', data))
      } catch (e) {
        notifier(`Не удалось загрузить отзывы. Ошибка: ${e.message}`)
      }
    },
    async loadDoctor({commit}, slug) {
      try {
        await axios.get(`${this.getters.getServerURL}/clinic/doctor/${slug}/`)
          .then(({data}) => commit('mutationDoctor', data))
      } catch (e) {
        notifier(`Не удалось загрузить отзывы. Ошибка: ${e.message}`)
      }
    }
  },
  mutations: {
    setHomeReviews(state, data) {
      state.homeReviews = data
    },
    mutationDoctor(state, data) {
      state.doctor = data
    }
  },
  getters: {
    getHomeReviews: state => state.homeReviews,
    getDoctor: state => state.doctor
  }
}
