<script setup>
import { ref } from 'vue'
import { validateProject } from '@/services/automationService'

const running = ref(false)
const result = ref(null)
const error = ref('')

async function runValidation() {
  running.value = true
  result.value = null
  error.value = ''

  try {
    result.value = await validateProject()
  } catch {
    error.value = 'Could not run validation.'
  } finally {
    running.value = false
  }
}
</script>

<template>
  <section>
    <h2>Automation</h2>

    <button
      @click="runValidation"
      :disabled="running"
    >
      {{ running ? 'Validating...' : 'Run Validation' }}
    </button>

    <p v-if="result">
      Status: {{ result.status }}
    </p>

    <pre v-if="result">{{ result }}</pre>
    <p v-if="error">{{ error }}</p>
  </section>
</template>