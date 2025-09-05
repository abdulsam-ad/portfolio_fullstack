import axios from 'axios'
const api = axios.create({ baseURL: '/' })

api.interceptors.response.use(
  (r) => r,
  async (error) => {
    console.error('API error:', error?.response?.data || error.message)
    throw error
  }
)

export default api
