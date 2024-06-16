<template>
  <div>
    <input v-model="searchQuery" @keyup.enter="searchReviews" placeholder="영화 제목을 검색해보세요">
    <button @click="searchReviews">검색</button>

    <div v-if="loading">로딩 중...</div>
    <div v-if="!loading && reviews.length">
      <youtube-card v-for="review in reviews" :key="review.id.videoId" :review="review" @card-clicked="handleCardClicked"/>
      <youtube-review-modal v-if="showModal" :videoId="currentVideoId" :show="showModal" @close="handleModalClose"/>
    </div>
  </div>
</template>

<script>
import YoutubeCard from '@/components/YoutubeCard.vue'
import YoutubeReviewModal from '@/components/YoutubeReviewModal.vue'
import axios from 'axios'

export default {
  components: {
    YoutubeCard,
    YoutubeReviewModal
  },
  data() {
    return {
      searchQuery: '',  // 사용자 검색어를 저장할 변수
      reviews: [],      // 검색 결과를 저장할 변수
      loading: false,    // 로딩 상태를 나타낼 변수
      showModal: false,
      currentVideoId: null,
    }
  },
  methods: {
    handleCardClicked(videoId) {
      this.currentVideoId = videoId
      this.showModal = true
    },
    handleModalClose() {
      this.showModal = false
    },
    
    searchReviews() {
      // 입력된 검색어가 없다면 바로 반환
      if (!this.searchQuery.trim()) {
        return
      }

      this.loading = true
      const apiKey = import.meta.env.VITE_YOUTUBE_API_KEY // 환경 변수에서 API 키 가져오기
      const searchQueryEncoded = encodeURIComponent(this.searchQuery) // 검색어 인코딩
      const url = `https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&q=${searchQueryEncoded}&key=${apiKey}`

      // YouTube API 호출
      axios.get(url)
        .then(response => {
          // 성공적으로 데이터를 가져온 경우, 'reviews' 데이터 속성을 업데이트
          this.reviews = response.data.items.map(item => ({
            id: item.id,
            title: item.snippet.title,
            videoUrl: `https://www.youtube.com/watch?v=${item.id.videoId}`
          }))
          this.loading = false
        })
        .catch(error => {
          // 오류가 발생한 경우, 오류를 처리
          console.error('Error fetching YouTube videos:', error)
          this.loading = false
        })
    }
  }
}
</script>

<style>
</style>