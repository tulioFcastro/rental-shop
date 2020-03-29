import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: () => import('@/views/HeaderLayout'),
    redirect: { name: 'Items' },
    children: [
      {
        path: '/',
        name: 'Items',
        component: () => import('@/views/Item'),
      },
    ],
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/Login'),
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: () => import('@/views/SignUp'),
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
