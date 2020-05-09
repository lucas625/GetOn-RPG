import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
const store = new Vuex.Store({
  strict: process.env.VUE_APP_ENVIRONMENT !== 'production'
})

export default store
