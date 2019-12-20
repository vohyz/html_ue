<template>
  <div class="task">
    <div class="guideBar">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/index' }">
          <span style="font-size: medium">首页</span>
        </el-breadcrumb-item>
        <el-breadcrumb-item>
          <span style="font-size: medium">游戏</span>
        </el-breadcrumb-item>
        <el-breadcrumb-item>
          <span style="font-size: medium">英雄联盟</span>
        </el-breadcrumb-item>
        <div class="plus">
          <router-link to="/index/createorder">
            <el-tooltip class="item" effect="light" content="创建任务" placement="right">
<!--              <el-button type="primary" icon="el-icon-plus" circle></el-button>-->
              <i class="el-icon-circle-plus-outline" style="font-size: 30px"></i>
            </el-tooltip>
          </router-link>
        </div>
      </el-breadcrumb>
    </div>
    <div class="taskCard">
      <el-col v-for="i in 8" :key="i">
        <el-card class="cards" shadow="hover">
          <div class="introWord">
            <p id="intro">
              <span class="taskTitle" style="font-size: large">标题</span><br>
              <i class="el-icon-coin" style="color: #ffd84d">50</i><br>
            </p>
            <el-date-picker
              v-model="value"
              type="daterange"
              start-placeholder="开始日期"
              end-placeholder="结束日期"
              :default-time="['00:00:00', '23:59:59']"
              style="margin-left: 10px;margin-top: 5px">
            </el-date-picker>
          </div>
          <div class="publisher">
            <p>
              发布者: Leo<br>
              发布时间: 2019/12/4
            </p>
          </div>
        </el-card>
      </el-col>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Task',
  data () {
    return {
      value: ''
    }
  }
}
</script>

<style scoped>
  .task{
    height: 100%;
  }
  .guideBar{
    padding-left: 15px;
    padding-top: 10px;
  }
  .taskCard{
    margin-top: 20px;
    width: 100%;
  }
  .el-col{
    width: 98%;
    padding-left: 1.5%;
  }
  .el-card{
    height: 110px;
  }
  .introWord{
    float: left;
    width: 70%;
    margin: 0;
    text-align: left;
  }
  #intro{
    margin: 0;
    text-align: left;
    padding-left: 20px;
  }
  .publisher{
    width: 25%;
    float: left;
    padding-top: 5px;
  }
  .el-card__body {
    padding: 10px;
  }
  .plus{
    width: 40px;
    height: 40px;
    padding-left: 85%;
  }
  .el-icon-circle-plus-outline{
    margin-top: 5px;
  }
  .cards{
    margin-bottom: 4px;
  }
</style>
