<script setup lang="ts">
import Card from 'primevue/card'
import type { Post } from '../types'

defineProps<{ item: Post }>()
</script>

<template>
  <Card class="post-card">
    <template #title>
      <span class="post-card__title">{{ item.title }}</span>
    </template>
    <template #content>
      <p class="post-card__content">{{ item.content }}</p>
    </template>
  </Card>
</template>

<style scoped>
.post-card {
  height: 100%;
  border: 1px solid var(--p-surface-300);
  box-shadow: 0 1px 3px rgb(0 0 0 / 0.1);
  transition: box-shadow 0.2s, border-color 0.2s;
}
.post-card:hover {
  border-color: var(--p-primary-color);
  box-shadow: 0 4px 12px rgb(0 0 0 / 0.06);
}
.post-card__title {
  font-size: 1.1rem;
}
.post-card__content {
  margin: 0;
  color: var(--p-text-muted-color);
  line-height: 1.6;
}
</style>
