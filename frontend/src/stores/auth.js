import { defineStore } from 'pinia'
import api from '../utils/api'

export const useAuth = defineStore('auth', {
  state: () => ({ access: null, refresh: null, user: null }),
  actions: {
    async login(username, password) {
      const { data } = await api.post('/api/auth/token/', { username, password })
      this.access = data.access
      this.refresh = data.refresh
      api.defaults.headers.common['Authorization'] = `Bearer ${this.access}`
      await this.me()
    },
    async refreshToken() {
      if (!this.refresh) return
      const { data } = await api.post('/api/auth/token/refresh/', { refresh: this.refresh })
      this.access = data.access
      api.defaults.headers.common['Authorization'] = `Bearer ${this.access}`
    },
    async me() {
      const { data } = await api.get('/api/auth/me/')
      this.user = data
    },
    logout() {
      this.access = null
      this.refresh = null
      this.user = null
      delete api.defaults.headers.common['Authorization']
    }
  },
})
