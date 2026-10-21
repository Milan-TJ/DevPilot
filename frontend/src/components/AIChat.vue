
<script setup>
import { ref, nextTick } from 'vue'
import { sendMessage } from '@/services/aiService'

const message = ref('')
const messages = ref([])
const loading = ref(false)
const error = ref('')
const chatContainer = ref(null)

async function scrollToBottom() {
  await nextTick()

  if (chatContainer.value) {
    chatContainer.value.scrollTop =
      chatContainer.value.scrollHeight
  }
}

async function askAssistant() {
  const userMessage = message.value.trim()

  if (!userMessage || loading.value) return

  // Add the user's message to the conversation.
  messages.value.push({
    role: 'user',
    content: userMessage,
  })

  message.value = ''
  loading.value = true
  error.value = ''

  await scrollToBottom()

  try {
    // Use your existing API service.
    const answer = await sendMessage(userMessage)

    messages.value.push({
      role: 'assistant',
      content: answer,
    })
  } catch (err) {
    error.value =
      err.response?.data?.detail ||
      'Unable to contact the AI assistant. Please try again.'
  } finally {
    loading.value = false
    await scrollToBottom()
  }
}

function startNewChat() {
  if (loading.value) return

  messages.value = []
  message.value = ''
  error.value = ''
}
</script>

<template>
  <section class="h-dvh flex flex-col bg-slate-50 text-gray-900">

    <!-- Header -->
    <header
      class="h-16 shrink-0 bg-white border-b border-gray-200
             flex items-center justify-between px-4 sm:px-8"
    >
      <div class="flex items-center gap-3">
        <div
          class="w-10 h-10 rounded-xl bg-indigo-600 text-white
                 flex items-center justify-center font-bold"
        >
          AI
        </div>

        <div>
          <h1 class="text-lg font-bold">DevPilot AI</h1>
          <p class="text-xs text-gray-500">
            Your development assistant
          </p>
        </div>
      </div>

      <button
        type="button"
        @click="startNewChat"
        :disabled="loading"
        class="rounded-lg px-3 py-2 text-sm font-medium
               text-indigo-600 hover:bg-indigo-50
               disabled:opacity-50"
      >
        + New chat
      </button>
    </header>

    <!-- Messages -->
    <main
      ref="chatContainer"
      class="flex-1 overflow-y-auto px-4 sm:px-6 py-6"
    >
      <div class="max-w-3xl mx-auto">

        <!-- Welcome screen -->
        <div
          v-if="messages.length === 0"
          class="min-h-[50vh] flex flex-col items-center
                 justify-center text-center"
        >
          <div
            class="w-16 h-16 rounded-2xl bg-indigo-100
                   text-indigo-700 flex items-center
                   justify-center text-2xl font-bold mb-5"
          >
            AI
          </div>

          <h2 class="text-2xl sm:text-3xl font-bold mb-3">
            How can I help you today?
          </h2>

          <p class="text-sm text-gray-500 max-w-md">
            Ask questions about Python, FastAPI, databases,
            APIs, or your development projects.
          </p>

          <div class="grid sm:grid-cols-2 gap-3 mt-8 w-full">
            <button
              v-for="suggestion in [
                'Explain FastAPI dependency injection',
                'Help me debug a Python error',
                'Design a PostgreSQL database schema',
                'How does JWT authentication work?',
              ]"
              :key="suggestion"
              type="button"
              @click="message = suggestion"
              class="rounded-xl border border-gray-200 bg-white
                     p-4 text-left text-sm text-gray-700
                     hover:border-indigo-400 hover:bg-indigo-50
                     transition"
            >
              {{ suggestion }}
            </button>
          </div>
        </div>

        <!-- Conversation bubbles -->
        <template v-else>
          <div
            v-for="(item, index) in messages"
            :key="index"
            class="flex gap-3 mb-6"
            :class="
              item.role === 'user'
                ? 'justify-end'
                : 'justify-start'
            "
          >
            <!-- AI avatar -->
            <div
              v-if="item.role === 'assistant'"
              class="w-9 h-9 shrink-0 rounded-xl bg-indigo-600
                     text-white flex items-center justify-center
                     text-sm font-bold"
            >
              AI
            </div>

            <!-- Message -->
            <div
              class="max-w-[85%] sm:max-w-[75%] rounded-2xl
                     px-4 py-3 shadow-sm"
              :class="
                item.role === 'user'
                  ? 'bg-indigo-600 text-white rounded-br-md'
                  : 'bg-white border border-gray-200 text-gray-800 rounded-bl-md'"
            >
              <p class="text-xs font-semibold mb-2 opacity-75">
                {{ item.role === 'user' ? 'You' : 'DevPilot AI' }}
              </p>

              <p
                class="text-sm leading-6 whitespace-pre-wrap
                       break-words"
              >{{ item.content }}</p>
            </div>

            <!-- User avatar -->
            <div
              v-if="item.role === 'user'"
              class="w-9 h-9 shrink-0 rounded-xl bg-gray-200
                     text-gray-700 flex items-center
                     justify-center text-sm font-bold"
            >
              U
            </div>
          </div>

          <!-- Loading indicator -->
          <div
            v-if="loading"
            class="flex items-center gap-3 mb-6"
            role="status"
            aria-live="polite"
          >
            <div
              class="w-9 h-9 shrink-0 rounded-xl bg-indigo-600
                     text-white flex items-center justify-center
                     text-sm font-bold"
            >
              AI
            </div>

            <div
              class="bg-white border border-gray-200 rounded-xl
                     px-4 py-3 text-sm text-gray-500"
            >
              Thinking...
            </div>
          </div>
        </template>

        <!-- Error -->
        <div
          v-if="error"
          class="mb-4 rounded-xl border border-red-200
                 bg-red-50 p-4 text-sm text-red-700"
          role="alert"
        >
          {{ error }}
        </div>
      </div>
    </main>

    <!-- Input area -->
    <footer class="shrink-0 border-t border-gray-200 bg-white
                   px-4 py-4 sm:px-6">
      <form
        @submit.prevent="askAssistant"
        class="max-w-3xl mx-auto"
      >
        <div
          class="flex items-end gap-3 rounded-2xl border
                 border-gray-300 bg-white p-3
                 focus-within:border-indigo-500
                 focus-within:ring-2
                 focus-within:ring-indigo-100"
        >
          <textarea
            v-model="message"
            rows="1"
            maxlength="2000"
            placeholder="Message DevPilot AI..."
            aria-label="Message DevPilot AI"
            @keydown.enter.exact.prevent="askAssistant"
            class="flex-1 min-w-0 resize-none outline-none
                   bg-transparent text-sm leading-6
                   min-h-10 max-h-32 py-2"
          />

          <button
            type="submit"
            :disabled="loading || !message.trim()"
            class="shrink-0 rounded-xl bg-indigo-600
                   px-4 py-3 text-sm font-semibold text-white
                   hover:bg-indigo-700
                   disabled:opacity-40
                   disabled:cursor-not-allowed transition"
          >
            {{ loading ? '...' : 'Send ↑' }}
          </button>
        </div>

        <p class="text-center text-xs text-gray-400 mt-3">
          AI-generated responses may contain errors.
        </p>
      </form>
    </footer>

  </section>
</template>
