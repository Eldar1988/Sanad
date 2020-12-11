import Vue from 'vue'
import Vuex from 'vuex'
import axiosInstance from 'axios'

// import example from './module-example'

Vue.use(Vuex)

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */

export default function ({ ssrContext }) {
  const Store = new Vuex.Store({
    modules: {
      // example
    },

    state() {
      return {
        siteURL: 'site.com',
        serverUrl: 'http://192.168.0.199:8000/api',
        homeData: [],
        directionData: [],
        doctorData: [],
        postDetail: [],
        actions: [],
        news: [],
        about: [],
        storyDetail: []
      }
    },

    mutations: {
      setHomeData(state, data) {
        state.homeData = data
      },

      setDirectionData(state, data) {
        state.directionData = data
      },
      setDoctorData(state, data) {
        state.doctorData = data
      },
      setPostData(state, data) {
        state.postDetail = data
      },
      setActionsData(state, data) {
        state.actions = data
      },
      setNewsData(state, data) {
        state.news = data
      },
      setAboutData(state, data) {
        state.about = data
      },
      setStoryData(state, data) {
        state.storyDetail = data
      }
    },

    actions: {
      // Загрузка данных для главной страницы
      fetchHomeData ({ commit }) {
        return axiosInstance.get(`${this.state.serverUrl}`).then(({ data }) => {
          commit('setHomeData', data)
        })
      },
      // Загрузка данных для страцниы направления
      fetchDirectionData({commit}, slug) {
        return axiosInstance.get(`${this.state.serverUrl}/direction/${slug}`).then(({ data }) => {
          commit('setDirectionData', data)
        })
      },
      // ЗАгрузка данных для страницы доктора
      fetchDoctorData({commit}, slug) {
        return axiosInstance.get(`${this.state.serverUrl}/doctor/${slug}`).then(({ data }) => {
          commit('setDoctorData', data)
        })
      },
      // Страница поста
      fetchPostData({commit}, slug) {
        return axiosInstance.get(`${this.state.serverUrl}/post/${slug}`).then(({ data }) => {
          commit('setPostData', data)
        })
      },
      // Страница истории
      fetchStoryData({commit}, slug) {
        return axiosInstance.get(`${this.state.serverUrl}/history/${slug}`).then(({ data }) => {
          commit('setStoryData', data)
        })
      },
      // Страница акций
      fetchActionsData({commit}) {
        return axiosInstance.get(`${this.state.serverUrl}/actions`).then(({ data }) => {
          commit('setActionsData', data)
        })
      },
      // Страница новостей
      fetchNewsData({commit}) {
        return axiosInstance.get(`${this.state.serverUrl}/news`).then(({ data }) => {
          commit('setNewsData', data)
        })
      },
      // Странциа о клинике
      fetchAboutData({commit}) {
        return axiosInstance.get(`${this.state.serverUrl}/about`).then(({ data }) => {
          commit('setAboutData', data)
        })
      }
    },

    // enable strict mode (adds overhead!)
    // for dev mode only
    strict: process.env.DEBUGGING
  })

  return Store
}
