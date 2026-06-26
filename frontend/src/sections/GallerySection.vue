<script setup lang="ts">
import { gallery } from '../data/gallery'

// Детерминированный градиент по id — чтобы плитки выглядели по-разному
// без внешних изображений.
function gradient(id: number): string {
  const hue = (id * 47) % 360
  return `linear-gradient(135deg, hsl(${hue} 55% 45%), hsl(${(hue + 40) % 360} 55% 35%))`
}
</script>

<template>
  <section id="gallery" class="section">
    <h2 class="section__title">Галерея</h2>
    <div class="gallery__grid">
      <figure v-for="item in gallery" :key="item.id" class="gallery__item">
        <img
          v-if="item.imageUrl"
          :src="item.imageUrl"
          :alt="item.title"
          loading="lazy"
          class="gallery__img"
        />
        <div v-else class="gallery__placeholder" :style="{ background: gradient(item.id) }">
          <i class="pi pi-image" />
        </div>
        <figcaption class="gallery__caption">{{ item.title }}</figcaption>
      </figure>
    </div>
  </section>
</template>

<style scoped>
.gallery__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  max-width: 1000px;
  margin: 0 auto;
}
.gallery__item {
  margin: 0;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid var(--p-surface-200);
}
.gallery__img,
.gallery__placeholder {
  width: 100%;
  height: 160px;
  object-fit: cover;
  display: flex;
  align-items: center;
  justify-content: center;
}
.gallery__placeholder {
  color: rgba(255, 255, 255, 0.85);
  font-size: 2rem;
}
.gallery__caption {
  padding: 0.6rem 0.8rem;
  font-size: 0.9rem;
  background: var(--p-surface-0);
}
</style>
