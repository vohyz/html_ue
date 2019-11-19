<template>
  <div class="container">
  <div id="111" class="logindesk" style="height:100%;width:100%;">
      <div class="logintop" style="height:6px;background-color:rgb(28, 134, 255);"></div>
      <div class="logintitle" style="height:40px;border-bottom: rgb(151, 151, 151, .2) solid 1px;border-top: rgb(151, 151, 151, .2) solid 1px;">
          <span class="glyphicon glyphicon-remove" id="close" style="cursor:pointer;color:black;float:right;margin-top:10px;margin-right:10px;font-size:16px;"></span>

          <ul id="myTab" class="nav nav-tabs" style="height:40px;">
              <li class="active">
                  <a href="#2codes" data-toggle="tab">
                      <span style="color:black;font-size:16px;">二维码登录</span>

                  </a>
              </li>
              <li>
                  <a href="#phonelogin" data-toggle="tab">
                      <span style="color:black;font-size:16px;">手机号登录</span>
                  </a>
              </li>
          </ul>
          <div id="myTabContent" class="tab-content" style="border: 0;">
              <div class="tab-pane fade in active" id="2codes">
              </div>
              <div class="tab-pane fade" id="phonelogin">
                  <form id="loginform" style="width:90%;margin:auto;padding:20px;">
                      <input class="ltextbox col-md-12 col-sm-12 col-xs-12" id="phonenumber" name="userphone" type="text" placeholder="请输入手机号">
                      <input class="ltextbox col-md-7 col-sm-7 col-xs-7" id="correctcode" name="correctcode" type="text" placeholder="请输入验证码">
                      <button class="lbutton1 col-md-5 col-sm-5 col-xs-5" disabled="disabled" id="getcode" type="button">获取验证码</button>
                      <div id="login-sms-code-err" style="color:red;height:20px;width:100%;"></div>
                      <div class="col-md-2 col-sm-2 col-xs-2"></div>
                      <button class="lbutton2 col-md-8 col-sm-8 col-xs-8" disabled="disabled" id="loginsubmit" type="button" value="提交">提交</button>
                      <div class="col-md-2 col-sm-2 col-xs-2"></div>
                  </form>
              </div>
          </div>
<el-container>
  <el-header>Header</el-header>
  <el-main>Main</el-main>
</el-container>
      </div>

  </div>
  </div>
</template>

<script>
export default {
  name: 'login',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<style>
  .container {
    width: 30%;
    height: 40%;
  }
  .ltextbox {
      margin-top: 30px;
      height: 50px;
      outline: none;
  }

  .nav-tabs>li {
      height: 40px;
  }
  .lbutton1 {
    margin-top: 30px;
    height: 50px;
    border: 0;
    border-radius: 2px;
    background-color: rgb(43, 56, 90);
    color: #fff;
}

.lbutton1:hover {
    background-color: rgb(28, 134, 255);
}
.lbutton2 {
    margin-top: 30px;
    height: 50px;
    border: 0;
    border-radius: 10px;
    background-color: rgb(28, 134, 255);
    color: #fff;
}

.lbutton2:disabled {
    cursor: not-allowed;
    background-color: rgb(170, 170, 170);
    color: black;
}
.lbutton1:disabled {
    cursor: not-allowed;
    background-color: rgb(170, 170, 170);
    color: black;
    box-shadow: unset;
}

  .nav-tabs>li>a {
      height: 40px;
      margin-right: 2px;
      line-height: 1.42857143;
      border: 1px solid transparent;
      border-radius: 0;
  }

  .nav-tabs>li.active>a,
  .nav-tabs>li.active>a:focus,
  .nav-tabs>li.active>a:hover {
      height: 40px;
      color: #555;
      cursor: default;
      background-color: #fff;
      border-left: 1px solid #ddd;
      border-right: 1px solid #ddd;
  }
</style>
