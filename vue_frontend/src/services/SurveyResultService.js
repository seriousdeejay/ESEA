import { API_URL } from '../utils/constants'
import BaseApiService from './BaseApiService'

const createUrl = ({ oId = 0, mId, sId, id, query = '' }) => {
	let base = `${API_URL}/methods/${mId}/surveys/${sId}/organisations/${oId}/responses`
	base = id ? `${base}/${id}` : base
	return `${base}/${query}`
}

export default new BaseApiService(createUrl)
