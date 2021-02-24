import NetworkService from '../../services/NetworkService'
import { mapMutations } from 'vuex'
// import { mapState } from 'vuex'
// import axios from 'axios'
// import axios from 'axios'
// import { AxiosInstance } from '../../plugins/axios'
// import { getRequestData } from '../../utils/helpers'

//  var config = { headers: { 'Authorization': 'Bearer ' +this.accessToken }
// axios({ method: 'get', url: 'http://localhost:8000/networks/', headers: { Authorization: 'Bearer ' + this.accessToken } })
// axios.get('http://localhost:8000/networks/', config)
// .then(response => (console.log(response.data)))

// const { response, error } = axios({ method: 'get', url: 'http://localhost:8000/networkorganisations/1/', headers: { Authorization: 'Bearer ' + this.accessToken } })
// if (error) {
// 	commit('setError', { error })
//     return
// }
//
// response.data.forEach(item => console.log(item.organisations))
// console.log(response.data[all nested dicts].organisations)

export default {
    namespaced: true,
    state: {
        networks: [],
        network: {},
        networkorganisations: [],
        // networkparticipants: [],
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
            state.networkorganisations = data.organisations || {}
        },
        setNetworkUsers (state, { data }) {
            state.networkparticipants = data || {}
        },
        deleteNetworkOrganisations (state, { id }) {
            state.networkorganisations = state.networkorganisations.filter(o => o.id !== id)
        },
        setError (state, { error }) {
            state.error = error
        },
        updateNetworkForm (state, data) {
			state.form = { ...state.form, ...data }
		}
    },
    // computed: {
    //     ...mapState('authentication', ['accesToken'])
    // },
    // getters: {
    //     AuthenticationToken (state, getters, rootState, rootGetters) { // Apparently state, getters & rootState are needed here
    //        return rootGetters['authentication/AuthenticationToken']
    //      }
    // },
    actions: {
        ...mapMutations('organisation', ['setOrganisations']),
        async fetchNetworks ({ commit }, payload) {
            const { response, error } = await NetworkService.get(payload)
            if (error) {
				commit('setError', { error })
                return
            }
            console.log(response.data)
            commit('setNetworks', response)
        },
        async fetchNetwork ({ commit, dispatch }, payload) {
            const { response, error } = await NetworkService.get(payload)
            if (error) {
                commit('setError', { error })
                return
            }
            commit('setNetwork', response)
            console.log(response.data.organisations)
            commit('setNetworkOrganisations', response)
        },
        // async fetchNetworkUsers ({ commit }, payload) {
        //     const query = `network=${payload.id}`
        //     const { response, error } = await UserService.get({ query: query })
        //     if (error) {
		// 		commit('setError', { error })
        //         return
        //     }
        //     commit('setNetworkUsers', response)
        // },
        async createNetwork ({ state, commit, dispatch }) {
            const data = state.form // getRequestData(state.form)
            const { response, error } = await NetworkService.post({ data, headers: { 'Content-Type': 'multipart/form-data' } })
            if (error) {
                commit('setError', { error })
                return
            }
            console.log(response.data)
            await dispatch('fetchNetworks', {})
            // commit('addNetworkToList', response)
            dispatch('setNetwork', response.data)
            // commit('resetOrganisationForm')
        },
        async updateNetwork ({ state, commit }) {
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
        async deleteNetworkOrganisations ({ state, commit }, payload) {
            const id = state.network.id
            const data = payload.data
            const { error } = await NetworkService.patch({ id, data, headers: { 'Content-Type': 'application/json' } })
            if (error) {
                commit('setError', { error })
                return
            }
            commit('deleteNetworkOrganisations', data)
        },
        setNetwork ({ state, commit }, { id }) {
            console.log(id)
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
        updateNetworkForm ({ commit }, payload) {
            console.log(payload)
			commit('updateNetworkForm', payload)
		}
    }
}
