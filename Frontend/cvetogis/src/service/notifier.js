import {Notify} from 'quasar'

export default function notifier(message, color='dark') {
  Notify.create({message: `${message}`, color: `${color}`, position: 'top'})
}
