
<script setup>
import { RouterLink } from 'vue-router'

const currentYear = new Date().getFullYear()
</script>

<template>
  <footer class="bg-gray-900 text-gray-300">
    <div
      class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12"
    >
      <div class="grid grid-cols-1 sm:grid-cols-2
                  lg:grid-cols-4 gap-8">

        <!-- Brand -->
        <div>
          <RouterLink
            to="/"
            class="text-2xl font-bold text-white"
          >
            DevPilot
          </RouterLink>

          <p class="mt-4 text-sm leading-6 text-gray-400">
            Build, manage, and track your development projects
            with a smarter workflow.
          </p>
        </div>

        <!-- Product -->
        <div>
          <h3 class="text-white font-semibold mb-4">
            Product
          </h3>

          <ul class="space-y-3 text-sm">
            <li>
              <RouterLink
                to="/projects"
                class="hover:text-white transition"
              >
                Projects
              </RouterLink>
            </li>
            <li>
              <RouterLink
                to="/features"
                class="hover:text-white transition"
              >
                Features
              </RouterLink>
            </li>
            <li>
              <RouterLink
                to="/pricing"
                class="hover:text-white transition"
              >
                Pricing
              </RouterLink>
            </li>
          </ul>
        </div>

        <!-- Resources -->
        <div>
          <h3 class="text-white font-semibold mb-4">
            Resources
          </h3>

          <ul class="space-y-3 text-sm">
            <li>
              <RouterLink
                to="/documentation"
                class="hover:text-white transition"
              >
                Documentation
              </RouterLink>
            </li>
            <li>
              <RouterLink
                to="/about"
                class="hover:text-white transition"
              >
                About Us
              </RouterLink>
            </li>
            <li>
              <RouterLink
                to="/contact"
                class="hover:text-white transition"
              >
                Contact
              </RouterLink>
            </li>
          </ul>
        </div>

        <!-- Social -->
        <div>
          <h3 class="text-white font-semibold mb-4">
            Connect
          </h3>

          <ul class="space-y-3 text-sm">
            <li>
              <a
                href="https://github.com"
                target="_blank"
                rel="noopener noreferrer"
                class="hover:text-white transition"
              >
                GitHub
              </a>
            </li>
            <li>
              <a
                href="https://linkedin.com"
                target="_blank"
                rel="noopener noreferrer"
                class="hover:text-white transition"
              >
                LinkedIn
              </a>
            </li>
          </ul>
        </div>
      </div>

      <!-- Copyright -->
      <div
        class="border-t border-gray-700 mt-10 pt-6
               text-center text-sm text-gray-400"
      >
        <p>
          © {{ currentYear }} DevPilot.
          All rights reserved.
        </p>
      </div>
    </div>
  </footer>
</template>
