import { AxiosInstance } from '../plugins/axios'

export default async ({ method = 'get', url, data }) => {
    try {
        console.log(url)
        const response = await AxiosInstance[method](url, data)
        return { response }
    } catch (error) {
        return { error }
    }
}
