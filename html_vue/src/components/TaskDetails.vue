<template>
  <div class="Main">
    <div class="Task">
      <el-card class="box-card">
        <div>
          <el-col :span="8"><span style="font-size: 20px;font-weight: 600;float: right;">{{task.title}}</span></el-col>
          <el-col :span="8">
            <span style="font-size: 20px;font-weight: 600;float: right;">元</span>
            <span style="font-size: 26px;font-weight: 600;color: red;float: right;">{{task.bonus}}</span>
            <span style="font-size: 20px;font-weight: 600;float: right;">悬赏金：</span>
          </el-col>
          <el-col :span="8" style="margin-bottom:10px;">
            <el-button style="float: right; padding: 3px 0;font-size: 20px;font-weight: 600" type="success" plain @click="receiveTask">认领</el-button>
          </el-col>
          <hr style="width:100%;">
          <el-col :span="8"><span style="font-size: 18px;font-weight: 400;float: right;line-height:30px;">标签：</span></el-col>
          <el-col :span="10">
            <el-tag v-for="tag in task.tags" :key="tag"  style="float: left;margin-right:5px;">{{tag}}</el-tag>
          </el-col>
          <el-col :span="6">
          </el-col>
          <el-col :span="24" style="text-indent: 2em;width:100%;margin-top:20px;margin-bottom:20px;">
            {{task.info}}
          </el-col>
          <div >
            <div class="allmap" id="allmap" style="height:300px;">
            </div>
          </div>
        </div>
      </el-card>
    </div>
    <div class="Chat">
      <div class="userInfo" style="padding: 20px;width:auto;">
        <div class="avatar" style="width: auto;float: left">
          <div class="picture">
            <el-avatar fit="fill" :size="90" src="../static/avatar.jpg"></el-avatar>
            <div class="status"></div>
          </div>
        </div>
        <div class="name">
          <span style="font-size: x-large;font-weight: 500">{{task.publisher}}</span><br>
          <span style="font-size: small;color: #72767b;font-style:oblique">最近登录: 2小时前</span>
        </div>
      </div>
      <div class="chatView" style="height: 300px">
      </div>
    </div>
  </div>
</template>

<script>
import chat from './chat.vue'
export default {
  name: 'TaskDetail',
  data () {
    return {
      task: {},
      user: []
    }
  },
  components: {
    chat: chat
  },
  computed: {
    task_id () {
      return this.$route.params.id
    }
  },
  beforeMount () {
    // 获取任务信息
    this.$axios.get('/task/getById', {
      params: {'id': this.task_id}
    }).then((response) => {
      this.task = response.data.thistask
    })
      .catch((error) => {
        console.log(error)
      })
    // 获取发布者信息
    this.$axios.get('/getuserinfo', {
      params: {'username': this.task.publisher}
    }).then((response) => {
      this.user = response.data.userinfo
    })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    receiveTask () {
      this.$axios.post('/getTask', {
        'taskId': this.task.id,
        'userName': this.user.userName
      }).then((response) => {
        console.log(response)
      })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>

<style scoped>
  @import '../element/index.css';
  .Task{
    width: 70%;
    float: left;
    margin-top: 5px;
    margin-left: 5px;
  }
  .Chat{
    width: 28%;
    float: left;
    margin-top: 5px;
    border-radius: 5px;
    background-color: white;
    margin-left: 1%;
  }
  .userInfo{
    border: 1px solid rgb(230,230,230);
    border-radius: 5px;
    width: 90%;
    height: 110px;
  }
  .chatView{
    border-radius: 5px;
    border-right: 1px solid rgb(230,230,230);
    border-left: 1px solid rgb(230,230,230);
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
