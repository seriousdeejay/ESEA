import TopicService from '../../../services/TopicService'

// const baseTopic = { name: '', description: '' }

export default {
    namespaced: true,
    state: {
        topics: [],
        topic: [],
        error: undefined
    },
    getters: {
        // getById:
        // getErrorById
        methodTopics: state => state.topics.filter(topic => !topic.parent_topic),
        subTopics: (state) => {
            const subTopics = state.topics.filter(topic => topic.parent_topic)
            const filtered = {}
            subTopics.forEach((subTopic) => {
                if (!filtered[subTopic.parent_topic]) {
                    filtered[subTopic.parent_topic] = []
                }
                filtered[subTopic.parent_topic] = [
                    ...filtered[subTopic.parent_topic],
                    subTopic
                ]
            })
            return filtered
        }
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
