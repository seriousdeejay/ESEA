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
    path: '/users',
    name: 'users',
    component: () => import('../views/Users.vue'),
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/userprofile',
    name: 'userprofile',
    component: () => import('../views/UserProfile.vue'),
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/networks',
    name: 'networks',
    component: () => import('../views/Networks.vue'),
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/organisations',
    name: 'organisations',
    component: () => import('../views/Organisations.vue'),
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/organisations/edit/:id',
    name: 'editorganisation',
    component: () => import('../views/DetailedOrganisation.vue')
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
