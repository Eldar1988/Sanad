import axios from 'axios'
import notifier from "src/utils/notifier";

export default {
  state: {
    clinicAction: {},
    clinicActions: null,
    clinicActionsForHomePage: null
  },
  actions: {
    async fetchClinicActions({commit}) {
      try{
        await axios.get(`${this.getters.getServerURL}/clinic/actions/`)
          .then(({data}) => commit('setClinicActions', data))
      } catch (e) {
        notifier('Не удалось загрузить акции')
      }
    },
    async loadClinicAction ({commit}, slug) {
      try{
        await axios.get(`${this.getters.getServerURL}/clinic/actions/${slug}/`)
          .then(({data}) => commit('setClinicAction', data))
      } catch (e) {
        notifier('Не удалось загрузить акции')
      }
    }
  },
  mutations: {
    setClinicAction (state, data) {
      state.clinicAction = data
    },
    setClinicActions(state, data) {
      state.clinicActions = data
      state.clinicActionsForHomePage = data.filter((item) => item.show_on_home_page)
    }
  },
  getters: {
    getClinicAction: (state) => state.clinicAction,
    getClinicActions: state => state.clinicActions,
    getClinicActionsFroHomePage: state => state.clinicActionsForHomePage
  }
}
