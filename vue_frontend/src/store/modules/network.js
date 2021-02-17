/* eslint-disable */
import NetworkService from '../../services/NetworkService'
import { mapState } from 'vuex'
// import { AxiosInstance } from '../../plugins/axios'
import axios from 'axios'
// import authentication from './authentication'
// import { getRequestData } from '../../utils/helpers'

// const baseNetwork = {
// 	name: 'TestNetwork',
// 	description: 'Network for testing purposes'
// }

export default {
    namespaced: true,
    state: {
        networks: [],
        network: {},
        form: {
            name: '',
            description: '',
            ispublic: true,
            organisations: [
                2
            ]
        },
        error: [],
        accessToken: ''
    },
    mutations: {
        setNetworks (state, { data }) {
            console.log(data.data)
            state.networks = data
        },
        setNetwork (state, { data }) {
            state.network = data || {}
            console.log(data)
        },
        addNetworkToList (state, { data }) {
            state.networks.push(data)
        },
        updateNetwork (state, { id, data }) {
            state.networks = state.networks.map((item) => {
                if (item.id !== id) { return item }
                return { ...item, ...data }
            })
        },
        deleteNetwork (state, { id }) {
            state.networks = state.networks.filter(n => n.id !== id)
        },
        setError (state, { error }) {
            state.error = error
        },
        updateOrganizationForm (state, data) {
			state.form = { ...state.form, ...data }
		}
    },
    computed: {
        ...mapState('authentication', ['accesToken'])
    },
    getters: {
        AuthenticationToken (state, getters, rootState, rootGetters) {
            return rootGetters['authentication/AuthenticationToken']
          }
    },
    actions: {
        async fetchNetworks ({ commit, getters, state }, payload) {
            console.log(getters.AuthenticationToken)
            const token = ''
            // const { response, error } = await NetworkService.get({ Authorization: `Bearer ${getters.AuthenticationToken}` })
            await axios.post('http://localhost:8000/api-token/', {
                username: 'admin',
                password: 'admin'
              }).then( response => (this.accessToken = response.data.access, console.log(this.accessToken)))
              console.log('c')
              var config = {
                headers: { 'Authorization': 'Bearer ' +this.accessToken }
            }            
            // axios({ method: 'get', url: 'http://localhost:8000/networks/', headers: { Authorization: 'Bearer ' + this.accessToken } })
            // axios.get('http://localhost:8000/networks/', config)
            // .then(response => (console.log(response.data)))
            const { response, error } = await NetworkService.get(payload)
            console.log('>>>', response.data)
            console.log(error)
            // console.log('>>')
            // console.log('??', response)
            // commit('setNetworks', response)
        },
        // async createNetwork ({ state, commit }, network) {
        //     console.log('check3')
        //     console.log(network)
        //     commit('setNetwork', network)
        // },
        async createNetwork ({ state, getters, commit }) {
            const data = state.form // getRequestData(state.form)
            console.log(getters.AuthenticationToken)
            const { response, error } = await NetworkService.post({ data, headers: { 'Content-Type': 'multipart/form-data' }, Authorization: `Bearer ${getters.AuthenticationToken}` })
            if (error) {
                commit('setError', { error })
                return
            }
            console.log(response)
            commit('addNetworkToList', response)
            commit('setNetwork', response)
            // commit('resetOrganisationForm')
        },

        async deleteNetwork ({ commit, dispatch }, payload) {
            const { error } = await NetworkService.delete(payload)
            if (error) {
                commit('setError', { error })
                return
            }
            commit('deleteNetwork', payload)
            dispatch('setNetwork', {})
        },
        setNetwork ({ state, commit }, { id }) {
            let data = state.networks.find(n => n.id === id)
            if (!data) {
                [data] = state.networks
            }
            commit('setNetwork', { data })
        },
        addNetworkToList (state, { data }) {
			state.organizations.push(data)
        },
        updateOrganizationForm ({ commit }, payload) {
			commit('updateOrganizationForm', payload)
		}
    }
}
