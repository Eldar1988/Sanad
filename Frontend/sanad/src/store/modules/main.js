import axios from 'axios'

export default {
  state: {
    mainInfo: {},
    banners: [],
    videos: [],
    aboutInfo: {},
    appointDialog: false,
    price: [],
    infoPages: [],
    infoPage: {}
  },
  actions: {
    async fetchMainInfo({commit}) {
      try{
        await axios.get(`${this.getters.getServerURL}/main/`)
          .then(({data}) => {
            commit('setMainInfo', data)
          })

      } catch (e) {
        throw e
      }
    },
    async fetchBanners({commit}) {
      try {
        await axios.get(`${this.getters.getServerURL}/main/banners/`)
          .then(({data}) => commit('setBanners', data))
      } catch (e) {
        throw e
      }
    },
    async loadPrice({commit}) {
      try {
        await axios.get(`${this.getters.getServerURL}/clinic/price/`)
          .then(({data}) => commit('setPrice', data))
      } catch (e) {
        throw e
      }
    },
    async loadVideos({commit, state}) {
      if (!state.videos.length) {
        try {
          await axios.get(`${this.getters.getServerURL}/main/videos/`)
            .then(({data}) => commit('setVideos', data))
        } catch (e) {
          throw e
        }
      }
    },
    async loadAboutInfo({commit}) {
        try {
          await axios.get(`${this.getters.getServerURL}/main/about/`)
            .then(({data}) => commit('setAbout', data))
        } catch (e) {
          throw e
        }
    },
    async loadInfoPages({commit}) {
      try {
        await axios.get(`${this.getters.getServerURL}/main/info_pages/`)
          .then(({data}) => commit('setInfoPages', data))
      } catch (e) {
        throw e
      }
    },
    async loadInfoPage({commit}, slug) {
      try {
        await axios.get(`${this.getters.getServerURL}/main/info_page/${slug}/`)
          .then(({data}) => commit('setInfoPage', data))
      } catch (e) {
        throw e
      }
    },
    changeAppointDialog ({ commit }) {
      commit('setAppointDialog')
    }
  },
  mutations: {
    setInfoPages (state, data) {
      state.infoPages = data
    },
    setInfoPage (state, data) {
      state.infoPage = data
    },
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
    },
    setPrice (state, data) {
      state.price = data
    }
  },
  getters: {
    getInfoPages: state => state.infoPages,
    getInfoPage: state => state.infoPage,
    getMainInfo: state => state.mainInfo,
    getAboutInfo: state => state.aboutInfo,
    getBanners: state => state.banners,
    getVideos: state => state.videos,
    getAppointDialog: state => state.appointDialog,
    getPrice: state => state.price
  }
}
