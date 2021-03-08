import { API_URL } from '../utils/constants'
import BaseApiService from './BaseApiService'

const createUrl = ({ mId, sId, id, query = ''}) => {
    let base = `${API_URL}/methods/${mId}/surveys/${sId}/responses/`
    base = id ? `${base}${id}/` : base
    return `${base}/${query}`
}

export default new BaseApiService(createUrl)