<template>
  <div class="task">
    <div class="guideBar">
      <div class="plus">
        <router-link to="/index/createorder">
          <el-tooltip class="item" effect="light" content="创建任务" placement="right">
            <i class="el-icon-circle-plus-outline" style="font-size: 30px"></i>
          </el-tooltip>
        </router-link>
      </div>
    </div>
    <div class="taskCard">
      <el-col v-for="task in tasks" :key="task">
        <el-card class="cards" shadow="hover" style="cursor: pointer">
          <a :href="'/taskdetail?id='+task.id" target="_blank">
            <div class="introWord">
              <p id="intro">
                <span class="taskTitle" style="font-size: large">{{task.title}}</span><br>
                <i class="el-icon-coin" style="color: #ffd84d;padding-top: 3%">{{task.bonus}}</i><br>
              </p>
              <div class="datetime" style="padding-top: 3%;padding-left: 4%">
                <i class="el-icon-date" style="float: left"></i>
                <span style="float: left">{{task.begintime}}</span>
                <span style="float: left;padding-left: 2%;padding-right: 2%">-</span>
                <span style="float: left">{{task.endtime}}</span>
              </div>
            </div>
            <div class="publisher">
              <p>
                发布者: {{task.publisher}}<br>
                发布时间: {{task.publishtime}}
              </p>
            </div>
          </a>
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
      value: '',
      tasks: []
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
