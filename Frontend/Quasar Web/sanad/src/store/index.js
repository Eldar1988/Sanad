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
        directionData: []
      }
    },

    mutations: {
      setHomeData(state, data) {
        state.homeData = data
      },

      setDirectionData(state, data) {
        state.directionData = data
      }
    },

    actions: {
      fetchHomeData ({ commit }) {
        return axiosInstance.get(`${this.state.serverUrl}`).then(({ data }) => {
          commit('setHomeData', data)
        })
      },

      fetchDirectionData({commit}, slug) {
        return axiosInstance.get(`${this.state.serverUrl}/direction/${slug}`).then(({ data }) => {
          commit('setDirectionData', data)
        })
      }
    },

    // enable strict mode (adds overhead!)
    // for dev mode only
    strict: process.env.DEBUGGING
  })

  return Store
}
