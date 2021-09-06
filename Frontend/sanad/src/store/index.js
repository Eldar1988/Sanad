import Vue from 'vue'
import Vuex from 'vuex'
import main from './modules/main'
import clinicActions from './modules/clinicActions'
import clinicDirections from "./modules/clinicDirections"
import posts from './modules/posts'
import stories from './modules/stories'
import doctors from './modules/doctors'
import reviews from './modules/reviews'

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

export default function (/* { ssrContext } */) {
  const Store = new Vuex.Store({
    modules: {
      main,
      clinicActions,
      clinicDirections,
      posts,
      stories,
      doctors,
      reviews
    },
    state: {
      // serverURL: 'http://192.168.0.199:8000'
      serverURL: 'https://sanad.kz.na4u.ru'
    },
    actions: {
      init({dispatch}) {
        dispatch('fetchClinicActions')
        dispatch('fetchDirections')
        dispatch('fetchHomePosts')
        dispatch('fetchHomeStories')
        dispatch('fetchHomeReviews')
        dispatch('fetchClinicLifePosts')
        dispatch('loadDoctors')
        dispatch('loadInfoPages')
        dispatch('fetchBanners')
      }
    },
    getters: {
      getServerURL: state => state.serverURL
    },

    // enable strict mode (adds overhead!)
    // for dev mode only
    strict: process.env.DEBUGGING
  })

  return Store
}
