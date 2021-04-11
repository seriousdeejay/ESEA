import TopicService from '../../../services/TopicService'

export default {
    namespaced: true,
    state: {
        topics: [],
        topic: [],
        error: undefined
    },
    mutations: {
        setTopics (state, { data }) {
			state.topics = data
			// state.debouncers = {}
			state.errors = {}
			// state.isSaved = {}
		},
        setError (state, { error }) {
            // if (id && error?.response?.data) {
            //     state.errors = { ...state.errors, [id]: error?.response?.data }
            //     return
            // }
            state.error = error
        }
    },
    actions: {
        async fetchTopics ({ commit }, payload) {
            const { response, error } = await TopicService.get(payload)
            if (error) {
                commit('setError', { error })
                return
            }
            commit('setTopics', response)
        }
    }
}
