<template>
  <div>
    <div class="flex benefits-wrapper">
      <div style="min-width: 229px">
        <div class="row flex" style="align-items: center">
          <div class="col-6">
            <q-img src="../../assets/images/Benefits/1.svg" class="benefit-img"/>
          </div>
          <div class="col-6">
            <p class="font-16 benefit-text">
              Большой выбор<br> подарков
            </p>
          </div>
        </div>
      </div>
      <div style="min-width: 229px">
        <div class="row flex" style="align-items: center">
          <div class="col-6">
            <q-img src="../../assets/images/Benefits/2.svg" class="benefit-img"/>
          </div>
          <div class="col-6">
            <p class="font-16 benefit-text">
              100% сходство букета c фотографией
            </p>
          </div>
        </div>
      </div>
      <div style="min-width: 229px">
        <div class="row flex" style="align-items: center">
          <div class="col-6">
            <q-img src="../../assets/images/Benefits/3.svg" class="benefit-img"/>
          </div>
          <div class="col-6">
            <p class="font-16 benefit-text">
              Только лучшие <br>исполнители
            </p>
          </div>
        </div>
      </div>
      <div style="min-width: 229px">
        <div class="row flex" style="align-items: center">
          <div class="col-6">
            <q-img src="../../assets/images/Benefits/4.svg" class="benefit-img"/>
          </div>
          <div class="col-6">
            <p class="font-16 benefit-text">
              Доставка по городам Казахстана
            </p>
          </div>
        </div>
      </div>
      <div style="min-width: 229px">
        <div class="row flex" style="align-items: center">
          <div class="col-6">
            <q-img src="../../assets/images/Benefits/5.svg" class="benefit-img"/>
          </div>
          <div class="col-6">
            <p class="font-16 benefit-text">
              Консультация по товару
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "gisBenefits",
  data() {
    return {}
  },
}
</script>

<style lang="sass">
.benefit-text
  margin-top: -20px !important

.benefits-wrapper
  max-width: 100%
  flex-wrap: nowrap
  overflow-x: scroll
</style>
