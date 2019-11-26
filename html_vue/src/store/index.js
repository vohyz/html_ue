import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  // 设置属性
  state: {
    isLogin: false,
    user: {}
  },

  // 获取属性的状态
  getters: {
    // 获取登录状态
    isLogin: state => state.isLogin
  },

  // 设置属性状态
  mutations: {
    // 保存登录状态
    userStatus (state, flag) {
      state.isLogin = flag
    },
    logout (state) {
      localStorage.setItem('Flag', 'not')
      state.isLogin = false
    }
  },

  // 应用mutations
  actions: {
    // 获取登录状态
    userLogin ({commit}, flag) {
      commit('userStatus', flag)
    },
    userLogout ({commit}) {
      commit('logout')
    }
  }
})

export default store
