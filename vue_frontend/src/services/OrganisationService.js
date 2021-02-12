import { API_URL } from '../utils/constants'
import BaseApiService from './BaseApiService'

const createUrl = ({ id }) => {
    const base = `${API_URL}/organisations/`
    return id ? `${base}${id}` : base
}

export default new BaseApiService(createUrl)