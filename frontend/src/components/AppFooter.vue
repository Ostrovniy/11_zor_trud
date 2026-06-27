<script setup lang="ts">
const year = new Date().getFullYear()
</script>

<template>
  <footer class="app-footer">
    <div class="app-footer__inner">
      <div>
        <div class="app-footer__brand">Зоря Труда</div>
        <div class="app-footer__muted">Раздельнянский район, Одесская область</div>
      </div>
      <div class="app-footer__muted">© {{ year }} · Учебный проект</div>
    </div>
  </footer>
</template>

<style scoped>
.app-footer {
  background: var(--p-surface-100);
  border-top: 1px solid var(--p-surface-200);
  margin-top: 3rem;
}
.app-footer__inner {
  max-width: 1100px;
  margin: 0 auto;
  padding: 1.5rem 1.25rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}
.app-footer__brand {
  font-weight: 700;
}
.app-footer__muted {
  color: var(--p-text-muted-color);
  font-size: 0.9rem;
}
</style>
