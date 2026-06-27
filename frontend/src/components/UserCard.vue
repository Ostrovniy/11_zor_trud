<script setup lang="ts">
import { computed } from 'vue'
import Avatar from 'primevue/avatar'
import type { User } from '../types'

const props = defineProps<{ item: User }>()

// Первая буква имени для аватара.
const initial = computed(() => props.item.name.charAt(0).toUpperCase())
</script>

<template>
  <div class="user-card">
    <Avatar :label="initial" shape="circle" size="large" class="user-card__avatar" />
    <div class="user-card__info">
      <div class="user-card__name">{{ item.name }}</div>
      <a :href="`tel:${item.phone}`" class="user-card__phone">
        <i class="pi pi-phone" />
        <span>{{ item.phone }}</span>
      </a>
    </div>
  </div>
</template>

<style scoped>
.user-card {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 1.25rem;
  border: 1px solid var(--p-surface-300);
  border-radius: 12px;
  background: var(--p-surface-0);
  box-shadow: 0 1px 3px rgb(0 0 0 / 0.1);
  transition: box-shadow 0.2s, border-color 0.2s;
}
.user-card:hover {
  border-color: var(--p-primary-color);
  box-shadow: 0 4px 12px rgb(0 0 0 / 0.06);
}
.user-card__avatar {
  flex-shrink: 0;
  background: var(--p-primary-color);
  color: var(--p-primary-contrast-color);
  font-weight: 700;
}
.user-card__info {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
  min-width: 0;
}
.user-card__name {
  font-weight: 600;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.user-card__phone {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  color: var(--p-text-muted-color);
  text-decoration: none;
  font-size: 0.9rem;
}
.user-card__phone:hover {
  color: var(--p-primary-color);
}
</style>
