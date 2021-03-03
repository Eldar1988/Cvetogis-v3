<template>
  <q-card
    class="shadow-0 rounded-10 product-card-v1"
  >
    <router-link :to="`/product/${product.slug}`">
      <q-img
        :src="product.miniature"
        class="product-card-v1-img"
      >
        <template v-slot:loading>
          <q-skeleton class="full-width product-card-v1-img" square/>
        </template>
      </q-img>
      <p class="font-18 q-pa-md text-secondary text-weight-medium ellipsis">{{ product.title }}</p>
    </router-link>

    <div class="product-meta-grid-v1 ">
        <div class="price-v1 q-pa-sm text-center ">
          <small v-if="product.old_price" class="font-14 text-grey-5 line-through">{{ product.old_price }}</small>
          <p class="font-24 text-weight-regular" :style="product.old_price ? `margin-top: -5px` : ``">{{ product.price }}<small> тг</small> </p>
        </div>
      <div class="price-v1 q-pa-sm border-left text-center">
        <gis-add-to-card-button-v1 :product="product"/>
      </div>
      <div class="q-pa-sm wish-v1 text-center border-left">
        <gis-add-to-wish-list-v-1 :product="product"/>
      </div>

      </div>
  </q-card>
</template>

<script>
import GisAddToCardButtonV1 from "components/shop/cart/gisAddToCardButton-v1";
import GisAddToWishListV1 from "components/shop/wishList/gisAddToWishListV-1";
export default {
  name: "gisProductCard-v1",
  components: {GisAddToWishListV1, GisAddToCardButtonV1},
  props: {
    product: {
      type: Object,
      default: null
    }
  }
}
</script>

<style lang="sass">
.product-card-v1-img
  height: 260px

.product-meta-grid-v1
  display: grid
  grid-template-columns: 2fr 2fr 1fr
  border-top: 1px solid $grey-3

</style>
