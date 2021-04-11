import OrganisationService from '../../services/OrganisationService'

export default {
    namespaced: true,
    state: {
        organisations: [],
        organisation: {},
        // organisationParticipants: [],
        error: []
    },
    mutations: {
        setOrganisations (state, { data }) {
            state.organisations = data
        },
        setOrganisation (state, { data }) {
            state.organisation = data || {}
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
        // setOrganisationParticipants (state, { data }) {
        //     state.organisationParticipants = data.participants || {}
        // },
        // deleteOrganisationUsers (state, { id }) {
        //     state.organisationParticipants = state.organisationParticipants.filter(o => o.id !== id)
        // },
        setError (state, { error }) {
            state.error = error
        }
    },
    actions: {
        async fetchOrganisations ({ commit }, payload) {
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
            // commit('setOrganisationParticipants', response)
        },
        async createOrganisation ({ state, commit, dispatch }, { data }) {
            const { response, error } = await OrganisationService.post({ data: data, headers: { 'Content-Type': 'multipart/form-data' } })
            if (error) {
                commit('setError', { error })
                return
            }
            await dispatch('fetchOrganisations', {})
            dispatch('setOrganisation', response.data)
        },
        async updateOrganisation ({ state, commit }) {
            const id = state.organisation.id
            const data = state.organisation
            const { response, error } = await OrganisationService.put({ id, data, headers: { 'Content-Type': 'multipart/form-data' } })
            if (error) {
                commit('setError', { error })
                return
            }
            commit('updateOrganisation', response)
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
        async patchOrganisation ({ state, commit }, payload) {
            const id = state.organisation.id
            const data = payload.data
            const { response, error } = await OrganisationService.patch({ id, data, headers: { 'Content-Type': 'application/json' } })
            if (error) {
                commit('setError', { error })
                return
            }
            commit('updateNetwork', { ...response, id })
            commit('setNetwork', response)
        },
        setOrganisation ({ state, commit }, { id }) {
            if (id) {
                const data = state.organisations.find(o => o.id === id)
                commit('setOrganisation', { data: data })
            } else {
                commit('setOrganisation', {})
            }
        }
    }
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
        // async fetchOrganisationUsers ({ commit }, payload) {
        //     const query = `organisation=${payload.id}`
        //     const { response, error } = await UserService.get({ query: query })
        //     if (error) {
		// 		commit('setError', { error })
        //         return
        //     }
        //     console.log(response)
            // var config = { headers: { Authorization: 'Bearer ' + getters.AuthenticationToken } }
            // const response = await axios.get(`http://localhost:8000/users/?network=${payload.id}`, config)
        //     commit('setNetworkUsers', response)
        // },
