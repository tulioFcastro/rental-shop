import axiosLocal from './axios';

export default {
  login({ email }) {
    console.log(email);
    return axiosLocal.post('login', {
      email,
    });
  },
};
