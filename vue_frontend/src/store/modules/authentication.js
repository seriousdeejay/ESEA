// import { createStore } from '../vuex'
import { AxiosInstance } from '../../plugins/axios'
import { STATUS } from '../../utils/constants'
import axios from 'axios'

export default {
    namespaced: true,
    state: {
        accessToken: null,
        refreshToken: null,
        currentuser: 'Username here',

        APIData: '',
        networks: '',
        network: '',
        networkorganisations: '',
        organisations: '',
        organisation: '',
        organisationparticipants: '',
        users: '',
        status: ''
    },
    mutations: {
        updateStorage (state, { access, refresh }) {
            state.accessToken = access
            state.refreshToken = refresh
            console.log(access)
            axios.get('http://localhost:8000/networks/', { headers: { Authorization: `bearer ${access}` } })
            .then(response => (console.log(response.data)))
          },
        destroyToken (state) {
            state.accessToken = null
            state.refreshToken = null
        },
        UpdateCurrentUser (state, username) {
            state.currentuser = username
        },
        error (state) {
            state.status = STATUS.ERROR
        }
    },
    getters: {
        loggedIn (state) {
          return state.accessToken != null
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
                  console.log(response.data.access)
                  context.commit('updateStorage', { access: response.data.access, refresh: response.data.refresh })
                  resolve()
                })
                .catch(err => {
                  reject(err)
                })
            })
          }
    }
}
