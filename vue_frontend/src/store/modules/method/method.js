import MethodService from '../../../services/MethodService'
// import { mapState } from "vuex"

export default {
    namespaced: true,
    state: {
        methods: [],
        method: {},
        error: []
    },
    mutations: {
        setMethods (state, { data }) {
            state.methods = data
        },
        setMethod (state, { data }) {
            state.method = data || {}
        },
        addMethodToList (state, { data }) {
            state.methods.push(data)
        },
        updateMethod (state, { id, data }) {
            state.methods = state.methods.map((item) => {
                if (item.id !== id) { return item }
                return { ...item, ...data }
            })
        },
        deleteMethod (state, { id }) {
            state.methods = state.methods.filter(m => m.id !== id)
        },
        setError (state, { error }) {
            state.error = error
        }
    },
    computed: {
    },
    actions: {
        async fetchMethods ({ commit }, payload) {
            const { response, error } = await MethodService.get(payload)
            if (error) {
                commit('setError', { error })
                return
            }
            commit('setMethods', response)
        },
    // Redundant! ID can already be passed to fetchMethods!
    //     async fetchMethod ({ commit }, payload) {
    //         const { response, error } = await MethodService.get(payload)
    //     }
        async updateMethod ({ state, commit }) {
            const id = state.method.id
            const data = state.method
            const { response, error } = await MethodService.put({ id, data, headers: { 'Content-Type': 'multipart/form-data' } })
            if (error) {
                commit('setError', { error })
                return
            }
            commit('updateMethod', { response })
        },
        async deleteMethod ({ commit, dispatch }, payload) {
            const { response, error } = await MethodService.post(payload)
            if (error) {
                commit('setError', { error })
                return
            }
            commit('deleteMethod', { response })
            dispatch('setMethod', {})
        },
        setMethod ({ state, commit }, { id }) {
            if (id) {
                const data = state.methods.find(m => m.id === id)
                commit('setMethod', { data })
            } else {
                commit('setMethod', {})
            }
        }
    }
}
