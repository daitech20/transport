import { createApp } from 'vue'
import App from './App.vue'
import router from './router/router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import 'babel-polyfill'
import Notifications from '@kyvg/vue3-notification'


const app = createApp(App)
app.use(router)
app.use(Notifications)
app.use(VueAxios, axios)
app.mount('#app')

