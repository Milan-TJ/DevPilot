import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

export async function getProjects() {
  const response = await api.get('/projects/all')
  return response.data
}

export async function createProject(project) {
  const response = await api.post('/projects/', project)
  return response.data
}