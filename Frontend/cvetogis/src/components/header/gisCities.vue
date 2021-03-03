<template>
  <div class="cities q-ml-md font-16">
    <q-btn-dropdown
      :label="currentCity"
      icon="near_me"
      dropdown-icon="keyboard_arrow_down"
      flat rounded
      class="font-16 city-choice"
      no-caps
    >
      <q-list class="rounded-10">
        <q-item
          v-for="city in cities" :key="city.id"
          clickable v-close-popup
          class="font-16 text-secondary text-weight-medium"
        >
          <q-item-section @click="setCity(city)">
            <q-item-label>{{ city.title }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-btn-dropdown>
  </div>
</template>

<script>
import setLocalStorageDefaults from "src/service/set_local_storage_defaults";

export default {
  name: "gisCities",
  computed: {
    cities() {
      return this.$store.getters.getMainData.cities
    }
  },
  created() {
    setLocalStorageDefaults(this.$route.query['city'])
    this.getCurrentCity()
  },
  data() {
    return {
      currentCity: null,
    }
  },
  methods: {
    setCity(city) {
      localStorage.setItem('city', city.slug)
      this.$store.commit('setCurrentCity', city)
      this.$root.$emit('updateCity')
      this.currentCity = city.title
      this.$router.push('/')
      location.reload()
    },
    getCurrentCity() {
      let city = ''
      this.cities.forEach(item => {
        if (item.slug === localStorage.getItem('city')) city = item
      })
      this.$store.commit('setCurrentCity', city)
      this.currentCity = city.title
    }
  },

}
</script>

<style lang="sass">
@media screen and (max-width: 1100px)
  .city-choice
    margin-left: -15px
    .on-left
      display: none
</style>
