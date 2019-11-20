<template>
  <div class="container">
    <el-card shadow="hover" v-for="(work,index) in works">
      {{work.message + index}}
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'workboard',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      works: [
        { message: 'work'},
        { message: 'work'},
        { message: 'work'},
        { message: 'work'},
        { message: 'work'},
        { message: 'work'},
        { message: 'work'},
        { message: 'work'},
        { message: 'work'}
      ],
      src: 'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg'
    }
  }
}
</script>

<style>
</style>
