<template>
  <div class="p-2 p-sm-4 p-md-5">
    <div class="w-100 d-flex justify-content-between pb-4">
      <b-button variant="primary" v-b-modal.create-item-type-modal>Add Item Type</b-button>
      <b-button variant="primary" v-b-modal.create-item-modal>Add Item</b-button>
    </div>
    <ItemTable :items="items" @reservedItem="loadItems" />
    <CreateItemTypeModal />
    <CreateItemModal @createdItem="loadItems" />
  </div>
</template>

<script>
import { itemService } from '@/services';
import { mapActions } from 'vuex';
import CreateItemTypeModal from './CreateItemTypeModal.vue';
import CreateItemModal from './CreateItemModal.vue';
import ItemTable from './ItemTable/index.vue';

export default {
  components: {
    CreateItemModal,
    CreateItemTypeModal,
    ItemTable,
  },
  data() {
    return {
      items: [],
    };
  },
  methods: {
    ...mapActions('itemType', ['loadItemTypes']),
    loadItems() {
      itemService
        .loadItems()
        .then(({ data }) => {
          this.items = data;
        })
        .catch((err) => console.log(err));
    },
  },
  created() {
    this.loadItems();
    this.loadItemTypes().then();
  },
};
</script>
