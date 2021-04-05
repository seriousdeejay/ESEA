import EseaAccountService from '../../services/EseaAccountService'
// import { AxiosInstance } from '../../plugins/axios'

export default {
    namespaced: true,
    state: {
        eseaAccounts: [],
        eseaAccount: {},
        error: []
    },
    mutations: {
        setEseaAccounts (state, { data }) {
            state.eseaAccounts = data
        },
        setEseaAccount (state, { data }) {
            state.eseaAccount = data || {}
        },
        addEseaAccountToList (state, { data }) {
            state.eseaAccounts.push(data)
        },
        updateEseaAccount (state, { data, id }) {
            state.eseaAccounts = state.eseaAccounts.map((item) => {
                if (item.id !== id) { return item }
                return { ...item, ...data }
            })
        },
        deleteEseaAccount (state, { id }) {
            state.eseaAccounts = state.setEseaAccount.filter(e => e.id !== id)
        },
        setError (state, { error }) {
            state.error = error
        }
    },
    actions: {
        async fetchEseaAccounts ({ commit }, payload) {
            const { response, error } = await EseaAccountService.get(payload)
            if (error) {
                commit('setError', { error })
                return
            }
            commit('setEseaAccounts', response)
        },
        async fetchEseaAccount ({ commit }, payload) {
            const { response, error } = await EseaAccountService.get(payload)
            if (error) {
                commit('setError', { error })
                return
            }
            commit('setEseaAccount', response)
        },
        async updateEseaAccount ({ state, commit }) {
            const id = state.eseaAccount.id
            const data = state.eseaAccount
            const { response, error } = await EseaAccountService.put({ id, data, headers: { 'Content-Type': 'multipart/form-data' } })
            if (error) {
                commit('setError', { error })
                return
            }
            commit('updateEseaAccount', response) // { ...response, id }
            commit('setEseaAccount', response)
        },
        async deleteEseaAccount ({ commit, dispatch }, payload) {
            const { error } = await EseaAccountService.delete(payload)
            if (error) {
                commit('setError', { error })
                return
            }
            commit('deleteEseaAccount', { payload })
            dispatch('setEseaAccount', {})
        },
        setEseaAccount ({ state, commit }, { id }) {
            if (id) {
                const data = state.eseaAccounts.find(e => e.id === id)
                commit('setEseaAccount', { data })
            } else {
                commit('setEseaAccount', {})
            }
        }
    }
}
