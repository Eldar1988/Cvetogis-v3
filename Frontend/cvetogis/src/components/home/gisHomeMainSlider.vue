<template>
  <div class="home-main-slider">
    <q-carousel
      animated
      v-model="slide"
      :arrows="!$q.platform.is.mobile"
      navigation
      infinite
      :autoplay="true"
      class="home-slider-image rounded-20"
      control-color="primary"
      swipeable
    >
      <q-carousel-slide
        v-for="(slide, index) in slides"
        :key="index"
        :name="index"
      >
        <!--        Image   -->
        <q-img
          :src="slide.image"
          class="rounded-20 home-slider-image"
        >

          <!--          Meta   -->
          <div class="home-slider-meta text-dark">
            <h2 class="slide-title">{{ slide.title }}</h2>
            <p class="py-25">{{ slide.text }}</p>
            <q-btn
              :label="slide.button_text"
              :to="slide.button_url"
              outline
              color="primary"
              class="rounded-5"
            />
          </div>

          <!--          Skeleton   -->
          <template v-slot:loading>
            <q-skeleton class="rounded-20 home-slider-image full-width"/>
          </template>

        </q-img>
      </q-carousel-slide>
    </q-carousel>
  </div>
</template>

<script>

export default {
  name: "gisHomeMainSlider",
  computed: {
    slides() {
      return this.$store.getters.getMainData.slides
    }
  },
  data() {
    return {
      slide: 0
    }
  },
}
</script>

<style lang="sass">
.home-slider-image
  height: 400px

.home-slider-meta
  max-width: 50%
  margin: 20px

  h2
    font-size: 56px
    font-weight: 700

  p
    font-size: 18px
    font-weight: 400

@media screen and (max-width: 992px)
  .home-main-slider
    margin: 0 20px


  .home-slider-meta
    max-width: 70%
    margin: 20px

    h2
      font-size: 24px
      font-weight: 700

@media screen and (max-width: 650px)

  .home-slider-image
    height: 300px
</style>
