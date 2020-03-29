<template>
  <b-modal id="create-item-type-modal" title="Create Item Type" centered hide-footer>
    <b-form @submit="onSubmit" class="d-flex flex-column w-100 h-auto">
      <b-input-group prepend="Name" class="mt-3">
        <b-form-input v-model="form.name" />
      </b-input-group>
      <b-button block class="mt-3" variant="primary" type="submit" :disabled="$v.form.$invalid">
        Confirm
      </b-button>
    </b-form>
  </b-modal>
</template>

<script>
import { required } from 'vuelidate/lib/validators';
import { mapActions } from 'vuex';
import ToastHelper from '@/helpers/toastHelper';

export default {
  data() {
    return {
      form: {
        name: null,
      },
    };
  },
  validations: {
    form: {
      name: {
        required,
      },
    },
  },
  methods: {
    ...mapActions('itemType', ['createItemType']),
    onSubmit(evt) {
      evt.preventDefault();
      this.createItemType({ name: this.form.name })
        .then(() => {
          ToastHelper.successMessage('Item Type Created');
          this.$bvModal.hide('create-item-type-modal');
        })
        .catch(() => {
          ToastHelper.dangerMessage('Some error while creating item type');
        });
    },
  },
};
</script>

<style></style>
