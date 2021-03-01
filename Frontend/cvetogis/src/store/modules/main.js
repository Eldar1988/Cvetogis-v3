import axiosInstance from 'axios'
import notifier from "src/service/notifier"

export default {
  state: {
    mainData: null,
    currentCity: null,
    currentCourse: null,
  },
  actions: {
    async fetchMainData({commit}) {
      try {
        await axiosInstance(`${this.getters.getServerURL}/api/`)
          .then(({data}) => {
            commit('setMainData', data)
          })

      } catch (e) {
        notifier(`Не удалось загрузить данные (${e.message})`)
        setTimeout(() => {
          location.reload()
        }, 5000)
      }
    }
  },
  mutations: {
    setMainData (state, data) {
      state.mainData = data
      state.currentCourse = data.courses[0]
    },
    setCurrentCity(state, data) {
      state.currentCity = data
    },
    setCurrentCourse(state, data) {
      state.currentCourse = data
    }
  },
  getters: {
    getMainData: (state) => state.mainData,
    getCurrentCity: (state) => state.currentCity,
    getCurrentCourse: (state) => state.currentCourse,
  }
}
