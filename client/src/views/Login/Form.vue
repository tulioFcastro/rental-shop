<template>
  <b-form @submit="onSubmit" class="d-flex flex-column w-100 h-auto">
    <h5>Login</h5>
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
        email: null,
      },
    };
  },
  validations: {
    form: {
      email: {
        required,
        email,
      },
    },
  },
  methods: {
    ...mapActions('user', ['login']),
    onSubmit(evt) {
      evt.preventDefault();
      this.login({ email: this.form.email })
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

<style lang="scss" scoped></style>
