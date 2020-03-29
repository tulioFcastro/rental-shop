export default {
  addItemTypesLoaded(state, itemType) {
    state.itemTypesLoaded.push(itemType);
  },
  setItemTypesLoaded(state, itemTypesLoaded) {
    state.itemTypesLoaded = itemTypesLoaded;
  },
};
