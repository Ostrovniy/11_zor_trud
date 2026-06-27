<script setup lang="ts">
import Skeleton from 'primevue/skeleton'
import {useUsers} from '../composables/useUsers'
import {usePosts} from '../composables/usePosts'
import UserCard from '../components/UserCard.vue'
import PostCard from '../components/PostCard.vue'

const {users, isLoading: isLoadingUsers} = useUsers()
const {posts, isLoading: isLoadingPosts} = usePosts()
</script>

<template>
  <section id="users" class="section">
    <h2 class="section__title">Пользователи</h2>

    <!-- v-if/v-else — аналог тернарника в JSX, но как директива -->
    <div v-if="isLoadingUsers" class="users__grid">
      <Skeleton v-for="n in 4" :key="n" height="10rem" border-radius="12px"/>
    </div>

    <div v-else-if="users.length" class="users__grid">
      <UserCard v-for="item in users" :key="item.phone" :item="item"/>
    </div>

    <p v-else class="users__empty">Пока нет юзеров.</p>
  </section>

  <section id="posts" class="section">
    <h2 class="section__title">Публикации</h2>

    <!-- v-if/v-else — аналог тернарника в JSX, но как директива -->
    <div v-if="isLoadingPosts" class="posts__grid">
      <Skeleton v-for="n in 4" :key="n" height="10rem" border-radius="12px"/>
    </div>

    <div v-else-if="posts.length" class="posts__grid">
      <PostCard v-for="item in posts" :key="item.title" :item="item"/>
    </div>

    <p v-else class="posts__empty">Пока нет записей.</p>
  </section>
</template>

<style scoped>
.section__title {
  color: #000;
}
.users__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.25rem;
  max-width: 1000px;
  margin: 0 auto;
}

.users__empty {
  text-align: center;
  color: var(--p-text-muted-color);
}

.posts__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.25rem;
  max-width: 1000px;
  margin: 0 auto;
}

.posts__empty {
  text-align: center;
  color: var(--p-text-muted-color);
}
</style>
