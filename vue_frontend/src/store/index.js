import { createStore } from 'vuex'
import { AxiosInstance } from '../plugins/axios'

import organisation from './modules/organisation'
import method from './modules/method/method'

export default createStore({
  modules:{
    organisation,
    method
  },
  state: {
    accessToken: null,
    refreshToken: null,
    currentuser: '',
    APIData: '',
    networks: '',
    network: '',
    networkorganisations: '',
    organisations: '',
    organisation: '',
    organisationparticipants: '',
    users: ''
 },
 mutations: {
   updateStorage (state, { access, refresh }) {
     state.accessToken = access
     state.refreshToken = refresh
   },
   destroyToken (state) {
     state.accessToken = null
     state.refreshToken = null
   }
 },
 getters: {
   loggedIn (state) {
     return state.accessToken != null
   }
 },
 actions: {
   userLogout (context) {
     if (context.getters.loggedIn) {
         context.commit('destroyToken')
     }
   },
   userLogin (context, usercredentials) {
     this.state.currentuser = usercredentials.username
     return new Promise((resolve, reject) => {
       AxiosInstance.post('/api-token/', {
         username: usercredentials.username,
         password: usercredentials.password
       })
         .then(response => {
           context.commit('updateStorage', { access: response.data.access, refresh: response.data.refresh })
           resolve()
         })
         .catch(err => {
           reject(err)
         })
     })
   }
 }
})

//   state: {
//   },
//   mutations: {
//   },
//   actions: {
//   },
//   modules: {
//   }
// })
