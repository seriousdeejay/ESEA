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
    path: '/',
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
    path: '/users/:id',
    name: 'userdetails',
    component: () => import('../views/UserDetails.vue'),
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
  },
  {
    path: '/methods/:id',
    name: 'methoddetails',
    component: () => import('../views/MethodDetails.vue'),
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/methods/:id/surveys',
    name: 'methodsurveys',
    component: () => import('../views/MethodSurveys.vue'),
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/methods/:id/surveys/:surveyId',
    name: 'survey-fill',
    component: () => import('../views/SurveyResponse.vue'),
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/methods/:id/surveys/:surveyId/result',
    name: 'method-survey-result',
    component: () => import('../views/SurveyUserResult.vue'),
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/methods/:id/surveys/:surveyId/results',
    name: 'method-survey-results',
    // component: () => import('../views/SurveyResults'),
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
