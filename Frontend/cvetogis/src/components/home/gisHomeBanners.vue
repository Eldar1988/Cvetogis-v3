<template>
  <div style="max-width: 100%; overflow: hidden">
    <div class="banners-wrapper">
      <div class="banner">
        <q-img src="../../assets/images/banner1.png" height="180px" class="rounded-20">
          <div class="banner-meta text-dark flex flex-center justify-start">
            <span class="block text-left text-accent">-30<span style="font-size: 18px">%</span></span>
            <p class="fon16">На сезонные цветы</p>
          </div>
        </q-img>
      </div>
      <div class="blue-banners-grid text-white">
        <div class="blue-banner bg-secondary rounded-20 flex flex-center">
          <div class="text-center">
            <img src="../../assets/images/banners/car.svg">
            <p class="font-14 q-mt-md">Доставим зa один час</p>
          </div>
        </div>
        <div class="blue-banner bg-secondary rounded-20 flex flex-center">
          <div class="text-center">
            <img src="../../assets/images/banners/world.svg">
            <p class="font-14 q-mt-md">Доставка в другом городе</p>
          </div>
        </div>
      </div>
    </div>
    <div class="banners-wrapper-mobile">

      <div class="banner mobile-banner">
        <q-img src="../../assets/images/banner1.png" height="180px" class="rounded-20">
          <div class="banner-meta text-dark flex flex-center justify-start">
            <span class="block text-left text-accent">-30<span style="font-size: 18px">%</span></span>
            <p class="fon16">На сезонные цветы</p>
          </div>
        </q-img>
      </div>
      <div class="blue-banner text-white bg-secondary rounded-20 flex flex-center mobile-banner">
        <div class="text-center">
          <img src="../../assets/images/banners/car.svg">
          <p class="font-14 q-mt-md">Доставим зa один час</p>
        </div>
      </div>
      <div class="blue-banner text-white bg-secondary rounded-20 flex flex-center mobile-banner">
        <div class="text-center">
          <img src="../../assets/images/banners/world.svg">
          <p class="font-14 q-mt-md">Доставка в другом городе</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "gisHomeBanners"
}
</script>

<style lang="sass">
.banners-wrapper-mobile
  display: none

.banners-wrapper
  height: 400px !important
  display: grid
  grid-template-rows: 1fr 1fr

.banner-meta
  max-width: 50%
  display: flex
  flex-direction: column
  height: 100%

  span
    font-size: 64px
    font-weight: 700

.blue-banners-grid
  display: grid
  grid-template-columns: 1fr 1fr
  grid-gap: 20px

@media screen and (max-width: 992px)
  .banners-wrapper
    display: none
    padding: 0 20px
    grid-gap: 20px

  .banners-wrapper-mobile
    max-width: 100vw
    display: flex
    overflow-x: scroll

  .mobile-banner
    min-width: 300px
    margin-left: 20px

  ::-webkit-scrollbar
    height: 0

  ::-moz-webkit-scrollbar
    height: 0


</style>
