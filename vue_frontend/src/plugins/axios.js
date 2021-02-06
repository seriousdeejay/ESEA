import axios from 'axios'

const AxiosInstance = axios.create({
    baseURL: 'http://127.0.0.1:8000', // process.env.baseURL || process.env.apiUrl ||
    timeout: 1000
})

export { AxiosInstance }