import { userService } from '@/services';

export default {
  signUp({ commit }, { name, email }) {
    return userService.signUp({ name, email }).then(({ data }) => {
      commit('setLoggedUser', data);

      return data;
    });
  },
};
