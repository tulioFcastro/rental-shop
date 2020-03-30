import axiosLocal from './axios';

export default {
  reserve({ user_id, item_id, rent_date }) {
    return axiosLocal.post('reservation', { user_id, item_id, rent_date });
  },
};