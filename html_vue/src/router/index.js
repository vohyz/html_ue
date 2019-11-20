import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import login from '@/components/login'
import usercenter from '@/components/usercenter'
import workboard from '@/components/workboard'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/usercenter',
      name: 'usercenter',
      component: usercenter,
      children: [
        {
          path: '/usercenter/workboard',
          name: 'workboard',
          component: workboard
        }
      ]
    }
  ],
  mode: 'history'
})
