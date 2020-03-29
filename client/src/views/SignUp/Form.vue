<template>
  <b-form @submit="onSubmit" class="d-flex flex-column w-100 h-auto">
    <h5>Sign-up</h5>
    <b-input-group prepend="Name" class="mt-3">
      <b-form-input v-model="form.name" />
    </b-input-group>
    <b-input-group prepend="Email" class="mt-3">
      <b-form-input v-model="form.email" />
    </b-input-group>
    <!-- eslint-disable-next-line -->
    <b-button block class="mt-3" variant="primary" type="submit" :disabled="$v.form.$invalid">
      Confirm
    </b-button>
  </b-form>
</template>

<script>
import ToastHelper from '@/helpers/toastHelper';
import { required, email } from 'vuelidate/lib/validators';
import { mapActions } from 'vuex';

export default {
  data() {
    return {
      form: {
        name: null,
        email: null,
      },
    };
  },
  validations: {
    form: {
      name: {
        required,
      },
      email: {
        required,
        email,
      },
    },
  },
  methods: {
    ...mapActions('user', ['signUp']),
    onSubmit(evt) {
      evt.preventDefault();
      this.signUp({ name: this.form.name, email: this.form.email })
        .then(() => {
          ToastHelper.successMessage('User successfully registered');
          this.$router.push({ name: 'Dashboard' });
        })
        .catch(() => {
          ToastHelper.dangerMessage('Email already in use');
        });
    },
  },
};
</script>
