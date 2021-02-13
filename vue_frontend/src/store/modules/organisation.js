// const baseOrganisation = {
//     ispublic: true,
//     name: '',
//     description: '',
// }

// import OrganisationService from "../../services/OrganisationService"
// import { AxiosInstance } from '../../plugins/axios'
// import TestService from '../../services/TestService'
import OrganisationService from '../../services/OrganisationService'
import { getRequestData } from '../../utils/helpers'

export default {
    namespaced: true,
    state: {
        organisations: [], // { name: '1' }, { name: '2' }, { name: '3' }
        organisation: {},
        error: []
    },
    mutations: {
        setOrganisations (state, { data }) {
            console.log(data)
            state.organisations = data
            console.log(state.organisations)
        },
        setOrganisation (state, { data }) {
            state.organisation = data || {}
        },
        updateOrganisation (state, { id, data }) {
        },
        addOrganisationToList (state, { data }) {
            state.organisations.push(data)
        },
        setError (state, { error }) {
            state.error = error
        }
    },
    actions: {
        async fetchOrganisations ({ commit }, payload) { // Working function
            const { response, error } = await OrganisationService.get(payload)
            console.log(response)
            console.log(error)
            commit('setOrganisations', response)
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
        },
        async createOrganisation ({ state, commit }) {
            const data = getRequestData(state.form)
            const { response, error } = await OrganisationService.post({ data, headers: { 'Content-Type': 'multipart/form-data' } })
            if (error) {
                commit('setError', { error })
                return
            }
            commit('addOrganisationinToList', response)
            commit('setOrganisation', response)
        },
        async updateOrganisation ({ state, commit }) {
        }
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
    }
}
