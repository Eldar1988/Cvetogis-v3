<template>
  <q-btn-dropdown
    :label="label"
    dropdown-icon="keyboard_arrow_down"
    flat rounded dense
    class="font-14 text-weight-bold" menu-anchor="bottom right"
    style="margin-top: -6px; margin-left: -5px"
  >
    <q-list class="rounded-10">
      <q-item
        v-for="item in items" :key="item.id"
        clickable v-close-popup
        class="font-16 text-secondary text-weight-medium"
      >
        <q-item-section>
          <router-link :to="`/shop?${filterField}=${item.title}`">
            <q-item-label>{{ item.title }}</q-item-label>
          </router-link>
        </q-item-section>
      </q-item>
    </q-list>
  </q-btn-dropdown>
</template>

<script>
export default {
  name: "gisNavDropdown",
  props: {
    label: {
      type: String,
      default: ''
    },
    items: {
      type: Array,
      default: null
    },
    filterField: {
      type: String,
      default: ''
    }
  }
}
</script>

<style scoped>

</style>
