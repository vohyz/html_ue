<template>
  <div id="app">
    <el-row>
      <el-col :span="24">
        <div class="grid-content bg-purple-dark">
          <div class="headline">
            <img class="logo" src="../static/LOGO.png">
            <el-link type="primary" :underline="false" href="/login">登录/注册</el-link>
            <div class="time">{{timeNow}}</div>
            <div class="city"><i class="el-icon-location" id="location"></i>上海</div>
          </div>
        </div>
      </el-col>
    </el-row>
    <router-view/>
  </div>
</template>
<script>
let moment = require('moment')
export default {
  name: 'App',
  data () {
    return {
      timeNow: ''
    }
  },
  mounted () {
    this.timeNow = moment().utc().format('YYYY年MM月DD日') + ' ' + moment().utc().format('dddd')
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
  border-radius: 4px;
}
.grid-content {
  background:#fff;
}
.headline {
  width:70%;
  height:50px;
  padding:10px;
  margin:0 auto;
}
.logo {
  height:50px;
  float:left;
  margin-left:40px;
}
.el-link {
  padding:10px;
  font-size:20px;
}
#location {
  font-size:24px;
}
.city {
  float:right;
  padding:10px;
  font-size:20px;
}
.time {
  float:right;
  padding:10px;
  font-size:20px;
}
</style>
