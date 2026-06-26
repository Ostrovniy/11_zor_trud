<script setup lang="ts">
import Skeleton from 'primevue/skeleton'
import { useNews } from '../composables/useNews'
import NewsCard from '../components/NewsCard.vue'

const { news, isLoading } = useNews()
</script>

<template>
  <section id="news" class="section">
    <h2 class="section__title">Новости</h2>

    <!-- v-if/v-else — аналог тернарника в JSX, но как директива -->
    <div v-if="isLoading" class="news__grid">
      <Skeleton v-for="n in 4" :key="n" height="10rem" border-radius="12px" />
    </div>

    <div v-else-if="news.length" class="news__grid">
      <NewsCard v-for="item in news" :key="item.id" :item="item" />
    </div>

    <p v-else class="news__empty">Пока нет записей.</p>
  </section>
</template>

<style scoped>
.news__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.25rem;
  max-width: 1000px;
  margin: 0 auto;
}
.news__empty {
  text-align: center;
  color: var(--p-text-muted-color);
}
</style>
