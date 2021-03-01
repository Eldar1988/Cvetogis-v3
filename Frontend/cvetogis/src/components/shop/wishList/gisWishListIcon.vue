<template>
  <div class="header-icon wish-icon">
    <router-link to="/wishlist">
    <img src="../../../assets/icons/wishlist.svg" alt="wishlist icon" class="bg-secondary shop-icon">
    <div
      v-if="wishListLen > 0"
      class="badge text-accent text-weight-medium"
    >
      {{ wishListLen }}
    </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "gisWishListIcon",
  data() {
    return {
      wishListLen: 0
    }
  },
  created() {
    this.getWishListLen()
    this.$root.$on('updateWishList', () => this.getWishListLen())
  },
  methods: {
    getWishListLen() {
      this.wishListLen = JSON.parse(localStorage.wishList).length
    }
  }
}
</script>

<style lang="sass">
@media screen and (max-width: 992px)
  .wish-icon
    position: fixed
    bottom: 110px
    right: 16px
    transform: scale(1.2)
    z-index: 99999

    img
      box-shadow: 3px 3px 7px 0 rgba(0,0,0,.2)
</style>
