import { API_URL } from '../utils/constants'
import BaseApiService from './BaseApiService'

// const createUrl = ({ id }) => {
//     const base = `${API_URL}/methods/`
//     return id ? `${base}${id}/` : base
// }

const createUrl = ({ id, query = '' }) => {
    console.log(query)
    let base = `${API_URL}/methods`
    base = id ? `${base}/${id}/` : base
    return `${base}/${query}`
}

export default new BaseApiService(createUrl)
