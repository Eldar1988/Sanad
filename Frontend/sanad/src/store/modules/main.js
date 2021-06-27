import axios from 'axios'
import notifier from "src/utils/notifier"


export default {
  state: {
    mainInfo: {},
    banners: []
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
    },
    async fetchBanners({commit}) {
      try {
        await axios.get(`${this.getters.getServerURL}/main/banners/`)
          .then(({data}) => commit('setBanners', data))
      } catch (e) {
        notifier(`Не удалось загрузить баннеры. Ошибка сервера: ${e.message}`)
      }
    }
  },
  mutations: {
    setMainInfo(state, data) {
      state.mainInfo = data
    },
    setBanners(state, data) {
      state.banners = data
    },
  },
  getters: {
    getMainInfo: state => state.mainInfo,
    getBanners: state => state.banners
  }
}
