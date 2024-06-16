<template>
  <div class="youtube-card" @click="handleClick">
    <h3>{{ review.title }}</h3>
    <iframe width="560" height="315" :src="videoSrc" frameborder="0" allowfullscreen></iframe>
  </div>
</template>

<script>
export default {
  props: {
    videoId: {
      type: String,
      required: true
    },
    review: {
      type: Object,
      required: true
    }
  },
  computed: {
    videoSrc() {
      return `https://www.youtube.com/embed/${this.review.id.videoId}`
    }
  },
  methods: {
    handleClick() {
      this.$emit('card-clicked', this.review.id.videoId)
    }
  }
}
</script>

<style scoped>
.youtube-card {
  margin-bottom: 20px;
}
</style>
