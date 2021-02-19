import { createStore } from 'vuex'

import authentication from './modules/authentication'
import network from './modules/network'
import organisation from './modules/organisation'
import method from './modules/method/method'

// const vuexLocalStorage = new VuexPersist({
//  ... can be used to use local storage
// })

export default createStore({
  modules: {
    authentication,
    network,
    organisation,
    method
  }
//   state: {
//     accessToken: null,
//     refreshToken: null,
//     currentuser: '',
//     APIData: '',
//     networks: '',
//     network: '',
//     networkorganisations: '',
//     organisations: '',
//     organisation: '',
//     organisationparticipants: '',
//     users: '',
//     status: ''
//  },
})
