<script setup lang="ts">
</script>

<template>
  <section id="map" class="section">
    <h2 class="section__title">Карта</h2>
    <div class="map__placeholder">
      <i class="pi pi-map" />
      <p>Интерактивная карта села — скоро</p>
    </div>
  </section>
</template>

<style scoped>
.map__placeholder {
  max-width: 1000px;
  margin: 0 auto;
  min-height: 280px;
  border: 2px dashed var(--p-surface-300);
  border-radius: 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  color: var(--p-text-muted-color);
  background: var(--p-surface-50);
}
.map__placeholder i {
  font-size: 2.5rem;
}
.map__placeholder p {
  margin: 0;
}
</style>
