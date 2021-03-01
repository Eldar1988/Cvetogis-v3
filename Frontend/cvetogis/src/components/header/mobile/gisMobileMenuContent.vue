<template>
<div>
<gis-header-nav />
  <q-separator />
  <gis-cities class="q-mt-md"/>
  <gis-courses class="q-mt-sm"/>
  <gis-header-contacts class="q-ml-md q-mt-md"/>
</div>
</template>

<script>
import GisHeaderNav from "components/header/gisHeaderNav";
import GisCities from "components/header/gisCities";
import GisCourses from "components/header/gisCourses";
import GisHeaderContacts from "components/header/gisHeaderContacts";
export default {
  name: "gisMobileMenuContent",
  components: {GisHeaderContacts, GisCourses, GisCities, GisHeaderNav}
}
</script>

<style lang="sass">

</style>
