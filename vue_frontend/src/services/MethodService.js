import { API_URL } from '../utils/constants'
import { BaseApiService } from './BaseApiService'

const createUrl = ({ id }) => {
    const base = `${API_URL}/methods/`
    return id ? `${API_URL}${id}/` : base
}

export default new BaseApiService(createUrl)