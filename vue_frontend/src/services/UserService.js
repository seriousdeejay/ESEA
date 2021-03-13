import { API_URL } from '../utils/constants'
import BaseApiService from './BaseApiService'

const createUrl = ({ id, query = '' }) => {
    console.log('ee', query)
    let base = `${API_URL}/users`
    base = id ? `${base}/${id}/` : base
    return `${base}/${query}`
}

export default new BaseApiService(createUrl)
