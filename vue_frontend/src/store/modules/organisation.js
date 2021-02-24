// import { AxiosInstance } from '../../plugins/axios'
// import TestService from '../../services/TestService'
import OrganisationService from '../../services/OrganisationService'
import UserService from '../../services/UserService'
// import { getRequestData } from '../../utils/helpers'

export default {
    namespaced: true,
    state: {
        organisations: [], // { name: '1' }, { name: '2' }, { name: '3' }
        organisation: {},
        organisationParticipants: [],
        form: {
            name: 'Network N',
            description: 'Description of Network N',
            ispublic: true,
            participants: [
            ]
        },
        error: []
    },
    mutations: {
        setOrganisations (state, { data }) {
            console.log(data)
            state.organisations = data
            // console.log(state.organisations)
        },
        setOrganisation (state, { data }) {
            state.organisation = data || {}
            console.log(state.organisation)
        },
        addOrganisationToList (state, { data }) {
            state.organisations.push(data)
        },
        updateOrganisation (state, { id, data }) {
            state.organisations = state.organisations.map((item) => {
                if (item.id !== id) { return item }
                return { ...item, ...data }
            })
        },
        deleteOrganisation (state, { id }) {
            state.organisations = state.organisations.filter(o => o.id !== id)
        },
        setNetworkUsers (state, { data }) {
            console.log(data)
            state.organisationParticipants = data || {}
        },
        setError (state, { error }) {
            state.error = error
        },
        updateOrganisationForm (state, data) {
            state.form = { ...state.form, ...data }
        }
    },
    actions: {
        async fetchOrganisations ({ commit }, payload) { // Working function
            const { response, error } = await OrganisationService.get(payload)
            if (error) {
                commit('setError', { error })
                return
            }
            commit('setOrganisations', response)
        },
        async fetchOrganisation ({ commit }, payload) {
            const { response, error } = await OrganisationService.get(payload)
            if (error) {
                commit('setError', { error })
                return
            }
            commit('setOrganisation', response)
        },
        async fetchOrganisationUsers ({ commit }, payload) {
            const query = `organisation=${payload.id}`
            const { response, error } = await UserService.get({ query: query })
            if (error) {
				commit('setError', { error })
                return
            }
            console.log(response)
            // var config = { headers: { Authorization: 'Bearer ' + getters.AuthenticationToken } }
            // const response = await axios.get(`http://localhost:8000/users/?network=${payload.id}`, config)
            commit('setNetworkUsers', response)
        },
        async createOrganisation ({ state, commit }) {
            const data = state.form // getRequestData(state.form)
            const { response, error } = await OrganisationService.post({ data, headers: { 'Content-Type': 'multipart/form-data' } })
            if (error) {
                commit('setError', { error })
                return
            }
            commit('addOrganisationToList', response)
            commit('setOrganisation', response)
        },
        async updateOrganisation ({ state, commit }) {
            const id = state.organisation.id
            const data = state.organisation
            const { response, error } = await OrganisationService.put({ id, data, headers: { 'Content-Type': 'multipart/form-data' } })
            if (error) {
                commit('setError', { error })
                return
            }
            commit('updateOrganisation', { response })
        },
        async deleteOrganisation ({ commit, dispatch }, payload) {
            const { error } = await OrganisationService.delete(payload)
            if (error) {
                commit('setError', { error })
                return
            }
            commit('deleteOrganisation', payload)
            dispatch('setOrganisation', {})
        },
        setOrganisation ({ state, commit }, { id }) {
            console.log(id)
            if (id) {
                const data = state.organisations.find(o => o.id === id)
                commit('setOrganisation', { data })
            } else {
                commit('setOrganisation', {})
            }
        },
        updateOrganisationForm ({ commit }, payload) {
            commit('updateOrganisationForm', payload)
        }
        // resetError ({ commit }) {
        //     commit('setError', { error: undefined })
        // }
        // }
        // async fetchOrganisations({ commit }, payload) {
        //     const { response, error } =  AxiosInstance.get(`http://127.0.0.1:8000/organisations/${this.$route.params.id}/`)
        //     //     .then(response => {
        //     //         console.log(response.data)
        //     //         this.post = response.data
        //     //     })
        //     await OrganisationService.get(payload)
        //     console.log(response)
        //     if (error) {
        //         commit('setError', { error })
        //         return
        //     }
        //     commit('setOrganisations', response)
        //
                // async fetchOrganisations () {
        //     await TestService.get()
        //     .then(response => {
        //         this.organisations = response.data
        //         console.log(this.organisations)
        //     })
        //     .catch(err => {
        //     console.log(err)
            // AxiosInstance.get('/organisations/', { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
            // .then(response => {
            //   commit('setOrganisations', response)
            // })
            // .catch(err => {
            //   console.log(err)
          //  })
    }
}
