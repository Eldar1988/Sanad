import axios from 'axios'
import notifier from "src/utils/notifier"


export default {
  state: {
    mainInfo: {}
  },
  actions: {
    async fetchMainInfo({commit}) {
      try{

        await axios.get(`${this.getters.getServerURL}/main/`)
          .then(({data}) => {
            commit('setMainInfo', data)
          })

      } catch (e) {
        notifier(`Не удалось получить данные с сервера: ${e.message}`)
        setTimeout(() => {
          location.reload()
        }, 3000)
      }
    }
  },
  mutations: {
    setMainInfo(state, data) {
      state.mainInfo = data
    }
  },
  getters: {
    getMainInfo: state => state.mainInfo
  }
}
