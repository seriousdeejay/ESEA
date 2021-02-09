import { createRouter, createWebHashHistory } from 'vue-router'

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
    path: '/home',
    name: 'home',
    component: () => import('../views/Home.vue'),
    meta: {
      requiresLogin: true
    }
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
    path: '/networks/edit/:id',
    name: 'networkdetails',
    component: () => import('../views/NetworkDetails.vue'),
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
    name: 'organisationdetails',
    component: () => import('../views/OrganisationDetails.vue'),
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/methods',
    name: 'methods',
    component: () => import('../views/Methods.vue'),
    meta: {
      requiresLogin: true
    }
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  // base: process.env.BASE_url, (?) -------------------------
  routes
})

export default router
