<template>
  <div>
    <b-table :items="items" :fields="fields" striped hover responsive>
      <template v-slot:cell(reservation_id)="row">
        {{ rentedOrReserved(row.item) }}
      </template>
      <template v-slot:cell(rent_id)="row">
        {{ rentedOrReserved(row.item) }}
      </template>
      <template v-slot:cell(value)="row">
        {{ row.item.value | currency }}
      </template>
      <template v-slot:cell(actions)="row">
        <b-dropdown size="lg" variant="link" toggle-class="text-decoration-none" no-caret>
          <template v-slot:button-content>
            <b-icon-three-dots-vertical></b-icon-three-dots-vertical>
            <span class="sr-only"></span>
          </template>
          <b-dropdown-item v-if="row.item.rent_id === null" @click="rentItem(row.item)">
            Rent
          </b-dropdown-item>
          <b-dropdown-item v-if="row.item.rent_id !== null" @click="returnItem(row.item)">
            Return Item
          </b-dropdown-item>
          <b-dropdown-item
            v-if="row.item.reservation_id === null"
            @click="reserveItem(row.item)">
            Reserve
          </b-dropdown-item>
          <b-dropdown-item
            v-if="row.item.reservation_id !== null"
            @click="cancelReservation(row.item)">
            Cancel Reservation
          </b-dropdown-item>
        </b-dropdown>
      </template>
    </b-table>
    <ReserveItemModal :item="selectedItem" @reservedItem="$emit('updateItem')" />
  </div>
</template>

<script>
import { rentService, reservationService } from '@/services';
import { mapState } from 'vuex';
import ToastHelper from '@/helpers/toastHelper';
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
    ...mapState('user', {
      loggedUser: (state) => state.loggedUser,
    }),
    fields() {
      return [
        {
          key: 'name',
          label: 'Item name',
          sortable: true,
          sortDirection: 'desc',
        },
        { key: 'value', label: 'Value' },
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
    cancelReservation(item) {
      reservationService
        .cancelReservation(item.reservation_id)
        .then(() => {
          ToastHelper.successMessage('Reservation canceled');
          this.$emit('updateItem');
        })
        .catch(() => {
          ToastHelper.dangerMessage('Some error while canceling reservation');
        });
    },
    rentItem(item) {
      rentService
        .rentItem({
          userId: this.loggedUser.id,
          itemId: item.id,
        })
        .then(() => {
          ToastHelper.successMessage('Item rented');
          this.$emit('updateItem');
        })
        .catch(() => {
          ToastHelper.dangerMessage('Some error while renting item');
        });
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
    returnItem(item) {
      rentService
        .returnItem(item.rent_id)
        .then(() => {
          ToastHelper.successMessage('Returned Item');
          this.$emit('updateItem');
        })
        .catch(() => {
          ToastHelper.dangerMessage('Some error while returning item');
        });
    },
  },
};
</script>
