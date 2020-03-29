<template>
  <div
    class="login-container
              p-3 p-sm-4 p-md-5 my-0
              mx-auto
              d-flex flex-column justify-content-center"
  >
    <div class="d-flex flex-column justify-content-center w-100">
      <Form />
    </div>
    <router-link class="font-weight-bold" :to="{ name: 'Login' }">
      Go to Login
    </router-link>
  </div>
</template>

<script>
import Form from './Form.vue';

export default {
  components: {
    Form,
  },
};
</script>

<style lang="scss" scoped>
.login-container {
  min-height: 100vh;
}
@media screen and (min-width: 576px) {
  .login-container {
    max-width: 50%;
  }
}
</style>
