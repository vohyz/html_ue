<template>
    <div class="Main">
      <div class="Task">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span style="font-size: 20px;font-weight: 600">任务标题</span>
            <el-button style="float: right; padding: 3px 0;font-size: 16px;font-weight: 600" type="text">认领</el-button>
          </div>
          <div v-for="o in 4" :key="o" class="text item">
            {{'列表内容 ' + o }}
          </div>
        </el-card>
      </div>
      <div class="Chat">
        <div class="userInfo" style="padding: 20px">
          <div class="avatar" style="width: auto;float: left">
            <div class="picture">
              <el-avatar fit="fill" :size="90" src="../static/avatar.jpg"></el-avatar>
              <div class="status"></div>
            </div>
          </div>
          <div class="name">
            <span style="font-size: x-large;font-weight: 500">Leo</span><br>
            <span style="font-size: small;color: #72767b;font-style:oblique">最近登录: 2小时前</span>
          </div>
        </div>
        <div class="chatView" style="height: 500px">
          这里是聊天视图
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: 'TaskDetail'
}
</script>

<style scoped>
  @import '../element/index.css';
  .Task{
    width: 70%;
    float: left;
    margin-top: 5px;
  }
  .Chat{
    width: 29%;
    float: left;
    margin-top: 5px;
    border-radius: 5px;
    background-color: white;
    margin-left: 1%;
  }
  .userInfo{
    border-bottom: 1px solid rgb(230,230,230);
    border-right: 1px solid rgb(230,230,230);
    border-left: 1px solid rgb(230,230,230);
    width: 100%;
    height: 110px;
  }
  .picture{
    text-align: left;
    width: 100px;
  }
  .status{
    background-color: #13ce66;
    border-radius: 100%;
    width: 16px;
    height: 16px;
    float: right;
    margin-top: -15px;
  }
  .name{
    float: left;
    width: 50%;
    margin-top: 16px;
    margin-left: 20px;
    text-align: left;
  }
  .text {
    font-size: 16px;
  }
  .item {
    margin-bottom: 18px;
  }
  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }
</style>
