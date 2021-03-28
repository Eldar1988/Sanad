import axios from 'axios'
import notifier from "src/utils/notifier"

export default {
  state: {
    adultsDirections: null,
    childDirections: null
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
    }
  },
  mutations: {
    setDirections(state, data) {
      console
      state.adultsDirections = data.filter(item => !item.is_for_kids_direction)
      state.childDirections = data.filter(item => item.is_for_kids_direction)
    }
  },
  getters: {
    getAdultsDirections: state => state.adultsDirections,
    getChildDirections: state => state.childDirections
  }
}
