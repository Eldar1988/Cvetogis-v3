<template>
<q-btn
  label="В корзину"
  flat dense no-caps
  color="accent"
  class="font-16 letter-1 text-weight-regular"
  @click="addToCard(product)"
/>
</template>

<script>
import notifier from "src/service/notifier";

export default {
  name: "gisAddToCardButton-v1",
  props: {
    product: {
      type: Object,
      default: null
    }
  },
  methods: {
    addToCard(product) {
      let cart = JSON.parse(localStorage.cart)
      let productInCart = false
      cart.forEach((item) => {
        if (item.id === product.id) {
          productInCart = true
          notifier(`Этот товар уже есть в вашей корзине`)
        }
      })
      if(!productInCart) {
        cart.push(product)
        notifier(`Товар '${product.title}' добавлен в корзину`, 'primary')
      }
      localStorage.setItem('cart', JSON.stringify(cart))
      this.$root.$emit('updateCart')
    }
  }
}
</script>

<style scoped>

</style>
