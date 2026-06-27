<script setup lang="ts">
import Button from 'primevue/button'
import heroImage from '../assets/hero.png'
import { village } from '../data/village'
</script>

<template>
  <section id="hero" class="hero" :style="{ backgroundImage: `url(${heroImage})` }">
    <div class="hero__overlay">
      <h1 class="hero__title">{{ village.name }}</h1>
      <p class="hero__subtitle">Цифровой архив, новости и история родного села</p>
      <Button label="Узнать больше" icon="pi pi-arrow-down" as="a" href="#about" />
    </div>
  </section>
</template>

<style scoped>
.hero {
  min-height: 70vh;
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
}
.hero__overlay {
  background: rgba(0, 0, 0, 0.45);
  color: #fff;
  padding: 2.5rem 2rem;
  border-radius: 16px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  max-width: 90%;
}
.hero__title {
  font-size: clamp(2.2rem, 6vw, 3.5rem);
  margin: 0;
}
.hero__subtitle {
  margin: 0;
  font-size: clamp(1rem, 2.5vw, 1.25rem);
  opacity: 0.92;
}
</style>
