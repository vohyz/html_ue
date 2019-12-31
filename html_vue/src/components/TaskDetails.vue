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
              <el-button style="float: right; padding: 3px 0;font-size: 20px;font-weight: 600" type="success" plain>认领</el-button>
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
        <div class="userInfo" style="padding: 20px;width: 357px;">
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
        <div class="chatView" style="height: 300px;width: 400px;">
          <chat v-if="chated" :aim_user="task.publisher"></chat>
        </div>
      </div>
    </div>
</template>

<script>
import chat from './chat.vue'
export default {
  name: 'taskdetail',
  data () {
    return {
      task: {},
      src: 'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg',
      chated: false
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
  methods: {
    getDetails (id) {
      this.$router.push({
        path: `/taskdetails/${id}`
      })
    }
  },
  created () {
    this.$axios.post('http://127.0.0.1:5001/task',
      {
        'task_id': this.task_id
      }
    )
      .then((response) => {
        console.log(response.data)
        this.task = response.data
        this.chated = true
        console.log(this.task.publisher)
        this.$store.dispatch('setaimuser', this.task.publisher)
      },
      (response) => {
        this.$message.error({
          message: '网络连接失败',
          showClose: true,
          type: 'error'
        })
      }
      )
  }
}
</script>

<style scoped>
  @import '../element/index.css';
  .Main {
    width:100%;
  }
  .Task{
    width: 68%;
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
