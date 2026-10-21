
import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: 60000,
})

export async function sendMessage(message) {
  const response = await api.post('/ai/chat', {
    message,
  })

  return response.data.answer
}
