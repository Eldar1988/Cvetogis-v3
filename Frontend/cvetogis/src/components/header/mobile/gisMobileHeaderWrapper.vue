<template>
<div class="mobile-header-wrapper">
  <gis-logo />
  <gis-mobile-menu />
</div>
</template>

<script>
import GisLogo from "components/header/gisLogo";
import GisMobileMenu from "components/header/mobile/gisMobileMenu";
export default {
  name: "gisMobileHeaderWrapper",
  components: {GisMobileMenu, GisLogo}
}
</script>

<style lang="sass">
.mobile-header-wrapper
  padding: 10px
  min-height: 85px
  display: grid
  grid-template-columns: 1fr 1fr
</style>
