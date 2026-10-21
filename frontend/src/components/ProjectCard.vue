<script setup>
defineProps({
  project: {
    type: Object,
    required: true,
  },
})
</script>

<template>
  <article class="project-card">
    <h3>{{ project.name }}</h3>
    <p>{{ project.description || 'No description provided' }}</p>
    <a
      v-if="project.repository"
      :href="project.repository"
      target="_blank"
      rel="noopener noreferrer"
    >
      View repository ↗
    </a>
  </article>
</template>

<style scoped>
.project-card {
  padding: 18px;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
}

.project-card h3 {
  margin-top: 0;
}

.project-card p {
  color: #64748b;
}
</style>