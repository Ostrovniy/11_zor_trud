# Главная страница сайта села Зоря Труда — дизайн (мок-данные)

**Дата:** 2026-06-26
**Автор:** Вадим (frontend)
**Статус:** одобрено

## Контекст

Пилотный учебный enterprise-проект сайта села Зоря Труда (Одесская область).
Разделение зон: Юра — backend, Вадим — frontend (папка `frontend/`).
Сейчас `frontend/` — чистый шаблон Vite + Vue 3 + TypeScript; `App.vue` содержит
заглушку «123». Цель этого шага — наполнить **одну главную страницу** мок-данными
и параллельно освоить Vue 3 (с опытом React).

Бэкенда пока нет — все данные статичные/имитированные на фронте.

## Решения (зафиксированы при брейнсторминге)

| Вопрос | Решение |
|--------|---------|
| Объём | Одна главная страница, разбитая на секции |
| Ядро | Ванильный Vue 3 (`<script setup>`, composables). Без vue-router и Pinia на этом этапе |
| UI-библиотека | PrimeVue (тема Aura) + primeicons |
| Стилизация | Компоненты PrimeVue + точечный scoped CSS |
| Язык интерфейса и контента | Русский |
| Обучение | Чистый код без учебных комментариев; отличия React→Vue разбираются в чате |

## Архитектура

Одностраничник: `App.vue` последовательно рендерит секции. Навигация — якорные
ссылки (скролл к секциям), без роутера.

### Структура папок

```
frontend/src/
  components/      AppHeader.vue  AppFooter.vue  NewsCard.vue  StatCard.vue
  sections/        HeroSection.vue  AboutSection.vue  NewsSection.vue
                   GallerySection.vue  MapSection.vue
  composables/     useNews.ts        # аналог кастомного React-хука
  data/            village.ts  news.ts  gallery.ts   # мок-данные
  types/           index.ts          # TS-интерфейсы
  App.vue  main.ts  style.css
```

**Разделение ответственности:**
- `components/` — переиспользуемые «глупые» UI-кусочки (получают данные через `defineProps`).
- `sections/` — крупные блоки главной страницы, каждый отвечает за свою секцию.
- `composables/` — переиспользуемая логика с состоянием.
- `data/` — мок-данные, изолированы, чтобы позже заменить на вызовы API.
- `types/` — общие TS-интерфейсы.

## Секции страницы (сверху вниз)

1. **AppHeader** — название села + якорные ссылки на секции.
2. **HeroSection** — `assets/hero.png`, название «Зоря Труда», слоган, кнопка «Узнать больше».
3. **AboutSection** — краткая история + карточки-факты (`StatCard`): год основания, население, район, область.
4. **NewsSection** — 3–4 карточки последних новостей (`NewsCard`); данные из `useNews()` с имитацией загрузки (skeleton при `isLoading`).
5. **GallerySection** — сетка фото-плейсхолдеров из `data/gallery.ts`.
6. **MapSection** — заглушка под будущий MapLibre: «Интерактивная карта — скоро».
7. **AppFooter** — контакты, копирайт.

## Данные

### Типы (`types/index.ts`)

```ts
export interface VillageFact { label: string; value: string; icon?: string }
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
  date: string        // ISO
  imageUrl?: string
}
export interface GalleryItem {
  id: number
  title: string
  imageUrl: string
}
```

### Мок-источники
- `data/village.ts` — статичный объект `VillageInfo` (история + факты).
- `data/news.ts` — массив `NewsItem[]` (3–4 элемента).
- `data/gallery.ts` — массив `GalleryItem[]` (6–8 плейсхолдеров).

### Composable `useNews()`
Учебный аналог `useState` + `useEffect` + fetch:
- возвращает `{ news: Ref<NewsItem[]>, isLoading: Ref<boolean> }`;
- в `onMounted` имитирует асинхронную загрузку через `setTimeout` (~600 мс),
  затем кладёт данные из `data/news.ts` и снимает `isLoading`.

Это специально показывает реактивность (`ref`), lifecycle (`onMounted`) и паттерн
загрузки, чтобы позже легко заменить `setTimeout` на реальный HTTP-запрос.

## Поток данных

```
data/*.ts  ──>  composable / прямой импорт  ──>  section  ──(props)──>  component
```

- `AboutSection` импортирует `village` напрямую (статика) и раздаёт факты в `StatCard`.
- `NewsSection` вызывает `useNews()`, отдаёт каждый элемент в `NewsCard`.
- `GallerySection` импортирует `gallery` напрямую.

## Обработка крайних случаев

- **Загрузка новостей:** пока `isLoading` — показываем PrimeVue `Skeleton` вместо карточек.
- **Пустые данные:** если массив пуст — короткое сообщение «Пока нет записей».
- **Изображения:** `loading="lazy"` на `<img>`; для плейсхолдеров галереи —
  локальные ассеты или data-URI/placeholder, без внешних запросов.

## Тестирование

Учебный фронтенд на мок-данных; формального TDD на этом шаге не вводим (нет бизнес-логики
с инвариантами). Верификация — ручная:
- `npm run build` (vue-tsc) проходит без ошибок типов;
- `npm run dev` открывается, все 7 секций видны, навигация по якорям работает,
  у новостей виден skeleton → затем карточки.

При появлении реальной логики (фильтры, парсинг markdown и т.п.) — вводим Vitest + TDD.

## Зависимости для установки

- `primevue`
- `@primevue/themes`
- `primeicons`

## Вне рамок (YAGNI на этом шаге)

- vue-router, Pinia — добавим, когда появятся реальные страницы/общий стейт.
- Реальная карта MapLibre — пока заглушка.
- Интеграция с backend, аутентификация, комментарии, CMS — следующие этапы по `TODO.md`.
