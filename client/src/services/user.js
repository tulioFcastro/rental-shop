import axiosLocal from './axios';

export default {
  signUp({ email, name }) {
    return axiosLocal.post('user', {
      email,
      name,
    });
  },
  update({ userId, name }) {
    return axiosLocal.put(`user/${userId}`, {
      name,
    });
  },
};
