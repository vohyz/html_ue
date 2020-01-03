<template>
  <div>
    <el-card shadow="hover" class="workcard" v-for="work in works" style="position:relative;" :key="work.title"  >
      <div>任务名：{{work.title}}</div>
      <button style="width:100%;height:100%;position:absolute;left:0;top:0;background: 0;border: 0;cursor: pointer" v-if="flag" @click="getDetails(work.id, type)"></button>
      <button style="width:100%;height:100%;position:absolute;left:0;top:0;background: 0;border: 0;cursor: pointer" v-if="!flag" @click="getDraftDetails(work.id,'get')"></button>
      <div style="float:left;">创建人：{{work.publisher}}</div>
      <div style="color:red">酬金：{{work.bonus}}</div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'workboard',
  data () {
    return {
      works: [],
      src: '',
      flag: true // 不是草稿箱
    }
  },
  computed: {
    type () {
      return this.$route.query.type
    }
  },
  watch: {
    type: function (thenew, theold) {
      if (thenew === 'caogao') {
        this.$axios.post('/api/getUserDrafts',
          {
            'user_name': localStorage.getItem('UserName')
          }
          // {headers: {'Content-Type': 'multipart/form-data'}}
        )
          .then((response) => {
            if (response.data.status === 'right') {
              this.works = response.data.List
              this.flag = false
            } else {
              this.$message.error({
                message: '没有发布的任务',
                showClose: true,
                type: 'error'
              })
            }
          },
          (response) => {
            this.$message.error({
              message: '网络连接失败',
              showClose: true,
              type: 'error'
            })
          }
          )
      } else if (thenew === 'exing') {
        this.$axios.post('/api/task/executeTask',
          {
            'user_name': localStorage.getItem('UserName')
          }
        )
          .then((response) => {
            if (response.data.status === 'right') {
              this.works = response.data.tasking
            } else {
              this.$message.error({
                message: '没有任务',
                showClose: true,
                type: 'error'
              })
            }
          },
          (response) => {
            this.$message.error({
              message: '网络连接失败',
              showClose: true,
              type: 'error'
            })
          }
          )
      } else { // post可以直接发参数，get必须用params打包
        this.$axios.post('/api/task/publishedTask',
          {
            'user_name': localStorage.getItem('UserName'),
            'type': thenew
          }
        )
          .then((response) => {
            if (response.data.status === 'right') {
              this.works = response.data.tasks
            } else {
              this.$message.error({
                message: '没有任务',
                showClose: true,
                type: 'error'
              })
            }
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
  },
  methods: {
    getDetails (id, type) {
      this.$router.push({
        path: `/taskdetails/${type}/${id}`
      })
    },
    getDraftDetails (id, type) {
      this.$router.push({
        path: `/usercenter/createorder/${type}/${id}`
      })
    }
  },
  mounted () {
    this.$axios.post('/api/task/publishedTask',
      {
        'user_name': localStorage.getItem('UserName'),
        'type': this.type
      }
    )
      .then((response) => {
        console.log(response.data.message)
        this.works = response.data.tasks
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

<style>
  .workcard {
    width:100%;
  }
</style>
