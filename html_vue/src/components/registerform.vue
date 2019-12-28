<template>
  <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
    <el-form-item label="用户名" prop="name">
      <el-input type="text" v-model="ruleForm.name" autocomplete="off"></el-input>
    </el-form-item>
    <el-form-item label="密码" prop="pass">
      <el-input type="password" v-model="ruleForm.pass" autocomplete="off"></el-input>
    </el-form-item>
    <el-form-item label="确认密码" prop="checkPass">
      <el-input type="password" v-model="ruleForm.checkPass" autocomplete="off"></el-input>
    </el-form-item>
    <el-form-item label="手机号码" prop="phone">
      <el-input v-model.number="ruleForm.phone"></el-input>
    </el-form-item>
    <el-form-item label="验证码" prop="vcode">
      <el-input v-model.number="ruleForm.vcode" style="width:60%;float:left;"></el-input>
      <el-button type="primary" style="width:35%;" @click="submitForm('ruleForm')">获取验证码</el-button>
    </el-form-item>
    <el-form-item label="年龄" prop="age">
      <el-input v-model.number="ruleForm.age"></el-input>
    </el-form-item>
    <el-form-item label="性别" prop="sex">
        <el-radio-group v-model="ruleForm.sex">
          <el-radio label="男"></el-radio>
          <el-radio label="女"></el-radio>
        </el-radio-group>
      </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
      <el-button @click="resetForm('ruleForm')">重置</el-button>
    </el-form-item>
  </el-form>
</template>
<script>
export default {
  name: 'registerform',
  data () {
    var validateName = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入用户名'))
      } else {
        callback()
      }
    }
    var checkAge = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('年龄不能为空'))
      }
      setTimeout(() => {
        if (!Number.isInteger(value)) {
          callback(new Error('请输入数字值'))
        } else {
          if (value < 16) {
            callback(new Error('必须年满16岁'))
          } else {
            callback()
          }
        }
      }, 1000)
    }
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        if (this.ruleForm.checkPass !== '') {
          this.$refs.ruleForm.validateField('checkPass')
        }
        callback()
      }
    }
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.ruleForm.pass) {
        callback(new Error('两次输入密码不一致!'))
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
    return {
      ruleForm: {
        name: '',
        pass: '',
        checkPass: '',
        phone: '',
        vcode: '',
        age: '',
        sex: ''
      },
      rules: {
        name: [
          { validator: validateName, trigger: 'blur' }
        ],
        pass: [
          { validator: validatePass, trigger: 'blur' }
        ],
        checkPass: [
          { validator: validatePass2, trigger: 'blur' }
        ],
        age: [
          { validator: checkAge, trigger: 'blur' }
        ],
        sex: [
          { validator: checksex, trigger: 'change' }
        ]
      }
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
              'phone': this.ruleForm.phone,
              'vcode': this.ruleForm.vcode,
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
    },
    send_smscode (formName) { // 此处需要补全图像验证码以及手机的validate
      this.ruleForm.phone.validate((valid) => {
        if (valid) {
          this.$axios.post('/sms_code',
            {
              'phone': this.ruleForm.phone
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
    }
  }
}
</script>
