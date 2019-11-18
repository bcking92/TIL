<template>
  <div class="bg-search">
    <input @change="onInput" type="text" />
  </div>
</template>

<script>
export default {
  name: 'Searchbar',
  methods: {
    onInput(event) {
      // console.log(event.target.value)
      // 부모한테 데이터를 올려 보내줄 때 $emit(): 자식 컴포넌트에서 부모 컴포넌트로 데이터를 올려(방출해) 줄 때,
      // this.$emit('이벤트이름', 보내줄 데이터)
      // console.log(this)
      this.$emit('inputChange', event.target.value)
      }
  },
}
</script>

<style scoped>
  .bg-search {
    background-color: bisque;
}
</style>