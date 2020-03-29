export default {
  name: (state) => (state.loggedUser ? state.loggedUser.name : ''),
};
