import axiosInstance from 'axios'

export default {
  namespaced: true,
  // IMPORTANT: state must be a function so the module can be
  // instantiated multiple times
  state: () => ({
    data: []
  }),
  actions: {
    fetchItem ({ commit }) {
      return axiosInstance.get('http://192.168.0.199:8000/api/').then(({ data }) => {
        commit('setData', data)
      })
    }
  },
  mutations: {
    setData(state, data) {
      state.data = data
    }
  }
}
