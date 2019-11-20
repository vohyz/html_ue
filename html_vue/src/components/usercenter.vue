<template>
  <div class="container">
    <div class="leftmenu">
        <div class="block">
            <el-image class="userimg" :src="src"></el-image>
            <span class="demonstration">用户名</span>
        </div>
        <el-menu router :default-active="$route.path" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose">
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-message-solid"></i>
              <span>我的需求</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="/usercenter/workboard">已发布</el-menu-item>
              <el-menu-item index="/usercenter/workboard">草稿箱</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title">
              <i class="el-icon-s-order"></i>
              <span>我的任务</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="/usercenter/workboard">进行中</el-menu-item>
              <el-menu-item index="/usercenter/workboard">已完成</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-menu-item index="/usercenter/workboard">
            <i class="el-icon-menu"></i>
            <span slot="title">联系人</span>
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
    }
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      src: 'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg'
    }
  }
}
</script>

<style>
.container {
  width: 80%;
  min-width:1000px;
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
