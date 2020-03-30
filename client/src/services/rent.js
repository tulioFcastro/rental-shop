import axiosLocal from './axios';

export default {
  rentItem: ({ userId, itemId }) => axiosLocal.post('rent', { user_id: userId, item_id: itemId }),
  returnItem: (rentId) => axiosLocal.delete(`rent/${rentId}`),
};
