<template>
<nav class="nav header-container">
  <ul
    class="font-14 text-uppercase text-dark text-weight-bold letter-1 q-pb-md q-pt-sm"
    style="margin-left: 10px"
  >
    <li class="nav-item">
      <router-link
        to="/"
        title="Главная страница"
      >
        Главная
      </router-link>
    </li>
    <li class="nav-item">
      <router-link
        to="/shop"
        title="Магазин"
        active-class="active-nav-item"
      >
        Магазин
      </router-link>
    </li>
    <li class="nav-item">
      <gis-nav-dropdown label="Кому" :items="peoples" filter-field="flowers_for"/>
    </li>
    <li class="nav-item">
      <gis-nav-dropdown label="Повод" :items="reasons" filter-field="reasons"/>
    </li>
    <li class="nav-item">
      <gis-nav-dropdown label="Подарки" :items="presentCategories" filter-field="present_category"/>
    </li>
    <li class="nav-item">
      <router-link
        to="/shipping"
        title="Условия оплаты и доставки"
        active-class="active-nav-item"
      >
        Оплата и доставка
      </router-link>
    </li>
    <li class="nav-item">
      <router-link
        to="/about"
        title="Условия оплаты и доставки"
        active-class="active-nav-item"
      >
        О нас
      </router-link>
    </li>
  </ul>
</nav>
</template>

<script>
import GisNavDropdown from "components/header/gisNavDropdown";
export default {
  name: "gisHeaderNav",
  components: {GisNavDropdown},
  computed: {
    reasons() {
      return this.$store.getters.getMainData.reasons
    },
    peoples() {
      return this.$store.getters.getMainData.peoples
    },
    presentCategories() {
      return this.$store.getters.getMainData.presentCategories
    }
  }
}
</script>

<style lang="sass">
.active-nav-item
  color: $dark
  position: relative

  &:before
    content: ''
    position: absolute
    bottom: -10px
    width: 5px
    height: 5px
    border-radius: 10px
    left: 50%
    margin-left: -2.5px
    background: $accent

.header
  li
    margin-left: 30px

.header
  ul
    display: flex

@media screen and (max-width: 992px)
  .header
    ul
      flex-direction: column !important

  .nav-item
    margin-top: 20px

  .active-nav-item

    &:before
      bottom: 40%
      width: 5px
      height: 5px
      border-radius: 10px
      left: 0
      margin-left: -10px
      background: $accent
</style>
