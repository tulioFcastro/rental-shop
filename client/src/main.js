import ToastHelper from '@/helpers/toastHelper';
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue';
import 'bootstrap-vue/dist/bootstrap-vue-icons.min.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import 'bootstrap/dist/css/bootstrap.css';
import Vue from 'vue';
import Vuelidate from 'vuelidate';
import App from './App.vue';
import './assets/global.scss';
import router from './router';
import store from './store';

Vue.use(BootstrapVueIcons);
Vue.use(BootstrapVue);
Vue.use(Vuelidate);
Vue.config.productionTip = false;

const comp = new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');

ToastHelper.configure(comp);
