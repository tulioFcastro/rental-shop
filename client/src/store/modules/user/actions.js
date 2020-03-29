import { userService, authService } from '@/services';

export default {
  login({ commit }, { email }) {
    return authService.login({ email }).then(({ data }) => {
      commit('setLoggedUser', data);

      return data;
    });
  },
  logout({ commit }) {
    commit('setLoggedUser', null);
    localStorage.removeItem(process.env.VUE_APP_STORED_DATA);
  },
  signUp({ commit }, { name, email }) {
    return userService.signUp({ name, email }).then(({ data }) => {
      commit('setLoggedUser', data);

      return data;
    });
  },
};
