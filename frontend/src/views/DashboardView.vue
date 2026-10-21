<script setup>
import { ref, computed, onMounted } from 'vue'
import { getProjects } from '../services/projectService'
import StatCard from '../components/StatCard.vue'
import ProjectCard from '../components/ProjectCard.vue'
import Validation from '../components/Validation.vue'


const projects = ref([])
const loading = ref(false)
const error = ref('')

const totalProjects = computed(() => projects.value.length)

async function loadDashboard() {
  loading.value = true
  error.value = ''

  try {
    projects.value = await getProjects()
  } catch (err) {
    error.value =
      err.response?.data?.detail ||
      'Unable to load projects. Check the backend connection.'
  } finally {
    loading.value = false
  }
}

onMounted(loadDashboard)
</script>

<template>
  <main class="dashboard">
    <header class="page-header">
      <div>
        <h1>Developer Dashboard</h1>
        <p>Manage your projects and development workflows.</p>
      </div>

      <button @click="loadDashboard" :disabled="loading">
        {{ loading ? 'Refreshing...' : 'Refresh' }}
      </button>
    </header>

    <section class="stats-grid">
      <StatCard
        title="Total Projects"
        :value="totalProjects"
        description="Projects registered"
      />

      <StatCard
        title="GitHub Integration"
        value="API-ready"
        description="Repository integration is a separate feature"
      />

      <StatCard
        title="CI/CD"
        value="Not configured"
        description="Automation will be added later"
      />
    </section>
    <section>
      <Validation />
    </section>
   

    <section class="projects-section">
      <h2>Projects</h2>

      <p v-if="loading">Loading projects...</p>
      <p v-else-if="error" class="error">{{ error }}</p>

      <div v-else-if="projects.length" class="projects-grid">
        <ProjectCard
          v-for="project in projects"
          :key="project.id"
          :project="project"
        />
      </div>

      <p v-else>No projects found. Create your first project.</p>
    </section>
  </main>
</template>

<style scoped>
.dashboard {
  max-width: 1200px;
  margin: 0 auto;
  padding: 32px 24px;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  margin-bottom: 28px;
}

.page-header p {
  color: #64748b;
}

.stats-grid,
.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
}

.projects-section {
  margin-top: 36px;
}

.error {
  color: #dc2626;
}

button {
  padding: 10px 16px;
  cursor: pointer;
}

@media (max-width: 600px) {
  .page-header {
    align-items: flex-start;
    flex-direction: column;
  }
}
</style>