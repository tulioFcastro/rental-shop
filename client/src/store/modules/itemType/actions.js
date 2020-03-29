import { itemTypeService } from '@/services';

export default {
  createItemType({ commit }, { name }) {
    return itemTypeService.create({ name }).then(({ data }) => {
      commit('addItemTypesLoaded', data);

      return data;
    });
  },
  loadItemTypes({ commit }) {
    return itemTypeService.load().then(({ data }) => {
      commit('setItemTypesLoaded', data);

      return data;
    });
  },
};
