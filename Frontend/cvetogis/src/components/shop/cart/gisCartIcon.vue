<template>
  <div class="header-icon cart-icon">
    <router-link to="/cart">
    <img src="../../../assets/icons/basket.svg" alt="cart icon" class="bg-secondary shop-icon q-ml-md" >
    <div
      v-if="cartLen > 0"
      class="badge text-accent text-weight-medium"
    >
      {{ cartLen }}
    </div>
      </router-link>
  </div>
</template>

<script>
export default {
name: "gisCartIcon",
  data() {
    return {
      cartLen: 0
    }
  },
  created() {
    this.getCartLen()
    this.$root.$on('updateCart', () => this.getCartLen())
  },
  methods: {
    getCartLen() {
      this.cartLen = JSON.parse(localStorage.cart).length
    }
  }
}
</script>

<style lang="sass">
@media screen and (max-width: 1100px)
  .cart-icon
    position: fixed
    bottom: 50px
    right: 20px
    transform: scale(1.4)
    z-index: 99999

    img
      box-shadow: 3px 3px 7px 0 rgba(0,0,0,.2)
</style>
