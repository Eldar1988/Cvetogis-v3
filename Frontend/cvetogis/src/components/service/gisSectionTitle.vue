<template>
<div>
  <h3 class="section-title">{{ title }}</h3>
</div>
</template>

<script>
export default {
  name: "gisSectionTitle",
  props: {
    title: {
      type: String,
      default: ''
    }
  }
}
</script>

<style lang="sass">
.section-title
  font-size: 36px
  font-weight: 700

@media screen and (max-width: 992px)
  .section-title
    font-size: 24px
</style>
