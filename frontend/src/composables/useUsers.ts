import { ref, onMounted } from 'vue'
import type { User } from '../types'

const API_URL = import.meta.env.VITE_API_URL as string

export function useUsers() {
  const users = ref<User[]>([])
  const isLoading = ref(true)
  const error = ref<string | null>(null)

  // onMounted может быть async — это аналог useEffect с async-функцией внутри.
  onMounted(async () => {
    try {
      const response = await fetch(`${API_URL}/users`)
      if (!response.ok) throw new Error(`HTTP ${response.status}`)
      users.value = await response.json()
    } catch (e) {
      error.value = e instanceof Error ? e.message : 'Не удалось загрузить пользователей'
    } finally {
      isLoading.value = false
    }
  })

  return { users, isLoading, error }
}
