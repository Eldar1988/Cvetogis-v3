import axiosInstance from "axios";
import notifier from "src/service/notifier";

export default {
  state: {
    homeProducts: null
  },
  actions: {
    async fetchHomeProducts({commit, state}, city) {
      if(!state.homeProducts) {
        try {
          await axiosInstance.get(`${this.getters.getServerURL}/api/home_products/?city=${city}`)
            .then(response => commit('setHomeProducts', response.data))
        } catch (e) {
          notifier(e.message)
        }
      }
    }
  },
  mutations: {
    setHomeProducts(state, data) {
      state.homeProducts = data
    }
  },
  getters: {
    getHomeProducts: (state) => state.homeProducts
  }
}
