<template>
  <h1>Movies</h1>
  <div class="card-container">
    <div @click="goDetail(movie)" class="movie-card" v-for="movie in movies" :key="movie.id">
      <img :src="makeImageUrl(movie.poster_path)" alt="Movie Poster" />
      <h3>{{ movie.title }}</h3>
      <p>{{ movie.overview }}</p>
    </div>
  </div>
</template>

  
  <!-- <template>
    <h1>Movies</h1>
    <div class="card-container">
      <RouterLink v-for="movie in movies" :key="movie.id" :to="{ name: 'MovieDetail', params: { id: movie.id }}">
        <div class="movie-card">
          <img :src="makeImageUrl(movie.poster_path)" alt="Movie Poster" />
          <h3>{{ movie.title }}</h3>
          <p>{{ movie.overview }}</p>
        </div>
      </RouterLink>
    </div>
  </template> -->
<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const movies = ref([])
const makeImageUrl = (path) => `https://image.tmdb.org/t/p/w500${path}`
const router = useRouter()

const goDetail = (movie) => {
  router.push({ name: 'movieDetail', params: { movieId: movie.id } })
}

onMounted(() => {
  const options = {
    method: 'GET',
    url: 'https://api.themoviedb.org/3/movie/top_rated',
    params: { language: 'en-US', page: '1' },
    headers: {
      accept: 'application/json',
      Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1Yzk1MjAyNzQ2Njg1Y2Q1NDUwNTM4ZjdhYTcxOGY3NiIsInN1YiI6IjY1M2Y1MDhhY2M5NjgzMDBjOWU0ZTkzNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.tTzg95Rf9a-1A21zZPard3tyJYjlIRhLBoqo2qkAN0Y' // 실제 API 키로 교체해야 합니다.
    }
  }

  axios
    .request(options)
    .then(function (response) {
      movies.value = response.data.results // 가져온 데이터를 movies 배열에 할당
    })
    .catch(function (error) {
      console.error(error)
    })
})
</script>
  
  <style scoped>
.card-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.movie-card {
  width: 400px; /* Fixed width of each card */
  border: 1px solid #ccc;
  padding: 10px;
  margin: 10px;
  text-align: center;
}

.movie-card img {
  max-width: 100%;
  height: auto;
}
  </style>
  


  