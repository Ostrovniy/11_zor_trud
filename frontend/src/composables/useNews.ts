import { ref, onMounted } from 'vue'
import type { NewsItem } from '../types'
import { news as mockNews } from '../data/news'

// Учебный аналог: useState (ref) + useEffect (onMounted) + fetch (setTimeout).
// Позже setTimeout заменим на реальный HTTP-запрос к backend Юры.
export function useNews() {
  const news = ref<NewsItem[]>([])
  const isLoading = ref(true)

  onMounted(() => {
    setTimeout(() => {
      news.value = mockNews
      isLoading.value = false
    }, 600)
  })

  return { news, isLoading }
}
