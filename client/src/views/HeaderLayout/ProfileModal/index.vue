<template>
  <b-modal id="profile-modal" title="User profile" hide-footer>
    <p class="my-4">Hello <b>{{ name }}</b>!</p>
    <Edit />
  </b-modal>
</template>

<script>
import { mapGetters } from 'vuex';
import Edit from './Edit.vue';

export default {
  components: {
    Edit,
  },
  computed: {
    ...mapGetters('user', ['name']),
  },
};
</script>
<style lang="scss" scoped>
.cursor {
  cursor: pointer;
}
</style>
