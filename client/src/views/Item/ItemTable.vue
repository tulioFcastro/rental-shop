<template>
  <b-table :items="items" :fields="fields" striped hover responsive>
    <template v-slot:cell(actions)="row">
      <b-dropdown size="lg" variant="link" toggle-class="text-decoration-none" no-caret>
        <template v-slot:button-content>
          <b-icon-three-dots-vertical></b-icon-three-dots-vertical>
          <span class="sr-only"></span>
        </template>
        <b-dropdown-item @click="info(row.item, row.index, $event.target)">Rent</b-dropdown-item>
        <b-dropdown-item @click="info(row.item, row.index, $event.target)">Reserve</b-dropdown-item>
      </b-dropdown>
    </template>
  </b-table>
</template>

<script>
export default {
  props: {
    items: {
      type: Array,
      default: () => [],
    },
  },
  computed: {
    fields() {
      return [
        {
          key: 'name',
          label: 'Item name',
          sortable: true,
          sortDirection: 'desc',
        },
        { key: 'actions', label: 'Actions' },
      ];
    },
  },
  methods: {
    info(item, index, button) {
      console.log(item, index, button);
    },
  },
};
</script>

<style></style>
