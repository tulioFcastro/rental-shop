import Vue from 'vue';
import Vuex from 'vuex';
import VuexPersist from 'vuex-persist';
import itemType from './modules/itemType';
import user from './modules/user';

Vue.use(Vuex);
const mutationsToCheck = ['user/setLoggedUser', 'itemType/setItemTypesLoaded'];

const vuexPersist = new VuexPersist({
  key: process.env.VUE_APP_STORED_DATA,
  storage: localStorage,
  reducer: (state) => ({
    itemType: {
      itemTypesLoaded: state.itemType.itemTypesLoaded,
    },
    user: {
      loggedUser: state.user.loggedUser,
    },
  }),
  filter: (mutation) => mutationsToCheck.includes(mutation.type),
});

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    itemType,
    user,
  },
  plugins: [vuexPersist.plugin],
});
