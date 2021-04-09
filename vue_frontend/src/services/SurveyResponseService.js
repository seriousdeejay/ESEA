import { API_URL } from '../utils/constants'
import BaseApiService from './BaseApiService'

const createUrl = ({ nId, cId, eaId, id, query = '' }) => {
    console.log(query)
    let base = `${API_URL}/networks/${nId}/campaigns/${cId}/esea-accounts/${eaId}/responses`
    base = id ? `${base}/${id}` : base
    return `${base}/${query}`
}

// const createUrl = ({ mId, sId, OrganisationId = 0, id, query = '' }) => {
//     let base = `${API_URL}/methods/${mId}/surveys/${sId}/organisations/${OrganisationId}/responses`
//     base = id ? `${base}/${id}` : base
//     return `${base}/${query}`
// }

export default new BaseApiService(createUrl)
