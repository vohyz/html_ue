<template>
    <div class="Main">
      <div class="Task">
        <el-card class="box-card">
          <div>
            <el-col :span="8"><span style="font-size: 20px;font-weight: 600;float: right;">{{task[0].title}}</span></el-col>
            <el-col :span="8">
              <span style="font-size: 20px;font-weight: 600;float: right;">元</span>
              <span style="font-size: 26px;font-weight: 600;color: red;float: right;">{{task[0].bonus}}</span>
              <span style="font-size: 20px;font-weight: 600;float: right;">悬赏金：</span>
            </el-col>
            <el-col :span="8" style="margin-bottom:10px;">
              <el-button style="float: right; padding: 3px 0;font-size: 20px;font-weight: 600" @click="receiveTask" type="success" plain>认领</el-button>
            </el-col>
            <hr style="width:100%;">
            <el-col :span="8"><span style="font-size: 18px;font-weight: 400;float: right;line-height:30px;">标签：</span></el-col>
            <el-col :span="10">
              <el-tag style="float: left;margin-right:5px;">{{task[0].tags}}</el-tag>
            </el-col>
            <el-col :span="6">
            </el-col>
            <el-col :span="24" style="text-indent: 2em;width:100%;margin-top:20px;margin-bottom:20px;">
              {{task[0].info}}
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
              <el-avatar fit="fill" :size="90" :src="userAvatar"></el-avatar>
              <div class="status"></div>
            </div>
          </div>
          <div class="name">
            <span style="font-size: x-large;font-weight: 500">{{task[0].publisher}}</span><br>
            <span style="font-size: small;color: #72767b;font-style:oblique">最近登录: 2小时前</span>
          </div>
        </div>
        <div class="chatView" style="height: 300px;width: 400px;">
          <chat v-if="chated" :aim_user="task[0].publisher"></chat>
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
      chated: false,
      userId: '',
      userAvatar: ''
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
  // created () {
  //   this.$axios.post('/api/task/findTaskondetail',
  //     {
  //       'task_id': this.task_id
  //     }
  //   )
  //     .then((response) => {
  //       // console.log(response.data)
  //       this.task = response.data.published
  //       this.chated = true
  //       console.log(this.task.publisher)
  //       this.$store.dispatch('setaimuser', this.task.publisher)
  //     })
  //       .catch((error) => {
  //         console.log(error)
  //       })
  //     // (response) => {
  //     //   this.$message.error({
  //     //     message: '网络连接失败',
  //     //     showClose: true,
  //     //     type: 'error'
  //     //   })
  //     // }
  //     // )
  // },
  beforeMount () {
    // 获取任务信息
    this.$axios.post('/api/task/findTaskondetail',
      {
        'task_id': this.task_id
      }).then((response) => {
      this.task = response.data.published
      console.log(this.task)
    })
      .catch((error) => {
        console.log(error)
      })
    // 获取发布者信息
    this.$axios.post('/api/getUserInfo',
      {
        'user_name': this.task.publisher
      }).then((response) => {
      this.userId = response.data.user_Id
      this.userAvatar = response.data.user_avatar
    })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    getDetails (id) {
      this.$router.push({
        path: `/taskdetails/${id}`
      })
    },
    receiveTask () {
      this.$axios.post('/api/task/receiveTask', {
        'task_id': this.task_id,
        'user_name': localStorage.getItem('UserName')
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
</style>
