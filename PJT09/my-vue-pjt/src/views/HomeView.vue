<template>
    <div>
        <nav>
            <img :src="logo" alt="ssafylogo" class="img-logo">
            <RouterLink to="/movies">Movie</RouterLink>
            |
            <RouterLink to="/review-search">리뷰검색</RouterLink>
        </nav>
    </div>
    <RouterView />
</template>

<script setup>
    import logo from '@/assets/logo.png'
</script>

<style scoped>
    nav {
    display: flex; /* Flexbox 레이아웃 사용 */
    align-items: center; /* 수직 방향으로 중앙 정렬 */
    justify-content: flex-start; /* 왼쪽으로 정렬 */
    background-color: rgb(204, 215, 226);
    padding-top: 6px;
    padding-right: 25px;
    padding-left: 25px;
    height: 75px;
    }

    .img-logo {
        width: 50px;
        margin-right: auto; /* 이미지와 텍스트 사이의 공간을 최대화 */
    }

    nav > * {
        margin: 0 10px; /* 모든 직접 자식 요소에 마진 적용 */
    }

    nav a {
        color: black;
        text-decoration-line: none;
    }

</style>