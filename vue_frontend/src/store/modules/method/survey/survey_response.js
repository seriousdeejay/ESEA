import { debounce } from 'lodash'
import SurveyResponseService from '@/services/SurveyResponseService'

const baseSurveyResponse = {
	question_responses: []
}

export default {
	namespaced: true,
	state: {
		surveyResponses: [],
		surveyResponse: {},
		error: undefined,
		debouncers: {},
		errors: {},
		isSaved: {}
	},
	getters: {
		getById: state => id => state.surveyResponses.find(
			object => object.id === id
		)
	},
	mutations: {
		setSurveyResponses (state, { data }) {
			state.surveyResponses = data
			state.debouncers = {}
			state.errors = {}
			state.isSaved = {}
		},
		setSurveyResponse (state, { data }) {
			state.surveyResponse = data || {}
		},
		deleteSurveyResponse (state, { id }) {
			delete state.debouncers[id]
			delete state.errors[id]
			delete state.isSaved[id]
			state.surveyResponses = state.surveyResponses.filter(q => q.id !== id)
		},
		setError (state, { error, id }) {
			if (id && error?.response?.data) {
				state.errors = { ...state.errors, [id]: error?.response?.data }
				return
			}
			state.error = error
		},
		updateList (state, { id, data }) {
			if (id !== data.id) {
				delete state.debouncers[id]
				delete state.errors[id]
				delete state.isSaved[id]
			}

			state.surveyResponses = state.surveyResponses.map((item) => {
				if (item.id !== id) return item
				return Object.assign(item, data)
			})
		},
		addSurveyResponse (state, { data: surveyResponse }) {
			state.surveyResponses.push(surveyResponse)
			state.surveyResponse = surveyResponse
		},
		setDebouncer (state, { id, token, commit }) {
			console.log(id)
			state.debouncers[id] = debounce(
				async ({ mId, sId, surveyResponse }) => {
					const { response, error } = await SurveyResponseService.put(
						{ mId, sId, id: token, data: surveyResponse }
					)
					if (error) {
						commit('setError', { error, id: surveyResponse.id })
						return
					}
					console.log(response)
					commit('setSurveyResponse', response)
					commit('setError', { error: {}, id: surveyResponse.id })
					commit('setIsSaved', { id: surveyResponse.id, isSaved: true })
					commit('updateList', {
						id: surveyResponse.id, data: { id: response.data.id }
					})
				},
				250
			)
		},
		setIsSaved (state, { id, isSaved = false }) {
			if (id) {
				state.isSaved = {
					...state.isSaved,
					[id]: isSaved
				}
			}
		}
	},
	actions: {
		async fetchSurveyResponses ({ commit, dispatch }, payload) {
			const { response, error } = await SurveyResponseService.get(payload)
			console.log(response)
			if (error) {
				commit('setError', { error })
				console.log(error)
				return
			}
			if (payload.id) {
				commit('setSurveyResponse', response)
			} else {
			commit('setSurveyResponses', response)
			}
		},
		async fetchSurveyResponse ({ commit }, payload) {
			const { response, error } = await SurveyResponseService.get(payload)
			if (error) {
				commit('setError', { error })
				return
			}
			commit('setSurveyResponse', response)
			return { response }
		},
		async deleteSurveyResponse ({ commit }, payload) {
			if (payload.id > 0) {
				const { error } = await SurveyResponseService.delete(payload)
				if (error) {
					commit('setError', { error })
					return
				}
			}
			commit('deleteSurveyResponse', payload)
		},
		async createSurveyResponse ({ commit }, { mId, sId, OrganisationId }) {
			console.log(mId, sId, OrganisationId)
			const { response, error } = await SurveyResponseService.post({
				mId, sId, OrganisationId, data: baseSurveyResponse
			})
			if (error) {
				commit('setError', { error })
				return { error }
			}
			commit('addSurveyResponse', response)
			// commit('setSurveyResponse', response)
			return { response }
		},
		updateSurveyResponse ({ state, commit }, { mId, sId, surveyResponse }) {
			console.log(surveyResponse.question_responses)
			if (!surveyResponse || !mId || !sId) return
			if (!state.debouncers[surveyResponse.id]) {
				commit('setDebouncer', { id: surveyResponse.id, token: surveyResponse.token, commit })
			}
			commit('updateList', { id: surveyResponse.id, data: surveyResponse })
			commit('setIsSaved', { id: surveyResponse.id })
			state.debouncers[surveyResponse.id]({ mId, sId, surveyResponse })
		},
		setSurveyResponse ({ state, commit }, { id } = {}) {
			console.log(id)
			const data = state.surveyResponses.find(r => r.id === parseInt(id))
			console.log(data)
			if (!data) return
			commit('setSurveyResponse', { data })
		},
		resetError ({ commit }) {
			commit('setError', { error: undefined })
		}
	}
}
