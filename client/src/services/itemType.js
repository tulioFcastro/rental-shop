import axiosLocal from './axios';

export default {
  create: ({ name }) => axiosLocal.post('item_type', { name }),
  load: () => axiosLocal.get('item_type'),
};
