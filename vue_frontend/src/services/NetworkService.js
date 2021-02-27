import { API_URL } from '../utils/constants'
import BaseApiService from './BaseApiService'

const createUrl = ({ id, query }) => {
    const base = `${API_URL}/networks/`
    if (id) {
        return `${base}${id}/`
    } else if (query) {
        return `${base}?${query}`
    } else {
        return base
    }
}

export default new BaseApiService(createUrl)
