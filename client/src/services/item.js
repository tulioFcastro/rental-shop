import axiosLocal from './axios';

export default {
  create({ name, itemTypeId, value }) {
    return axiosLocal.post('item', { name, item_type_id: itemTypeId, value });
  },
  loadItems: () => axiosLocal.get('item'),
};
