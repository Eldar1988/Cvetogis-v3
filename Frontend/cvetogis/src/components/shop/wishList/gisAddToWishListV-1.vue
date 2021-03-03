<template>
  <q-btn
    :icon="productInWishList ? 'favorite' : 'favorite_border'"
    round flat
    :text-color="productInWishList ? `accent` : `dark`"
    unelevated dense
    :color="productInWishList ? `accent` : `white`"
    @click="addToWishList(product)"
  />
</template>

<script>
import notifier from "src/service/notifier";
export default {
  name: "gisAddToWishListV-1",
  props: {
    product: {
      type: Object,
      default: null
    }
  },
  mounted() {
    this.checkList()
  },
  data() {
    return {
      productInWishList: false
    }
  },
  methods: {
    addToWishList(product) {
      let wishList = JSON.parse(localStorage.wishList)
      let productInList = false

      wishList.forEach((item) => {
        if (item.id === product.id) {
          productInList = true
          wishList.splice(wishList.indexOf(item), 1)
          notifier(`Товар ${product.title.toLowerCase()} удален из избранного`)
          this.productInWishList = false
        }
      })
      if (!productInList) {
        wishList.push(product)
        notifier(`Товар ${product.title.toLowerCase()} добавлен в избранное`, 'primary')
        this.productInWishList = true
      }
      localStorage.setItem('wishList', JSON.stringify(wishList))
      this.$root.$emit('updateWishList')
    },
    checkList() {
      if (localStorage.getItem('wishList') !== null) {
        let localList = JSON.parse(localStorage.wishList)
        localList.forEach((item) => {
          if (this.product.id === item.id) {
            this.productInWishList = true
          }
        })
      }
    }
  }
}
</script>

<style scoped>

</style>
