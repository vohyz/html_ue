<template>
  <div class="Module">
    <div class="sideModule">
      <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">
        <el-radio-button :label="false">展开</el-radio-button>
        <el-radio-button :label="true">收起</el-radio-button>
      </el-radio-group>
      <el-menu default-active="1-4-1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" :collapse="isCollapse">
        <el-submenu index="1">
          <template slot="title">
            <i class="first">
              <i class="el-icon-location"></i>
              <label style="cursor: pointer">导航一</label>
            </i>
          </template>
          <el-menu-item-group>
            <el-menu-item index="1-1">
              <router-link to="/index/task">
                选项1
              </router-link>
            </el-menu-item>
            <el-menu-item index="1-2">选项2</el-menu-item>
          </el-menu-item-group>
            <el-menu-item index="1-3">选项3</el-menu-item>
          <el-submenu index="1-4">
            <span slot="title">选项4</span>
            <el-menu-item index="1-4-1">选项1</el-menu-item>
          </el-submenu>
        </el-submenu>
        <el-menu-item index="2">
          <i class="second">
            <i class="el-icon-location"></i>
            <label style="cursor: pointer">导航二</label>
          </i>
        </el-menu-item>
        <el-menu-item index="3">
          <i class="third">
            <i class="el-icon-location"></i>
            <label style="cursor: pointer">导航三</label>
          </i>
        </el-menu-item>
        <el-menu-item index="4">
          <i class="forth">
            <i class="el-icon-setting"></i>
            <label style="cursor: pointer">导航四</label>
          </i>
        </el-menu-item>
      </el-menu>
    </div>
    <div class="taskModule">
      <router-view></router-view>
    </div>
    <div class="rightModule">
      <div class="avatar" style="margin-top: 10px">
        <el-avatar :size="95" fit="fill" src="../static/avatar.jpg"></el-avatar><br>
      </div>
      <div class="name" style="margin-top: 20px">
        <span style="font-size: x-large">Leo</span>
      </div>
<!--      <div class="selectWord" style="width: 115px;padding-left: 36%;margin-top: 50px">-->
<!--        <el-tabs v-model="activeName" @tab-click="handleClick">-->
<!--          <el-tab-pane label="About" name="first"></el-tab-pane>-->
<!--          <el-tab-pane label="Tasks" name="second"></el-tab-pane>-->
<!--        </el-tabs>-->
<!--      </div>-->
      <div class="info" style="height: 500px">
        <div class="credit" style="border-radius: 50%;width: 100px;background-color: #F56C6C;height: 30px;padding-top: 5px;margin-top: 50px;float: left">
          <i class="el-icon-coin"></i>
          <label>信誉分</label>
        </div>
        <div class="wechat" style="padding-top: 5px;margin-top: 50px;border-radius: 100%;width: 100px;height: 30px;background-color: #67C23A;float: left">
          <i class="el-icon-chat-dot-round"></i>
          <label>绑定微信</label>
        </div>
        <div class="plus">
          <el-tooltip class="item" effect="light" content="创建任务" placement="right">
            <el-button type="primary" icon="el-icon-plus" circle></el-button>
          </el-tooltip>
        </div>
        <div class="mytasks">
          <span>我接单的任务: 2</span><br>
          <span>我发布的任务: 5</span><br>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Index',
  methods: {
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClick (tab, event) {
      console.log(tab, event)
    },
    test () {
      alert('success')
    }
  },
  data () {
    return {
      isCollapse: true,
      activeName: 'first'
    }
  }
}
</script>

<style scoped>
  .sideModule{
    width: 14%;
    min-width: 150px;
    margin-top: 8px;
    float: left;
    background-color: white;
    height: max-content;
  }
  .taskModule{
    margin-top: 8px;
    margin-left: 0.8%;
    width: 60%;
    min-width: 600px;
    float: left;
    background-color: white;
  }
  .rightModule{
    width: 24.4%;
    min-width: 200px;
    margin-left: 0.8%;
    margin-top: 8px;
    float: left;
    background-color: white;
  }
  .el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 99%;
    min-height: 400px;
  }
  .plus{
    width: 40px;
    height: 40px;
    padding-left: 90%;
  }
  .el-menu--collapse {
    width: 50%;
  }
  .el-tooltip{
    disabled: false;
  }
  .el-menu{
    border-right: none;
  }
</style>
