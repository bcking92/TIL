<template>
  <div>
    <h1>Youtube Searcher</h1>
    <!-- 자식한테 일이 생기면 -->
    <SearchBar @inputChange="onInputChange" />
    <VideoList :videos="videos" />
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar'
import VideoList from './components/VideoList'

const API_KEY = ''
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
  },
  data: function() {
    return {
      videos: [],
    }
  },
  methods: {
    onInputChange (inputValue) {
      console.log(inputValue)
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: inputValue,
        }
      }).then(() => {
        this.videos = res.data.items
        console.log(this)
      })
    },
  },
}
</script>

<style>

</style>