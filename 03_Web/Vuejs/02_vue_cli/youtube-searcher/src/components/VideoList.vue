<template>
  <div>
    <h2>Video List</h2>
    <ul>
      <li v-for="video in videos" v-bind:key="video.id.videoId">
        <img :src="video.snippet.thumbnails.default.url">
      </li>
    </ul>
    
  </div>
  
</template>

<script>
export default {
  name: 'VideoList',
  props: {
    videos: {
      type: Array,
    },
  },
}
</script>

<style>

</style>
