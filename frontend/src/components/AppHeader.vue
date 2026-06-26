<script setup lang="ts">
// Якорная навигация по секциям одностраничника.
const links = [
  { label: 'О селе', href: '#about' },
  { label: 'Новости', href: '#news' },
  { label: 'Галерея', href: '#gallery' },
  { label: 'Карта', href: '#map' },
]
</script>

<template>
  <header class="app-header">
    <div class="app-header__inner">
      <a href="#hero" class="app-header__brand">Зоря Труда</a>
      <nav class="app-header__nav">
        <a v-for="link in links" :key="link.href" :href="link.href" class="app-header__link">
          {{ link.label }}
        </a>
      </nav>
    </div>
  </header>
</template>

<style scoped>
.app-header {
  position: sticky;
  top: 0;
  z-index: 10;
  background: var(--p-surface-0);
  border-bottom: 1px solid var(--p-surface-200);
}
.app-header__inner {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0.85rem 1.25rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}
.app-header__brand {
  font-weight: 800;
  font-size: 1.15rem;
  color: var(--p-primary-color);
  text-decoration: none;
}
.app-header__nav {
  display: flex;
  gap: 1.25rem;
  flex-wrap: wrap;
}
.app-header__link {
  color: var(--p-text-color);
  text-decoration: none;
  font-size: 0.95rem;
}
.app-header__link:hover {
  color: var(--p-primary-color);
}
</style>
