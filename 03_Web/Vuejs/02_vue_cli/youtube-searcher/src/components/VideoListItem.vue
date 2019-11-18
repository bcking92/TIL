<template>
<li>
    <button @click="onSelect"><img :src="url"></button>
</li>
</template>

<script>
export default {
  name: "VideoListItem",
  props: {
    video: {
      type: Object,
      required: true,
    }
  },
  methods:{
    onSelect() {
      this.$emit("videoSelect", this.video)
    }
  },
  computed: {
    url() {
      return this.video.snippet.thumbnails.default.url
    },
  }
}
</script>

<style>

</style>