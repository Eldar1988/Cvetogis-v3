<template>
  <div
    v-if="$q.platform.is.mobile"
    class="hide-on-desktop"
  >
    <gis-wish-list-icon />
    <gis-cart-icon />
  <div class="bottom-bar text-uppercase text-weight-bold">
    <div>
      <a href="#" class="text-white">VK</a>
    </div>
    <div>
      <a href="#" class="text-white">Instagram</a>
    </div>
    <div>
      <q-btn
        icon="mdi-whatsapp"
        color="white"
        text-color="primary"
        round
        size="sm"
        unelevated
        type="a"
        href="https://wa.me/77079514936"
      />
    </div>
  </div>
  </div>
</template>

<script>
import GisCartIcon from "components/shop/cart/gisCartIcon";
import GisWishListIcon from "components/shop/wishList/gisWishListIcon";
export default {
  name: "gisBottomBar",
  components: {GisWishListIcon, GisCartIcon}
}
</script>

<style lang="sass">
.bottom-bar
  position: fixed
  bottom: 0
  left: 0
  right: 0
  height: 40px
  background: $primary
  display: flex
  justify-content: space-between
  color: #ffffff
  align-items: center
  padding: 0 20px
  z-index: 10
</style>
