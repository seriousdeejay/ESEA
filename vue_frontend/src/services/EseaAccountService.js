import { API_URL } from '../utils/constants'
import BaseApiService from './BaseApiService'

const createUrl = ({ nId, cId, id, query = '' }) => {
    console.log(query)
    let base = `${API_URL}/networks/${nId}/campaigns/${cId}/esea-accounts`
    base = id ? `${base}/${id}` : base
    return `${base}/${query}`
}

export default new BaseApiService(createUrl)
