import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ReviewSearchView from '@/views/ReviewSearchView.vue'
import MovieListView from '../views/MovieListView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'  // MovieDetailView를 import

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/review-search',
      name: 'ReviewSearch',
      component: ReviewSearchView
    },
    {
      path: '/movies',
      name: 'movies',
      component: MovieListView
    },
    {
      path: '/movie/:movieId',
      name: 'movieDetail',
      component: MovieDetailView
    }
  ]
})

export default router
