<template>
  <div>
    <el-card shadow="hover" class="workcard" v-for="work in works" style="position:relative;" :key="work.title"  >
      <div>{{work.title}}</div>
      <button style="width:100%;height:100%;position:absolute;left:0;top:0;background: 0;border: 0;cursor: pointer" @click="getDetails(work.id)"></button>
      <div style="float:left;">{{work.beinger}}</div>
      <div style="float:right;">{{work.ender}}</div>
      <div style="color:red">{{work.price}}</div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'workboard',
  data () {
    return {
      works: [],
      src: 'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg'
    }
  },
  computed: {
    type () {
      return this.$route.query.type
    }
  },
  watch: {
    type: function (thenew, theold) {
      // post可以直接发参数，get必须用params打包
      this.$axios.post('/order',
        {
          'order_id': '1',
          'user_id': '1',
          'order_type': this.$route.query.type
        }
      )
        .then((response) => {
          console.log(response.data.message)
          this.works = response.data.works
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
  },
  methods: {
    getDetails (id) {
      this.$router.push({
        path: `/taskdetails/${id}`
      })
    }
  },
  mounted () {
    this.$axios.post('/order',
      {
        'order_id': '1',
        'user_id': '1',
        'order_type': this.$route.query.type
      }
    )
      .then((response) => {
        console.log(response.data.message)
        this.works = response.data.works
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
