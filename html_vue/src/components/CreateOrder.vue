<template>
  <div>
    <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
      <el-form-item label="任务名" prop="name">
        <el-input type="text" v-model="ruleForm.name" autocomplete="off" maxlength="15" show-word-limit></el-input>
      </el-form-item>
      <el-form-item label="任务描述" prop="introduce">
        <el-input type="textarea"
          v-model="ruleForm.introduce"
          placeholder="请输入对任务的具体描述"
          :rows="2"
          resize=none
          autocomplete="off"
          maxlength="200"
          show-word-limit></el-input>
      </el-form-item>
      <el-form-item label="出价" prop="price">
        <el-input v-model.number="ruleForm.price"></el-input>
      </el-form-item>
      <el-form-item label="标签" prop="tags">
        <el-cascader
          :options="options"
          :props="props"
          :show-all-levels="false"
          clearable>
        </el-cascader>
      </el-form-item>
      <el-form-item label="时间范围" prop="time">
        <el-date-picker
          v-model="ruleForm.time"
          type="datetimerange"
          :picker-options="pickerOptions"
          range-separator="至"
          start-placeholder="开始日期"
          end-placeholder="结束日期"
          align="center">
        </el-date-picker>
      </el-form-item>
      <el-form-item label="频率" prop="frequency">
          <el-radio-group v-model="ruleForm.frequency">
            <el-radio label="仅一次"></el-radio>
            <el-radio label="两次"></el-radio>
            <el-radio label="多次"></el-radio>
          </el-radio-group>
        </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
        <el-button @click="resetForm('ruleForm')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'createorder',
  data () {
    var validateName = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入任务名'))
      } else {
        callback()
      }
    }
    var checkPrice = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('出价不能为空'))
      }
      setTimeout(() => {
        if (!Number.isInteger(value)) {
          callback(new Error('请输入数字值'))
        } else {
          if (value > 100) {
            callback(new Error('必须少于100元'))
          } else {
            callback()
          }
        }
      }, 1000)
    }
    var validateIntroduce = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请描述一下任务细节'))
      } else {
        callback()
      }
    }
    var checksex = (rule, value, callback) => {
      if (!value) {
        callback(new Error('请选择性别'))
      } else {
        callback()
      }
    }
    var checkfrequency = (rule, value, callback) => {
      if (!value) {
        callback(new Error('请选择频率'))
      } else {
        callback()
      }
    }
    return {
      ruleForm: {
        name: '',
        introduce: '',
        price: '',
        sex: '',
        frequency: ''
      },
      rules: {
        name: [
          { validator: validateName, trigger: 'blur' }
        ],
        introduce: [
          { validator: validateIntroduce, trigger: 'blur' }
        ],
        price: [
          { validator: checkPrice, trigger: 'blur' }
        ],
        sex: [
          { validator: checksex, trigger: 'change' }
        ],
        frequency: [
          { validator: checkfrequency, trigger: 'blur' }
        ]
      },
      pickerOptions: {
        shortcuts: [{
          text: '三天',
          onClick (picker) {
            const end = new Date()
            const start = new Date()
            end.setTime(end.getTime() + 3600 * 1000 * 24 * 3)
            picker.$emit('pick', [start, end])
          }
        }, {
          text: '一周',
          onClick (picker) {
            const end = new Date()
            const start = new Date()
            end.setTime(end.getTime() + 3600 * 1000 * 24 * 7)
            picker.$emit('pick', [start, end])
          }
        }, {
          text: '半个月',
          onClick (picker) {
            const end = new Date()
            const start = new Date()
            end.setTime(end.getTime() + 3600 * 1000 * 24 * 15)
            picker.$emit('pick', [start, end])
          }
        }, {
          text: '一个月',
          onClick (picker) {
            const end = new Date()
            const start = new Date()
            end.setTime(end.getTime() + 3600 * 1000 * 24 * 30)
            picker.$emit('pick', [start, end])
          }
        }]
      },
      value1: [new Date(2000, 10, 10, 10, 10), new Date(2000, 10, 11, 10, 10)],
      value2: '',
      props: { multiple: true },
      options: [{
        value: 1,
        label: '娱乐',
        children: [{
          value: 2,
          label: '游戏',
          children: [
            { value: 3, label: '电脑游戏' },
            { value: 4, label: '手机游戏' },
            { value: 5, label: '线下游戏' }
          ]
        }, {
          value: 7,
          label: '运动',
          children: [
            { value: 8, label: '跑步' },
            { value: 9, label: '健身' },
            { value: 10, label: '远足' }
          ]
        }, {
          value: 12,
          label: '吃喝',
          children: [
            { value: 13, label: '火锅' },
            { value: 14, label: '海底捞' },
            { value: 15, label: '随便吃' }
          ]
        }]
      }, {
        value: 17,
        label: '学习',
        children: [{
          value: 18,
          label: '校内学习',
          children: [
            { value: 19, label: '图书馆' },
            { value: 20, label: '自习室' }
          ]
        }, {
          value: 21,
          label: '校外学习',
          children: [
            { value: 22, label: '星巴克' },
            { value: 23, label: '金拱门' }
          ]
        }]
      }]
    }
  },
  methods: {
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.$axios.post('/register',
            {
              'name': this.ruleForm.name,
              'pass': this.ruleForm.pass,
              'checkPass': this.ruleForm.checkPass,
              'age': this.ruleForm.age,
              'sex': this.ruleForm.sex
            }
          )
            .then((response) => {
              this.$message.success({
                message: '提交成功',
                showClose: true,
                type: 'success'
              })
            },
            (response) => {
              this.$message.error({
                message: '注册失败',
                showClose: true,
                type: 'error'
              })
            }
            )
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    }
  }
}
</script>

<style>
  .workcard {
    width:100%;
  }
  .el-picker-panel el-date-range-picker el-popper has-sidebar has-time {
    border:0;
  }
</style>
