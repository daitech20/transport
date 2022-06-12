import { createWebHistory, createRouter } from 'vue-router'
import Login from '@/components/Login.vue'
import Register from '@/components/Register.vue'
import NotFound from '@/components/NotFound.vue'
import Home from '@/components/Home.vue'
import Checkout from '@/components/Checkout.vue'
import ValidateCustomer from '@/components/ValidateCustomer.vue'

import 'bootstrap'

const routes = [
    { path: '/', name: 'Home', component: Home},
    { path: '/login', name: 'Login', component: Login },
    { path: '/register', name: 'Register', component: Register},
    { path: '/checkout', name: 'Checkout', component: Checkout},
    { path: '/validateCustomer', name: 'ValidateCustomer', component: ValidateCustomer},
    { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound },
]

  const router = createRouter({
    history: createWebHistory(),
    routes,
  })

export default router