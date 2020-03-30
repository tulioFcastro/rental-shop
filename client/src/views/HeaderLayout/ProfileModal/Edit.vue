<template>
  <b-form @submit="onSubmit" class="d-flex flex-column w-100 h-auto">
    <h5>If you want edit your profile</h5>
    <b-input-group prepend="Name">
      <b-form-input v-model="form.name" />
    </b-input-group>
    <b-input-group prepend="Email" class="mt-3 mb-5">
      <b-form-input v-model="form.email" disabled />
    </b-input-group>
    <b-button block variant="primary" type="submit" :disabled="$v.form.$invalid">
      Confirm
    </b-button>
  </b-form>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import ToastHelper from '@/helpers/toastHelper';
import { required, email } from 'vuelidate/lib/validators';

export default {
  computed: {
    ...mapState('user', {
      loggedUser: (state) => state.loggedUser,
    }),
  },
  data() {
    return {
      form: {
        email: null,
        name: null,
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
    ...mapActions('user', ['updateUser']),
    onSubmit(evt) {
      evt.preventDefault();
      this.updateUser({ name: this.form.name, email: this.form.email, userId: this.loggedUser.id })
        .then(() => {
          ToastHelper.successMessage('User successfully registered');
        })
        .catch(() => {
          ToastHelper.dangerMessage('Email already in use');
        });
    },
  },
  mounted() {
    this.form.email = this.loggedUser.email;
    this.form.name = this.loggedUser.name;
  },
};
</script>

<style></style>
