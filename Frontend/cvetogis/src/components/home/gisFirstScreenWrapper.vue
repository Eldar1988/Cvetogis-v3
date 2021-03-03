<template>
<section>
  <div class="container">
    <div class="first-screen-grid ">
      <gis-home-main-slider />
      <div>
        <gis-home-banners />
      </div>
    </div>
  </div>
</section>
</template>

<script>
import GisHomeMainSlider from "components/home/gisHomeMainSlider";
import GisHomeBanners from "components/home/gisHomeBanners";
export default {
  name: "gisFirstScreenWrapper",
  components: {GisHomeBanners, GisHomeMainSlider}
}
</script>

<style lang="sass">
.first-screen-grid
  margin-top: 60px
  display: grid
  grid-gap: 20px
  grid-template-columns: 2fr 1fr

@media screen and (max-width: 992px)
  .first-screen-grid
    margin-top: 20px
    grid-template-columns: 1fr
</style>
