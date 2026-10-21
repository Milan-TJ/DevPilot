
<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'

const menuOpen = ref(false)

const closeMenu = () => {
  menuOpen.value = false
}
</script>

<template>
  <nav class="bg-white border-b border-gray-200 shadow-sm">
    <div
      class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"
    >
      <div class="flex justify-between items-center h-16">

        <!-- Logo -->
        <RouterLink
          to="/"
          class="text-2xl font-bold text-indigo-600"
          @click="closeMenu"
        >
          DevPilot
        </RouterLink>

        <!-- Desktop Navigation -->
        <div class="hidden md:flex items-center gap-8">
          <RouterLink
            to="/chat"
            class="text-gray-700 hover:text-indigo-600"
            active-class="!text-indigo-600 font-semibold"
          >
            Chat
          </RouterLink>

          <RouterLink
            to="/projects"
            class="text-gray-700 hover:text-indigo-600"
            active-class="!text-indigo-600 font-semibold"
          >
            Projects
          </RouterLink>

          <RouterLink
            to="/about"
            class="text-gray-700 hover:text-indigo-600"
            active-class="!text-indigo-600 font-semibold"
          >
            About
          </RouterLink>
        </div>

        <!-- Authentication -->
        <div class="hidden md:flex items-center gap-4">
          <RouterLink
            to="/login"
            class="text-gray-700 hover:text-indigo-600"
          >
            Login
          </RouterLink>

          <RouterLink
            to="/register"
            class="bg-indigo-600 text-white px-4 py-2 rounded-lg
                   hover:bg-indigo-700 transition"
          >
            Get Started
          </RouterLink>
        </div>

        <!-- Mobile Menu Button -->
        <button
          @click="menuOpen = !menuOpen"
          class="md:hidden p-2 text-gray-700"
          :aria-expanded="menuOpen"
          aria-label="Toggle navigation menu"
        >
          <svg
            v-if="!menuOpen"
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16"
            />
          </svg>

          <svg
            v-else
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M6 18L18 6M6 6l12 12"
            />
          </svg>
        </button>
      </div>

      <!-- Mobile Navigation -->
      <div
        v-if="menuOpen"
        class="md:hidden border-t border-gray-200 py-4 space-y-3"
      >
        <RouterLink
          to="/"
          class="block text-gray-700 hover:text-indigo-600"
          @click="closeMenu"
        >
          Home
        </RouterLink>

        <RouterLink
          to="/projects"
          class="block text-gray-700 hover:text-indigo-600"
          @click="closeMenu"
        >
          Projects
        </RouterLink>

        <RouterLink
          to="/about"
          class="block text-gray-700 hover:text-indigo-600"
          @click="closeMenu"
        >
          About
        </RouterLink>

        <RouterLink
          to="/login"
          class="block text-gray-700 hover:text-indigo-600"
          @click="closeMenu"
        >
          Login
        </RouterLink>

        <RouterLink
          to="/register"
          class="block bg-indigo-600 text-white text-center
                 px-4 py-2 rounded-lg"
          @click="closeMenu"
        >
          Get Started
        </RouterLink>
      </div>
    </div>
  </nav>
</template>
