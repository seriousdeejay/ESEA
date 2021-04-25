import axios from 'axios'
import requestAuthInterceptor from '../utils/requestAuthInterceptor'
// import responseAuthInterceptor from '../utils/responseAuthInterceptor'

const AxiosInstance = axios.create({
    baseURL: 'http://127.0.0.1:8000', // process.env.baseURL || process.env.apiUrl ||
    timeout: 1000
})

AxiosInstance.interceptors.request.use(...requestAuthInterceptor)

// AxiosInstance.interceptors.response.use(...responseAuthInterceptor)

export { AxiosInstance }
