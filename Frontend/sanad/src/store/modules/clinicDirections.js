import axios from 'axios'
import notifier from "src/utils/notifier"

export default {
  state: {
    adultsDirections: null,
    childDirections: null,
    direction: {},
  },
  actions: {
    async fetchDirections({commit}) {
      try {
        await axios.get(`${this.getters.getServerURL}/clinic/directions/`)
          .then(({data}) => {
            commit('setDirections', data)
          })
      } catch (e) {
        notifier(`Не удалось загрузить направления. Ошибка сервера: ${e.message}`)
      }
    },
    async loadDirection({ commit }, slug) {
      try {
        await axios.get(`${this.getters.getServerURL}/clinic/direction/${slug}/`)
          .then(({data}) => {
            commit('mutationDirection', data)
          })
      } catch (e) {
        throw e
      }
    }
  },
  mutations: {
    mutationDirection(state, data) {
      state.direction = data
    },
    setDirections(state, data) {
      state.adultsDirections = data.filter(item => item.is_adults_direction)
      state.childDirections = data.filter(item => item.is_for_kids_direction)
    }
  },
  getters: {
    getAdultsDirections: state => state.adultsDirections,
    getChildDirections: state => state.childDirections,
    getDirection: state => state.direction
  }
}
