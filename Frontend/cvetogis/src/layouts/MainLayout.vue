<template>
  <q-layout view="lHh Lpr lFf">
    <q-header
      v-if="!$q.platform.is.mobile"
      class="header text-dark hide-on-mobile"
    >
      <gis-header-wrapper />
      <gis-header-nav />
    </q-header>
    <q-header
      v-if="$q.platform.is.mobile"
      class="header mobile-header text-dark hide-on-desktop"
    >
      <gis-mobile-header-wrapper />
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
    <gis-bottom-bar />
  </q-layout>
</template>

<script>

import GisHeaderWrapper from "components/header/gisHeaderWrapper";
import setLocalStorageDefaults from "src/service/set_local_storage_defaults";
import GisHeaderNav from "components/header/gisHeaderNav";
import GisMobileHeaderWrapper from "components/header/mobile/gisMobileHeaderWrapper";
import GisBottomBar from "components/service/gisBottomBar";
export default {
  name: 'MainLayout',
  components: {GisBottomBar, GisMobileHeaderWrapper, GisHeaderNav, GisHeaderWrapper},

  data () {
    return {
    }
  },
  preFetch({store}) {
    return  store.dispatch('fetchMainData')
  }
}
</script>

<style lang="sass">
.header
  background: #F2F2F2
  box-shadow: 0 4px 4px rgba(0, 0, 0, 0.05)
</style>
