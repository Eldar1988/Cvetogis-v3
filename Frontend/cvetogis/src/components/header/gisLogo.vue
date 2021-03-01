<template>
  <div class="logo relative-position">
    <router-link to="/">
      <img src="../../assets/logo.svg" alt="Logo">
      <div class="logo-text">
        <h1>Сеть доставки цветов <br>и подарков</h1>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "gisLogo"
}
</script>

<style lang="sass">
.logo-text
  position: absolute
  top: 30px
  left: 40px

  h1
    color: grey
    font-size: 14px
    line-height: 15px
</style>
