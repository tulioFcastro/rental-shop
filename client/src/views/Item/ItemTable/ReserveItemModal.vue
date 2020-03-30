<template>
  <b-modal id="reserve-item-modal" title="Create Item" size="md" centered hide-footer>
    <b-form @submit="onSubmit" class="d-flex flex-column w-100 h-auto">
      <h5 class="mb-2">Select datetime to reserve item</h5>
      <b-form-timepicker v-model="form.time" />
      <b-form-datepicker class="mt-2 mb-5" v-model="form.date" />
      <b-button block variant="primary" type="submit" :disabled="$v.form.$invalid">
        Confirm
      </b-button>
    </b-form>
  </b-modal>
</template>

<script>
import { required } from 'vuelidate/lib/validators';
import { reservationService } from '@/services';
import { mapState } from 'vuex';
import moment from 'moment-timezone';
import ToastHelper from '@/helpers/toastHelper';

export default {
  props: {
    item: {
      type: Object,
      default: () => ({}),
    },
  },
  computed: {
    ...mapState('user', {
      loggedUser: (state) => state.loggedUser,
    }),
  },
  data() {
    return {
      form: {
        date: null,
        time: null,
      },
    };
  },
  validations: {
    form: {
      date: {
        required,
      },
      time: {
        required,
      },
    },
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      reservationService
        .reserve({
          user_id: this.loggedUser.id,
          item_id: this.item.id,
          rent_date: moment(`${this.form.date} ${this.form.time}`).format(),
        })
        .then(() => {
          ToastHelper.successMessage('Item reserved');
          this.$emit('reservedItem');
          this.$bvModal.hide('reserve-item-modal');
        })
        .catch(() => {
          ToastHelper.dangerMessage('Some error while reserving item');
        });
    },
  },
};
</script>

<style></style>
