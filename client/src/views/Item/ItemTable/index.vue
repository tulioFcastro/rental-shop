<template>
  <div>
    <b-table :items="items" :fields="fields" striped hover responsive>
      <template v-slot:cell(reservation_id)="row">
        {{ rentedOrReserved(row.item) }}
      </template>
      <template v-slot:cell(rent_id)="row">
        {{ rentedOrReserved(row.item) }}
      </template>
      <template v-slot:cell(actions)="row">
        <b-dropdown size="lg" variant="link" toggle-class="text-decoration-none" no-caret>
          <template v-slot:button-content>
            <b-icon-three-dots-vertical></b-icon-three-dots-vertical>
            <span class="sr-only"></span>
          </template>
          <b-dropdown-item @click="rentItem(row.item)">Rent</b-dropdown-item>
          <b-dropdown-item @click="reserveItem(row.item)">Reserve</b-dropdown-item>
        </b-dropdown>
      </template>
    </b-table>
    <ReserveItemModal :item="selectedItem" @reservedItem="$emit('reservedItem')" />
  </div>
</template>

<script>
import ReserveItemModal from './ReserveItemModal.vue';

export default {
  components: {
    ReserveItemModal,
  },
  props: {
    items: {
      type: Array,
      default: () => [],
    },
  },
  computed: {
    fields() {
      return [
        {
          key: 'name',
          label: 'Item name',
          sortable: true,
          sortDirection: 'desc',
        },
        { key: 'reservation_id', label: 'Reserved' },
        { key: 'rent_id', label: 'Rented' },
        { key: 'actions', label: 'Actions' },
      ];
    },
  },
  data() {
    return {
      selectedItem: null,
    };
  },
  methods: {
    rentItem(item) {
      console.log(item);
    },
    reserveItem(item) {
      this.selectedItem = item;
      this.$bvModal.show('reserve-item-modal');
    },
    rentedOrReserved(item) {
      if (item.rent_id !== null) return 'Rented';
      if (item.reservation_id !== null) return 'Reserved';

      return 'Free';
    },
  },
};
</script>
