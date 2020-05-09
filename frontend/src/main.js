import Vue from 'vue'
import App from '@/App'
import router from '@/plugins/vue-router'
import vuetify from '@/plugins/vuetify'
import store from '@/store/store'

import '@/init/auto-load-base-components'

Vue.config.productionTip = false
require('dotenv').config()

new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')
