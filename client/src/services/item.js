import axiosLocal from './axios';

export default {
  create({ name, item_type_id }) {
    return axiosLocal.post('item', { name, item_type_id });
  },
  loadItems: () => axiosLocal.get('item'),
};
