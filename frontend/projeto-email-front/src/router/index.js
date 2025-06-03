import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import ListarEmails from '../pages/modelos/listar.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/email/listar', component: ListarEmails },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
