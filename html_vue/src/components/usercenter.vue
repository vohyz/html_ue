<template>
  <div class="container">
    <div class="leftmenu">
        <div class="block">
            <el-image class="userimg" :src="src"></el-image>
            <p><span class="demonstration">{{user_id}}</span></p>
            <el-button :plain="true" @click="logout">登出</el-button>
        </div>
        <el-menu router :default-active="$route.path" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose">
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-message-solid"></i>
              <span>我的需求</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="/usercenter/workboard?type=publiced">已发布</el-menu-item>
              <el-menu-item index="/usercenter/workboard?type=caogao">草稿箱</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title">
              <i class="el-icon-s-order"></i>
              <span>我的任务</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="/usercenter/workboard?type=ing">进行中</el-menu-item>
              <el-menu-item index="/usercenter/workboard?type=achieved">已完成</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-menu-item index="/usercenter/createorder">
            <i class="el-icon-menu"></i>
            <span slot="title">发布任务</span>
          </el-menu-item>
        </el-menu>
    </div>
    <el-card class="rightcontent" shadow="never">
      <router-view></router-view>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'usercenter',
  methods: {
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    },
    logout () {
      this.$store.dispatch('userLogout')
      this.$message({
        showClose: true,
        message: '登出成功',
        type: 'success'
      })
      this.$router.push('/')
    }
  },
  data () {
    return {
      src: 'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg',
      user_id: ''
    }
  },
  mounted () {
    this.user_id = localStorage.getItem('User')
  }
}
</script>

<style>
.container {
  width: 80%;
  min-width:1005px;
  margin: 0 auto;
}
.leftmenu {
  float: left;
  width: 200px;
}
.rightcontent {
  float: left;
  width: 750px;
  margin-left:50px;
}
.block {
  border-right: solid 1px #e6e6e6;
  list-style: none;
  position: relative;
  margin: 0;
  padding: 10px;
  background-color: #FFF;
}
.userimg {
  width: 160px;
  margin: 0 auto;
  border-radius: 5px;
}
</style>
