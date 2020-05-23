import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import store from './store'
import 'bootstrap'; 

//Global CSS imports
import 'bootstrap/dist/css/bootstrap.min.css';

Vue.config.productionTip = false

new Vue({
  store,
  render: function (h) { return h(App) }
}).$mount('#app')
