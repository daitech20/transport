import { createApp } from 'vue'
import App from './App.vue'
import router from './router/router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

const app = createApp(App)
app.use(router)
app.use(VueAxios, axios)
app.mount('#app')
