<template>
  <div>
    <h1>Youtube Searcher</h1>
    <!-- 자식한테 일이 생기면 -->
    <SearchBar @inputChange="onInputChange" />
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar'

const API_KEY = 'AIzaSyC3Lm8yUU6ZgXtdqcpLxRvMN4wTDfjKSHw'
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    SearchBar,
  },
  methods: {
    onInputChange (inputValue) {
      console.log(inputValue)
      const response = axios.get(API_URL, {
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: inputValue,
        }
      })
      response.then(function(res){
        console.log(res)
      })
    },
  },
}
</script>

<style>

</style>