<template>
    <div
      class="header-wrapper header-container"
    >
      <div class="logo-cities-grid">
        <gis-logo/>
        <div class="flex">
          <gis-cities/>
          <gis-courses/>
        </div>
      </div>
      <div class="flex">
        <gis-delivery-time/>
        <gis-header-contacts class="q-ml-xl"/>
      </div>
      <div class="flex justify-end">
        <gis-wish-list-icon/>
        <gis-cart-icon/>
      </div>
    </div>
</template>

<script>
import GisLogo from "components/header/gisLogo";
import GisCities from "components/header/gisCities";
import GisCourses from "components/header/gisCourses";
import GisDeliveryTime from "components/header/gisDeliveryTime";
import GisHeaderContacts from "components/header/gisHeaderContacts";
import GisWishListIcon from "components/shop/wishList/gisWishListIcon";
import GisCartIcon from "components/shop/cart/gisCartIcon";

export default {
  name: "gisHeaderWrapper",
  components: {GisCartIcon, GisWishListIcon, GisHeaderContacts, GisDeliveryTime, GisCourses, GisCities, GisLogo}
}
</script>

<style lang="sass">
.header-wrapper
  display: grid
  grid-template-columns: 3fr 3fr 1fr
  padding: 20px 0


.logo-cities-grid
  display: grid
  grid-template-columns: 1fr 2fr

.header-wrapper
  .on-left
    color: $grey-5 !important
</style>
