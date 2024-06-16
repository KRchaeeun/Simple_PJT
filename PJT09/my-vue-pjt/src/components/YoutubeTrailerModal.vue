<template>
    <div v-if="props.isVisible">
            <h4>{{ props.movieTitle }} 공식 예고편</h4>
    <hr>
    <div v-if="videoId">
        <iframe :src="`https://www.youtube.com/embed/${videoId}`" frameborder="0" allowfullscreen></iframe>
    </div>
    <button @click="closeModal">닫기</button>  <!-- Close button to close the modal -->
    </div>
</template>

<script setup>
    import { ref, watch } from 'vue'
    import axios from 'axios'

    const props = defineProps({
        movieTitle: String,
        isVisible: Boolean
    })

    const videoId = ref('')

    watch(() => props.movieTitle, (newTitle) => {
    if (newTitle) {
        axios.get(`https://www.googleapis.com/youtube/v3/search?part=snippet&q=${encodeURIComponent(newTitle)} 예고편&key=${import.meta.env.VITE_YOUTUBE_API_KEY}`)
        .then(response => {
            if (response.data.items.length > 0) {
            // 첫 번째 검색 결과의 videoId를 사용
            videoId.value = response.data.items[0].id.videoId
            }
        })
        .catch(error => console.error('티저 영상이 존재하지 않습니다:', error))
    }
    })
    const emit = defineEmits(['close-modal'])

// 모달을 닫는 함수
const closeModal = () => {
    emit('close-modal')
}
</script>
  
<style scoped>
/* 스타일링 */
</style>