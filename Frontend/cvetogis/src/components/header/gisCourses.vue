<template>
  <div class="courses">
    <q-btn-dropdown
      :label="currentCourse"
      dropdown-icon="keyboard_arrow_down"
      flat rounded
      class="font-16"
      no-caps
    >
      <q-list class="rounded-10">
        <q-item
          v-for="course in courses" :key="course.id"
          clickable v-close-popup
          class="font-16 text-secondary text-weight-medium"
        >
          <q-item-section @click="setCourse(course)">
            <q-item-label>{{ course.title }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-btn-dropdown>
  </div>
</template>

<script>
import notifier from "src/service/notifier";

export default {
  name: "gisCourses",
  data() {
    return {
      courses: null,
      currentCourse: null
    }
  },
  mounted() {
    this.getCourses()
  },
  methods: {
    getCourses() {
      try {
        this.courses = this.$store.getters.getMainData.courses
        this.currentCourse = this.$store.getters.getCurrentCourse.title
      } catch (e) {
        setTimeout(() => {
          this.getCourses()
        }, 500)
      }
    },
    setCourse(course) {
      this.$store.commit('setCurrentCourse', course)
      this.currentCourse = this.$store.getters.getCurrentCourse.title
    }
  }
}
</script>

<style scoped>

</style>
