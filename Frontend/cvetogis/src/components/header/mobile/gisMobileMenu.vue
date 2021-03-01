<template>
  <div class="text-right">
    <img
      src="../../../assets/icons/menu.svg"
      class="mobile-menu-icon"
      @click="dialog = true"
    />

    <q-dialog
      position="right"
      v-model="dialog"
    >
      <q-slide-transition appear>
        <q-card
          class="shadow-0 rounded-10 bg-white mobile-menu-dialog"
        >
          <div>
            <q-btn
              icon="east"
              flat
              style="position: absolute; right: 0"
              v-close-popup
            />
          </div>
          <gis-mobile-menu-content/>
        </q-card>
      </q-slide-transition>
    </q-dialog>
  </div>
</template>

<script>
import GisMobileMenuContent from "components/header/mobile/gisMobileMenuContent";

export default {
  name: "gisMobileMenu",
  components: {GisMobileMenuContent},
  data() {
    return {
      dialog: false
    }
  },
}
</script>

<style lang="sass">
.mobile-menu-icon
  width: 40px

.mobile-menu-dialog
  position: fixed
  min-width: 80%
  max-width: 80%
  right: 20px
  top: 20px
  bottom: 20px
  transition: 1s all
</style>
