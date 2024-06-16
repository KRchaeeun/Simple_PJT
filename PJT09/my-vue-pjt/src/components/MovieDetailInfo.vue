<template>
    <div>
        <img v-if="movieDetail.poster_path" :src="`https://image.tmdb.org/t/p/w500/${movieDetail.poster_path}`" alt="Poster">
        <p v-else>포스터 이미지를 사용할 수 없습니다.</p>
        <h3>{{ movieDetail.title }}</h3>
        <div>
            <p><strong>개봉일: </strong>{{ movieDetail.release_date }}</p>
            <p><strong>러닝타임: </strong>{{ movieDetail.runtime }} 분</p>
            <p><strong>TMDB 평점: </strong>{{ movieDetail.vote_average }}</p>
        </div>
        <h3>장르</h3>
        <div>
            <p v-if="movieDetail.genres && movieDetail.genres.length">
                {{ movieDetail.genres.map(genre => genre.name).join(' ') }}
            </p>
            <p v-else>장르 정보가 없습니다.</p>
        </div>
        <div>
            <h2>줄거리</h2>
            <p>{{ movieDetail.overview }}</p>
        </div>
        <div>
            <h2>공식 예고편</h2>
            <img :src="youtubeLogo" alt="YouTube Logo" @click="toggleTrailerModal"/> <!-- Updated this line -->
            <!-- <img :src="youtubeLogo" alt="YouTube Logo" @click="showTrailerModal"/>  로고 클릭시 showTrailerModal 함수가 시작 -->
        </div>
    </div>
    <YoutubeTrailerModal :movieTitle="movieDetail.title" :isVisible="isTrailerModalVisible" @close-modal="toggleTrailerModal"/>
</template>

<script setup>
import { ref, onMounted } from 'vue'  // Vue의 반응형 API import
import { useRoute } from 'vue-router'   
import axios from 'axios'  // HTTP 요청을 위한 axios 라이브러리 import
import youtubeLogo from '@/assets/youtube_logo.PNG'  // assets 폴더에서 youtube_log 이미지 가져오기
import YoutubeTrailerModal from '@/components/YoutubeTrailerModal.vue'

const route = useRoute()  // 현재 라우트의 정보에 접근하기 위한 useRoute
const movieDetail = ref({})  // 영화 상세 정보를 저장할 반응형 참조 객체를 생성

// 영화 상세 정보를 API로부터 가져오는 비동기 함수
const fetchMovieDetail = () => {
const movieId = route.params.movieId  // URL에서 영화 ID를 추출
    axios.get(`https://api.themoviedb.org/3/movie/${movieId}?api_key=${import.meta.env.VITE_TMDB_API_KEY}`)  // 보안을 위해 API 키를 .env파일에 저장
        .then(response => {
        movieDetail.value = response.data  // API 응답 데이터를 movieDetail 참조 객체에 저장
        })
        .catch(error => {
        console.error('영화 상세 정보를 가져오는 데 실패했습니다:', error)  // API 요청 중 오류가 발생하면 콘솔에 오류 출력
        })
    }

onMounted(() => {
    fetchMovieDetail()  // TMDB API에서 영화의 상세 정보를 가져오기
})

const isTrailerModalVisible = ref(false)  // 모달 가시성을 제어하기 위한 반응형 상태

// 모달을 토글하는 함수
const toggleTrailerModal = () => {
    isTrailerModalVisible.value = !isTrailerModalVisible.value
}
</script>

<style scoped>

</style>