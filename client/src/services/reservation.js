import axiosLocal from './axios';

export default {
  cancelReservation(id) {
    return axiosLocal.delete(`reservation/${id}`);
  },
  reserve({ userId, itemId, rentDate }) {
    return axiosLocal.post('reservation', {
      user_id: userId,
      item_id: itemId,
      rent_date: rentDate,
    });
  },
};
