<template>
  <main class="min-h-screen bg-gray-50 text-gray-900">
    <header class="bg-gradient-to-r from-purple-600 via-pink-500 to-red-500 shadow-lg sticky top-0 z-50">
      <nav class="max-w-6xl mx-auto flex items-center justify-between px-6 py-4 text-white">
        <!-- Logo -->
        <h1 class="text-2xl md:text-3xl font-extrabold tracking-wide">
          🚀 Portfolio
        </h1>

        <!-- Links -->
        <div class="space-x-6 text-lg font-semibold">
          <RouterLink
              to="/"
              class="hover:text-yellow-300 transition-colors duration-300"
          >
            Home
          </RouterLink>
          <RouterLink
              to="/projects"
              class="hover:text-yellow-300 transition-colors duration-300"
          >
            Projects
          </RouterLink>
          <RouterLink
              to="/login"
              class="hover:text-yellow-300 transition-colors duration-300"
          >
            Login
          </RouterLink>
        </div>
      </nav>
    </header>

    <section class="max-w-5xl mx-auto p-6">
      <RouterView />
    </section>
    <footer class="p-6 text-center text-sm text-gray-500">© {{ year }} Portfolio</footer>
  </main>
</template>

<script setup>
import { computed } from 'vue'
const year = computed(() => new Date().getFullYear())
</script>
