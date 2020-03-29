import axiosLocal from './axios';

export default {
  signUp({ email, name }) {
    return axiosLocal.post('user', {
      email,
      name,
    });
  },
};
