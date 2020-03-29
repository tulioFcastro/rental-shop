import store from '@/store';
import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: () => import('@/views/HeaderLayout'),
    redirect: { name: 'Items' },
    meta: { requiresAuth: true },
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
  {
    path: '/logout',
    name: 'Logout',
    beforeEnter: (to, from, next) => {
      store.dispatch('user/logout');
      next({ name: 'Login' });
    },
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((route) => route.meta.requiresAuth)) {
    if (store.getters['user/isLoggedUser']) {
      next();
    } else {
      next({ name: 'Login', query: { name: to.name }, params: to.params });
    }
  } else {
    next();
  }
});

export default router;
