<script setup lang="ts">
import { computed } from 'vue'
import Card from 'primevue/card'
import Tag from 'primevue/tag'
import type { NewsItem } from '../types'

const props = defineProps<{ item: NewsItem }>()

// computed — аналог useMemo: пересчитывается при изменении item.date.
const formattedDate = computed(() =>
  new Date(props.item.date).toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
  }),
)
</script>

<template>
  <Card class="news-card">
    <template #title>{{ item.title }}</template>
    <template #subtitle>
      <Tag :value="formattedDate" severity="secondary" />
    </template>
    <template #content>
      <p class="news-card__excerpt">{{ item.excerpt }}</p>
    </template>
  </Card>
</template>

<style scoped>
.news-card {
  height: 100%;
}
.news-card__excerpt {
  margin: 0;
  color: var(--p-text-muted-color);
  line-height: 1.5;
}
</style>
