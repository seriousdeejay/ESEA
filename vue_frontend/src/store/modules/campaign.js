import CampaignService from '../../services/CampaignService'
// import { AxiosInstance } from '../../../plugins/axios'

export default {
    namespaced: true,
    state: {
        campaigns: [],
        campaign: {},
        error: []
    },
    mutations: {
        setCampaigns (state, { data }) {
            state.campaigns = data || {}
        },
        setCampaign (state, { data }) {
            state.campaign = data || {}
        },
        addCampaignToList (state, { data }) {
            state.campaigns.push(data)
        },
        updateCampaign (state, { data, id }) {
            state.campaigns = state.campaigns.map((item) => {
                if (item.id !== id) { return item }
                return { ...item, ...data }
            })
        },
        deleteCampaign (state, { id }) {
            state.campaigns = state.campaigns.filter(c => c.id !== id)
        },
        setError (state, { error }) {
            state.error = error
        }
    },
    actions: {
        async fetchCampaigns ({ commit }, payload) {
            const { response, error } = await CampaignService.get(payload)
            if (error) {
                commit('setError', { error })
                return
            }
            commit('setCampaigns', response)
        },
        async fetchCampaign ({ commit }, payload) {
            const { response, error } = await CampaignService.get(payload)
            if (error) {
                commit('setError', { error })
                return
            }
            commit('setCampaign', response)
        },
        async createCampaign ({ commit, dispatch }, { nId, data }) {
            console.log(data)
            const { response, error } = await CampaignService.post({ nId, data: data })
            if (error) {
                commit('setError', { error })
                return
            }
            await dispatch('fetchCampaigns', {})
            console.log(response.data)
            dispatch('setCampaign', response.data)
        },
        async updateCampaign ({ state, commit }) {
            const id = state.campaign.id
            const data = state.campaign
            const { response, error } = await CampaignService.put({ id, data, headers: { 'Content-Type': 'multipart/form-data' } })
            if (error) {
                commit('setError', { error })
                return
            }
            commit('updateCampaign', response)
        },
        async deleteCampaign ({ commit, dispatch }, payload) {
            const { error } = await CampaignService.delete(payload)
            if (error) {
                commit('setError', { error })
                return
            }
            commit('deleteCampaign', { payload })
            dispatch('setCampaign', {})
        },
        setCampaign ({ state, commit }, { id }) {
            console.log(id)
            if (id) {
                const data = state.campaigns.find(m => m.id === id)
                console.log(data)
                commit('setCampaign', { data })
            } else {
                commit('setCampaign', {})
            }
        }
    }
}
