import UserService from '../../services/UserService'

export default {
    namespaced: true,
    state: {
        users: [],
        user: {},
        error: []
    },
    mutations: {
        setUsers (state, { data }) {
            state.users = data
        },
        setUser (state, { data }) {
            state.user = data || {}
        },
        setError (state, { error }) {
            state.error = error
        }
    },
    actions: {
        async fetchUsers ({ commit }, payload) {
            const { response, error } = await UserService.get(payload)
            if (error) {
                commit('setError', { error })
                return
            }
            commit('setUsers', response)
        },
        async fetchUser ({ commit }, payload) {
            const { response, error } = await UserService.get(payload)
            if (error) {
                commit('setError', { error })
                return
            }
            commit('setUser', response)
        },
        setUser ({ state, commit }, { id }) {
            console.log(id)
            if (id) {
                const data = state.users.find(u => u.id === id)
                commit('setUser', { data })
            } else {
                commit('setUser', {})
            }
        }
    }
}
