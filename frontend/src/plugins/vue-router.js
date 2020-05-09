import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/get-home-view')
  }
]

export default new VueRouter({ mode: 'history', routes: routes })
