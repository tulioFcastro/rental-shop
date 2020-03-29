export default {
  name: (state) => (state.loggedUser ? state.loggedUser.name : ''),
  isLoggedUser: (state) => (state.loggedUser ? state.loggedUser.id !== null : false),
};
