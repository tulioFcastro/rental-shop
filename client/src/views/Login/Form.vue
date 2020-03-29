<template>
  <b-form @submit="onSubmit" class="d-flex flex-column w-100 h-auto">
    <h5>Login</h5>
    <b-input-group prepend="Email" class="mt-3">
      <b-form-input></b-form-input>
    </b-input-group>
    <b-button block class="auth-form-button mt-3" variant="primary" type="submit">
      Login
    </b-button>
  </b-form>
</template>

<script>
export default {
  data() {
    return {
      form: {
        name: null,
      },
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      // console.log('onSubmit', this.form.name);
    },
  },
};
</script>

<style lang="scss" scoped></style>
