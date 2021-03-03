<template>
  <q-page>
    <gis-first-screen-wrapper/>
    <section class="container mt-60">
      <gis-benefits/>
    </section>
    <section class="container mt-50">
      <gis-section-title title="Доставим в течение часа" class="text-center"/>
      <gis-products-slider :products="futureProducts" class="mt-50"/>
    </section>
    <section class="container mt-50">
      <gis-section-title title="Повод" class="text-center"/>
    </section>
  </q-page>
</template>

<script>
import GisFirstScreenWrapper from "components/home/gisFirstScreenWrapper";
import GisBenefits from "components/home/gisBenefits";
import GisSectionTitle from "components/service/gisSectionTitle";
import GisProductsSlider from "components/shop/product/gisProductsSlider";

export default {
  name: 'PageIndex',
  components: {GisProductsSlider, GisSectionTitle, GisBenefits, GisFirstScreenWrapper},
  async created() {
    await this.$store.dispatch('fetchHomeProducts', localStorage.getItem('city'))
    await this.getFutureProducts()
    setTimeout(() => {

    }, 2000)
  },
  data() {
    return {
      futureProducts: []
    }
  },
  methods: {
    getFutureProducts() {
      this.futureProducts = this.$store.getters.getHomeProducts.futureProducts
    }
  }
}
</script>


