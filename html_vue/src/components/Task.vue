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
      </el-breadcrumb>
    </div>
    <div class="taskCard">
      <el-col>
        <el-card shadow="hover">
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
    height: 800px;
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
</style>
