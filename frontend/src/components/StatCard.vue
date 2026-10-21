<script setup>
defineProps({
  title: {
    type: String,
    required: true,
  },
  value: {
    type: [Number, String],
    required: true,
  },
  description: {
    type: String,
    default: '',
  },
})
</script>

<template>
  <article class="stat-card">
    <p class="stat-title">{{ title }}</p>
    <h2 class="stat-value">{{ value }}</h2>
    <p class="stat-description">{{ description }}</p>
  </article>
</template>

<style scoped>
.stat-card {
  padding: 20px;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  background: white;
}

.stat-title,
.stat-description {
  color: #64748b;
  margin: 0;
}

.stat-value {
  font-size: 2rem;
  margin: 12px 0;
}
</style>