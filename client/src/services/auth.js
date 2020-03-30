import axiosLocal from './axios';

export default {
  login: ({ email }) => axiosLocal.post('login', { email }),
};
