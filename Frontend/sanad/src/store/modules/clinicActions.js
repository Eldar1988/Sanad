import axios from 'axios'
import notifier from "src/utils/notifier";

export default {
  state: {
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
    }
  },
  mutations: {
    setClinicActions(state, data) {
      state.clinicActions = data
      state.clinicActionsForHomePage = data.filter((item) => item.show_on_home_page)
    }
  },
  getters: {
    getClinicActions: state => state.clinicActions,
    getClinicActionsFroHomePage: state => state.clinicActionsForHomePage
  }
}
