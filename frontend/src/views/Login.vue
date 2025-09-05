<script setup>
import { ref } from 'vue'
import { useAuth } from '../stores/auth'
const auth = useAuth()
const username = ref('')
const password = ref('')
const error = ref(null)
const loading = ref(false)

const submit = async () => {
  error.value = null
  loading.value = true
  try {
    await auth.login(username.value, password.value)
  } catch (e) {
    error.value = e?.response?.data?.detail || 'Login failed'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <form @submit.prevent="submit" class="max-w-md space-y-4">
    <h2 class="text-2xl font-bold">Login</h2>
    <input v-model="username" placeholder="Username" class="w-full p-2 border rounded" />
    <input v-model="password" type="password" placeholder="Password" class="w-full p-2 border rounded" />
    <button class="px-4 py-2 rounded bg-black text-white" :disabled="loading">
      {{ loading ? '...' : 'Login' }}
    </button>
    <p v-if="error" class="text-red-600">{{ error }}</p>
  </form>
</template>
