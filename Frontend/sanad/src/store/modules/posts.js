import axios from 'axios'
import notifier from "src/utils/notifier"

export default {
  state: {
    post: {},
    posts: [],
    homePosts: [],
    clinicLifePosts: []
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
    async fetchClinicLifePosts({commit}) {
      try {
        await axios.get(`${this.getters.getServerURL}/blog/clinic_life_posts/`)
          .then(({data}) => commit('setClinicLifePosts', data))
      } catch (e) {
        notifier(`Не удалось загрузить статьи. Ошибка сервера: ${e.message}`)
      }
    },
    async loadPosts({commit}) {
      try {
        await axios.get(`${this.getters.getServerURL}/blog/posts/`)
          .then(({data}) => commit('setPosts', data))
      } catch (e) {
        notifier(`Не удалось загрузить статьи. Ошибка сервера: ${e.message}`)
      }
    },
    async loadPost({commit}, slug) {
      try {
        await axios.get(`${this.getters.getServerURL}/blog/post/${slug}/`)
          .then(({data}) => commit('setPost', data))
      } catch (e) {
        notifier(`Не удалось загрузить статьи. Ошибка сервера: ${e.message}`)
      }
    }
  },
  mutations: {
    setHomePosts(state, data) {
      state.homePosts = data
    },
    setPosts (state, data) {
      state.posts = data
    },
    setPost (state, data) {
      state.post = data
    },
    setClinicLifePosts(state, data) {
      state.clinicLifePosts = data
    }
  },
  getters: {
    getPost: (state) => state.post,
    getPosts: (state) => state.posts,
    getHomePosts: state => state.homePosts,
    getClinicLifeActions: state => state.clinicLifePosts
  }
}
