import axios from 'axios'
import notifier from "src/utils/notifier"

export default {
  state: {
    homePosts: null,
    actualPosts: null,
    clinicLifePosts: null
  },
  actions: {
    async fetchHomePosts({commit}) {
      try {
        await axios.get(`${this.getters.getServerURL}/blog/home_page_posts/`)
          .then(({data}) => commit('setHomePosts', data))
      } catch (e) {
        notifier(`Не удалось загрузить статьи. Ошибка сервера: ${e.message}`)
      }
    },
    async fetchActualPosts({commit}) {
      try {
        await axios.get(`${this.getters.getServerURL}/blog/actual_posts/`)
          .then(({data}) => commit('setActualPosts', data))
      } catch (e) {
        notifier(`Не удалось загрузить статьи. Ошибка сервера: ${e.message}`)
      }
    },
    async fetchClinicLifePosts({commit}) {
      try {
        await axios.get(`${this.getters.getServerURL}/blog/clinic_life_posts/`)
          .then(({data}) => commit('setClinicLifePosts', data))
      } catch (e) {
        notifier(`Не удалось загрузить статьи. Ошибка сервера: ${e.message}`)
      }
    }
  },
  mutations: {
    setHomePosts(state, data) {
      state.homePosts = data
    },
    setActualPosts(state, data) {
      state.actualPosts = data
    },
    setClinicLifePosts(state, data) {
      state.clinicLifePosts = data
    },
  },
  getters: {
    getHomePosts: state => state.homePosts,
    getActualPosts: state => state.actualPosts,
    getClinicLifeActions: state => state.clinicLifePosts
  }
}
