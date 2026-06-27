import { ref, onMounted } from 'vue'
import type { Post } from '../types'

const API_URL = import.meta.env.VITE_API_URL as string

export function usePosts() {
    const posts = ref<Post[]>([])
    const isLoading = ref(true)
    const error = ref<string | null>(null)

    // onMounted может быть async — это аналог useEffect с async-функцией внутри.
    onMounted(async () => {
        try {
            const response = await fetch(`${API_URL}/posts`)
            if (!response.ok) throw new Error(`HTTP ${response.status}`)
            posts.value = await response.json()
        } catch (e) {
            error.value = e instanceof Error ? e.message : 'Не удалось загрузить публикации'
        } finally {
            isLoading.value = false
        }
    })

    return { posts, isLoading, error }
}
