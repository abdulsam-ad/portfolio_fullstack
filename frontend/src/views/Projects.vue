<script setup>
import { ref, onMounted } from 'vue'
import api from '../utils/api'

const projects = ref([])
const loading = ref(false)
const error = ref(null)

onMounted(async () => {
  loading.value = true
  try {
    const { data } = await api.get('/api/portfolio/projects/')
    projects.value = data
  } catch (e) {
    error.value = e?.response?.data || e.message
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="space-y-4">
    <h2 class="text-2xl font-bold">Your Projects</h2>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error" class="text-red-600">{{ error }}</div>
    <div class="grid md:grid-cols-2 gap-4">
      <article v-for="p in projects" :key="p.id" class="p-4 rounded-xl shadow bg-white">
        <h3 class="font-semibold text-lg">{{ p.title }}</h3>
        <p class="text-gray-600">{{ p.description }}</p>
        <a v-if="p.link" :href="p.link" target="_blank" class="text-blue-600 underline">Visit</a>
      </article>
    </div>
  </div>
</template>
