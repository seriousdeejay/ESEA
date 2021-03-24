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
      requiresLogin: true,
      breadcrumb: [{ label: 'networks', to: '/networks' }]
    }
  },
  {
    path: '/network/:NetworkId',
    name: 'network',
    component: () => import('../views/network/Network'),
    children: [
      {
        path: 'overview',
        name: 'networkoverview',
        component: () => import('../views/network/NetworkOverview'),
        meta: {
          requiresLogin: true,
          breadcrumb: [
            { label: 'Networks', to: '/networks' },
            { label: '', to: { name: 'networkoverview', params: { id: '' } } },
            { label: 'Overview', to: { name: 'networkoverview' } }
          ]
        }
      },
      {
        path: 'methods',
        name: 'networkmethods',
        component: () => import('../views/network/NetworkMethods'),
        meta: {
          requiresLogin: true,
          breadcrumb: [
            { label: 'Networks', to: '/networks' },
            { label: '', to: { name: 'networkoverview', params: { id: '' } } },
            { label: 'Methods', to: { name: 'networkmethods' } }
          ]
        }
      },
      {
        path: 'method/:MethodId',
        name: 'networkmethod',
        component: () => import('../views/network/NetworkMethod'),
        meta: {
          requiresLogin: true,
          breadcrumb: [
            { label: 'Networks', to: '/networks' },
            { label: '', to: { name: 'networkoverview', params: { id: '' } } },
            { label: 'Methods', to: { name: 'networkmethods' } },
            { label: 'BIA', to: { name: 'networkmethod' } }
          ]
        }
      },
      {
        path: 'organisations',
        name: 'networkorganisations',
        component: () => import('../views/network/NetworkOrganisations'),
        meta: {
          requiresLogin: true,
          breadcrumb: [
            { label: 'Networks', to: '/networks' },
            { label: '', to: { name: 'networkoverview', params: { id: '' } } },
            { label: 'Organisations', to: { name: 'networkorganisations' } }
          ]
        }
      },
      {
        path: 'settings',
        name: 'networksettings',
        component: () => import('../views/network/NetworkSettings'),
        meta: {
          requiresLogin: true,
          breadcrumb: [
            { label: 'Networks', to: '/networks' },
            { label: '', to: { name: 'networkoverview', params: { id: '' } } },
            { label: 'Settings', to: { name: 'networksettings' } }
          ]
        }
      }
    ],
    meta: {
      requiresLogin: true,
      breadcrumb: [{ label: 'networks', to: '/networks' }, { label: '', to: { name: 'networkoverview', params: { id: '' } } }]
    }
  },
  // {
  //   path: '/networks/:id',
  //   name: 'networkdetails',
  //   component: () => import('../views/NetworkDetails.vue'),
  //   meta: {
  //     requiresLogin: true,
  //     breadcrumb: [{ label: 'networks', to: '/networks' }, { label: '', to: { name: 'networkdetails', params: { id: '' } } }]
  //   }
  // },
  {
    path: '/organisation/:OrganisationId',
    name: 'organisation',
    component: () => import('../views/organisation/Organisation'),
    children: [
      {
        path: 'overview',
        name: 'organisationoverview',
        component: () => import('../views/organisation/OrganisationOverview'),
        meta: {
          breadcrumb: [
            { label: 'Organisations', to: '/organisations' },
            { label: '', to: { name: 'organisationoverview', params: { id: '' } } },
            { label: 'Overview', to: { name: 'organisationoverview' } }
          ]
        }
      },
      {
      path: 'reports',
      name: 'organisationreports',
      component: () => import('../views/organisation/OrganisationReports'),
      meta: {
        breadcrumb: [
          { label: 'Organisations', to: '/organisations' },
          { label: '', to: { name: 'organisationoverview', params: { id: '' } } },
          { label: 'Reports', to: { name: 'organisationreports' } }
        ]
      }
      },
      {
      path: 'surveys',
      name: 'organisationsurveys',
      component: () => import('../views/organisation/OrganisationSurveys'),
      meta: {
        breadcrumb: [
          { label: 'Organisations', to: '/organisations' },
          { label: '', to: { name: 'organisationoverview', params: { id: '' } } },
          { label: 'Surveys', to: { name: 'organisationsurveys' } }
        ]
      }
      },
      {
        path: 'stakeholders',
        name: 'organisationstakeholders',
        component: () => import('../views/organisation/OrganisationStakeholders'),
        meta: {
          breadcrumb: [
            { label: 'Organisations', to: '/organisations' },
            { label: '', to: { name: 'organisationoverview', params: { id: '' } } },
            { label: 'Stakeholders', to: { name: 'organisationstakeholders' } }
          ]
        }
      },
      {
        path: 'networks',
        name: 'organisationnetworks',
        component: () => import('../views/organisation/OrganisationNetworks'),
        meta: {
          breadcrumb: [
            { label: 'Organisations', to: '/organisations' },
            { label: '', to: { name: 'organisationoverview', params: { id: '' } } },
            { label: 'Networks', to: { name: 'organisationnetworks' } }
          ]
        }
      },
      {
        path: 'settings',
        name: 'organisationsettings',
        component: () => import('../views/organisation/OrganisationSettings'),
        meta: {
          breadcrumb: [
            { label: 'Organisations', to: '/organisations' },
            { label: '', to: { name: 'organisationoverview', params: { id: '' } } },
            { label: 'Settings', to: { name: 'organisationsettings' } }
          ]
        }
      }
    ],
    meta: {
      breadcrumb: [
        { label: 'Organisations', to: '/organisations' },
        { label: '', to: { name: 'organisation', params: { id: '' } } }
      ]
    }
  },
  {
    path: '/organisations',
    name: 'organisations',
    component: () => import('../views/Organisations.vue'),
    meta: {
      requiresLogin: true,
      breadcrumb: [
        { label: 'Organisations', to: '/organisations' }
      ]
    }
  },
  // {
  //   path: '/organisations/:id',
  //   name: 'organisationdetails',
  //   component: () => import('../views/OrganisationDetails.vue'),
  //   meta: {
  //     requiresLogin: true,
  //     breadcrumb: [
  //       { label: 'Organisations', to: '/organisations' },
  //       { label: '', to: { name: 'organisationdetails', params: { id: '' } } }
  //     ]
  //   }
  // },
  // {
  //   path: '/organisations/:id/reports',
  //   name: 'organisationreports',
  //   component: () => import('../views/OrganisationReports.vue'),
  //   meta: {
  //     requiresLogin: true,
  //     breadcrumb: [
  //       { label: 'Organisations', to: '/organisations' },
  //       { label: '', to: { name: 'organisationdetails', params: { id: '' } } },
  //       { label: 'Reports', to: { name: 'organisationreports', params: { id: '' } } }
  //     ]
  //   }
  // },
  // {
  //   path: '/organisations/:id/surveys',
  //   name: 'organisationsurveys',
  //   component: () => import('../views/OrganisationSurveys.vue'),
  //   meta: {
  //     requiresLogin: true,
  //     breadcrumb: [
  //       { label: 'Organisations', to: '/organisations' },
  //       { label: '', to: { name: 'organisationdetails', params: { id: '' } } },
  //       { label: 'Surveys', to: { name: 'organisationsurveys', params: { id: '' } } }
  //     ]
  //   }
  // },
  // {
  //   path: '/organisations/:id/stakeholders',
  //   name: 'organisationstakeholders',
  //   component: () => import('../views/OrganisationStakeholders.vue'),
  //   meta: {
  //     requiresLogin: true,
  //     breadcrumb: [
  //       { label: 'Organisations', to: '/organisations' },
  //       { label: '', to: { name: 'organisationdetails', params: { id: '' } } },
  //       { label: 'Stakeholders', to: { name: 'organisationstakeholders', params: { id: '' } } }
  //     ]
  //   }
  // },
  // {
  //   path: '/organisations/:id/networks',
  //   name: 'organisationnetworks',
  //   component: () => import('../views/OrganisationNetworks.vue'),
  //   meta: {
  //     requiresLogin: true,
  //     breadcrumb: [
  //       { label: 'organisations', to: '/organisations' },
  //       { label: '', to: { name: 'organisationdetails', params: { id: '' } } },
  //       { label: 'Networks', to: { name: 'organisationnetworks', params: { id: '' } } }
  //     ]
  //   }
  // },
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
    path: '/organisations/:OrganisationId/methods/:id/surveys/:surveyId',
    name: 'survey-fill',
    component: () => import('../views/SurveyResponse.vue'),
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/organisations/:OrganisationId/methods/:methodId/surveys/:surveyId/result/:id',
    name: 'method-survey-result',
    component: () => import('../views/SurveyUserResult.vue'),
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/methods/:id/surveys/:surveyId/results',
    name: 'method-survey-results',
    component: () => import('../views/SurveyResults'),
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/:pathMatch(.*)*',
    name: '404',
    component: () => import('../views/Logout.vue')
}
]

const router = createRouter({
  history: createWebHashHistory(),
  // base: process.env.BASE_url, (?) -------------------------
  routes
})

export default router

// let resolved = this.$router.resolve('YOUR URL')
// if(resolved.route.name != '404')
//    // DO SOMETHING
