import NetworkService from '../../services/NetworkService'
import { mapState } from 'vuex'
import axios from 'axios'
// import { AxiosInstance } from '../../plugins/axios'
// import { getRequestData } from '../../utils/helpers'

// const baseNetwork = {
// 	name: 'TestNetwork',
// 	description: 'Network for testing purposes'
// }

//  var config = { headers: { 'Authorization': 'Bearer ' +this.accessToken }
// axios({ method: 'get', url: 'http://localhost:8000/networks/', headers: { Authorization: 'Bearer ' + this.accessToken } })
// axios.get('http://localhost:8000/networks/', config)
// .then(response => (console.log(response.data)))

// const { response, error } = axios({ method: 'get', url: 'http://localhost:8000/networkorganisations/1/', headers: { Authorization: 'Bearer ' + this.accessToken } })
// if (error) {
// 	commit('setError', { error })
//     return
// }

export default {
    namespaced: true,
    state: {
        networks: [],
        network: {},
        networkorganisations: [],
        form: {
            name: 'Network N',
            description: 'Description of Network N',
            ispublic: true,
            organisations: [
            ]
        },
        error: []
    },
    mutations: {
        setNetworks (state, { data }) {
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
        setNetworkOrganisations (state, { data }) {
            state.networkorganisations = data || {}
            console.log(data)
        },
        setError (state, { error }) {
            state.error = error
        },
        updateNetworkForm (state, data) {
			state.form = { ...state.form, ...data }
		}
    },
    computed: {
        ...mapState('authentication', ['accesToken'])
    },
    getters: {
        AuthenticationToken (state, getters, rootState, rootGetters) { // Apparently state, getters & rootState are needed here
           return rootGetters['authentication/AuthenticationToken']
         }
    },
    actions: {
        async fetchNetworks ({ commit }, payload) {
            const { response, error } = await NetworkService.get(payload) // How can i import id as payload?
            if (error) {
				commit('setError', { error })
                return
            }
            commit('setNetworks', response)
        },
        async fetchNetwork ({ commit }, payload) {
            const { response, error } = await NetworkService.get(payload)
            if (error) {
                commit('setError', { error })
                return
            }
            commit('setNetwork', response)
        },
        async fetchNetworkOrganisations ({ commit, state, getters }, payload) {
            console.log(getters.AuthenticationToken)
            var config = { headers: { Authorization: 'Bearer ' + getters.AuthenticationToken } }
            const response = await axios.get(`http://localhost:8000/networkorganisations/${payload}/`, config)
            console.log(response)
            commit('setNetworkOrganisations', response)
        },
        // async createNetwork ({ state, commit }, network) {
        //     console.log(network)
        //     commit('setNetwork', network)
        // },
        async createNetwork ({ state, commit }) {
            const data = state.form // getRequestData(state.form)
            const { response, error } = await NetworkService.post({ data, headers: { 'Content-Type': 'multipart/form-data' } })
            if (error) {
                commit('setError', { error })
                return
            }
            console.log(response)
            commit('addNetworkToList', response)
            commit('setNetwork', response)
            // commit('resetOrganisationForm')
        },
        async updateNetwork ({ state, commit }) {
            console.log(state.network)
            const id = state.network.id
            const data = state.network
            const { response, error } = await NetworkService.put({ id, data, headers: { 'Content-Type': 'multipart/form-data' } })
            if (error) {
                commit('setError', { error })
                return
            }
            commit('updateNetwork', { ...response, id })
            commit('setNetwork', response)
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
            if (id) {
                const data = state.networks.find(n => n.id === id)
                commit('setNetwork', { data })
            } else {
                commit('setNetwork', {})
            }
            // if (!data) {
            //     [data] = state.networks
            // }
        },
        addNetworkToList (state, { data }) {
			state.organizations.push(data)
        },
        updateNetworkForm ({ commit }, payload) {
			commit('updateNetworkForm', payload)
		}
    }
}
