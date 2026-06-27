# Главная страница (мок-данные) — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Наполнить одну главную страницу сайта села Зоря Труда мок-данными на Vue 3 + PrimeVue, попутно показав ключевые механики Vue.

**Architecture:** Одностраничник без роутера: `App.vue` рендерит 7 секций сверху вниз. Данные — статичные мок-модули в `data/`; новости проходят через composable `useNews()` с имитацией асинхронной загрузки. UI — PrimeVue (тема Aura) + точечный scoped CSS.

**Tech Stack:** Vue 3 (`<script setup lang="ts">`), TypeScript, Vite, PrimeVue 4 + `@primeuix/themes` + primeicons.

> **Верификация:** по одобренной спеке вместо TDD — ручная проверка: `npm run build` (vue-tsc без ошибок типов) + `npm run dev` (визуальный осмотр). Vitest введём, когда появится реальная логика.

> **Рабочая директория для всех команд:** `frontend/`. Все пути ниже — относительно `frontend/`.

---

## File Structure

| Файл | Ответственность |
|------|-----------------|
| `src/types/index.ts` | Общие TS-интерфейсы (`VillageInfo`, `NewsItem`, `GalleryItem`, ...) |
| `src/data/village.ts` | Статичные данные о селе (история + факты) |
| `src/data/news.ts` | Мок-массив новостей |
| `src/data/gallery.ts` | Мок-массив элементов галереи |
| `src/composables/useNews.ts` | Загрузка новостей с состоянием `isLoading` (имитация async) |
| `src/components/StatCard.vue` | Карточка одного факта о селе |
| `src/components/NewsCard.vue` | Карточка одной новости |
| `src/components/AppHeader.vue` | Шапка с навигацией по якорям |
| `src/components/AppFooter.vue` | Подвал |
| `src/sections/HeroSection.vue` | Hero-блок |
| `src/sections/AboutSection.vue` | О селе + факты |
| `src/sections/NewsSection.vue` | Новости (использует `useNews`) |
| `src/sections/GallerySection.vue` | Галерея |
| `src/sections/MapSection.vue` | Заглушка карты |
| `src/main.ts` | Подключение PrimeVue (Modify) |
| `src/App.vue` | Сборка страницы (Modify) |
| `src/style.css` | Глобальные токены/сброс (Modify) |

> **Уточнение к спеке:** `GalleryItem.imageUrl` делаем **опциональным** — для мока рисуем CSS-градиентные плитки с заголовком (полностью офлайн, без внешних запросов). Реальные `imageUrl` подставим позже.

---

## Task 1: Установка и подключение PrimeVue

**Files:**
- Modify: `src/main.ts`

- [ ] **Step 1: Установить зависимости**

В директории `frontend/`:

```bash
npm install primevue @primeuix/themes primeicons
```

Expected: пакеты добавлены в `package.json` → `dependencies`.

- [ ] **Step 2: Подключить PrimeVue в `src/main.ts`**

Заменить содержимое `src/main.ts` целиком на:

```ts
import { createApp } from 'vue'
import PrimeVue from 'primevue/config'
import Aura from '@primeuix/themes/aura'
import 'primeicons/primeicons.css'
import './style.css'
import App from './App.vue'

createApp(App)
  .use(PrimeVue, {
    theme: {
      preset: Aura,
      options: {
        prefix: 'p',
        darkModeSelector: 'system',
        cssLayer: false,
      },
    },
  })
  .mount('#app')
```

- [ ] **Step 3: Проверить, что dev-сервер стартует**

Run: `npm run dev`
Expected: Vite поднимается без ошибок, страница открывается (пока со старой заглушкой «123»). Остановить сервер (Ctrl+C).

- [ ] **Step 4: Commit**

```bash
git add frontend/package.json frontend/package-lock.json frontend/src/main.ts
git commit -m "feat(frontend): add and configure PrimeVue with Aura theme"
```

---

## Task 2: TS-типы

**Files:**
- Create: `src/types/index.ts`

- [ ] **Step 1: Создать `src/types/index.ts`**

```ts
export interface VillageFact {
  label: string
  value: string
  icon: string // primeicons class, напр. 'pi pi-users'
}

export interface VillageInfo {
  name: string
  region: string
  history: string
  facts: VillageFact[]
}

export interface NewsItem {
  id: number
  title: string
  excerpt: string
  date: string // ISO, напр. '2026-06-20'
}

export interface GalleryItem {
  id: number
  title: string
  imageUrl?: string
}
```

- [ ] **Step 2: Проверить типы**

Run: `npm run build`
Expected: vue-tsc проходит без ошибок (файл пока ни на что не влияет, но не должен ломать сборку).

- [ ] **Step 3: Commit**

```bash
git add frontend/src/types/index.ts
git commit -m "feat(frontend): add shared TypeScript types"
```

---

## Task 3: Мок-данные

**Files:**
- Create: `src/data/village.ts`
- Create: `src/data/news.ts`
- Create: `src/data/gallery.ts`

- [ ] **Step 1: Создать `src/data/village.ts`**

```ts
import type { VillageInfo } from '../types'

export const village: VillageInfo = {
  name: 'Зоря Труда',
  region: 'Раздельнянский район, Одесская область',
  history:
    'Зоря Труда — село с богатой историей, выросшее вокруг сельскохозяйственной ' +
    'общины. На протяжении десятилетий жители бережно хранят традиции, культуру ' +
    'и память о родном крае. Сегодня село объединяет несколько поколений семей, ' +
    'которые продолжают развивать его и передавать историю дальше.',
  facts: [
    { label: 'Год основания', value: '1924', icon: 'pi pi-calendar' },
    { label: 'Население', value: '≈ 1 200', icon: 'pi pi-users' },
    { label: 'Район', value: 'Раздельнянский', icon: 'pi pi-map' },
    { label: 'Область', value: 'Одесская', icon: 'pi pi-map-marker' },
  ],
}
```

- [ ] **Step 2: Создать `src/data/news.ts`**

```ts
import type { NewsItem } from '../types'

export const news: NewsItem[] = [
  {
    id: 1,
    title: 'Открытие обновлённого сельского клуба',
    excerpt:
      'После ремонта снова работает культурный центр села — с залом для ' +
      'мероприятий и кружками для детей.',
    date: '2026-06-20',
  },
  {
    id: 2,
    title: 'Субботник: высадили 50 деревьев',
    excerpt:
      'Жители вместе благоустроили центральную улицу и высадили молодую ' +
      'аллею вдоль дороги к школе.',
    date: '2026-06-12',
  },
  {
    id: 3,
    title: 'Сбор материалов для цифрового архива',
    excerpt:
      'Запущен сбор старых фотографий и воспоминаний для будущей ' +
      'исторической летописи села.',
    date: '2026-06-01',
  },
  {
    id: 4,
    title: 'Ярмарка местных хозяйств',
    excerpt:
      'В выходные прошла ярмарка с продукцией местных фермеров и ' +
      'мастеров — мёд, сыры, овощи и ремёсла.',
    date: '2026-05-25',
  },
]
```

- [ ] **Step 3: Создать `src/data/gallery.ts`**

```ts
import type { GalleryItem } from '../types'

export const gallery: GalleryItem[] = [
  { id: 1, title: 'Центральная улица' },
  { id: 2, title: 'Сельский клуб' },
  { id: 3, title: 'Поля на рассвете' },
  { id: 4, title: 'Школа' },
  { id: 5, title: 'Пруд' },
  { id: 6, title: 'Праздник урожая' },
]
```

- [ ] **Step 4: Проверить сборку**

Run: `npm run build`
Expected: vue-tsc проходит без ошибок.

- [ ] **Step 5: Commit**

```bash
git add frontend/src/data
git commit -m "feat(frontend): add mock data for village, news, gallery"
```

---

## Task 4: Composable useNews

**Files:**
- Create: `src/composables/useNews.ts`

- [ ] **Step 1: Создать `src/composables/useNews.ts`**

```ts
import { ref, onMounted } from 'vue'
import type { NewsItem } from '../types'
import { news as mockNews } from '../data/news'

// Учебный аналог: useState (ref) + useEffect (onMounted) + fetch (setTimeout).
// Позже setTimeout заменим на реальный HTTP-запрос к backend Юры.
export function useNews() {
  const news = ref<NewsItem[]>([])
  const isLoading = ref(true)

  onMounted(() => {
    setTimeout(() => {
      news.value = mockNews
      isLoading.value = false
    }, 600)
  })

  return { news, isLoading }
}
```

- [ ] **Step 2: Проверить сборку**

Run: `npm run build`
Expected: vue-tsc проходит без ошибок.

- [ ] **Step 3: Commit**

```bash
git add frontend/src/composables/useNews.ts
git commit -m "feat(frontend): add useNews composable with simulated loading"
```

---

## Task 5: Презентационные компоненты StatCard и NewsCard

**Files:**
- Create: `src/components/StatCard.vue`
- Create: `src/components/NewsCard.vue`

- [ ] **Step 1: Создать `src/components/StatCard.vue`**

```vue
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
```

- [ ] **Step 2: Создать `src/components/NewsCard.vue`**

```vue
<script setup lang="ts">
import { computed } from 'vue'
import Card from 'primevue/card'
import Tag from 'primevue/tag'
import type { NewsItem } from '../types'

const props = defineProps<{ item: NewsItem }>()

// computed — аналог useMemo: пересчитывается при изменении item.date.
const formattedDate = computed(() =>
  new Date(props.item.date).toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
  }),
)
</script>

<template>
  <Card class="news-card">
    <template #title>{{ item.title }}</template>
    <template #subtitle>
      <Tag :value="formattedDate" severity="secondary" />
    </template>
    <template #content>
      <p class="news-card__excerpt">{{ item.excerpt }}</p>
    </template>
  </Card>
</template>

<style scoped>
.news-card {
  height: 100%;
}
.news-card__excerpt {
  margin: 0;
  color: var(--p-text-muted-color);
  line-height: 1.5;
}
</style>
```

- [ ] **Step 3: Проверить сборку**

Run: `npm run build`
Expected: vue-tsc проходит без ошибок.

- [ ] **Step 4: Commit**

```bash
git add frontend/src/components/StatCard.vue frontend/src/components/NewsCard.vue
git commit -m "feat(frontend): add StatCard and NewsCard components"
```

---

## Task 6: AppHeader и AppFooter

**Files:**
- Create: `src/components/AppHeader.vue`
- Create: `src/components/AppFooter.vue`

- [ ] **Step 1: Создать `src/components/AppHeader.vue`**

```vue
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
```

- [ ] **Step 2: Создать `src/components/AppFooter.vue`**

```vue
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
```

- [ ] **Step 3: Проверить сборку**

Run: `npm run build`
Expected: vue-tsc проходит без ошибок.

- [ ] **Step 4: Commit**

```bash
git add frontend/src/components/AppHeader.vue frontend/src/components/AppFooter.vue
git commit -m "feat(frontend): add AppHeader and AppFooter"
```

---

## Task 7: HeroSection и AboutSection

**Files:**
- Create: `src/sections/HeroSection.vue`
- Create: `src/sections/AboutSection.vue`

- [ ] **Step 1: Создать `src/sections/HeroSection.vue`**

```vue
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
```

- [ ] **Step 2: Создать `src/sections/AboutSection.vue`**

```vue
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
```

- [ ] **Step 3: Проверить сборку**

Run: `npm run build`
Expected: vue-tsc проходит без ошибок.

- [ ] **Step 4: Commit**

```bash
git add frontend/src/sections/HeroSection.vue frontend/src/sections/AboutSection.vue
git commit -m "feat(frontend): add Hero and About sections"
```

---

## Task 8: NewsSection, GallerySection, MapSection

**Files:**
- Create: `src/sections/NewsSection.vue`
- Create: `src/sections/GallerySection.vue`
- Create: `src/sections/MapSection.vue`

- [ ] **Step 1: Создать `src/sections/NewsSection.vue`**

```vue
<script setup lang="ts">
import Skeleton from 'primevue/skeleton'
import { useNews } from '../composables/useNews'
import NewsCard from '../components/NewsCard.vue'

const { news, isLoading } = useNews()
</script>

<template>
  <section id="news" class="section">
    <h2 class="section__title">Новости</h2>

    <!-- v-if/v-else — аналог тернарника в JSX, но как директива -->
    <div v-if="isLoading" class="news__grid">
      <Skeleton v-for="n in 4" :key="n" height="10rem" border-radius="12px" />
    </div>

    <div v-else-if="news.length" class="news__grid">
      <NewsCard v-for="item in news" :key="item.id" :item="item" />
    </div>

    <p v-else class="news__empty">Пока нет записей.</p>
  </section>
</template>

<style scoped>
.news__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.25rem;
  max-width: 1000px;
  margin: 0 auto;
}
.news__empty {
  text-align: center;
  color: var(--p-text-muted-color);
}
</style>
```

- [ ] **Step 2: Создать `src/sections/GallerySection.vue`**

```vue
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
```

- [ ] **Step 3: Создать `src/sections/MapSection.vue`**

```vue
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
```

- [ ] **Step 4: Проверить сборку**

Run: `npm run build`
Expected: vue-tsc проходит без ошибок.

- [ ] **Step 5: Commit**

```bash
git add frontend/src/sections/NewsSection.vue frontend/src/sections/GallerySection.vue frontend/src/sections/MapSection.vue
git commit -m "feat(frontend): add News, Gallery and Map sections"
```

---

## Task 9: Сборка App.vue и глобальные стили

**Files:**
- Modify: `src/App.vue`
- Modify: `src/style.css`

- [ ] **Step 1: Заменить `src/App.vue` целиком**

```vue
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
```

- [ ] **Step 2: Заменить `src/style.css` целиком**

```css
:root {
  font-family: system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  color-scheme: light;
}

* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  background: var(--p-surface-50, #fafafa);
  color: var(--p-text-color, #1f1f1f);
}

.section {
  max-width: 1100px;
  margin: 0 auto;
  padding: 3.5rem 1.25rem;
}

.section__title {
  text-align: center;
  font-size: clamp(1.6rem, 4vw, 2.2rem);
  margin: 0 0 1.5rem;
}
```

- [ ] **Step 3: Финальная проверка сборки**

Run: `npm run build`
Expected: vue-tsc + vite build проходят без ошибок.

- [ ] **Step 4: Визуальная проверка в браузере**

Run: `npm run dev`
Expected:
- Видны все 7 блоков: шапка → hero (с фоновым `hero.png`) → О селе (4 карточки-факта) → Новости → Галерея (6 градиентных плиток) → Карта (заглушка) → подвал.
- Клик по ссылкам в шапке плавно скроллит к секциям.
- В блоке «Новости» сначала ~0.6с видны skeleton-плейсхолдеры, затем появляются 4 карточки с датами на русском.

> Опционально: проверить через Playwright MCP (скриншот), как требует CLAUDE.md для фронтенда.

- [ ] **Step 5: Commit**

```bash
git add frontend/src/App.vue frontend/src/style.css
git commit -m "feat(frontend): assemble home page and global styles"
```

---

## Очистка (опционально)

- `src/components/HelloWorld.vue`, `src/assets/vue.svg`, `src/assets/vite.svg` от стартового шаблона больше не используются. Удалить можно отдельным коммитом `chore(frontend): remove Vite starter leftovers` — но не обязательно на этом этапе.

---

## Self-Review (выполнено при написании плана)

- **Покрытие спеки:** все 7 секций, типы, 3 мок-источника, `useNews` с загрузкой, skeleton/empty-состояния, lazy-загрузка картинок, заглушка карты, установка PrimeVue — каждый пункт имеет задачу. ✔
- **Плейсхолдеры:** код приведён полностью в каждом шаге, «TODO/TBD» нет. ✔
- **Согласованность типов:** `VillageInfo/VillageFact/NewsItem/GalleryItem` из Task 2 используются единообразно в Task 3–8; `useNews()` возвращает `{ news, isLoading }`, как потребляется в NewsSection. ✔
- **Отклонение от спеки:** `GalleryItem.imageUrl` сделан опциональным (градиентные плитки) — зафиксировано выше. ✔
