<script setup lang="ts">
import type { VillageFact } from '../types'

// defineProps — аналог props в React; типобезопасно через generic.
defineProps<{ fact: VillageFact }>()
</script>

<template>
  <div class="stat-card">
    <i :class="fact.icon" class="stat-card__icon" />
    <div class="stat-card__value">{{ fact.value }}</div>
    <div class="stat-card__label">{{ fact.label }}</div>
  </div>
</template>

<style scoped>
.stat-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.35rem;
  padding: 1.5rem 1rem;
  border: 1px solid var(--p-surface-200);
  border-radius: 12px;
  background: var(--p-surface-0);
  text-align: center;
}
.stat-card__icon {
  font-size: 1.75rem;
  color: var(--p-primary-color);
}
.stat-card__value {
  font-size: 1.5rem;
  font-weight: 700;
}
.stat-card__label {
  color: var(--p-text-muted-color);
  font-size: 0.9rem;
}
</style>
