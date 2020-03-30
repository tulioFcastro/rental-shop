<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand>Rental Shop - You're welcome {{ name }}</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item-dropdown right>
            <template v-slot:button-content>
              <em>Options</em>
            </template>
            <b-dropdown-item @click.prevent="$bvModal.show('profile-modal')">
              Profile
            </b-dropdown-item>
            <b-dropdown-item href="Logout">Logout</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <router-view class="container" />
    <ProfileModal />
  </div>
</template>
<script>
import { mapGetters } from 'vuex';
import ProfileModal from './ProfileModal/index.vue';

export default {
  components: {
    ProfileModal,
  },
  computed: {
    ...mapGetters('user', ['name']),
  },
};
</script>
