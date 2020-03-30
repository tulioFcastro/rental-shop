import axios from 'axios';

const axiosLocal = axios.create({
  baseURL: process.env.VUE_APP_BASE_URL,
});

axiosLocal.interceptors.request.use(
  (config) => {
    /* eslint no-param-reassign: "error" */
    config.headers['Content-Type'] = 'application/json';

    return config;
  },
  (error) => Promise.reject(error),
);

axiosLocal.interceptors.response.use(
  (response) => response,
  (error) => Promise.reject(error),
);

export default axiosLocal;
