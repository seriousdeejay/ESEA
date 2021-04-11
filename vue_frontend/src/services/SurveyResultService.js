import { API_URL } from '../utils/constants'
import BaseApiService from './BaseApiService'

const createUrl = ({ nId = 0, cId = 0, eaId, id, query = '' }) => {
	let base = `${API_URL}/networks/${nId}/campaigns/${cId}/esea-accounts/${eaId}/responses`
	base = id ? `${base}/${id}` : base
	return `${base}/${query}`
}

export default new BaseApiService(createUrl)
