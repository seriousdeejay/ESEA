import { isInteger } from 'lodash' // random, debounce,
import IndirectIndicatorService from '../../../services/IndirectIndicatorService'

// const baseIndirectIndicator = { name: '', formula: '' }

export default {
    namespaced: true,
    state: {
        indirectIndicators: [],
        indirectIndicator: {},
        error: undefined,
        debouncers: {},
        errors: {},
        isSaved: {}
    },
    getters: {
        getById: state => id => state.indirectIndicatorsfilter(object => object.id === id),
        topicIndirectIndicators: (state) => {
            const filtered = {}
            state.indirectIndicators.forEach((indirectIndicator) => {
                filtered[indirectIndicator.topic] = !filtered[indirectIndicator.topic] ? [indirectIndicator] : [...filtered[indirectIndicator.topic], indirectIndicator]
            })
            console.log('filtered:', filtered)
            return filtered
        },
        // What does this getter do exactly?
        getValidIndicatorNumber: (state) => {
            const indicators = state.indirectIndicators.map(indicator => parseInt(indicator.name.match(/[^_]*$/), 10)).filter(indicator => isInteger(indicator))
            return indicators.length ? Math.max(...indicators) + 1 : 1
        }
    },
    mutations: {
        setIndirectIndicators (state, { data }) {
            state.indirectIndicators = data
            state.debouncers = {}
            state.errors = {}
            state.isSaved = {}
        },
        setIndirectIndicator (state, { data }) {
            state.indirectIndicator = data || {}
        },
        setError (state, { error, id }) {
            if (id && error?.response?.data) {
                state.errors = { ...state.errors, [id]: error?.response?.data }
                return
            }
            state.error = error
        }
    },
    actions: {
        async fetchIndirectIndicators ({ commit }, payload) {
            const { response, error } = await IndirectIndicatorService.get(payload)
            if (response) {
                commit('setError', { error })
                return
            }
            console.log(response)
            commit('setIndirectIndicators', response)
        },
        setIndirectIndicator ({ state, commit }, { id } = {}) {
            const data = state.indirectIndicators.find(indirectIndicator => indirectIndicator.id === id)
            if (data && data.id === state.indirectIndicator.id) return
            commit('setIndirectIndicator', { data })
        }
    }
}
