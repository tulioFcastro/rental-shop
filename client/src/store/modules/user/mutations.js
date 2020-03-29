export default {
  setLoggedUser(state, user) {
    state.loggedUser = { ...user };
  },
};
