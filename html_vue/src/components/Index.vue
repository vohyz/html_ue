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
        <el-avatar :size="95" shape="square" fit="fill" src="../static/avatar.jpg"></el-avatar><br>
      </div>
      <div class="name" style="margin-top: 20px">
        <span style="font-size: x-large">Leo</span>
      </div>
      <div class="info" style="height: 500px">
        <div class="credit" style="width: 50%;border-right: 1px solid rgb(200,200,200);">
          <i class="el-icon-coin" style="color: #13ce66"></i>
          <label>信誉分</label>
        </div>
        <div class="wechat" style="width: 49%">
          <i class="el-icon-chat-dot-round" style="color: #13ce66"></i>
          <label>绑定微信</label>
        </div>
        <div class="mytasks">
          <el-collapse v-model="activeNames" @change="handleChange">
            <el-collapse-item name="1">
              <template slot="title">
                <div style="width: 100%">
                  <el-badge :value="4" class="item">
                    <span style="font-size: 17px">正在执行的任务</span>
                  </el-badge>
                </div>
              </template>
                <el-col v-for="o in 4" :key="o" >
                  <el-card class="box-card" shadow="never">
                    <div class="text item">
                      {{'列表内容 ' + o }}
                    </div>
                  </el-card>
                </el-col>
            </el-collapse-item>
            <el-collapse-item name="2">
              <template slot="title">
                <div style="width: 100%">
                  <el-badge :value="4" class="item">
                    <span style="font-size: 17px">当前发布的任务</span>
                  </el-badge>
                </div>
              </template>
              <el-col v-for="o in 4" :key="o" >
                <el-card class="box-card" shadow="never">
                  <div class="text item">
                    {{'列表内容 ' + o }}
                  </div>
                </el-card>
              </el-col>
            </el-collapse-item>
          </el-collapse>
        </div>
      </div>
    </div>
  </div>
</template>

<script type="text/javascript">
export default {
  name: 'Index',
  mounted () {
    // 事件监听滚动条
    window.addEventListener('scroll', this.watchScroll)
  },
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
    handleChange (val) {
      console.log(val)
    },
    test () {
      alert('success')
    }
    // showTask () {
    //
    // }
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
  .Module{
    height: 1000px;
  }
  .sideModule{
    width: 14%;
    min-width: 150px;
    margin-top: 8px;
    float: left;
    background-color: white;
    height: 100%;
  }
  .taskModule{
    margin-top: 8px;
    margin-left: 0.8%;
    width: 60%;
    min-width: 600px;
    float: left;
    background-color: white;
    height: 100%;
  }
  .rightModule{
    width: 24.4%;
    min-width: 200px;
    margin-left: 0.8%;
    margin-top: 8px;
    float: left;
    background-color: white;
    height: 100%;
  }
  .el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 99%;
    min-height: 400px;
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
  .mytasks{
    padding-top: 150px;
  }
  .credit{
    width: 100px;
    height: 30px;
    margin-top: 50px;
    float: left;
  }
  .wechat{
    width: 100px;
    height: 30px;
    float: left;
    margin-top: 50px;
  }
</style>
