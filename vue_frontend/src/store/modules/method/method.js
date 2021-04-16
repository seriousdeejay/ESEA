import MethodService from '../../../services/MethodService'
import { AxiosInstance } from '../../../plugins/axios'
import _ from 'lodash'

const baseMethod = { name: 'Untitled method', description: '...' }

export default {
    namespaced: true,
    state: {
        methods: [],
        method: { },
        error: undefined,
        debouncers: {},
        debouncer: _.debounce(async ({ id, method, commit }) => {
            const { response, error } = await MethodService.put({ id: id, data: method })
            if (error) {
                commit('setError', { error })
            } else {
                console.log('debouncing', response)
                commit('setMethod', response)
            }
        }, 1000)
            // function () { console.log('Debouncing!') }, 2000)
        // debouncer: debounce(
        //     async ({ id, data, commit }) => {
        //         console.log('chheec')
        //         const { response, error } = await MethodService.put({ id, data, headers: { 'Content-Type': 'multipart/form-data' } })
        //         if (error) {
        //             commit('setError', { error })
        //         } else {
        //             commit('setMethod', response)
        //             commit('addMethodToList', { ...response, id })
        //         }
        //     }, 1000
        // )

    },
    mutations: {
        setMethods (state, { data }) {
            state.methods = data
        },
        setMethod (state, { data }) {
            state.method = { ...data } || baseMethod
        },
        addMethodToList (state, { data }) {
            state.methods.push(data)
        },
        // updateMethod(state, data) {},
        // setDebouncer (state, { id, commit }) {
        //     console.log('ccchheeck')
        //     state.debouncers[id] = debounce(
        //         async ({ id, data }) => {
        //             console.log('zzz', data)
        //             const { response, error } = await MethodService.put({ id, data: data })
        //             if (error) {
        //                 console.log(error)
        //                 commit('setError', { error })
        //                 return
        //             }
        //             commit('setMethod', response)
        //             state.methods = state.methods.map((item) => {
        //             if (item.id !== response.data.id) { return item }
        //                 return { ...item, ...response.data }
        //             })
        //         },
        //         1000
        //     )
        // },
        deleteMethod (state, { id }) {
            state.methods = state.methods.filter(m => m.id !== id)
        },
        setError (state, { error }) {
            state.error = error
        }
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
        async createMethod ({ commit, dispatch }) {
            const { response, error } = await MethodService.post({ data: baseMethod })
            if (error) {
                commit('setError', { error })
                return
            }
            await dispatch('fetchMethods', {})
            commit('setMethod', response)
        },
        async updateMethod ({ state, commit }, method) {
            if (method.id !== state.method.id) { return }
            state.debouncer({ id: method.id, method, commit })
        },
        // async patchMethod ({ state, commit }, payload) {
        //     console.log(state.method.id)
        //     const id = payload.id || state.method.id
        //     console.log(id)
        //     const data = payload.data
        //     console.log(data)
        //     const { response, error } = await MethodService.patch({ id, data, headers: { 'Content-Type': 'application/json' } })
        //     console.log(response)
        //     if (error) {
        //         commit('setError', { error })
        //         return
        //     }
        //     commit('updateMethod', { ...response, id })
        //     commit('setMethod', response.data)
        // },
        async deleteMethod ({ commit, dispatch }, payload) {
            const { response, error } = await MethodService.delete(payload)
            if (error) {
                commit('setError', { error })
                return
            }
            commit('deleteMethod', { response })
            dispatch('setMethod', {})
        },
        setMethod ({ state, commit }, { id }) {
            console.log('ld:', id)
            if (id) {
                const data = state.methods.find(m => m.id === id)
                console.log('}}}', data)
                commit('setMethod', { data })
            } else {
                commit('setMethod', {})
            }
        }
    }
}

           // debounce(
            // //     console.log('debounce works!')
            // // , 10000)
            // if (!state.debouncers[method.id]) {
            //     console.log('ddd')
            //     commit('setDebouncer', { id: method.id, commit })
            // }
            // state.debouncers[method.id]({ method })
            // state.debouncer({ id, data: payload, commit })
            // commit('updateMethod', { id: id, data: method })

            // const data = payload
            // const { response, error } = await MethodService.put({ id, data, headers: { 'Content-Type': 'multipart/form-data' } })
            // console.log(error)
            // if (error) {
            //     commit('setError', { error })
            //     return
            // }
            // // commit('updateMethod', { response })
            // await dispatch('fetchMethods', {})
            // dispatch('setMethod', response.data)

        // async patchMethod ({ state, commit }, payload) {
        //     console.log(state.method.id)
        //     const id = payload.id || state.method.id
        //     console.log(id)
        //     const data = payload.data
        //     console.log(data)
        //     const { response, error } = await MethodService.patch({ id, data, headers: { 'Content-Type': 'application/json' } })
        //     console.log(response)
        //     if (error) {
        //         commit('setError', { error })
        //         return
        //     }
        //     commit('updateMethod', { ...response, id })
        //     commit('setMethod', response.data)
        // },
