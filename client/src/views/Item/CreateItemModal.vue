<template>
  <b-modal id="create-item-modal" title="Create Item" centered hide-footer>
    <b-form @submit="onSubmit" class="d-flex flex-column w-100 h-auto">
      <h5>Select Item Type</h5>
      <b-form-select v-model="form.itemTypeSelected" :options="itemTypes"></b-form-select>
      <b-input-group prepend="Name" class="my-2">
        <b-form-input v-model="form.name" />
      </b-input-group>
      <b-input-group prepend="$" append=".00" class="my-2">
        <b-form-input type="number" v-model="form.value" />
      </b-input-group>
      <b-button block class="mt-3" variant="primary" type="submit" :disabled="$v.form.$invalid">
        Confirm
      </b-button>
    </b-form>
  </b-modal>
</template>

<script>
import { required, numeric } from 'vuelidate/lib/validators';
import { mapState } from 'vuex';
import ToastHelper from '@/helpers/toastHelper';
import { itemService } from '@/services';

export default {
  computed: {
    ...mapState('itemType', {
      itemTypes: (state) => state.itemTypesLoaded.map((itl) => ({ value: itl.id, text: itl.name })),
    }),
  },
  data() {
    return {
      form: {
        name: null,
        itemTypeSelected: null,
        value: 0,
      },
    };
  },
  validations: {
    form: {
      name: {
        required,
      },
      itemTypeSelected: {
        required,
      },
      value: {
        numeric,
      },
    },
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      itemService
        .create({
          name: this.form.name,
          item_type_id: this.form.itemTypeSelected,
          value: this.form.value,
        })
        .then(() => {
          ToastHelper.successMessage('Item Created');
          this.$bvModal.hide('create-item-modal', true);
          this.$emit('createdItem');
        })
        .catch(() => {
          ToastHelper.dangerMessage('Some error while creating item type');
        });
    },
  },
};
</script>

<style></style>
