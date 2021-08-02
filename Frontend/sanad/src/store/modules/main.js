import axios from 'axios'
import notifier from "src/utils/notifier"


export default {
  state: {
    mainInfo: {},
    banners: [],
    videos: [],
    aboutInfo: {},
    appointDialog: false
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
      }
    },
    async fetchBanners({commit}) {
      try {
        await axios.get(`${this.getters.getServerURL}/main/banners/`)
          .then(({data}) => commit('setBanners', data))
      } catch (e) {
        notifier(`Не удалось загрузить баннеры. Ошибка сервера: ${e.message}`)
      }
    },
    async loadVideos({commit, state}) {
      if (!state.videos.length) {
        try {
          await axios.get(`${this.getters.getServerURL}/main/videos/`)
            .then(({data}) => commit('setVideos', data))
        } catch (e) {
          notifier(`Не удалось загрузить баннеры. Ошибка сервера: ${e.message}`)
        }
      }
    },
    async loadAboutInfo({commit}) {
        try {
          await axios.get(`${this.getters.getServerURL}/main/about/`)
            .then(({data}) => commit('setAbout', data))
        } catch (e) {
          notifier(`Не удалось загрузить баннеры. Ошибка сервера: ${e.message}`)
        }
    },
    changeAppointDialog ({ commit }) {
      commit('setAppointDialog')
    }
  },
  mutations: {
    setMainInfo(state, data) {
      state.mainInfo = data
    },
    setVideos(state, data) {
      state.videos = data
    },
    setBanners(state, data) {
      state.banners = data
    },
    setAbout(state, data) {
      state.aboutInfo = data
    },
    setAppointDialog (state) {
      state.appointDialog = !state.appointDialog
    }
  },
  getters: {
    getMainInfo: state => state.mainInfo,
    getAboutInfo: state => state.aboutInfo,
    getBanners: state => state.banners,
    getVideos: state => state.videos,
    getAppointDialog: state => state.appointDialog
  }
}
