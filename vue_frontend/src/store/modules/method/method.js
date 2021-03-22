import MethodService from '../../../services/MethodService'
import { AxiosInstance } from '../../../plugins/axios'

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
        async fetchMethod ({ commit }, payload) {
            const { response, error } = await MethodService.get(payload)
            if (error) {
                commit('setError', { error })
                return
            }
            commit('setMethod', response)
        },
        async uploadMethod (payload) {
            var formData = new FormData()
            formData.append('file', payload)
            console.log(payload)
            return new Promise((resolve, reject) => {
                AxiosInstance.post('/import-yaml/', formData, { headers: { 'Content-Type': 'multipart/form-data' } }) // { headers: { 'Content-Type': 'multipart/form-data' } }
            .then(response => {
                console.log(response)
                resolve()
                })
            .catch(err => { reject(err) })
            })
        },
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
        async patchMethod ({ state, commit }, payload) {
            console.log(state.method.id)
            const id = payload.id || state.method.id
            console.log(id)
            const data = payload.data
            console.log(data)
            const { response, error } = await MethodService.patch({ id, data, headers: { 'Content-Type': 'application/json' } })
            console.log(response)
            if (error) {
                commit('setError', { error })
                return
            }
            commit('updateMethod', { ...response, id })
            commit('setMethod', response.data)
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
