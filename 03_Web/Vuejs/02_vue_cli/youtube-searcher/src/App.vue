<template>
  <div class="bg-app">
    <h1>Youtube Searcher</h1>
    <!-- 자식한테 일이 생기면 -->
    <SearchBar @inputChange="onInputChange" />
    <VideoDetail :video="selectedVideo" />
    <VideoList :videos="videos" @videoSelected="renderVideo" />
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar'
import VideoList from './components/VideoList'
import VideoDetail from './components/VideoDetail'

const API_KEY = process.env.VUE_APP_YOUTUBE_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data: function() {
    return {
      videos: [],
      selectedVideo: null,
      // 자기 데이터만 가지고 있고 싶어서 함수형식으로 리턴함
    }
  },
  methods: {
    onInputChange (inputValue) {
      // console.log(inputValue)
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: inputValue,
        }
      }).then((res) => {
        this.videos = res.data.items
        // console.log(this)
      }).catch(err => {
        console.log(err)
      })
    },
    renderVideo(video) {
      console.log(video)
      this.selectedVideo = video
    },
  },
}
</script>

<style scoped>
.bg-app {
    background-color: darkorchid;
}
</style>