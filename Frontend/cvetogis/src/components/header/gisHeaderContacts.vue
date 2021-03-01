<template>
  <div>
    <div class="whatsapp">
      <a href="https://wa.me/77079514936" class="font-24 text-weight-bold text-dark ">
        <img src="../../assets/icons/whatsapp.svg" alt="whatsapp">
      </a>
      <div class="q-ml-sm" style="margin-top: -7px">
        <a href="https://wa.me/77079514936" class="font-24 text-weight-bold text-dark ">+7 707 951-49-36</a>
        <gis-call-back/>
      </div>
    </div>
  </div>
</template>

<script>
import GisCallBack from "components/header/gisCallBack";

export default {
  name: "gisHeaderContacts",
  components: {GisCallBack}
}
</script>

<style lang="sass">
.whatsapp
  display: flex
</style>
