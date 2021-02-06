import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Posts from '../views/Posts.vue' // Could also use a similar method to the 'about' route

const routes = [
  {
    path: '/register',
    name: 'register',
    component: () => import('../views/Register.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/logout',
    name: 'logout',
    component: () => import('../views/Logout.vue')
  },
  {
    path: '/',
    name: 'posts',
    component: Posts,
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/home',
    name: 'home',
    component: Home
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  // base: process.env.BASE_url, (?) -------------------------
  routes
})

export default router
