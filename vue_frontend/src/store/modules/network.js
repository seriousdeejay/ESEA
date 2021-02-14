import NetworkService from '../../services/NetworkService'
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
        setError (state, { error }) {
            state.error = error
        },
        updateOrganizationForm (state, data) {
			state.form = { ...state.form, ...data }
		}
    },
    actions: {
        async fetchNetworks ({ commit }, payload) {
            const { response, error } = await NetworkService.get(payload)
            console.log(error)
            commit('setNetworks', response)
        },
        // async createNetwork ({ state, commit }, network) {
        //     console.log('check3')
        //     console.log(network)
        //     commit('setNetwork', network)
        // },
        async createNetwork ({ state, commit }) {
            console.log(state.form)
            const data = state.form // getRequestData(state.form)
            const { response, error } = await NetworkService.post({ data, headers: { 'Content-Type': 'multipart/form-data' } }) // , Authorization: `Bearer ${rootState.accessToken}`
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
