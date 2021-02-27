import { AxiosInstance } from '../../plugins/axios'
import { STATUS } from '../../utils/constants'
import UserService from '../../services/UserService'
// import axios from 'axios'

export default {
    namespaced: true,
    state: {
        accessToken: null,
        refreshToken: null,
        authenticatedUser: null,
        currentuser: 'Username here',
        status: ''

        // APIData: '',
        // networks: '',
        // network: '',
        // networkorganisations: '',
        // organisations: '',
        // organisation: '',
        // organisationparticipants: '',
        // users: '',
    },
    mutations: {
        updateStorage (state, { access, refresh }) {
            state.accessToken = access
            state.refreshToken = refresh
          },
        destroyToken (state) {
            state.accessToken = null
            state.refreshToken = null
        },
        UpdateCurrentUser (state, username) {
            state.currentuser = username
        },
        saveAuthenticatedUserDetails (state, { data }) {
          state.authenticatedUser = data[0]
        },
        error (state) {
            state.status = STATUS.ERROR
        }
    },
    getters: {
        loggedIn (state) {
          return ((state.accessToken != null) & (state.authenticatedUser != null))
        },
        AuthenticationToken (state) {
          return state.accessToken
        }
      },

    actions: {
        userLogout (context) {
            if (context.getters.loggedIn) {
                context.commit('destroyToken')
            }
        },
        userLogin (context, usercredentials) {
            context.commit('UpdateCurrentUser', usercredentials.username)
            return new Promise((resolve, reject) => {
              AxiosInstance.post('/api-token/', {
                username: usercredentials.username,
                password: usercredentials.password
              })
                .then(response => {
                  context.commit('updateStorage', { access: response.data.access, refresh: response.data.refresh })
                  resolve(context.dispatch('saveAuthenticatedUserDetails'))
                })
                .catch(err => {
                  reject(err)
                })
            })
          },
          async saveAuthenticatedUserDetails (context) {
            const { response, error } = await UserService.get({ query: 'currentuser=1' })
            if (error) {
              console.log(error)
            }
            context.commit('saveAuthenticatedUserDetails', response)
          }
    }
}
