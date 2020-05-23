import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    msg: ""
  },
  mutations: {
    msg(state, msg) {
      state.msg = msg;
    },
  },
  actions: {
  },
  modules: {
  },
  getters: {
    msg: (state) => {
      return state.msg;
    },
  }
})
