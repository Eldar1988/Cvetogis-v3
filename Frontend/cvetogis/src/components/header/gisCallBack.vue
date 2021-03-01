<template>
  <div class="call-back" style="margin-top: -7px">
    <span
      class="text-weight-regular text-secondary cursor-pointer dashed font-16"
      @click="dialog = true"
    >
        Обратный звонок </span><span class="text-grey">(9:00–18:00)
    </span>

    <q-dialog v-model="dialog">
      <q-card
        style="width: 500px; max-width: 100%"
        class="shadow-0 relative-position text-center rounded-10 q-px-md"
      >
        <q-btn
          style="position: absolute; top:-0; right: 0; z-index: 10"
          icon="close"
          text-color="dark"
          flat dense
          v-close-popup
        />
        <q-toolbar>
          <q-toolbar-title class=" text-weight-bold font-24">Заказ обратного звонка</q-toolbar-title>
        </q-toolbar>
        <q-separator color="grey-3"/>
        <p class="font-16 py-25">Оставьте свой номер телефона и мы вам перезвоним</p>
        <q-input
          v-model="callBackData.phone"
          filled dense outlined
          input-class="rounded-10"
          type="tel"
          mask="# ### ### ####"
        />
        <q-btn
          color="accent"
          class="my-25 rounded-5 font-14 letter-1 text-weight-bold q-pl-md"
          label="Отправить"
          icon-right="east"
          unelevated
          @click="createCallBack"
          :loading="loading"
        />
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
import notifier from "src/service/notifier";

export default {
  name: "gisCallBack",
  data() {
    return {
      dialog: false,
      callBackData: {
        phone: ''
      },
      loading: false
    }
  },
  methods: {
    async createCallBack() {
      // Validate
      if(this.callBackData.phone.length < 5) {
        notifier('Необходимо указать номер телефона')
        return null
      }
      this.loading = true
      // Sent CallBack Data
      try {
        await fetch(`${this.$store.getters.getServerURL}/api/orders/create_callback/`, {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify(this.callBackData)
        }).then(response => {
          if(response.status === 201) {
            setTimeout(() => {
              notifier('Спасибо! Ваша заявка принята', 'positive')
              this.loading = false
              this.dialog = false
              return true
            },1500)
          }
          else {
            notifier('Извините, не удалось создать заявку. Попробуйте еще раз')
            this.loading = false
          }
        })
      } catch (e) {
        notifier(e.message)
        this.loading = false
      }
    }
  }
}
</script>

<style lang="sass">
.dashed
  border-bottom: 1px dashed $grey
</style>
