import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
})

export async function validateProject() {
  const response = await api.post('/automation/validate')
  return response.data
}