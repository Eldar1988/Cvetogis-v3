<template>
<div class="products-slider">
  <splide :options="options" :slides="products">
    <splide-slide v-for="product in products" :key="product.id" style="padding: 5px">
      <gis-product-card-v1 :product="product"/>
    </splide-slide>
  </splide>
</div>
</template>

<script>
import { Splide, SplideSlide } from '../../../../../node_modules/@splidejs/vue-splide';
import '../../../../../node_modules/@splidejs/splide/dist/css/themes/splide-sea-green.min.css';
import GisProductCardV1 from "components/shop/product/gisProductCard-v1";

export default {
  name: "gisProductsSlider",
  components: {GisProductCardV1, Splide, SplideSlide},
  props: {
    products: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      options: {
        type: 'loop',
        gap: 10,
        perPage: 4,
        arrows: false,
        pagination: true,
        breakpoints: {
          1650: {
            perPage: 4
          },
          992: {
            perPage: 2.7,
            pagination: false
          },
          650: {
            perPage: 1.3,
            pagination: false
          }
        }
      }
    }
  },
}
</script>

<style lang="sass">
@media screen and (max-width: 800px)
  .products-slider
    margin-left: 15px !important
</style>
