<template>
  <div class="bg-detail">
  <h1>detail</h1>
  <iframe :src="iframeURL" frameborder="0"></iframe>
  </div>
</template>

<script>
export default {
  name: "VideoDetail",
  props: {
    video: {
      type: Object,
    }
  },
  computed: {
    iframeURL() {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    },
  },
}
</script>

<style scoped>
  .bg-detail {
    background-color: chartreuse
  }
</style>