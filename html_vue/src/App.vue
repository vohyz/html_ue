<template>
  <div id="app">
    <el-row>
      <el-col :span="24">
        <div class="grid-content bg-purple-dark">
          <div class="headline">
            <router-link to="/"><img class="logo" src="../static/LOGO.png"></router-link>
            <el-link type="primary" :underline="false" :href="loginlink">{{hellouseer}}</el-link>
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
      timeNow: '',
      hellouseer: '',
      loginlink: '',
      Flag: ''
    }
  },
  computed: {
    listenFlag () {
      return this.$store.state.isLogin
    }
  },
  watch: {
    listenFlag: function (thenew, theold) {
      console.log('theold' + theold)
      console.log('thenew' + thenew)
      if (theold === false && thenew === true) {
        let User = localStorage.getItem('User')
        this.hellouseer = '欢迎 [' + User + '] 个人中心'
        this.loginlink = '/usercenter'
      } else {
        this.hellouseer = '登录/注册'
        this.loginlink = '/login'
      }
    }
  },
  mounted () {
    this.timeNow = moment().utc().format('YYYY年MM月DD日') + ' ' + moment().utc().format('dddd')
    let islogin = this.$store.state.isLogin
    if (islogin === true) {
      let User = localStorage.getItem('User')
      this.hellouseer = '欢迎 [' + User + ']个人中心'
      this.loginlink = '/usercenter'
    } else {
      this.hellouseer = '登录/注册'
      this.loginlink = '/login'
    }
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
  color:#E16D00;
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
