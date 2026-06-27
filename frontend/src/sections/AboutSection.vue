<script setup lang="ts">
import { village } from '../data/village'
import StatCard from '../components/StatCard.vue'
</script>

<template>
  <section id="about" class="about section">
    <h2 class="section__title">О селе</h2>
    <p class="about__history">{{ village.history }}</p>
    <div class="about__facts">
      <StatCard v-for="fact in village.facts" :key="fact.label" :fact="fact" />
    </div>
  </section>
</template>

<style scoped>
.about__history {
  max-width: 760px;
  margin: 0 auto 2rem;
  text-align: center;
  line-height: 1.6;
  color: var(--p-text-color);
}
.about__facts {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 1rem;
  max-width: 900px;
  margin: 0 auto;
}
</style>
