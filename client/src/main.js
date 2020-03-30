import ToastHelper from '@/helpers/toastHelper';
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue';
import 'bootstrap-vue/dist/bootstrap-vue-icons.min.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import 'bootstrap/dist/css/bootstrap.css';
import moment from 'moment-timezone';
import Vue from 'vue';
import VueCurrencyFilter from 'vue-currency-filter';
import VueMoment from 'vue-moment';
import Vuelidate from 'vuelidate';
import App from './App.vue';
import './assets/global.scss';
import router from './router';
import store from './store';

Vue.use(BootstrapVueIcons);
Vue.use(BootstrapVue);
Vue.use(Vuelidate);
moment.locale('pt-BR');
Vue.use(VueMoment, {
  moment,
});
Vue.use(VueCurrencyFilter, {
  symbol: '$',
  thousandsSeparator: '.',
  fractionCount: 2,
  fractionSeparator: ',',
  symbolPosition: 'front',
  symbolSpacing: true,
});
Vue.config.productionTip = false;

const comp = new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');

ToastHelper.configure(comp);
