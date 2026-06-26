<script setup lang="ts">
import AppHeader from './components/AppHeader.vue'
import AppFooter from './components/AppFooter.vue'
import HeroSection from './sections/HeroSection.vue'
import AboutSection from './sections/AboutSection.vue'
import NewsSection from './sections/NewsSection.vue'
import GallerySection from './sections/GallerySection.vue'
import MapSection from './sections/MapSection.vue'
</script>

<template>
  <AppHeader />
  <main>
    <HeroSection />
    <AboutSection />
    <NewsSection />
    <GallerySection />
    <MapSection />
  </main>
  <AppFooter />
</template>
